from dataclasses import dataclass

@dataclass
class Material:
    name: str
    yield_strength: float
    tensile_strength: float
    friction_coeff: float

materials = {
    "Steel": {
        "4.6": Material("Steel 4.6", 240, 400, 0.14),
        "5.8": Material("Steel 5.8", 340, 520, 0.14),
        "8.8": Material("Steel 8.8", 640, 800, 0.14),
        "9.8": Material("Steel 9.8", 800, 900, 0.13),
        "10.9": Material("Steel 10.9", 940, 1040, 0.13),
        "12.9": Material("Steel 12.9", 1100, 1220, 0.12),
        "ASTM A36": Material("A36 Mild Steel", 250, 400, 0.18),
        "ASTM A193-B7": Material("A193-B7 Alloy", 720, 860, 0.14),
        "ASTM A307": Material("A307 Low Carbon", 240, 400, 0.18),
    },
    "Stainless": {
        "A1-50": Material("A1-50 Stainless", 210, 500, 0.17),
        "A2-50": Material("A2-50 Stainless", 210, 500, 0.17),
        "A2-70": Material("A2-70 Stainless", 450, 700, 0.16),
        "A4-70": Material("A4-70 Stainless", 450, 700, 0.16),
        "A4-80": Material("A4-80 Stainless", 640, 800, 0.14),
        "316": Material("316 Stainless", 290, 580, 0.15),
        "304": Material("304 Stainless", 215, 505, 0.16),
        "17-4PH": Material("17-4PH Stainless", 1000, 1100, 0.16),
    },
    "Titanium": {
        "Grade 2": Material("Titanium Grade 2", 275, 345, 0.15),
        "Grade 5": Material("Titanium Grade 5 (Ti-6Al-4V)", 830, 900, 0.17),
        "Grade 23": Material("Titanium Grade 23 (ELI)", 795, 860, 0.17),
    },
    "Aluminum": {
        "6061-T6": Material("Aluminum 6061-T6", 250, 310, 0.16),
        "6082-T6": Material("Aluminum 6082-T6", 250, 340, 0.16),
        "7075-T6": Material("Aluminum 7075-T6", 500, 560, 0.16),
        "2024-T4": Material("Aluminum 2024-T4", 320, 470, 0.16),
        "1100": Material("Aluminum 1100 (Pure)", 45, 110, 0.18),
    },
    "Copper": {
        "C110 (pure)": Material("Copper C110 (pure)", 70, 220, 0.25),
        "C101": Material("Copper C101 (OFHC)", 70, 220, 0.25),
        "CW614N": Material("Copper CW614N", 270, 450, 0.24),
    },
    "Brass": {
        "CW614N": Material("Brass CW614N", 200, 350, 0.16),
        "CW617N": Material("Brass CW617N", 250, 450, 0.16),
        "Naval": Material("Naval Brass", 275, 500, 0.18),
        "Default": Material("Brass (generic)", 200, 350, 0.16),
    },
    "Bronze": {
        "CuSn8": Material("Bronze CuSn8", 350, 480, 0.18),
        "PB102": Material("Bronze PB102 (Phosphor)", 250, 400, 0.17),
        "SAE 660": Material("Bronze SAE 660", 200, 380, 0.18),
    },
    "Plastic": {
        "PA66 (Nylon)": Material("Nylon PA66", 70, 90, 0.23),
        "POM (Delrin)": Material("POM Delrin", 65, 70, 0.23),
        "PTFE (Teflon)": Material("PTFE (Teflon)", 20, 30, 0.20),
        "PEEK": Material("PEEK", 90, 130, 0.23),
        "PVC": Material("PVC", 50, 80, 0.26),
        "UHMW-PE": Material("UHMW-PE", 22, 42, 0.20),
    },
    "Zinc": {
        "Zamak 3": Material("Zamak 3", 170, 280, 0.20),
        "Zinc (pure)": Material("Zinc (pure)", 35, 110, 0.20),
    },
    "Cast Iron": {
        "Gray": Material("Gray Cast Iron", 130, 240, 0.20),
        "Ductile": Material("Ductile Iron", 350, 500, 0.20),
    }
}