import tkinter as tk
import os
import sys
import traceback 

# Allow access to the models folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.predict import predict_url

# ===========================
# Main Window
# ===========================

window = tk.Tk()
window.title("Project KITSUNE")
window.geometry("1000x700")
window.configure(bg="#0F172A")

# ===========================
# Title
# ===========================

title = tk.Label(
    window,
    text="🦊 PROJECT KITSUNE",
    font=("Times New Roman", 24, "bold"),
    bg="#1B2D55",
    fg="#38BDF8"
)
title.pack(pady=20)

subtitle = tk.Label(
    window,
    text="AI Powered Phishing URL Detection System",
    font=("Arial", 12),
    bg="#0F172A",
    fg="white"
)
subtitle.pack(pady=(0,20))

# ===========================
# URL Entry
# ===========================

url_label = tk.Label(
    window,
    text="Enter Website URL",
    bg="#0F172A",
    fg="white",
    font=("Arial", 12)
)
url_label.pack()

url_entry = tk.Entry(
    window,
    width=70,
    font=("Arial", 12)
)
url_entry.pack(pady=10, ipady=5)

# ===========================
# Scan Button
# ===========================
def scan_url():
    url = url_entry.get().strip()

# Automatically add HTTPS if the user doesn't type it
    if not url.startswith(("http://", "https://")):
      url = "https://" + url

    if not url:
        result_label.config(
            text="Please enter a URL first.",
            fg="white"
        )
        return

    status.config(text="Status: Scanning...")

    try:
        prediction, confidence, features, reasons = predict_url(url)

        reason_text = "\n".join(f"• {reason}" for reason in reasons)

        if prediction == 0:
            result_text = (
                f"❌ PHISHING WEBSITE DETECTED\n\n"
                f"Confidence: {confidence:.2f}%\n\n"
                f"Reasons:\n{reason_text}"
            )

            result_frame.config(bg="#7F1D1D")
            result_label.config(bg="#7F1D1D", fg="white")

        else:
            result_text = (
                f"✅ SAFE WEBSITE\n\n"
                f"Confidence: {confidence:.2f}%\n\n"
                f"Analysis:\n{reason_text}"
            )

            result_frame.config(bg="#064E3B")
            result_label.config(bg="#064E3B", fg="white")

        result_label.config(text=result_text)

    except Exception:
        traceback.print_exc()
        result_label.config(
            text="An error occurred while scanning the URL.",
            fg="red"
        )

    status.config(text="Status: Ready")

scan_button = tk.Button(
    window,
    text="Scan URL",
    command=scan_url,
    font=("Arial", 12, "bold"),
    bg="#38BDF8",
    fg="black",
    padx=20,
    pady=5
)
scan_button.pack(pady=15)

# ===========================
# Result Box
# ===========================

result_frame = tk.Frame(
    window,
    bg="#1E293B",
    width=700,
    height=300
)
result_frame.pack(pady=20)

result_frame.pack_propagate(False)

result_label = tk.Label(
    result_frame,
    text="Scan results will appear here...",
    bg="#1E293B",
    fg="white",
    font=("Arial", 13)
)
result_label.pack(expand=True)

# ===========================
# Status Bar
# ===========================

status = tk.Label(
    window,
    text="Status: Ready",
    bg="#0F172A",
    fg="#94A3B8",
    font=("Arial", 10)
)
status.pack(side="bottom", pady=10)

window.mainloop()