import os
import requests
import tkinter as tk
from tkinter import filedialog, Label, Entry, Button, ttk
import threading

def download_image(image_url, local_file_name, update_callback, progress_callback):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(local_file_name, 'wb') as file:
                file.write(response.content)
            update_callback(f"Downloaded: {local_file_name}")
            progress_callback()
            return True
        else:
            update_callback(f"Error downloading image: {image_url}")
            return False
    except Exception as e:
        update_callback(f"Error: {e}")
        return False

def update_status(message):
    status_label.config(text=message)
    root.update()

def update_progress():
    progress['value'] += 1
    progress_label.config(text=f"{progress['value']}/{progress['maximum']}")
    root.update()

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_selected)

def start_download_thread(download_missing_only=False):
    folder_path = folder_path_entry.get()
    if folder_path:
        threading.Thread(target=start_download, args=(folder_path, download_missing_only)).start()
    else:
        update_status("Select a destination folder.")

def start_download(folder_path, download_missing_only):
    try:
        json_url = "https://www.digiprintmon.com/digimon_cardlist.json"
        response = requests.get(json_url)
        if response.status_code == 200:
            image_names = response.json()
            existing_files = set(os.listdir(folder_path)) if download_missing_only else set()
            images_to_download = [img for img in image_names if img not in existing_files]
            progress['maximum'] = len(images_to_download)
            progress_label.config(text=f"0/{progress['maximum']}")
            for image_name in images_to_download:
                image_url = f"https://www.digiprintmon.com/img/{image_name}"
                complete_path = f"{folder_path}/{image_name}"
                if not download_image(image_url, complete_path, update_status, update_progress):
                    print(f"Failed to download {image_name}")
            update_status("Download completed.")
        else:
            update_status("Error fetching JSON.")
    except Exception as e:
        update_status(f"Error: {e}")

# Configure the main window
root = tk.Tk()
root.title("Digimon Art Downloader ")

# Create and position widgets
Label(root, text="Folder Path:").grid(row=0, column=0, padx=10, pady=10)
folder_path_entry = Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Select Folder", command=select_folder).grid(row=0, column=2, padx=10, pady=10)
Button(root, text="Download All", command=lambda: start_download_thread(download_missing_only=False)).grid(row=1, column=1, pady=10)
Button(root, text="Download Missing Cards", command=lambda: start_download_thread(download_missing_only=True)).grid(row=2, column=1, pady=10)

status_label = Label(root, text="")
status_label.grid(row=5, column=1, pady=10)

progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.grid(row=3, column=1, pady=10)

progress_label = Label(root, text="0/0")
progress_label.grid(row=4, column=1, pady=10)

# Start the GUI
root.mainloop()
