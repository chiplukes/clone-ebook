# Import the subpackage_module
from .screen import screen_coordinates


def clone_ebook_main():
    sc = screen_coordinates.screen_coordinates()

    sc.draw_rectangle()

    sc.get_screenshot()
