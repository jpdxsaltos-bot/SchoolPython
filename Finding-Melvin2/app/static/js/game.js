let gameState = {};
let airports = [];
let bestScore = localStorage.getItem('bestQuickScore') || '--';
let updateUI = null;

const BANTER_LINES = [
    "Neha: 'Where to next?'",
    "Jose: 'Efficient route! Keep it up!'",
    "Mahim: 'Momentum building, lets go team!'",
    "Neha: 'Melvin's signal getting stronger!'",
    "Jose: 'Hop in Lets Fly!'",
    "Mahim: 'Keep looking and great work!'"
];

const AIRPORT_POSITIONS = {
    HEL: { x: 0.57, y: 0.25 },
    LIS: { x: 0.57, y: 0.25 },
    OPO: { x: 0.57, y: 0.25 },
    CDG: { x: 0.57, y: 0.25 },
    FRA: { x: 0.57, y: 0.25 },

    JFK: { x: 0.20, y: 0.40 },
    LAX: { x: 0.20, y: 0.40 },
    GRU: { x: 0.30, y: 0.65 },
    MEX: { x: 0.30, y: 0.65 },
    YYZ: { x: 0.20, y: 0.30 },

    CPT: { x: 0.53, y: 0.66 },
    JNB: { x: 0.53, y: 0.66 },
    CAI: { x: 0.53, y: 0.66 },
    ADD: { x: 0.53, y: 0.66 },
    LOS: { x: 0.53, y: 0.66 },

    DXB: { x: 0.70, y: 0.42 },
    DEL: { x: 0.70, y: 0.42 },
    HND: { x: 0.70, y: 0.42 },
    SIN: { x: 0.70, y: 0.42 },
    PEK: { x: 0.70, y: 0.42 },


    SYD: { x: 0.88, y: 0.78 },
    MEL: { x: 0.88, y: 0.78 },
    AKL: { x: 0.88, y: 0.78 },
    BNE: { x: 0.85, y: 0.78 },
    PER: { x: 0.88, y: 0.78 }
  };

async function initGame() {
    document.getElementById('best-score').textContent = bestScore;

    const res = await fetch('/api/airports');
    airports = await res.json();
    renderAirports();

    await updateUI();
    setInterval(updateUI, 1000);
}

updateUI = async function () {
    const res = await fetch('/api/state');
    gameState = await res.json();
    const turnsEl = document.getElementById('turns-text');
    const crewEl = document.getElementById('crew-hours');
    const fragEl = document.getElementById('fragments');
    const clock = document.getElementById('clock');
    const hintEl = document.getElementById('hint-text');

    turnsEl.textContent = gameState.turns_left;
    crewEl.textContent = gameState.crew_hours;
    fragEl.textContent = gameState.fragments_recovered;

    const maxTurns = gameState.quick_mode ? 10 : 20;
    const progress = gameState.turns_left / maxTurns;
    const offset = 314 * (1 - progress);
    clock.style.strokeDashoffset = offset;
    if (gameState.turns_left <= 5) {
        clock.classList.add('low-turns');
    } else {
        clock.classList.remove('low-turns');
    }
    const crewStat = document.querySelector('.crew-hours');
    if (crewStat) {
        if (gameState.crew_hours < 20) {
            crewStat.classList.add('low');
        } else {
            crewStat.classList.remove('low');
        }
    }
	const modeBtn = document.getElementById('mode-btn');
	if (modeBtn) {
	    if (gameState.quick_mode) {
	        modeBtn.textContent = 'Switch to Normal Game';
	    } else {
	        modeBtn.textContent = 'Switch to Quick Game';
	    }
	}
    if (typeof updateUI.lastFragments === 'undefined') {
        updateUI.lastFragments = gameState.fragments_recovered;
    } else if (gameState.fragments_recovered > updateUI.lastFragments) {
        addBanterLine("Fragment found near this airport!");
        updateUI.lastFragments = gameState.fragments_recovered;
    }

    const beacon = document.getElementById('beacon');
    if (beacon) {
        if (gameState.beacon_active) {
            beacon.classList.remove('hidden');
        } else {
            beacon.classList.add('hidden');
        }
    }
   
    if (gameState.hint_flags) {
        let text = '';
        if (gameState.hint_flags.fragment_region) {
            text += `Hint: At least one fragment is in ${gameState.hint_flags.fragment_region}. `;
        }
        if (gameState.hint_flags.melvin_region) {
            text += `Melvin is somewhere in ${gameState.hint_flags.melvin_region}.`;
        }   
        if (text && text !== updateUI.lastHintText) {
            addBanterLine(text);
            updateUI.lastHintText = text;
        }
    }
    hintEl.textContent = '';
	if (gameState.turns_left <= 0 && !gameState.won) {
	  showLose();
	}
    if (gameState.won) {
        showVictory();
    }
    updatePlanePosition();
};

function updatePlanePosition() {
    const map = document.getElementById('world-map');
    const plane = document.getElementById('plane-icon');
    if (!map || !plane || !gameState.current_airport) return;

    const pos = AIRPORT_POSITIONS[gameState.current_airport];
    if (!pos) return;

    const rect = map.getBoundingClientRect();
    plane.style.left = `${pos.x * rect.width}px`;
    plane.style.top  = `${pos.y * rect.height}px`;
}
function renderAirports() {
    const container = document.getElementById('airports');
    container.innerHTML = airports.map(airport => `
        <button class="airport-btn region-${airport.region.toLowerCase()}" onclick="flyTo('${airport.iata}')">
            <strong>${airport.iata}</strong><br>
            ${airport.name}
        </button>
    `).join('');
}
async function flyTo(iata) {
    try {
        const response = await fetch(`/api/fly/${iata}`, {
            method: 'POST'
        });

        if (!response.ok) {
            console.error('Flight request failed:', response.status, await response.text());
            return;
        }
        await updateUI();
		addBanterLine(BANTER_LINES[Math.floor(Math.random() * BANTER_LINES.length)]);
    } catch (err) {
        console.error('Network error while flying:', err);
    }
}
function addBanterLine(text) {
    const log = document.getElementById('banter-log');
    const line = document.createElement('div');
    line.className = 'banter-line';
    line.textContent = text;
    log.appendChild(line);

    while (log.children.length > 5) {
        log.removeChild(log.firstChild);
    }

    log.scrollTop = log.scrollHeight;
}
function addBanter() {
    addBanterLine(BANTER_LINES[Math.floor(Math.random() * BANTER_LINES.length)]);
}

function toggleQuickMode() {
    fetch('/api/quick_mode', { method: 'POST' })
        .then(() => {
            document.getElementById('banter-log').innerHTML = '';
            updateUI();
        })
        .catch(err => console.error('Quick mode toggle error', err));
}
function toggleQuickMode() {
    if (gameState.quick_mode) {
        fetch('/api/normal_mode', { method: 'POST' })
          .then(() => {
              document.getElementById('banter-log').innerHTML = '';
              updateUI();
          })
          .catch(err => console.error('Normal mode error', err));
    } else {
        fetch('/api/quick_mode', { method: 'POST' })
          .then(() => {
              document.getElementById('banter-log').innerHTML = '';
              updateUI();
          })
          .catch(err => console.error('Quick mode error', err));
    }
}

function showVictory() {
    document.getElementById('final-fragments').textContent = gameState.fragments_recovered;
    const maxTurns = gameState.quick_mode ? 10 : 20;
    document.getElementById('final-turns').textContent = maxTurns - gameState.turns_left;
    document.getElementById('victory-modal').classList.remove('hidden');
    if (gameState.quick_mode) {
        const turnsUsed = 10 - gameState.turns_left;
        if (bestScore === '--' || turnsUsed < parseInt(bestScore)) {
            bestScore = turnsUsed;
            localStorage.setItem('bestQuickScore', bestScore);
            document.getElementById('best-score').textContent = bestScore;
        }
    }
}
function showLose() {
  document.getElementById('final-fragments-lose').textContent = gameState.fragments_recovered;
  document.getElementById('lose-modal').classList.remove('hidden');
}
function restartGame() {
    document.getElementById('victory-modal').classList.add('hidden');
    document.getElementById('banter-log').innerHTML = '';
    fetch('/api/state', { method: 'DELETE' })
        .then(() => {
            window.location.reload();
        })
        .catch(() => {
            window.location.reload();
        });
}
function startFromIntro() {
    const intro = document.getElementById('intro-screen');
    if (intro) intro.classList.add('hidden');
    updateUI();
}
initGame();