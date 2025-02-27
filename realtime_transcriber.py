import os
import whisper
import torch
import time
import threading
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load Whisper model only once for better performance
model = whisper.load_model("small", device=device)

# Store processed files to avoid duplicate transcriptions
processed_files = set()
observer = None

class TranscriptionHandler(FileSystemEventHandler):
    """Watches a folder for new audio/video files and transcribes them."""
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_ext = os.path.splitext(file_path)[1].lower()
        
        # Process only media files
        allowed_extensions = {".mp3", ".wav", ".mp4", ".mkv", ".mov", ".flv", ".aac", ".m4a"}
        if file_ext in allowed_extensions and file_path not in processed_files:
            log_message(f"📌 New file detected: {file_path}")
            transcribe_file(file_path)

def transcribe_file(file_path):
    """Transcribes an audio or video file and saves the output."""
    log_message(f"📝 Transcribing: {file_path}...")

    # Transcribe the file
    result = model.transcribe(file_path)

    # Save the transcription as a .txt file
    output_path = file_path.rsplit(".", 1)[0] + ".txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Mark the file as processed
    processed_files.add(file_path)
    log_message(f"✅ Transcription saved: {output_path}")

def start_monitoring(folder_path):
    """Starts monitoring the folder for new media files."""
    global observer
    if observer:
        log_message("⚠️ Already monitoring. Stop first!")
        return

    event_handler = TranscriptionHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()

    log_message(f"🔍 Monitoring folder: {folder_path} (Click 'Stop' to stop)")

def stop_monitoring():
    """Stops the folder monitoring."""
    global observer
    if observer:
        observer.stop()
        observer.join()
        observer = None
        log_message("🛑 Stopped folder monitoring.")

def log_message(message):
    """Logs messages in the GUI."""
    log_area.insert(tk.END, message + "\n")
    log_area.see(tk.END)

def browse_folder():
    """Opens a folder dialog and sets the path."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def start_threaded_monitoring():
    """Runs monitoring in a separate thread to keep GUI responsive."""
    folder = folder_path.get()
    if not os.path.exists(folder):
        messagebox.showerror("Error", "Invalid folder path!")
        return
    threading.Thread(target=start_monitoring, args=(folder,), daemon=True).start()

# Create the GUI
root = tk.Tk()
root.title("Automated Transcription System")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Folder selection
folder_path = tk.StringVar()
tk.Label(root, text="Select Folder to Monitor:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=50).pack(pady=5)
tk.Button(root, text="Browse", command=browse_folder, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(pady=5)

# Start & Stop buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start Monitoring", command=start_threaded_monitoring, bg="#008CBA", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Stop Monitoring", command=stop_monitoring, bg="#f44336", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

# Log area
log_area = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD, font=("Arial", 10))
log_area.pack(pady=10)

# Run the GUI
root.mainloop()
