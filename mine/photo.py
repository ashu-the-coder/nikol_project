import tkinter as tk
from PIL import Image, ImageTk
import os

class DigitalSignage:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Signage")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.label = tk.Label(root, bg="black")
        self.label.pack(expand=True, fill='both')

        self.image_paths = [
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\image_1 .jpg",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\image_2.JPG",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\image_3.jpg",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\image_4.JPG",
            r"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Nikol_project\\mine\\photo\\image_5.JPG"
        ]

        # Check if files exist
        for path in self.image_paths:
            if not os.path.isfile(path):
                print(f"File not found: {path}")
        
        self.images = [ImageTk.PhotoImage(Image.open(path)) for path in self.image_paths]
        self.current_image = 0
        self.update_image()

    def update_image(self):
        self.label.config(image=self.images[self.current_image])
        self.current_image = (self.current_image + 1) % len(self.images)
        self.root.after(3000, self.update_image)  # Change image every 3 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalSignage(root)
    root.mainloop()
