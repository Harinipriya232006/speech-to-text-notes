import tkinter as tk
from tkinter import messagebox, filedialog
import speech_recognition as sr


# Create the main application window
root = tk.Tk()
root.title("Speech-to-Text Notes Application")
root.geometry("750x550")
root.configure(bg="#f0f4f8")

# Create the speech recognizer
recognizer = sr.Recognizer()


# Application heading
heading = tk.Label(
    root,
    text="Speech-to-Text Notes",
    font=("Arial", 22, "bold"),
    bg="#f0f4f8",
    fg="#1f2937"
)
heading.pack(pady=15)


# Instructions
instructions = tk.Label(
    root,
    text="Click Start Recording and speak into your microphone.",
    font=("Arial", 11),
    bg="#f0f4f8"
)
instructions.pack(pady=5)


# Text area for displaying recognized speech
text_area = tk.Text(
    root,
    height=15,
    width=75,
    font=("Arial", 11),
    wrap="word"
)
text_area.pack(padx=20, pady=10, fill="both", expand=True)


# Status message
status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="blue"
)
status_label.pack(pady=5)


# Function to record speech
def start_recording():
    record_button.config(state="disabled")
    status_label.config(text="Status: Listening...", fg="orange")
    root.update_idletasks()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=15
            )

        status_label.config(
            text="Status: Converting speech to text...",
            fg="orange"
        )
        root.update_idletasks()

        text = recognizer.recognize_google(audio)

        text_area.insert(tk.END, text + "\n\n")

        status_label.config(
            text="Status: Speech converted successfully!",
            fg="green"
        )

    except sr.WaitTimeoutError:
        status_label.config(text="Status: No speech detected", fg="red")
        messagebox.showwarning(
            "No Speech",
            "No speech detected. Please try again."
        )

    except sr.UnknownValueError:
        status_label.config(text="Status: Speech not understood", fg="red")
        messagebox.showwarning(
            "Recognition Error",
            "Sorry, I could not understand your speech."
        )

    except sr.RequestError:
        status_label.config(text="Status: Connection error", fg="red")
        messagebox.showerror(
            "Connection Error",
            "Speech recognition failed. Check your internet connection."
        )

    except (OSError, AttributeError):
        status_label.config(text="Status: Microphone error", fg="red")
        messagebox.showerror(
            "Microphone Error",
            "Check your microphone connection and permissions."
        )

    finally:
        record_button.config(state="normal")


# Function to save notes
def save_notes():
    content = text_area.get("1.0", tk.END).strip()

    if not content:
        messagebox.showwarning(
            "Empty Notes",
            "Please record some speech before saving."
        )
        return

    file_path = filedialog.asksaveasfilename(
        title="Save Your Notes",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

            messagebox.showinfo(
                "Success",
                "Your notes have been saved successfully!"
            )

        except OSError as error:
            messagebox.showerror(
                "Save Error",
                f"Could not save the notes:\n{error}"
            )


# Function to clear notes
def clear_notes():
    text_area.delete("1.0", tk.END)
    status_label.config(text="Status: Ready", fg="blue")


# Create a frame to hold the buttons
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=15)


# Start recording button
record_button = tk.Button(
    button_frame,
    text="Start Recording",
    command=start_recording,
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    width=16,
    cursor="hand2"
)
record_button.grid(row=0, column=0, padx=8)


# Save notes button
save_button = tk.Button(
    button_frame,
    text="Save Notes",
    command=save_notes,
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
save_button.grid(row=0, column=1, padx=8)


# Clear notes button
clear_button = tk.Button(
    button_frame,
    text="Clear Notes",
    command=clear_notes,
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
clear_button.grid(row=0, column=2, padx=8)


# Start the application
root.mainloop()