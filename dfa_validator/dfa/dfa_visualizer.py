import tkinter as tk
import time
import threading

# ---------- DFA Definitions ----------
CAPTIONS = {
    "Password": {
        "q0": "Start",
        "q1": "Has lowercase",
        "q2": "Has uppercase",
        "q3": "Has digit",
        "q4": "Has special character (Accept)"
    },

    "Email": {
        "q0": "Start",
        "q1": "Local part",
        "q2": "Contains @",
        "q3": "Domain & TLD (Accept)"
    },

    "URL": {
        "q0": "Start",
        "q1": "Protocol (http/https)",
        "q2": "Domain name",
        "q3": "Valid TLD (Accept)"
    },

    "Phone": {
        "q0": "Start",
        "q1": "Digit sequence",
        "q2": "Valid length (Accept)"
    }
}

DFAS = {
    "Password": {
        "states": ["q0", "q1", "q2", "q3", "q4"],
        "accept": "q4",
        "transition": lambda state, ch: {
            "q0": "q1" if ch.islower() else "q0",
            "q1": "q2" if ch.isupper() else "q1",
            "q2": "q3" if ch.isdigit() else "q2",
            "q3": "q4" if not ch.isalnum() else "q3",
            "q4": "q4"
        }[state]
    },

    "Email": {
    "states": ["q0", "q1", "q2", "q3"],
    "accept": "q3",
    "transition": lambda state, ch: (
        "qd" if ch.isspace() else
        {
            "q0": "q1" if ch.isalnum() else "qd",
            "q1": "q1" if ch.isalnum() else ("q2" if ch == "@" else "qd"),
            "q2": "q3" if ch.isalpha() else "qd",
            "q3": "q3" if ch.isalpha() or ch == "." else "qd",
            "qd": "qd"
        }[state]
    )
    },

    "URL": {
        "states": ["q0", "q1", "q2", "q3"],
        "accept": "q3",
        "transition": lambda state, ch: {
            "q0": "q1" if ch.isalpha() else "q0",
            "q1": "q2" if ch == "." else "q1",
            "q2": "q3" if ch.isalpha() else "q2",
            "q3": "q3"
        }[state]
    },

    "Phone": {
        "states": ["q0", "q1", "q2"],
        "accept": "q2",
        "transition": lambda state, ch: {
            "q0": "q1" if ch.isdigit() else "q0",
            "q1": "q2" if ch.isdigit() else "q1",
            "q2": "q2"
        }[state]
    }
}


# ---------- GUI ----------
root = tk.Tk()
root.title("Animated DFA Visualizer")
root.geometry("820x500")

canvas = tk.Canvas(root, width=800, height=250)
canvas.pack(pady=10)

input_var = tk.StringVar()
model_var = tk.StringVar(value="Password")
status_var = tk.StringVar(value="Enter input and start")

# ---------- Controls ----------
control = tk.Frame(root)
control.pack()

tk.Label(control, text="Input:").grid(row=0, column=0)
tk.Entry(control, textvariable=input_var, width=30).grid(row=0, column=1)

tk.Label(control, text="Model:").grid(row=0, column=2)
tk.OptionMenu(control, model_var, *DFAS.keys()).grid(row=0, column=3)

tk.Label(root, textvariable=status_var, font=("Arial", 12)).pack(pady=10)

# ---------- Drawing ----------
def draw_states(states, current, accept, model):
    canvas.delete("all")

    x, y = 80, 130
    r = 30

    for i, state in enumerate(states):
        cx = x + i * 150
        cy = y

        # Highlight current state
        color = "lightgreen" if state == current else "white"

        # State circle
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color)
        canvas.create_text(cx, cy, text=state, font=("Arial", 10, "bold"))

        # Accept state (double circle)
        if state == accept:
            canvas.create_oval(cx-r+5, cy-r+5, cx+r-5, cy+r-5)

        # Caption below state
        caption = CAPTIONS[model][state]
        canvas.create_text(cx, cy + 45, text=caption, font=("Arial", 9))

        # Arrow to next state
        if i < len(states) - 1:
            canvas.create_line(cx+r, cy, cx+150-r, cy, arrow=tk.LAST)


# ---------- Animation ----------
def animate():
    model = model_var.get()
    dfa = DFAS[model]

    state = dfa["states"][0]
    status_var.set("Processing...")
    draw_states(dfa["states"], state, dfa["accept"], model)

    for ch in input_var.get():
        time.sleep(0.8)
        state = dfa["transition"](state, ch)
        draw_states(dfa["states"], state, dfa["accept"], model)

    if state == dfa["accept"]:
        status_var.set("✔ ACCEPTED")
    else:
        status_var.set("✖ REJECTED")


def start_animation():
    threading.Thread(target=animate).start()


tk.Button(root, text="Start DFA", command=start_animation).pack(pady=5)

root.mainloop()
