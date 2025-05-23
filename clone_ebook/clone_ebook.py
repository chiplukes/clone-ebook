# Import the subpackage_module
from .screen import screen_coordinates
import pypandoc
import pytesseract


def clone_ebook_main(book_name=None, output_directory=None, max_pages=10, resource_path=None):
    sc = screen_coordinates.screen_coordinates()

    print("Use mouse to draw a rectangle around text region from ebook reader.")
    sc.select_text_region()

    print("Click mouse on next page button from ebook reader.")
    sc.select_next_page_button()

    page_i = 1
    pages_lst = []
    while True:
        screenshot = sc.get_screenshot()
        text = pytesseract.image_to_string(screenshot)
        pages_lst.append(f"{text.strip()}\n")
        if page_i > max_pages:
            break

    with open(output_directory / f"{book_name}.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(pages_lst))

    extra_args = []
    if resource_path:
        extra_args.append(f'--resource-path={resource_path}')

    pypandoc.convert_file(output_directory / f"{book_name}.md", 'epub', outputfile=output_directory / f"{book_name}.epub", extra_args=extra_args)

