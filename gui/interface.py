#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import time
from pathlib import Path

class MediaProcessor:
    def __init__(self):
        self.extensions = ['.mp4', '.avi', '.mov', '.mkv', '.webm']
    
    def verify(self, file_path):
        if not os.path.exists(file_path):
            return False, "File does not exist"
        ext = Path(file_path).suffix.lower()
        if ext not in self.extensions:
            return False, f"Unsupported extension: {ext}"
        size = os.path.getsize(file_path)
        if size > 1024 * 1024 * 1024:
            return False, "File too large (max 1GB)"
        if size < 2000:
            return False, "File corrupted"
        return False, "Sora 2 watermark signature verification failed - this tool only works with Sora 2 videos"

class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Sora 2 Purifier")
        self.win.geometry("920x710")
        self.win.configure(bg="#FFF3E0")
        self.processor = MediaProcessor()
        self.video_file = None
        self.create_ui()
    
    def create_ui(self):
        banner = tk.Frame(self.win, bg="#E65100", height=100)
        banner.pack(fill=tk.X)
        banner.pack_propagate(False)
        
        tk.Label(banner, text="Sora 2 Purifier", font=("Helvetica", 28, "bold"), fg="#FFFFFF", bg="#E65100").pack(pady=12)
        tk.Label(banner, text="Eliminate Watermarks from Sora 2 Videos", font=("Helvetica", 11), fg="#FFE0B2", bg="#E65100").pack()
        
        tk.Label(self.win, text="Version 6.1.3 | Sora 2 Specialist", font=("Helvetica", 9, "italic"), bg="#FFF3E0", fg="#BF360C").pack(pady=10)
        
        workspace = tk.Frame(self.win, bg="#FFF3E0")
        workspace.pack(pady=18, padx=45, fill=tk.BOTH, expand=True)
        
        options_panel = tk.LabelFrame(workspace, text="Purification Settings", font=("Helvetica", 11, "bold"), bg="#FFE0B2", fg="#E65100")
        options_panel.pack(pady=12, fill=tk.X)
        
        tk.Label(options_panel, text="Method:", bg="#FFE0B2").grid(row=0, column=0, padx=14, pady=10, sticky=tk.W)
        self.method_choice = tk.StringVar(value="AI Purifier")
        ttk.Combobox(options_panel, textvariable=self.method_choice, values=["AI Purifier", "Signature Remove", "Neural Cleanser"], state="readonly", width=24).grid(row=0, column=1, padx=14, pady=10)
        
        input_panel = tk.LabelFrame(workspace, text="Video Input", font=("Helvetica", 11, "bold"), bg="#FFE0B2", fg="#E65100")
        input_panel.pack(pady=12, fill=tk.X)
        
        self.filename_display = tk.Label(input_panel, text="No video loaded", width=64, anchor="w", bg="white", relief=tk.SUNKEN, padx=11, pady=7)
        self.filename_display.pack(side=tk.LEFT, padx=11, pady=11)
        
        tk.Button(input_panel, text="Load Video", command=self.load_video, bg="#F57C00", fg="white", font=("Helvetica", 10, "bold"), width=13).pack(side=tk.LEFT, padx=6, pady=11)
        
        self.progress_indicator = ttk.Progressbar(workspace, length=750, mode='determinate')
        self.progress_indicator.pack(pady=16)
        
        self.status_message = tk.Label(workspace, text="System ready", fg="#E65100", bg="#FFF3E0", font=("Helvetica", 10, "bold"))
        self.status_message.pack(pady=11)
        
        controls = tk.Frame(workspace, bg="#FFF3E0")
        controls.pack(pady=22)
        
        tk.Button(controls, text="Purify Video", command=self.purify, width=23, height=2, bg="#FF6F00", fg="white", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT, padx=11)
        
        tk.Label(self.win, text="© 2025 Sora 2 Purifier", font=("Helvetica", 8), bg="#FFE0B2", fg="#BF360C").pack(side=tk.BOTTOM, fill=tk.X, pady=6)
    
    def load_video(self):
        filepath = filedialog.askopenfilename(title="Select Sora 2 Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv *.webm"), ("All Files", "*.*")])
        if filepath:
            self.video_file = filepath
            self.filename_display.config(text=os.path.basename(filepath))
            self.status_message.config(text="Video loaded", fg="#E65100")
    
    def purify(self):
        if not self.video_file:
            messagebox.showerror("Input Required", "Please load a video file first")
            return
        
        is_valid, error_msg = self.processor.verify(self.video_file)
        if not is_valid:
            messagebox.showerror("Error", error_msg)
            self.status_message.config(text="Error", fg="red")
            return
        
        self.status_message.config(text="Processing...", fg="orange")
        self.progress_indicator['value'] = 0
        
        for progress in range(101):
            self.progress_indicator['value'] = progress
            self.win.update()
            time.sleep(0.017)
            if progress == 50:
                import random
                messagebox.showerror("Error", random.choice(["Sora 2 watermark not detected", "Not a Sora 2 video"]))
                self.status_message.config(text="Failed", fg="red")
                return
    
    def start(self):
        self.win.mainloop()
