import tkinter as tk

from PIL import ImageGrab


class screen_coordinates:
    def __init__(self):
        self.root = None
        self.canvas = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.rect = None
        self.screenshot = None

    def draw_rectangle(self):
        self.root = tk.Tk()

        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)

        self.canvas = tk.Canvas(self.root, highlightthickness=0, background="black")
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.root.mainloop()

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = None

    def on_drag(self, event):
        cur_x = event.x
        cur_y = event.y
        if self.rect:
            self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)
        else:
            self.rect = self.canvas.create_rectangle(
                self.start_x, self.start_y, cur_x, cur_y, outline="white", width=2
            )

    def on_release(self, event):
        if self.start_x is not None and self.start_y is not None and self.rect:
            x1, y1, x2, y2 = self.canvas.coords(self.rect)
            self.end_y = y2
            self.end_x = x2
            self.root.destroy()

    def get_screenshot(self):
        self.screenshot = ImageGrab.grab(
            bbox=(self.start_x, self.start_y, self.end_x, self.end_y)
        )
        self.screenshot.show()
