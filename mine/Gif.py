import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os

class DigitalSignage:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Signage")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.label = tk.Label(root, bg="black")
        self.label.pack(expand=True, fill='both')

        self.gif_paths = [
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\animation1.gif",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\animation2.gif",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\animation3.gif",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\animation4.gif",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\animation5.gif"
        ]

        # Check if files exist
        for path in self.gif_paths:
            if not os.path.isfile(path):
                print(f"File not found: {path}")

        self.gifs = []
        self.frames = []
        for path in self.gif_paths:
            gif = Image.open(path)
            self.gifs.append(gif)
            frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]
            self.frames.append(frames)

        self.current_gif = 0
        self.current_frame = 0
        self.update_image()

    def update_image(self):
        current_frames = self.frames[self.current_gif]
        self.label.config(image=current_frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(current_frames)
        
        if self.current_frame == 0:
            self.current_gif = (self.current_gif + 1) % len(self.frames)
        
        self.root.after(100, self.update_image)  # Change frame every 100 ms for a smooth GIF

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalSignage(root)
    root.mainloop()
