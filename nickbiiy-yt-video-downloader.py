import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL

# Function to download the video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        ydl_opts = {}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        progress_bar['value'] = 0  # Reset progress bar after download

# Function to update the progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_bar['value'] = percentage
    root.update_idletasks()

# Create the main window
root = tk.Tk()
root.title("NickBiiy-Youtube-Video-Downloader")
root.geometry("400x200")

# URL Entry
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Download Button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=10)

# Run the application
root.mainloop()