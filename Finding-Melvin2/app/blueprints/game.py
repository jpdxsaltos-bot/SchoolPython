from flask import Blueprint, jsonify
from app import db
from app.models.game_state import NormalGameState, QuickGameState
import random

game_bp = Blueprint('game', __name__, url_prefix='/api')

AIRPORTS = [
    {'iata': 'HEL', 'name': 'Helsinki',      'lat': 60.3172, 'lon': 24.9633,  'region': 'Europe'},
    {'iata': 'LIS', 'name': 'Lisbon',        'lat': 38.7818, 'lon': -9.1280,  'region': 'Europe'},
    {'iata': 'OPO', 'name': 'Porto',         'lat': 41.2481, 'lon': -8.6814,  'region': 'Europe'},
    {'iata': 'CDG', 'name': 'Paris',         'lat': 49.0097, 'lon': 2.5479,   'region': 'Europe'},
    {'iata': 'FRA', 'name': 'Frankfurt',     'lat': 50.0379, 'lon': 8.5622,   'region': 'Europe'},

    {'iata': 'JFK', 'name': 'New York JFK',  'lat': 40.6398, 'lon': -73.7789, 'region': 'Americas'},
    {'iata': 'LAX', 'name': 'Los Angeles',   'lat': 33.9416, 'lon': -118.4085,'region': 'Americas'},
    {'iata': 'GRU', 'name': 'São Paulo',     'lat': -23.4356,'lon': -46.4731, 'region': 'Americas'},
    {'iata': 'MEX', 'name': 'Mexico City',   'lat': 19.4361, 'lon': -99.0719, 'region': 'Americas'},
    {'iata': 'YYZ', 'name': 'Toronto',       'lat': 43.6777, 'lon': -79.6248, 'region': 'Americas'},

    {'iata': 'CPT', 'name': 'Cape Town',     'lat': -33.9690,'lon': 18.5972,  'region': 'Africa'},
    {'iata': 'JNB', 'name': 'Johannesburg',  'lat': -26.1337,'lon': 28.2420,  'region': 'Africa'},
    {'iata': 'CAI', 'name': 'Cairo',         'lat': 30.1219, 'lon': 31.4056,  'region': 'Africa'},
    {'iata': 'ADD', 'name': 'Addis Ababa',   'lat': 8.9779,  'lon': 38.7993,  'region': 'Africa'},
    {'iata': 'LOS', 'name': 'Lagos',         'lat': 6.5774,  'lon': 3.3211,   'region': 'Africa'},

    {'iata': 'DXB', 'name': 'Dubai',         'lat': 25.2532, 'lon': 55.3657,  'region': 'Asia'},
    {'iata': 'DEL', 'name': 'Delhi',         'lat': 28.5562, 'lon': 77.1000,  'region': 'Asia'},
    {'iata': 'HND', 'name': 'Tokyo Haneda',  'lat': 35.5494, 'lon': 139.7798, 'region': 'Asia'},
    {'iata': 'SIN', 'name': 'Singapore',     'lat': 1.3644,  'lon': 103.9915, 'region': 'Asia'},
    {'iata': 'PEK', 'name': 'Beijing',       'lat': 40.0799, 'lon': 116.6031, 'region': 'Asia'},

    {'iata': 'SYD', 'name': 'Sydney',        'lat': -33.9399,'lon': 151.1753, 'region': 'Oceania'},
    {'iata': 'MEL', 'name': 'Melbourne',     'lat': -37.6733,'lon': 144.8430, 'region': 'Oceania'},
    {'iata': 'AKL', 'name': 'Auckland',      'lat': -37.0082,'lon': 174.7850, 'region': 'Oceania'},
    {'iata': 'BNE', 'name': 'Brisbane',      'lat': -27.3842,'lon': 153.1175, 'region': 'Oceania'},
    {'iata': 'PER', 'name': 'Perth',         'lat': -31.9403,'lon': 115.9670, 'region': 'Oceania'},
]

def init_fragments_and_melvin(state):
    all_iatas = [a['iata'] for a in AIRPORTS]
    fragments = random.sample(all_iatas, 4)
    state.fragment_airports = fragments
    state.melvin_airport = random.choice(all_iatas)

@game_bp.route('/state')
def get_state():
    quick_state = QuickGameState.query.first()
    if quick_state and quick_state.turns_left > 0:
        db.session.add(quick_state)
        db.session.commit()
        return jsonify(quick_state.to_dict())
    normal_state = NormalGameState.query.first()
    if not normal_state:
        normal_state = NormalGameState()
        init_fragments_and_melvin(normal_state)
        normal_state.hint_flags = {}
        db.session.add(normal_state)

    db.session.commit()
    return jsonify(normal_state.to_dict())

@game_bp.route('/state', methods=['DELETE'])
def reset_state():
    NormalGameState.query.delete()
    QuickGameState.query.delete()
    db.session.commit()
    return jsonify({"success": True})
    
@game_bp.route('/fly/<iata>', methods=['POST'])
def fly(iata):
    quick_state = QuickGameState.query.first()
    if quick_state and quick_state.turns_left > 0:
        state = quick_state
    else:
        state = NormalGameState.query.first() or NormalGameState()
    db.session.add(state)
    result = state.attempt_flight(iata, AIRPORTS)
    state.turns_left = max(0, state.turns_left - 1)
    state.won = (
        state.fragments_recovered >= 4
        and state.current_airport == state.melvin_airport
    )
    db.session.flush()
    db.session.refresh(state)
    db.session.commit()
    return jsonify({**state.to_dict(), **result})
    
@game_bp.route('/hint', methods=['POST'])
def buy_hint():
    state = QuickGameState.query.first()
    if not (state and state.turns_left > 0):
        state = NormalGameState.query.first() or NormalGameState()
    if state.turns_left < 2:
        return jsonify({'success': False, **state.to_dict()})
    state.turns_left = max(0, state.turns_left - 1)
    if not state.hint_flags:
        state.hint_flags = {}
    if 'fragment_region' not in state.hint_flags and state.fragment_airports:
        frag_iata = random.choice(state.fragment_airports)
        frag_airport = next(a for a in AIRPORTS if a['iata'] == frag_iata)
        state.hint_flags['fragment_region'] = frag_airport['region']
    elif 'melvin_region' not in state.hint_flags and state.melvin_airport:
        melvin_airport = next(a for a in AIRPORTS if a['iata'] == state.melvin_airport)
        state.hint_flags['melvin_region'] = melvin_airport['region']
    db.session.add(state)
    db.session.commit()
    return jsonify({'success': True, **state.to_dict()})

@game_bp.route('/quick_mode', methods=['POST'])
def start_quick_mode():
    QuickGameState.query.delete()
    state = QuickGameState()
    init_fragments_and_melvin(state)
    state.hint_flags = {}
    db.session.add(state)
    db.session.commit()
    return jsonify(state.to_dict())

@game_bp.route('/normal_mode', methods=['POST'])
def start_normal_mode():
    QuickGameState.query.delete()
    db.session.commit()
    NormalGameState.query.delete()
    db.session.commit()
    return jsonify({"success": True})


@game_bp.route('/airports')
def get_airports():
    return jsonify(AIRPORTS)