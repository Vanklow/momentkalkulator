from dataclasses import dataclass

@dataclass
class GasketMaterial:
    name: str
    yield_strength: float       # MPa
    sealing_pressure: float     # MPa, typical required sealing pressure
    friction_coeff: float       # friction coefficient for torque calc

gasket_materials = {
    # Copper variants
    "Copper (soft)": GasketMaterial("Copper (soft)", yield_strength=70, sealing_pressure=40, friction_coeff=0.25),
    "Copper (hard)": GasketMaterial("Copper (hard)", yield_strength=110, sealing_pressure=60, friction_coeff=0.22),
    "Copper (annealed)": GasketMaterial("Copper (annealed)", yield_strength=60, sealing_pressure=35, friction_coeff=0.25),
    # Aluminium
    "Aluminum (soft)": GasketMaterial("Aluminum (soft)", yield_strength=40, sealing_pressure=20, friction_coeff=0.23),
    "Aluminum (hard)": GasketMaterial("Aluminum (hard)", yield_strength=80, sealing_pressure=28, friction_coeff=0.19),
    # Steel
    "Steel (mild)": GasketMaterial("Steel (mild)", yield_strength=200, sealing_pressure=120, friction_coeff=0.20),
    "Steel (SS316)": GasketMaterial("Steel SS316", yield_strength=200, sealing_pressure=100, friction_coeff=0.16),
    # Fiber
    "Aramid fiber": GasketMaterial("Aramid fiber (Klinger)", yield_strength=30, sealing_pressure=15, friction_coeff=0.19),
    "Cellulose fiber": GasketMaterial("Cellulose fiber", yield_strength=20, sealing_pressure=10, friction_coeff=0.21),
    # Rubber
    "Neoprene": GasketMaterial("Neoprene", yield_strength=15, sealing_pressure=10, friction_coeff=0.15),
    "EPDM": GasketMaterial("EPDM", yield_strength=12, sealing_pressure=9, friction_coeff=0.16),
    "Nitrile (NBR)": GasketMaterial("Nitrile (NBR)", yield_strength=18, sealing_pressure=11, friction_coeff=0.16),
    "Viton": GasketMaterial("Viton", yield_strength=16, sealing_pressure=10, friction_coeff=0.17),
    "Rubber (generic)": GasketMaterial("Rubber", yield_strength=20, sealing_pressure=12, friction_coeff=0.20),
    # PTFE
    "PTFE": GasketMaterial("PTFE", yield_strength=25, sealing_pressure=8, friction_coeff=0.18),
    "Expanded PTFE": GasketMaterial("ePTFE", yield_strength=20, sealing_pressure=7, friction_coeff=0.17),
    # Graphite
    "Graphite": GasketMaterial("Graphite", yield_strength=40, sealing_pressure=30, friction_coeff=0.22),
    "Reinforced graphite": GasketMaterial("Reinforced graphite", yield_strength=70, sealing_pressure=50, friction_coeff=0.20),
    # Paper
    "Paper": GasketMaterial("Paper", yield_strength=10, sealing_pressure=7, friction_coeff=0.23),
    # Metal-reinforced
    "Spiral wound SS/graphite": GasketMaterial("Spiral wound SS/graphite", yield_strength=150, sealing_pressure=90, friction_coeff=0.17),
    "Spiral wound SS/PTFE": GasketMaterial("Spiral wound SS/PTFE", yield_strength=130, sealing_pressure=75, friction_coeff=0.16),
    "Metal jacketed": GasketMaterial("Metal jacketed", yield_strength=110, sealing_pressure=80, friction_coeff=0.18),
    # Ceramic fiber (high temp)
    "Ceramic fiber": GasketMaterial("Ceramic fiber", yield_strength=25, sealing_pressure=20, friction_coeff=0.21),
    # Asbestos (legacy, not for new use)
    "Asbestos (legacy)": GasketMaterial("Asbestos (legacy)", yield_strength=30, sealing_pressure=15, friction_coeff=0.18),
}
