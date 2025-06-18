"""Core dataclass definitions used across the calculator."""

from dataclasses import dataclass

__all__ = ["Material", "ThreadSpec", "GasketMaterial"]

@dataclass
class Material:
    name: str
    yield_strength: float
    tensile_strength: float
    friction_coeff: float

@dataclass
class ThreadSpec:
    name: str
    major_dia: float
    minor_dia: float
    tensile_area: float
    head_dia: float

@dataclass
class GasketMaterial:
    name: str
    yield_strength: float
    sealing_pressure: float
    friction_coeff: float
