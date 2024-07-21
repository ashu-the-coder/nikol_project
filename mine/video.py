import tkinter as tk
from PIL import Image, ImageTk
import cv2
import os

class DigitalSignage:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Signage")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.label = tk.Label(root, bg="black")
        self.label.pack(expand=True, fill='both')

        self.video_paths = [
            r"photo\video1.mp4",
            r"photo\video2.mp4",
            r"photo\video3.mp4",
            r"photo\video4.mp4",
            r"photo\video5.mp4"
            ]


        # Check if files exist
        for path in self.video_paths:
            if not os.path.isfile(path):
                print(f"File not found: {path}")

        self.videos = [cv2.VideoCapture(path) for path in self.video_paths]
        self.current_video = 0
        self.update_video()

    def update_video(self):
        ret, frame = self.videos[self.current_video].read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image_tk = ImageTk.PhotoImage(image)
            self.label.config(image=image_tk)
            self.label.image = image_tk  # Keep a reference to avoid garbage collection
        else:
            # When video ends, release and move to next video
            self.videos[self.current_video].release()
            self.current_video = (self.current_video + 1) % len(self.videos)
            self.videos[self.current_video] = cv2.VideoCapture(self.video_paths[self.current_video])
        
        self.root.after(33, self.update_video)  # Update frame every ~33ms (~30 fps)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalSignage(root)
    root.mainloop()
