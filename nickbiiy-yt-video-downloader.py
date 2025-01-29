import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL
import os

# Function to download the video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        # Define download options
        ydl_opts = {
            'format': 'best',  # Download the best quality video with audio
            'outtmpl': os.path.join(os.path.expanduser("~"), "Downloads", "%(title)s.%(ext)s"),  # Save to Downloads folder
            'progress_hooks': [on_progress],  # Add progress hook
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        progress_bar['value'] = 0  # Reset progress bar after download

# Function to update the progress bar
def on_progress(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes', 0)
        downloaded = d.get('downloaded_bytes', 0)
        if total_size > 0:
            percentage = (downloaded / total_size) * 100
            progress_bar['value'] = percentage
            root.update_idletasks()  # Update the GUI to reflect the progress

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create the main window
root = tk.Tk()
root.title("NickBiiy-Youtube-Video-Downloader")
root.geometry("400x200")
center_window(root, 400, 200)  # Center the window

# URL Entry
url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12))
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=40, font=("Arial", 10))
url_entry.pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Download Button (Styled)
download_button = tk.Button(
    root,
    text="Download Video",
    command=download_video,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",  # Green background
    fg="white",    # White text
    padx=10,
    pady=5,
    borderwidth=0,
    relief="flat",
    activebackground="#45a049",  # Darker green when clicked
    activeforeground="white"
)
download_button.pack(pady=10)

# Run the application
root.mainloop()