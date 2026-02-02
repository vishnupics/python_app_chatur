import tkinter as tk
from tkinter import ttk
import json
import os
root = tk.Tk()
root.title("Dynamic Textbox Generator")
root.geometry("900x700")
canvas = tk.Canvas(root, highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(canvas)
window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

def resize_canvas(event):
    canvas.itemconfig(window_id, width=event.width)

canvas.bind("<Configure>", resize_canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.configure(yscrollcommand=scrollbar.set)
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

feature_entries = []
category_entries = []
tk.Label(
    scrollable_frame,
    text="Multilayered and Multidimensional Quality Control\nDuring Data Management",
    font=("Arial", 18, "bold"),
    justify="center"
).pack(pady=15)


tk.Label(scrollable_frame, text="Team Members", font=("Arial", 12, "bold")).pack()
tk.Label(
    scrollable_frame,
    text="Chaturvyuha   |   Gayathri   |   Sarvani   |   Bhargav",
    font=("Arial", 11)
).pack(pady=5)

main_frame = tk.Frame(scrollable_frame)
main_frame.pack(pady=20)

def build_feature_category_frames():
    global feature_frame, category_frame
    global feature_entry, category_entry
    global feature_boxes_frame, category_boxes_frame
    global feature_entries, category_entries

    feature_entries.clear()
    category_entries.clear()
    feature_frame = tk.LabelFrame(main_frame, text="Features", font=("Arial", 12, "bold"), padx=20, pady=10)
    feature_frame.grid(row=0, column=0, padx=40, sticky="n")

    tk.Label(feature_frame, text="Number of features:").pack(anchor="w")
    feature_entry = tk.Entry(feature_frame, width=5)
    feature_entry.pack(anchor="w", pady=5)

    feature_boxes_frame = tk.Frame(feature_frame)
    feature_boxes_frame.pack()

    def generate_features():
        feature_entries.clear()
        for w in feature_boxes_frame.winfo_children():
            w.destroy()

        try:
            count = int(feature_entry.get())
        except ValueError:
            return

        for i in range(count):
            row = tk.Frame(feature_boxes_frame)
            row.pack(pady=3)
            tk.Label(row, text=f"Feature {i+1}:", width=12, anchor="w").pack(side="left")
            entry = tk.Entry(row, width=25)
            entry.pack(side="left")
            feature_entries.append(entry)

    tk.Button(feature_frame, text="Generate Features", font=("Arial", 10, "bold"),
              command=generate_features).pack(pady=5)

   
    category_frame = tk.LabelFrame(main_frame, text="Categories", font=("Arial", 12, "bold"), padx=20, pady=10)
    category_frame.grid(row=0, column=1, padx=40, sticky="n")

    tk.Label(category_frame, text="Number of categories:").pack(anchor="w")
    category_entry = tk.Entry(category_frame, width=5)
    category_entry.pack(anchor="w", pady=5)

    category_boxes_frame = tk.Frame(category_frame)
    category_boxes_frame.pack()

    def generate_categories():
        category_entries.clear()
        for w in category_boxes_frame.winfo_children():
            w.destroy()

        try:
            count = int(category_entry.get())
        except ValueError:
            return

        for i in range(count):
            row = tk.Frame(category_boxes_frame)
            row.pack(pady=3)
            tk.Label(row, text=f"Category {i+1}:", width=12, anchor="w").pack(side="left")
            entry = tk.Entry(row, width=25)
            entry.pack(side="left")
            category_entries.append(entry)

    tk.Button(category_frame, text="Generate Categories", font=("Arial", 10, "bold"),
              command=generate_categories).pack(pady=5)

build_feature_category_frames()

target_frame = tk.LabelFrame(scrollable_frame, text="Target Element Feature",
                             font=("Arial", 12, "bold"), padx=20, pady=10)
target_frame.pack(pady=15)

target_entry = tk.Entry(target_frame, width=40)
target_entry.pack(pady=5)

missing_frame = tk.LabelFrame(scrollable_frame, text="Missing Values Handling",
                              font=("Arial", 12, "bold"), padx=20, pady=15)
missing_frame.pack(pady=15)


num_frame = tk.Frame(missing_frame)
num_frame.pack(pady=6)

tk.Label(num_frame, text="Numerical Data:", width=18, anchor="w",
         font=("Arial", 11, "bold")).pack(side="left")

num_option = tk.StringVar()
num_dropdown = ttk.Combobox(
    num_frame,
    textvariable=num_option,
    values=["Mean", "bfill", "afill", "Elimination"],
    state="readonly",
    width=22
)
num_dropdown.set("Select Method")
num_dropdown.pack(side="left", padx=10)


str_frame = tk.Frame(missing_frame)
str_frame.pack(pady=6)

tk.Label(str_frame, text="String Data:", width=18, anchor="w",
         font=("Arial", 11, "bold")).pack(side="left")

string_entry = tk.Entry(str_frame, width=25, fg="grey")
string_entry.pack(side="left", padx=10)
string_entry.insert(0, "Keep or Eliminate")

def on_focus_in(e):
    if string_entry.get() == "Keep or Eliminate":
        string_entry.delete(0, tk.END)
        string_entry.config(fg="black")

def on_focus_out(e):
    if string_entry.get() == "":
        string_entry.insert(0, "Keep or Eliminate")
        string_entry.config(fg="grey")

string_entry.bind("<FocusIn>", on_focus_in)
string_entry.bind("<FocusOut>", on_focus_out)

encoding_frame = tk.LabelFrame(scrollable_frame, text="Is Encoding Required?",
                               font=("Arial", 12, "bold"), padx=20, pady=10)
encoding_frame.pack(pady=15)

encoding_choice = tk.StringVar(value="No")
tk.Radiobutton(encoding_frame, text="Yes", variable=encoding_choice,
               value="Yes").pack(side="left", padx=20)
tk.Radiobutton(encoding_frame, text="No", variable=encoding_choice,
               value="No").pack(side="left", padx=20)

button_frame = tk.Frame(scrollable_frame)
button_frame.pack(pady=30)

def reset_action():
    feature_frame.destroy()
    category_frame.destroy()
    build_feature_category_frames()

    target_entry.delete(0, tk.END)
    num_dropdown.set("Select Method")
    string_entry.delete(0, tk.END)
    string_entry.insert(0, "Keep or Eliminate")
    string_entry.config(fg="grey")
    encoding_choice.set("No")

    scrollable_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(0)

def proceed_action():
    data = {
        "features": [e.get() for e in feature_entries if e.get()],
        "categories": [e.get() for e in category_entries if e.get()],
        "target_feature": target_entry.get(),
        "missing_values": {
            "numerical": num_option.get(),
            "string": string_entry.get()
        },
        "encoding_required": encoding_choice.get()
    }

    with open("project_config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    os.startfile("project_config.json")

tk.Button(
    button_frame,
    text="Proceed",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    height=2,
    command=proceed_action
).pack(side="left", padx=20)

tk.Button(
    button_frame,
    text="Reset",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    width=15,
    height=2,
    command=reset_action
).pack(side="left", padx=20)

root.mainloop()
