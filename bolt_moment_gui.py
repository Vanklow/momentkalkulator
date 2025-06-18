# bolt_moment_gui – GUI for Bolt Moment Calculator (wide layout, with manual material inputs)

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from metric_threads import metric_threads
from materials import materials
from main import (
    bolt_tensile_capacity,
    thread_strip_out,
    torque_from_force,
    gasket_compression_force
)
from friction_data import friction_table


# --- Root setup ---
root = tk.Tk()
root.title("Bolt Moment Calculator GUI (Wide Layout)")
root.columnconfigure(0, weight=0, minsize=460)
root.columnconfigure(1, weight=1, minsize=700)

# ---- Input panel ----
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, sticky='nswe', padx=8, pady=8)
row_i = 0

# --- Thread type ---
ttk.Label(input_frame, text="Thread type:").grid(row=row_i, column=0, sticky='e')
thread_type_var = tk.StringVar()
thread_type_menu = ttk.Combobox(input_frame, textvariable=thread_type_var, values=list(metric_threads.keys()), state='readonly')
thread_type_menu.grid(row=row_i, column=1, sticky='w')

# --- Thread size ---
ttk.Label(input_frame, text="Thread size:").grid(row=row_i, column=2, sticky='e')
thread_var = tk.StringVar()
thread_menu = ttk.Combobox(input_frame, textvariable=thread_var, state='readonly')
thread_menu.grid(row=row_i, column=3, sticky='w')
row_i += 1

# --- Bolt material ---
ttk.Label(input_frame, text="Bolt material:").grid(row=row_i, column=0, sticky='e')
bolt_type_var = tk.StringVar()
bolt_type_menu = ttk.Combobox(input_frame, textvariable=bolt_type_var, values=list(materials.keys()), state='readonly')
bolt_type_menu.grid(row=row_i, column=1, sticky='w')

# --- Bolt grade ---
ttk.Label(input_frame, text="Bolt grade:").grid(row=row_i, column=2, sticky='e')
bolt_mat_var = tk.StringVar()
bolt_mat_menu = ttk.Combobox(input_frame, textvariable=bolt_mat_var, state='readonly')
bolt_mat_menu.grid(row=row_i, column=3, sticky='w')

# --- Bolt manual yield strength ---
ttk.Label(input_frame, text="Yield strength [MPa]:").grid(row=row_i, column=4, sticky='e')
bolt_yield_entry = ttk.Entry(input_frame, width=10)
bolt_yield_entry.grid(row=row_i, column=5, sticky='w')

# --- Bolt manual tensile strength ---
ttk.Label(input_frame, text="Tensile strength [MPa]:").grid(row=row_i, column=6, sticky='e')
bolt_tensile_entry = ttk.Entry(input_frame, width=10)
bolt_tensile_entry.grid(row=row_i, column=7, sticky='w')

row_i += 1

# --- Nut material ---
ttk.Label(input_frame, text="Nut material:").grid(row=row_i, column=0, sticky='e')
nut_type_var = tk.StringVar()
nut_type_menu = ttk.Combobox(input_frame, textvariable=nut_type_var, values=list(materials.keys()), state='readonly')
nut_type_menu.grid(row=row_i, column=1, sticky='w')

# --- Nut grade ---
ttk.Label(input_frame, text="Nut grade:").grid(row=row_i, column=2, sticky='e')
nut_mat_var = tk.StringVar()
nut_mat_menu = ttk.Combobox(input_frame, textvariable=nut_mat_var, state='readonly')
nut_mat_menu.grid(row=row_i, column=3, sticky='w')

# --- Nut manual yield strength ---
ttk.Label(input_frame, text="Yield strength [MPa]:").grid(row=row_i, column=4, sticky='e')
nut_yield_entry = ttk.Entry(input_frame, width=10)
nut_yield_entry.grid(row=row_i, column=5, sticky='w')

# --- Nut manual tensile strength ---
ttk.Label(input_frame, text="Tensile strength [MPa]:").grid(row=row_i, column=6, sticky='e')
nut_tensile_entry = ttk.Entry(input_frame, width=10)
nut_tensile_entry.grid(row=row_i, column=7, sticky='w')

# --- Nut manual friction coefficient ---
nut_friction_label = ttk.Label(input_frame, text="Friction coefficient:")
nut_friction_label.grid(row=row_i, column=8, sticky='e')
nut_friction_entry = ttk.Entry(input_frame, width=10)
nut_friction_entry.grid(row=row_i, column=9, sticky='w')
row_i += 1

# --- Plate material ---
ttk.Label(input_frame, text="Plate material:").grid(row=row_i, column=0, sticky='e')
plate_type_var = tk.StringVar()
plate_type_menu = ttk.Combobox(input_frame, textvariable=plate_type_var, values=list(materials.keys()), state='readonly')
plate_type_menu.grid(row=row_i, column=1, sticky='w')

# --- Plate grade ---
ttk.Label(input_frame, text="Plate grade:").grid(row=row_i, column=2, sticky='e')
plate_mat_var = tk.StringVar()
plate_mat_menu = ttk.Combobox(input_frame, textvariable=plate_mat_var, state='readonly')
plate_mat_menu.grid(row=row_i, column=3, sticky='w')

# --- Plate manual yield strength ---
ttk.Label(input_frame, text="Yield strength [MPa]:").grid(row=row_i, column=4, sticky='e')
plate_yield_entry = ttk.Entry(input_frame, width=10)
plate_yield_entry.grid(row=row_i, column=5, sticky='w')

# --- Plate manual tensile strength ---
ttk.Label(input_frame, text="Tensile strength [MPa]:").grid(row=row_i, column=6, sticky='e')
plate_tensile_entry = ttk.Entry(input_frame, width=10)
plate_tensile_entry.grid(row=row_i, column=7, sticky='w')

# --- Plate manual friction coefficient ---
plate_friction_label = ttk.Label(input_frame, text="Friction coefficient:")
plate_friction_label.grid(row=row_i, column=8, sticky='e')
plate_friction_entry = ttk.Entry(input_frame, width=10)
plate_friction_entry.grid(row=row_i, column=9, sticky='w')
row_i += 1

from gasket_materials import gasket_materials  # import your new gasket library

# --- Lubrication / Surface Condition ---
ttk.Label(input_frame, text="Lubrication:").grid(row=row_i, column=0, sticky='e')
lubrication_var = tk.StringVar(value="Dry")
ttk.Combobox(input_frame, textvariable=lubrication_var, values=["Dry", "Oiled", "Waxed", "Threadlock"], state='readonly').grid(row=row_i, column=1, sticky='w')
row_i += 1

# --- Gasket material ---
ttk.Label(input_frame, text="Gasket material:").grid(row=row_i, column=0, sticky='e')
gasket_type_var = tk.StringVar()
gasket_type_menu = ttk.Combobox(input_frame, textvariable=gasket_type_var, values=list(gasket_materials.keys()), state='readonly')
gasket_type_menu.grid(row=row_i, column=1, sticky='w')

# --- Gasket sealing pressure manual ---
ttk.Label(input_frame, text="Sealing pressure [MPa]:").grid(row=row_i, column=2, sticky='e')
gasket_pressure_entry = ttk.Entry(input_frame, width=10)
gasket_pressure_entry.grid(row=row_i, column=3, sticky='w')

# --- Gasket friction coefficient manual ---
ttk.Label(input_frame, text="Friction coefficient:").grid(row=row_i, column=4, sticky='e')
gasket_friction_entry = ttk.Entry(input_frame, width=10)
gasket_friction_entry.grid(row=row_i, column=5, sticky='w')

row_i += 1

# --- Function to fill gasket manual inputs ---
def on_gasket_material_change(*args):
    material = gasket_materials.get(gasket_type_var.get())
    if material:
        gasket_pressure_entry.delete(0, tk.END)
        gasket_pressure_entry.insert(0, str(material.sealing_pressure))
        gasket_friction_entry.delete(0, tk.END)
        gasket_friction_entry.insert(0, str(material.friction_coeff))
    else:
        gasket_pressure_entry.delete(0, tk.END)
        gasket_friction_entry.delete(0, tk.END)

# --- Bind gasket material dropdown change ---
gasket_type_var.trace_add('write', on_gasket_material_change)

# --- Modify run_calc() to read gasket manual inputs ---
# (All reading is handled inside run_calc(); no global try/except needed)

# --- Plate engagement [mm] ---
ttk.Label(input_frame, text="Plate engagement [mm]:").grid(row=row_i, column=0, sticky='e')
engagement_entry = ttk.Entry(input_frame, width=10)
engagement_entry.insert(0, "10")
engagement_entry.grid(row=row_i, column=1, sticky='w')

# --- Nut engagement [mm] ---
ttk.Label(input_frame, text="Nut engagement [mm]:").grid(row=row_i, column=2, sticky='e')
nut_engagement_entry = ttk.Entry(input_frame, width=10)
nut_engagement_entry.insert(0, "8")
nut_engagement_entry.grid(row=row_i, column=3, sticky='w')
row_i += 1

# --- Connection Type Radio Buttons ---
connection_type_var = tk.StringVar(value="Nut")
connection_frame = ttk.LabelFrame(input_frame, text="Connection type")
connection_frame.grid(row=row_i, column=0, columnspan=6, sticky='w', pady=(8,0))
ttk.Radiobutton(connection_frame, text="Nut", variable=connection_type_var, value="Nut").grid(row=0, column=0, sticky='w', padx=(4, 12))
ttk.Radiobutton(connection_frame, text="Threaded Plate", variable=connection_type_var, value="Plate").grid(row=0, column=1, sticky='w', padx=(0, 12))
row_i += 1

# --- Show only nut or plate friction K field ---
def update_friction_fields(*args):
    if connection_type_var.get() == "Nut":
        nut_friction_entry.config(state='normal')
        nut_friction_label.grid()
        nut_friction_entry.grid()
        plate_friction_entry.config(state='disabled')
        plate_friction_label.grid_remove()
        plate_friction_entry.grid_remove()
    else:
        plate_friction_entry.config(state='normal')
        plate_friction_label.grid()
        plate_friction_entry.grid()
        nut_friction_entry.config(state='disabled')
        nut_friction_label.grid_remove()
        nut_friction_entry.grid_remove()
connection_type_var.trace_add('write', update_friction_fields)
update_friction_fields()

# --- Include Gasket Checkbox ---
include_gasket_var = tk.BooleanVar(value=True)
ttk.Checkbutton(input_frame, text="Include gasket calculations", variable=include_gasket_var).grid(row=row_i, column=0, columnspan=4, sticky='w')
row_i += 1

# --- Safety Factor ---
ttk.Label(input_frame, text="Safety factor:").grid(row=row_i, column=0, sticky='e')
safety_factor_entry = ttk.Entry(input_frame, width=10)
safety_factor_entry.insert(0, "1.5")
safety_factor_entry.grid(row=row_i, column=1, sticky='w')
row_i += 1

# --- Use percent of yield option ---
use_percent_var = tk.BooleanVar(value=False)
ttk.Checkbutton(input_frame, text="Use preload as percent of yield", variable=use_percent_var).grid(row=row_i, column=0, sticky='w')
preload_percent_entry = ttk.Entry(input_frame, width=6)
preload_percent_entry.insert(0, "78")
ttk.Label(input_frame, text="% of yield").grid(row=row_i, column=1, sticky='w')
preload_percent_entry.grid(row=row_i, column=2, sticky='w')
row_i += 1




# --- Functions to update manual material fields from dropdown selections ---

def fill_material_fields(material_obj, yield_entry, tensile_entry, friction_entry=None):
    if material_obj:
        yield_entry.delete(0, tk.END)
        yield_entry.insert(0, str(material_obj.yield_strength))
        tensile_entry.delete(0, tk.END)
        tensile_entry.insert(0, str(material_obj.tensile_strength))
        if friction_entry is not None:
            friction_entry.delete(0, tk.END)
            friction_entry.insert(0, str(material_obj.friction_coeff))
    else:
        yield_entry.delete(0, tk.END)
        tensile_entry.delete(0, tk.END)
        if friction_entry is not None:
            friction_entry.delete(0, tk.END)

def on_bolt_material_change(*args):
    mat_type = bolt_type_var.get()
    grade = bolt_mat_var.get()
    material = materials.get(mat_type, {}).get(grade)
    fill_material_fields(material, bolt_yield_entry, bolt_tensile_entry)

def on_nut_material_change(*args):
    mat_type = nut_type_var.get()
    grade = nut_mat_var.get()
    material = materials.get(mat_type, {}).get(grade)
    fill_material_fields(material, nut_yield_entry, nut_tensile_entry, nut_friction_entry)

def on_plate_material_change(*args):
    mat_type = plate_type_var.get()
    grade = plate_mat_var.get()
    material = materials.get(mat_type, {}).get(grade)
    fill_material_fields(material, plate_yield_entry, plate_tensile_entry, plate_friction_entry)

# --- K-value suggestion ---
def suggest_bolt_friction(*args):
    bolt_mat = bolt_type_var.get()
    lube = lubrication_var.get()
    if connection_type_var.get() == "Nut":
        mating_mat = nut_type_var.get()
        k = friction_table.get((bolt_mat, mating_mat, lube))
        if k is not None:
            nut_friction_entry.delete(0, tk.END)
            nut_friction_entry.insert(0, f"{k:.2f}")
    else:
        mating_mat = plate_type_var.get()
        k = friction_table.get((bolt_mat, mating_mat, lube))
        if k is not None:
            plate_friction_entry.delete(0, tk.END)
            plate_friction_entry.insert(0, f"{k:.2f}")

# --- Calculation function ---

def run_calc():
    try:
        # --- Thread selection ---
        thread_type = thread_type_var.get()
        thread_val = thread_var.get()
        thread_dict = metric_threads.get(thread_type, {})
        thread = thread_dict.get(thread_val)
        if not thread:
            output_box.delete('1.0', tk.END)
            output_box.insert(tk.END, "Error: Invalid thread type or thread selected.\n")
            return

        # --- Bolt material properties (manual override) ---
        bolt_yield = try_float(bolt_yield_entry.get())
        bolt_tensile = try_float(bolt_tensile_entry.get())
        if bolt_yield is None or bolt_tensile is None:
            output_box.delete('1.0', tk.END)
            output_box.insert(tk.END, "Error: Invalid numeric input for bolt material properties.\n")
            return

        # --- Nut material properties ---
        nut_yield = try_float(nut_yield_entry.get())
        nut_tensile = try_float(nut_tensile_entry.get())
        nut_friction = try_float(nut_friction_entry.get())
        if nut_yield is None or nut_tensile is None or nut_friction is None:
            output_box.delete('1.0', tk.END)
            output_box.insert(tk.END, "Error: Invalid numeric input for nut material properties.\n")
            return

        # --- Plate material properties ---
        plate_yield = try_float(plate_yield_entry.get())
        plate_tensile = try_float(plate_tensile_entry.get())
        plate_friction = try_float(plate_friction_entry.get())
        if plate_yield is None or plate_tensile is None or plate_friction is None:
            output_box.delete('1.0', tk.END)
            output_box.insert(tk.END, "Error: Invalid numeric input for plate material properties.\n")
            return

        # --- Gasket material properties ---
        gasket_pressure = try_float(gasket_pressure_entry.get())
        gasket_friction = try_float(gasket_friction_entry.get())
        if gasket_pressure is None:
            gasket_pressure = 40.0  # fallback default
        if gasket_friction is None:
            gasket_friction = 0.25  # fallback default

        # --- Engagement lengths ---
        try:
            engagement_mm = float(engagement_entry.get())
        except Exception:
            engagement_mm = 10.0
        try:
            nut_engagement_mm = float(nut_engagement_entry.get())
        except Exception:
            nut_engagement_mm = 8.0

        # --- Build Material dataclasses from manual inputs ---
        from main import Material
        # Bolt friction not used for torque, so just set to 0.15
        bolt_material = Material("Bolt manual", bolt_yield, bolt_tensile, 0.15)
        nut_material = Material("Nut manual", nut_yield, nut_tensile, nut_friction)
        plate_material = Material("Plate manual", plate_yield, plate_tensile, plate_friction)

        # --- Calculate limiting modes ---
        if connection_type_var.get() == "Nut":
            limiting_modes = {
                "Bolt Tensile": bolt_tensile_capacity(thread, bolt_material),
                "Nut Thread Strip-Out": thread_strip_out(thread, nut_material, nut_engagement_mm),
            }
        else:
            limiting_modes = {
                "Bolt Tensile": bolt_tensile_capacity(thread, bolt_material),
                "Threaded Plate Strip-Out": thread_strip_out(thread, plate_material, engagement_mm),
            }
        weakest_mode = min(limiting_modes, key=limiting_modes.get)
        weakest_limit = limiting_modes[weakest_mode]

        if use_percent_var.get():
            try:
                preload_pct = float(preload_percent_entry.get()) / 100.0
                if not (0 < preload_pct < 1):
                    preload_pct = 0.78
            except Exception:
                preload_pct = 0.78
            safe_force = weakest_limit * preload_pct
            sf_mode_note = f"Preload set to {preload_pct*100:.0f}% of {weakest_mode} ({safe_force/1000:.2f} kN)"
        else:
            try:
                safety_factor = float(safety_factor_entry.get())
                if safety_factor <= 0:
                    safety_factor = 1.5
            except Exception:
                safety_factor = 1.5
            safe_force = weakest_limit / safety_factor
            sf_mode_note = f"Recommended clamping force (SF={safety_factor:.2f} on {weakest_mode}): {safe_force/1000:.2f} kN"

        # === Torque Range Calculation ===
        d_m = thread.major_dia / 1000
        K_min = 0.10
        K_max = 0.25

        # Use only the active K (nut or plate) for all torque calcs
        if connection_type_var.get() == "Nut":
            K_typ = nut_material.friction_coeff
        else:
            K_typ = plate_material.friction_coeff

        torque_min = K_min * safe_force * d_m
        torque_typ = K_typ * safe_force * d_m
        torque_max = K_max * safe_force * d_m

        # For max load (no safety factor)
        torque_yield_min = K_min * weakest_limit * d_m
        torque_yield_typ = K_typ * weakest_limit * d_m
        torque_yield_max = K_max * weakest_limit * d_m

        # --- Gasket force and torque (only if included) ---
        gasket_output_lines = []
        if include_gasket_var.get():
            gasket_outer_dia = thread.head_dia
            gasket_inner_dia = thread.major_dia
            gasket_force, gasket_area = gasket_compression_force(gasket_outer_dia, gasket_inner_dia, gasket_pressure)
            gasket_torque_mat = gasket_friction * gasket_force * (thread.major_dia / 1000)
            gasket_torque_mat_pm = gasket_torque_mat * 0.10
            gasket_output_lines.append("--- Gasket Compression ---")
            gasket_output_lines.append(f"Gasket OD (head): {gasket_outer_dia:.2f} mm, ID (thread): {gasket_inner_dia:.2f} mm, Sealing pressure: {gasket_pressure} MPa")
            gasket_output_lines.append(f"Gasket area: {gasket_area:.1f} mm²")
            gasket_output_lines.append(f"Required compression force (gasket only): {gasket_force/1000:.2f} kN")
            gasket_output_lines.append(f"Torque required to reach gasket force (friction K={gasket_friction:.2f}): {gasket_torque_mat:.2f} Nm ± {gasket_torque_mat_pm:.2f} Nm (10%)")
        # --- Output ---
        output = []
        output.append("==== Bolt Joint Calculation ====")
        output.append("All recommended torques use a safety factor of 1.5 unless otherwise noted. Typical K is based on material database or user input. Min/Max use plausible friction bounds for steel joints.")
        output.append(f"Thread: {thread.name}")
        output.append(f"  Major diameter: {thread.major_dia:.2f} mm")
        output.append(f"  Tensile area: {thread.tensile_area:.2f} mm²")
        output.append(f"  Head diameter: {thread.head_dia:.2f} mm")
        output.append(f"Bolt material: {bolt_material.name}")
        output.append(f"  Yield strength: {bolt_material.yield_strength} MPa, Tensile strength: {bolt_material.tensile_strength} MPa")
        if connection_type_var.get() == "Nut":
            output.append(f"Nut material: {nut_material.name}")
            output.append(f"  Yield strength: {nut_material.yield_strength} MPa, Tensile strength: {nut_material.tensile_strength} MPa, Friction coeff.: {nut_material.friction_coeff}")
            output.append(f"Nut engagement: {nut_engagement_mm} mm")
            mating_mat = nut_material.name
        else:
            output.append(f"Plate material: {plate_material.name}")
            output.append(f"  Yield strength: {plate_material.yield_strength} MPa, Tensile strength: {plate_material.tensile_strength} MPa, Friction coeff.: {plate_material.friction_coeff}")
            output.append(f"Plate engagement: {engagement_mm} mm")
            mating_mat = plate_material.name
        output.append(f"Friction coefficient (K): {K_typ:.2f} (for {bolt_material.name}/{mating_mat} [{lubrication_var.get()}])")
        output.append("--- Results ---")
        output.append("NOTE: Thread strip-out uses the thread's internal minor diameter and 60% of material yield strength, per ISO/Machinery's Handbook.")
        output.append(f"Bolt tensile limit: {limiting_modes['Bolt Tensile']/1000:.2f} kN")
        if connection_type_var.get() == "Nut":
            output.append(f"Nut thread strip-out limit: {limiting_modes['Nut Thread Strip-Out']/1000:.2f} kN")
        else:
            output.append(f"Threaded plate strip-out limit: {limiting_modes['Threaded Plate Strip-Out']/1000:.2f} kN")
        output.append(f"Weakest mode: {weakest_mode}")
        output.append("")
        output.append(sf_mode_note)
        output.append("Torque range for safe force (SF=1.5):")
        output.append(f"  Min (K={K_min:.2f}): {torque_min:.2f} Nm")
        output.append(f"  Typ (K={K_typ:.2f}): {torque_typ:.2f} Nm")
        output.append(f"  Max (K={K_max:.2f}): {torque_max:.2f} Nm")
        output.append("")
        output.append("Torque range at yield (no safety factor):")
        output.append(f"  Min (K={K_min:.2f}): {torque_yield_min:.2f} Nm")
        output.append(f"  Typ (K={K_typ:.2f}): {torque_yield_typ:.2f} Nm")
        output.append(f"  Max (K={K_max:.2f}): {torque_yield_max:.2f} Nm")
        output.append("")
        # Calculate resultant compression force from recommended torque (typical K)
        try:
            compression_force_from_torque = torque_typ / (K_typ * (thread.major_dia / 1000))
        except ZeroDivisionError:
            compression_force_from_torque = float('nan')
        output.append(f"Resultant compression force at typical torque: {compression_force_from_torque/1000:.2f} kN")
        output.append("")
        # --- Automatic Safety Warnings ---
        if weakest_mode == "Bolt Tensile":
            if torque_typ > torque_yield_min or torque_max > torque_yield_min:
                output.append("WARNING: The typical or maximum torque in this range can EXCEED the bolt's yield strength if friction is lower than expected (K approaches 0.10).")
                output.append("  - Only use these values if friction is well controlled (e.g., lubricated assembly).")
                output.append("  - For dry/unknown friction, use the MINIMUM torque for safety, or control your process to match the assumed K.")
            output.append("NOTE: If you use a higher torque and friction is lower than expected, the bolt may yield or break. If in doubt, always use the minimum torque in the range.")
        elif weakest_mode == "Nut Thread Strip-Out":
            nut_strip_limit = limiting_modes['Nut Thread Strip-Out']
            torque_nut_strip_min = K_min * nut_strip_limit * d_m
            if torque_typ > torque_nut_strip_min or torque_max > torque_nut_strip_min:
                output.append("WARNING: The typical or maximum torque in this range can EXCEED the nut thread strip-out strength if friction is lower than expected (K approaches 0.10).")
                output.append("  - Only use these values if friction is well controlled (e.g., lubricated assembly).")
                output.append("  - For dry/unknown friction, use the MINIMUM torque for safety, or control your process to match the assumed K.")
            output.append("NOTE: If you use a higher torque and friction is lower than expected, the nut threads may strip. If in doubt, always use the minimum torque in the range.")
        elif weakest_mode == "Threaded Plate Strip-Out":
            plate_strip_limit = limiting_modes['Threaded Plate Strip-Out']
            torque_plate_strip_min = K_min * plate_strip_limit * d_m
            if torque_typ > torque_plate_strip_min or torque_max > torque_plate_strip_min:
                output.append("WARNING: The typical or maximum torque in this range can EXCEED the threaded plate strip-out strength if friction is lower than expected (K approaches 0.10).")
                output.append("  - Only use these values if friction is well controlled (e.g., lubricated assembly).")
                output.append("  - For dry/unknown friction, use the MINIMUM torque for safety, or control your process to match the assumed K.")
            output.append("NOTE: If you use a higher torque and friction is lower than expected, the threaded plate may strip. If in doubt, always use the minimum torque in the range.")
        # Gasket output
        for line in gasket_output_lines:
            output.append(line)

        output_box.delete('1.0', tk.END)
        output_box.tag_configure('red', foreground='red', font=("Consolas", 10, 'bold'))
        output_box.tag_configure('bold', font=("Consolas", 10, 'bold'))
        output_box.tag_configure('section', font=("Consolas", 10, 'bold'))

        for line in output:
            if line.startswith("===="):
                output_box.insert(tk.END, "\n" + line + "\n", 'section')
            elif line.startswith("---"):
                output_box.insert(tk.END, "\n" + line + "\n", 'section')
            elif line.startswith("WARNING") or line.strip().startswith("- "):
                output_box.insert(tk.END, line + "\n", 'red')
            elif (
                line.startswith("Recommended clamping force") or
                line.startswith("Torque range for safe force") or
                line.startswith("Torque range at yield") or
                line.startswith("Resultant compression force") or
                line.startswith("Bolt tensile limit") or
                line.startswith("Nut thread strip-out limit") or
                line.startswith("Threaded plate strip-out limit") or
                line.startswith("Weakest mode:")
            ):
                output_box.insert(tk.END, line + "\n", 'bold')
            else:
                output_box.insert(tk.END, line + "\n")

    except Exception as ex:
        output_box.delete('1.0', tk.END)
        output_box.tag_configure('red', foreground='red', font=("Consolas", 10, 'bold'))
        if 'output' in locals():
            for line in output:
                if line.startswith("WARNING") or line.strip().startswith("- "):
                    output_box.insert(tk.END, line + "\n", 'red')
                else:
                    output_box.insert(tk.END, line + "\n")
        output_box.insert(tk.END, f"\nException: {ex}\n", 'red')
        messagebox.showerror("Error", f"Exception occurred:\n{ex}")

def try_float(s):
    try:
        return float(s)
    except Exception:
        return None


# --- Button ---
ttk.Button(input_frame, text="Calculate", command=run_calc).grid(row=row_i, column=0, columnspan=10, pady=5)
for i in range(row_i+1):
    input_frame.rowconfigure(i, pad=2)

# --- Output panel on the right ---
output_frame = ttk.Frame(root)
output_frame.grid(row=0, column=1, sticky='nswe', padx=8, pady=8)
output_frame.columnconfigure(0, weight=1)
output_box = scrolledtext.ScrolledText(output_frame, width=90, height=48, font=("Consolas", 10))
output_box.tag_configure('bold', font=("Consolas", 10, 'bold'))
output_box.tag_configure('section', font=("Consolas", 10, 'bold'))
output_box.grid(row=0, column=0, sticky='nswe')

# --- Dropdown updaters ---
def update_thread_options(*args):
    thread_type = thread_type_var.get()
    if thread_type in metric_threads:
        size_list = list(metric_threads[thread_type].keys())
    else:
        size_list = []
    thread_menu['values'] = size_list
    if size_list:
        thread_var.set(size_list[0])
    else:
        thread_var.set('')

def update_bolt_material_options(*args):
    mat_type = bolt_type_var.get()
    if mat_type in materials:
        grade_list = list(materials[mat_type].keys())
    else:
        grade_list = []
    bolt_mat_menu['values'] = grade_list
    if grade_list:
        bolt_mat_var.set(grade_list[0])
    else:
        bolt_mat_var.set('')
    on_bolt_material_change()

def update_nut_material_options(*args):
    mat_type = nut_type_var.get()
    if mat_type in materials:
        grade_list = list(materials[mat_type].keys())
    else:
        grade_list = []
    nut_mat_menu['values'] = grade_list
    if grade_list:
        nut_mat_var.set(grade_list[0])
    else:
        nut_mat_var.set('')
    on_nut_material_change()

def update_plate_material_options(*args):
    mat_type = plate_type_var.get()
    if mat_type in materials:
        grade_list = list(materials[mat_type].keys())
    else:
        grade_list = []
    plate_mat_menu['values'] = grade_list
    if grade_list:
        plate_mat_var.set(grade_list[0])
    else:
        plate_mat_var.set('')
    on_plate_material_change()

# --- Hook dropdown updaters ---
lubrication_var.trace_add('write', suggest_bolt_friction)
bolt_type_var.trace_add('write', suggest_bolt_friction)
nut_type_var.trace_add('write', suggest_bolt_friction)
plate_type_var.trace_add('write', suggest_bolt_friction)
connection_type_var.trace_add('write', suggest_bolt_friction)

thread_type_var.trace_add('write', lambda *args: update_thread_options())

bolt_type_var.trace_add('write', lambda *args: update_bolt_material_options())
bolt_mat_var.trace_add('write', lambda *args: on_bolt_material_change())

nut_type_var.trace_add('write', lambda *args: update_nut_material_options())
nut_mat_var.trace_add('write', lambda *args: on_nut_material_change())

plate_type_var.trace_add('write', lambda *args: update_plate_material_options())
plate_mat_var.trace_add('write', lambda *args: on_plate_material_change())


# Initialize dropdowns and manual fields
update_thread_options()
update_bolt_material_options()
update_nut_material_options()
update_plate_material_options()

# --- Ensure friction is auto-populated on startup
suggest_bolt_friction()

# --- Main loop ---
root.mainloop()

