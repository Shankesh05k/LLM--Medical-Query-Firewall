import tkinter as tk
from tkinter import scrolledtext

# -----------------------------
# FIREWALL ENGINE
# -----------------------------

danger_keywords = [
    "dose", "dosage", "mg", "ml", "take", "prescription", "tablet",
    "self medicate", "self-medicate", "pill", "drug", "medication",
    "how many", "how much", "increase", "decrease", "adjust dose"
]

unsafe_intents = [
    "give me dosage", "tell me dosage", "how much should i take",
    "recommend medicine", "give medicine", "prescribe", "suggest medicine"
]

medicine_list = [
    "paracetamol", "ibuprofen", "aspirin", "amoxicillin",
    "azithromycin", "dolo", "metformin", "insulin"
]

# Classifier + rule engine
def firewall_check(query):
    q = query.lower()

    # Rule 1: block if numeric (dose-like queries)
    for token in q.split():
        if token.isdigit():
            return False, "Blocked: Query contains numeric values that may indicate dosage."

    # Rule 2: keyword block
    for word in danger_keywords:
        if word in q:
            return False, f"Blocked: Harmful keyword detected ('{word}')."

    # Rule 3: unsafe intent block
    for intent in unsafe_intents:
        if intent in q:
            return False, "Blocked: Unsafe medical intent detected."

    # Rule 4: medicine name block
    for med in medicine_list:
        if med in q:
            return False, f"Blocked: Query contains medicine name ('{med}')."

    return True, "Allowed: Safe query."


# -----------------------------
# GUI USING TKINTER
# -----------------------------

def evaluate_query():
    query = text_input.get("1.0", tk.END).strip()

    if not query:
        result_label.config(text="Please enter a query.", fg="red")
        return

    allowed, message = firewall_check(query)

    if allowed:
        result_label.config(text=message, fg="green")
        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Firewall Result: Query is SAFE.\n\n")
        output_box.insert(tk.END, "Simulated LLM Response:\n")
        output_box.insert(tk.END, "➡ I can help with general health information.\n")
        output_box.config(state='disabled')

    else:
        result_label.config(text=message, fg="red")
        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Firewall Result: Query BLOCKED.\n\n")
        output_box.insert(tk.END, "Reason:\n")
        output_box.insert(tk.END, f"{message}\n\n")
        output_box.insert(tk.END, "Safe Alternative:\n")
        output_box.insert(tk.END, "➡ Please consult a licensed medical professional.")
        output_box.config(state='disabled')

# Main window
root = tk.Tk()
root.title("Medical LLM Firewall Prototype")
root.geometry("560x520")
root.resizable(False, False)

title_label = tk.Label(root, text="Medical LLM Firewall", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

desc_label = tk.Label(root, text="A safety wrapper around a medical LLM\nDetects and blocks unsafe queries.",
                      font=("Arial", 11), fg="#555")
desc_label.pack()

# Query box
text_input = scrolledtext.ScrolledText(root, width=60, height=6, font=("Arial", 12))
text_input.pack(pady=10)

# Button
evaluate_btn = tk.Button(root, text="Run Firewall", font=("Arial", 12, "bold"),
                         bg="#4a90e2", fg="white", width=20, command=evaluate_query)
evaluate_btn.pack(pady=5)

# Result message
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=8)

# Output
output_box = scrolledtext.ScrolledText(root, width=60, height=12, font=("Arial", 11))
output_box.pack(pady=10)
output_box.config(state='disabled')

root.mainloop()