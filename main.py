# Bolt Moment Calculator - Main v1.2.0 (single-file, Canvas/online ready, dynamic diameters)
# Versioned: 2025-05-16
from datatypes import Material, ThreadSpec
from metric_threads import flat_metric_threads as metric_threads

materials_simple = {
    "4.6": Material("Steel 4.6", 240, 400, 0.14),
    "8.8": Material("Steel 8.8", 640, 800, 0.14),
    "10.9": Material("Steel 10.9", 940, 1040, 0.13),
    "12.9": Material("Steel 12.9", 1100, 1220, 0.12),
    "A2-70": Material("A2-70 Stainless", 450, 700, 0.16),
    "A4-70": Material("A4-70 Stainless", 450, 700, 0.16),
    "A4-80": Material("A4-80 Stainless", 640, 800, 0.14),
    "Ti-Grade2": Material("Titanium Grade 2", 275, 345, 0.15),
    "Ti-Grade5": Material("Titanium Grade 5 (Ti-6Al-4V)", 830, 900, 0.17),
    "316": Material("316 Stainless", 290, 580, 0.15),
    "304": Material("304 Stainless", 215, 505, 0.16),
    "Al6061": Material("Aluminum 6061", 250, 310, 0.16),
    "Al6082": Material("Aluminum 6082", 250, 340, 0.16),
    "Copper": Material("Copper (soft)", 70, 220, 0.25),
    "Brass": Material("Brass", 200, 350, 0.16),
}


def bolt_tensile_capacity(thread: ThreadSpec, material: Material):
    return thread.tensile_area * material.tensile_strength  # N

def thread_strip_out(thread: ThreadSpec, material: Material, engagement_mm: float):
    """
    Engineering-grade: Uses internal minor diameter and 0.6 × yield strength for conservative strip-out.
    """
    shear_strength = 0.6 * material.yield_strength  # MPa
    shear_area = 3.1416 * thread.minor_dia * engagement_mm  # mm^2
    return shear_area * shear_strength  # N


def torque_from_force(force_N: float, thread: ThreadSpec, material: Material):
    d_m = thread.major_dia / 1000  # mm → m
    K = material.friction_coeff
    return K * force_N * d_m  # Nm

def gasket_compression_force(outer_dia_mm, inner_dia_mm, required_pressure_mpa):
    import math
    area_mm2 = math.pi / 4 * (outer_dia_mm**2 - inner_dia_mm**2)
    force_n = area_mm2 * required_pressure_mpa
    return force_n, area_mm2

if __name__ == "__main__":
    # === Inputs ===
    thread_name = "M8x1.25"
    bolt_material_name = "8.8"
    plate_material_name = "316"
    nut_material_name = "A4-80"
    engagement_mm = 10
    nut_engagement_mm = 8
    use_nut = True

    # === Lookup ===
    thread = metric_threads[thread_name]
    bolt_mat = materials_simple[bolt_material_name]
    plate_mat = materials_simple[plate_material_name]
    nut_mat = materials_simple[nut_material_name]

    # === Calculations ===
    bolt_capacity = bolt_tensile_capacity(thread, bolt_mat)
    plate_strip = thread_strip_out(thread, plate_mat, engagement_mm)
    nut_strip = thread_strip_out(thread, nut_mat, nut_engagement_mm)

    if use_nut:
        limiting_modes = {
            "Bolt Tensile": bolt_capacity,
            "Nut Thread Strip-Out": nut_strip
        }
    else:
        limiting_modes = {
            "Bolt Tensile": bolt_capacity,
            "Threaded Plate Strip-Out": plate_strip
        }
    weakest_mode = min(limiting_modes, key=limiting_modes.get)
    weakest_limit = limiting_modes[weakest_mode]
    safe_force = weakest_limit / 1.5

    recommended_torque = torque_from_force(safe_force, thread, bolt_mat)
    torque_pm = recommended_torque * 0.10

    # === Output ===
    print("==== Bolt Joint Calculation ====")
    print(f"Thread: {thread.name}")
    print(f"    Major diameter: {thread.major_dia:.2f} mm")
    print(f"    Tensile area: {thread.tensile_area:.2f} mm²")
    print(f"    Head diameter: {thread.head_dia:.2f} mm")
    print(f"Bolt material: {bolt_mat.name}")
    print(f"    Yield strength: {bolt_mat.yield_strength} MPa, Tensile strength: {bolt_mat.tensile_strength} MPa, Friction coeff.: {bolt_mat.friction_coeff}")
    if use_nut:
        print(f"Nut material: {nut_mat.name}")
        print(f"    Yield strength: {nut_mat.yield_strength} MPa, Tensile strength: {nut_mat.tensile_strength} MPa, Friction coeff.: {nut_mat.friction_coeff}")
        print(f"Nut engagement: {nut_engagement_mm} mm")
    else:
        print(f"Plate material: {plate_mat.name}")
        print(f"    Yield strength: {plate_mat.yield_strength} MPa, Tensile strength: {plate_mat.tensile_strength} MPa, Friction coeff.: {plate_mat.friction_coeff}")
        print(f"Plate engagement: {engagement_mm} mm")
    print("--- Results ---")
    print(f"Bolt tensile limit: {bolt_capacity/1000:.2f} kN")
    if use_nut:
        print(f"Nut thread strip-out limit: {nut_strip/1000:.2f} kN")
    else:
        print(f"Threaded plate strip-out limit: {plate_strip/1000:.2f} kN")
    print(f"Weakest mode: {weakest_mode}")
    print(f"Safe clamping force (SF=1.5): {safe_force/1000:.2f} kN")

    # --- Multi-scenario Torque Output ---
    # Scenario 1: Recommended (database friction coeff)
    print(f"Recommended torque (material K={bolt_mat.friction_coeff:.2f}): {recommended_torque:.2f} Nm ± {torque_pm:.2f} Nm (10%)")

    # Scenario 2: Reference dry (K=0.20)
    ref_K_dry = 0.20
    torque_dry = ref_K_dry * safe_force * (thread.major_dia / 1000)
    torque_dry_pm = torque_dry * 0.10
    print(f"Reference torque (dry, K=0.20): {torque_dry:.2f} Nm ± {torque_dry_pm:.2f} Nm (10%)")

    # Scenario 3: Reference lubricated (K=0.14)
    ref_K_lub = 0.14
    torque_lub = ref_K_lub * safe_force * (thread.major_dia / 1000)
    torque_lub_pm = torque_lub * 0.10
    print(f"Reference torque (lubricated, K=0.14): {torque_lub:.2f} Nm ± {torque_lub_pm:.2f} Nm (10%)")

    # Scenario 4: Max torque at yield (no safety margin)
    max_force_yield = weakest_limit  # Not divided by 1.5
    torque_yield = bolt_mat.friction_coeff * max_force_yield * (thread.major_dia / 1000)
    torque_yield_pm = torque_yield * 0.10
    print(f"MAX torque (at yield, K={bolt_mat.friction_coeff:.2f}): {torque_yield:.2f} Nm ± {torque_yield_pm:.2f} Nm (10%)")

    # --- Copper Gasket Compression (dynamic diameters) ---
    gasket_pressure = 40   # MPa (typical copper gasket sealing pressure)
    gasket_outer_dia = thread.head_dia
    gasket_inner_dia = thread.major_dia

    gasket_force, gasket_area = gasket_compression_force(
        gasket_outer_dia, gasket_inner_dia, gasket_pressure
    )
    gasket_torque = torque_from_force(gasket_force, thread, bolt_mat)
    gasket_torque_pm = gasket_torque * 0.10

    import math
    compression_area = math.pi / 4 * (thread.head_dia ** 2 - thread.major_dia ** 2)
    compression_force = compression_area * gasket_pressure  # N
    compression_torque = torque_from_force(compression_force, thread, bolt_mat)
    compression_torque_pm = compression_torque * 0.10

    print("\n--- Copper Gasket Compression ---")
    print(f"Gasket OD (head): {gasket_outer_dia:.2f} mm, ID (thread): {gasket_inner_dia:.2f} mm, Required Pressure: {gasket_pressure} MPa")
    print(f"Gasket area: {gasket_area:.1f} mm²")
    print(f"Required compression force (gasket only): {gasket_force/1000:.2f} kN")
    
    k_mat = bolt_mat.friction_coeff
    # Gasket torque - material K
    gasket_torque_mat = k_mat * gasket_force * (thread.major_dia / 1000)
    gasket_torque_mat_pm = gasket_torque_mat * 0.10
    print(f"Torque required to reach gasket force (material K={k_mat:.2f}): {gasket_torque_mat:.2f} Nm ± {gasket_torque_mat_pm:.2f} Nm (10%)")
    # Gasket torque - dry
    gasket_torque_dry = 0.20 * gasket_force * (thread.major_dia / 1000)
    gasket_torque_dry_pm = gasket_torque_dry * 0.10
    print(f"Torque for gasket force (dry, K=0.20): {gasket_torque_dry:.2f} Nm ± {gasket_torque_dry_pm:.2f} Nm (10%)")
    # Gasket torque - lubricated
    gasket_torque_lub = 0.14 * gasket_force * (thread.major_dia / 1000)
    gasket_torque_lub_pm = gasket_torque_lub * 0.10
    print(f"Torque for gasket force (lubricated, K=0.14): {gasket_torque_lub:.2f} Nm ± {gasket_torque_lub_pm:.2f} Nm (10%)")
    
    print(f"Bolt head Ø: {thread.head_dia:.2f} mm, Thread Ø: {thread.major_dia:.2f} mm")
    print(f"Compression area under head (bolt head - thread): {compression_area:.1f} mm²")
    print(f"Required compression force under head: {compression_force/1000:.2f} kN")
    
    # Under-head torque - material K
    compression_torque_mat = k_mat * compression_force * (thread.major_dia / 1000)
    compression_torque_mat_pm = compression_torque_mat * 0.10
    print(f"Torque for this area/force (material K={k_mat:.2f}): {compression_torque_mat:.2f} Nm ± {compression_torque_mat_pm:.2f} Nm (10%)")
    # Under-head torque - dry
    compression_torque_dry = 0.20 * compression_force * (thread.major_dia / 1000)
    compression_torque_dry_pm = compression_torque_dry * 0.10
    print(f"Torque for this area/force (dry, K=0.20): {compression_torque_dry:.2f} Nm ± {compression_torque_dry_pm:.2f} Nm (10%)")
    # Under-head torque - lubricated
    compression_torque_lub = 0.14 * compression_force * (thread.major_dia / 1000)
    compression_torque_lub_pm = compression_torque_lub * 0.10
    print(f"Torque for this area/force (lubricated, K=0.14): {compression_torque_lub:.2f} Nm ± {compression_torque_lub_pm:.2f} Nm (10%)")
