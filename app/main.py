import tkinter as tk
from tkinter import filedialog, messagebox
import json
import threading

from config import load_config
from profiles import load_profiles, save_profiles
from estimator import estimate
from planner import build_plan
from hash_preview import preview_pdf
from progress import simulate_progress

# --------------------
# Load configuration
# --------------------
cfg = load_config()
profiles = load_profiles()
selected_pdf = ""

# --------------------
# GUI setup
# --------------------
root = tk.Tk()
root.title("PDF Recovery Framework")
root.geometry("800x650")

# --------------------
# Output area
# --------------------
output = tk.Text(root, height=18, width=95)
output.pack(pady=10)

# --------------------
# Profile selector
# --------------------
profile_var = tk.StringVar(value=cfg.get("DEFAULT_PROFILE", "bank_bill"))

tk.Label(root, text="Profile").pack()
profile_menu = tk.OptionMenu(root, profile_var, *profiles.keys())
profile_menu.pack()

# --------------------
# PDF picker
# --------------------
def pick_pdf():
    global selected_pdf
    selected_pdf = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")]
    )
    pdf_label.config(text=selected_pdf if selected_pdf else "No file selected")

tk.Button(root, text="Pick PDF", command=pick_pdf).pack()
pdf_label = tk.Label(root, text="No file selected")
pdf_label.pack(pady=5)

# --------------------
# Hash / encryption preview
# --------------------
def show_preview():
    output.insert(tk.END, "\n--- PDF Encryption Preview ---\n")
    preview = preview_pdf(selected_pdf)
    output.insert(tk.END, json.dumps(preview, indent=2) + "\n")

tk.Button(root, text="Preview PDF Encryption", command=show_preview).pack(pady=5)

# --------------------
# Progress simulation
# --------------------
progress_var = tk.IntVar()
progress_bar = tk.Scale(
    root,
    variable=progress_var,
    from_=0,
    to=100,
    orient="horizontal",
    length=500,
    label="Simulated Progress"
)
progress_bar.pack(pady=5)

def run_simulation():
    progress_var.set(0)

    def update(val):
        progress_var.set(val)
        root.update_idletasks()

    threading.Thread(
        target=simulate_progress,
        args=(update,),
        daemon=True
    ).start()

tk.Button(root, text="Simulate Progress", command=run_simulation).pack(pady=5)

# --------------------
# Build plan
# --------------------
def build():
    if not selected_pdf:
        messagebox.showwarning("Missing file", "Please select a PDF file first.")
        return

    profile = profile_var.get()
    p = profiles.get(profile)

    letters = p.get("letters", 0)
    digits = p.get("digits", 0)

    est = estimate(
        letters,
        digits,
        int(cfg["CPU_GUESSES_PER_SEC"]),
        int(cfg["GPU_GUESSES_PER_SEC"])
    )

    plan = build_plan(
        p["tool"],
        p["attack"],
        selected_pdf,
        letters,
        digits
    )

    output.delete("1.0", tk.END)
    output.insert(tk.END, json.dumps({
        "profile": profile,
        "estimate": est,
        "plan": plan
    }, indent=2))

    export_btn.config(command=lambda: export_plan(plan))

tk.Button(root, text="Build Plan", command=build).pack(pady=8)

# --------------------
# Export plan
# --------------------
def export_plan(plan):
    path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON", "*.json")]
    )
    if path:
        with open(path, "w") as f:
            json.dump(plan, f, indent=2)
        messagebox.showinfo("Exported", "Plan exported successfully")

export_btn = tk.Button(root, text="Export Plan to JSON")
export_btn.pack(pady=5)

# --------------------
# Profile editor
# --------------------
def edit_profile():
    win = tk.Toplevel(root)
    win.title("Edit / Add Profile")

    tk.Label(win, text="Profile name").grid(row=0, column=0)
    name = tk.Entry(win)
    name.grid(row=0, column=1)

    tk.Label(win, text="Tool (hashcat / pdfrip)").grid(row=1, column=0)
    tool = tk.Entry(win)
    tool.grid(row=1, column=1)

    tk.Label(win, text="Attack").grid(row=2, column=0)
    attack = tk.Entry(win)
    attack.grid(row=2, column=1)

    tk.Label(win, text="Letters").grid(row=3, column=0)
    letters = tk.Entry(win)
    letters.grid(row=3, column=1)

    tk.Label(win, text="Digits").grid(row=4, column=0)
    digits = tk.Entry(win)
    digits.grid(row=4, column=1)

    def save():
        profiles[name.get()] = {
            "tool": tool.get(),
            "attack": attack.get(),
            "letters": int(letters.get() or 0),
            "digits": int(digits.get() or 0)
        }
        save_profiles(profiles)

        profile_menu["menu"].add_command(
            label=name.get(),
            command=tk._setit(profile_var, name.get())
        )
        win.destroy()

    tk.Button(win, text="Save Profile", command=save).grid(row=5, column=1)

tk.Button(root, text="Edit Profiles", command=edit_profile).pack(pady=8)

# --------------------
# Start GUI
# --------------------
root.mainloop()