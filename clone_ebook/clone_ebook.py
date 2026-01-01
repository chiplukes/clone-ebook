# Import the subpackage_module
import time

import pypandoc
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

from .screen import screen_coordinates


def clone_ebook_main(
    book_names_lst=None, output_directory=None, max_pages=10, input_pdf=None
):
    output_directory.mkdir(parents=True, exist_ok=True)

    # If input_pdf is provided, skip screen capture and just convert
    if input_pdf is not None:
        input_pdf_path = (
            input_pdf
            if hasattr(input_pdf, "exists")
            else __import__("pathlib").Path(input_pdf)
        )
        if not input_pdf_path.exists():
            raise FileNotFoundError(f"Input PDF not found: {input_pdf_path}")

        # Use the PDF filename (without extension) as the book name
        book_name = input_pdf_path.stem
        output_book_directory = output_directory / book_name
        output_book_directory.mkdir(parents=True, exist_ok=True)

        # Copy or link the PDF to the output directory if not already there
        target_pdf = output_book_directory / f"{book_name}.pdf"
        if input_pdf_path.resolve() != target_pdf.resolve():
            import shutil

            shutil.copy2(input_pdf_path, target_pdf)

        book_names_lst = [book_name]
    else:
        # Screen capture mode
        sc = screen_coordinates.screen_coordinates()

        for book_name in book_names_lst:
            print(f"Capturing book: {book_name}")
            input("Open ebook reader and press enter to select text region")

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
            output_book_directory = output_directory / book_name
            output_book_directory.mkdir(parents=True, exist_ok=True)
            pages_lst[0].save(
                output_book_directory / f"{book_name}.pdf",
                "PDF",
                resolution=100.0,
                save_all=True,
                append_images=pages_lst[1:],
            )

    for book_name in book_names_lst:
        print(f"Converting book: {book_name}")
        output_book_directory = output_directory / book_name

        converter = PdfConverter(
            artifact_dict=create_model_dict(),
        )
        rendered = converter(str(output_book_directory / f"{book_name}.pdf"))
        text, _, images = text_from_rendered(rendered)

        with open(
            output_book_directory / f"{book_name}.md", "wt", encoding="utf-8"
        ) as f:
            f.write(text)

        for x in images:
            img_path = output_book_directory / f"{x}"
            images[x].save(f"{str(img_path)!s}")

        extra_args = []
        extra_args.append(f"--resource-path={str(output_book_directory)!s}")

        pypandoc.convert_file(
            output_book_directory / f"{book_name}.md",
            "epub",
            outputfile=output_book_directory / f"{book_name}.epub",
            extra_args=extra_args,
        )
