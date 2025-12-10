from app import db
from sqlalchemy import Column, Integer, String, Boolean, Float, JSON
from math import radians, sin, cos, sqrt, atan2
import random


class BaseGameState(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    turns_left = Column(Integer, default=20)
    crew_hours = Column(Integer, default=300)
    current_airport = Column(String(3), default='HEL')
    fragments_recovered = Column(Integer, default=0)
    streak_count = Column(Integer, default=0)
    beacon_active = Column(Boolean, default=False)
    hint_flags = Column(JSON, default=dict)
    weather_modifier = Column(Float, default=1.0)
    quick_mode = Column(Boolean, default=False)
    fragment_airports = Column(JSON, default=list)
    melvin_airport = Column(String(3), default=None)
    def apply_penalty(self):
        self.turns_left -= 2
        return {"success": False, "reason": "rest_penalty"}
    def calculate_cc_raw(self, from_airport, to_airport):
        lat1, lon1 = radians(float(from_airport["lat"])), radians(float(from_airport["lon"]))
        lat2, lon2 = radians(float(to_airport["lat"])), radians(float(to_airport["lon"]))
        dlat, dlon = lat2 - lat1, lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = 6371 * c
        return (distance / 100) * self.weather_modifier
    def calculate_cc_capped(self, from_airport, to_airport, multiplier=1.0, cap=30):
        base = self.calculate_cc_raw(from_airport, to_airport)
        cc = base * multiplier
        return min(cc, cap)
    def update_streak(self, cc_cost):
        return
        
    def to_dict(self):
        return {
            "turns_left": self.turns_left,
            "crew_hours": self.crew_hours,
            "current_airport": self.current_airport,
            "fragments_recovered": self.fragments_recovered,
            "beacon_active": self.beacon_active,
            "hint_flags": self.hint_flags or {},
            "weather_modifier": round(self.weather_modifier, 2),
            "quick_mode": self.quick_mode,
            "fragment_airports": self.fragment_airports or [],
            "melvin_airport": self.melvin_airport,
            "won": (
                self.turns_left > 0
                and self.fragments_recovered >= 4
                and self.current_airport == self.melvin_airport
            ),
        }

class NormalGameState(BaseGameState):
    __tablename__ = "game_states"
    def attempt_flight(self, target_iata, airports):
        current = next((a for a in airports if a["iata"] == self.current_airport), airports[0])
        target = next((a for a in airports if a["iata"] == target_iata), airports[0])
        cc_cost = self.calculate_cc_capped(current, target, multiplier=1.0, cap=30)
        if cc_cost > self.crew_hours:
            return self.apply_penalty()
        self.crew_hours -= int(cc_cost)
        self.turns_left -= 1
        self.current_airport = target_iata
        self.update_streak(cc_cost)
        if self.turns_left <= 15:
            self.beacon_active = True
        got_fragment = False
        if target_iata in self.fragment_airports:
            self.fragments_recovered += 1
            got_fragment = True
        if random.random() < 0.1:
            self.weather_modifier = random.uniform(0.9, 1.2)
        print(
            f"Clicked {target_iata}, fragments: {self.fragment_airports}, got fragment: {got_fragment}"
        )
        return {"success": True, "cc_cost": round(cc_cost, 1)}
        
class QuickGameState(BaseGameState):
    __tablename__ = "quick_games"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turns_left = 15
        self.crew_hours = 230
        self.quick_mode = True
    def attempt_flight(self, target_iata, airports):
        current = next((a for a in airports if a["iata"] == self.current_airport), airports[0])
        target = next((a for a in airports if a["iata"] == target_iata), airports[0])
        cc_cost = self.calculate_cc_capped(current, target, multiplier=0.7, cap=20)
        if cc_cost > self.crew_hours:
            return self.apply_penalty()
        self.crew_hours -= int(cc_cost)
        self.turns_left -= 1
        self.current_airport = target_iata
        self.update_streak(cc_cost)
        if self.turns_left <= 8:
            self.beacon_active = True
        got_fragment = False
        if target_iata in self.fragment_airports:
            self.fragments_recovered += 1
            got_fragment = True
        if random.random() < 0.1:
            self.weather_modifier = random.uniform(0.9, 1.2)

        print(
            f"Clicked {target_iata}, fragments: {self.fragment_airports}, got fragment: {got_fragment}"
        )
        return {"success": True, "cc_cost": round(cc_cost, 1), "quick_bonus": True}