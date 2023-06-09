from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Watermark App")
        self.master.geometry("400x400")

        self.upload_btn = Button(self.master, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        self.text_entry = Entry(self.master, width=30)
        self.text_entry.pack(pady=10)

        self.add_text_btn = Button(self.master, text="Add Text Watermark", command=self.add_text_watermark)
        self.add_text_btn.pack(pady=10)

        self.add_logo_btn = Button(self.master, text="Add Logo Watermark", command=self.add_logo_watermark)
        self.add_logo_btn.pack(pady=10)

        self.logo_path = None

    def upload_image(self):
        self.filename = filedialog.askopenfilename(initialdir="./", title="Select Image File", filetypes=(("Image Files", "*.jpg;*.jpeg"), ("All Files", "*.*")))
        self.image = Image.open(self.filename)
        self.image = self.image.rotate(180)  # Rotate image by 180 degrees

    def upload_logo(self):
        self.logo_path = filedialog.askopenfilename(initialdir="./", title="Select Logo File", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))

    def add_text_watermark(self):
        text = self.text_entry.get()
        if text:
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype("arial.ttf", 70)
            textwidth, textheight = draw.textsize(text, font)
            width, height = self.image.size
            x = width - textwidth - 10
            y = height - textheight - 10
            draw.text((x, y), text, font=font)

            self.image.show()


    def add_logo_watermark(self):
        logo_path = filedialog.askopenfilename(initialdir="./", title="Select Logo File", filetypes=(("Image Files", "*.png"), ("All Files", "*.*")))
        if logo_path:
            logo = Image.open(logo_path).convert("RGBA")
            width, height = self.image.size
            logo_width, logo_height = logo.size
            x = width - logo_width - 10  # Set x-coordinate for bottom right corner
            y = height - logo_height - 10  # Set y-coordinate for bottom right corner
            logo_transparent = Image.new("RGBA", self.image.size, (0, 0, 0, 0))  # Create transparent canvas
            logo_transparent.paste(logo, (x, y), logo)  # Paste logo onto canvas at specified coordinates
            self.image = self.image.convert("RGBA")
            self.image = Image.alpha_composite(self.image, logo_transparent)  # Overlay canvas onto original image
            self.image = self.image.convert("RGB")
            self.image.show()


root = Tk()
watermark_app = WatermarkApp(root)
root.mainloop()



