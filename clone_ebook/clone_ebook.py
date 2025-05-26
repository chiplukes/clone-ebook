# Import the subpackage_module
import time

import pypandoc
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

from .screen import screen_coordinates


def clone_ebook_main(book_name=None, output_directory=None, max_pages=10):
    sc = screen_coordinates.screen_coordinates()

    print("Use mouse to draw a rectangle around text region from ebook reader.")
    sc.select_text_region()

    print("Click mouse on next page button from ebook reader.")
    sc.select_next_page_button()

    page_i = 1
    pages_lst = []
    screen_previous = None
    while True:
        print(f"Page {page_i}")
        page_i += 1
        screenshot = sc.get_screenshot()
        # text = pytesseract.image_to_string(screenshot)
        # pages_lst.append(f"{text.strip()}\n")
        pages_lst.append(screenshot)
        if (
            (screen_previous is not None) and (screenshot == screen_previous)
        ) or page_i > max_pages:
            break
        screen_previous = screenshot
        sc.next_page()
        time.sleep(2)
    output_directory.mkdir(parents=True, exist_ok=True)
    pages_lst[0].save(
        output_directory / f"{book_name}.pdf",
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=pages_lst[1:],
    )

    converter = PdfConverter(
        artifact_dict=create_model_dict(),
    )
    rendered = converter(str(output_directory / f"{book_name}.pdf"))
    text, _, images = text_from_rendered(rendered)

    with open(output_directory / f"{book_name}.md", "wt", encoding="utf-8") as f:
        f.write(text)

    for x in images:
        img_path = output_directory / f"{x}"
        images[x].save(f"{str(img_path)!s}")

    extra_args = []
    extra_args.append(f"--resource-path={str(output_directory)!s}")

    pypandoc.convert_file(
        output_directory / f"{book_name}.md",
        "epub",
        outputfile=output_directory / f"{book_name}.epub",
        extra_args=extra_args,
    )
