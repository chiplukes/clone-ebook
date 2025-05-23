import argparse
import importlib.metadata
from pathlib import Path

import clone_ebook

if __name__ == "__main__":
    print(f"{__file__}:__main__")

    parser = argparse.ArgumentParser()

    # Optional argument for book name
    parser.add_argument(
            "--book_name",
            type=str,
            default="ebook",
            help="Name of the book to be created",
        )

    # Optional argument for output directory
    parser.add_argument(
        "--output_dir",
        type=Path,
        default=Path(__file__).absolute().parent / "output",
        help="Path to the data directory",
    )

    # Optional argument for max pages
    parser.add_argument(
        "--max_pages",
        type=int,
        default=10,
        help="Maximum number of pages to process",
    )

    # Optional argument flag which defaults to False
    parser.add_argument("-d", "--debug", action="store_true", default=False)

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbosity (-v, -vv, etc)"
    )

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(
            version=importlib.metadata.version("clone_ebook")
        ),
    )

    args = parser.parse_args()

    solved = clone_ebook.clone_ebook_main(output_directory=args.output_dir,book_name=args.book_name, max_pages=args.max_pages)
