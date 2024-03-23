import argparse
import logging
import pathlib

import libxmp


def process_files(directory, verbose):
    if verbose:
        logging.basicConfig(level=logging.INFO)

    for file_path in pathlib.Path(directory).glob("*"):
        if file_path.suffix.lower() != ".md":
            logging.info(f"Processing file: {file_path}")
            xmp_file = libxmp.XMPFiles(file_path=str(file_path), open_forupdate=True)
            xmp_data = xmp_file.get_xmp()
            if xmp_data:
                logging.info(f"XMP data for {file_path}:")
                logging.info(xmp_data)
            else:
                logging.info(f"No XMP data found for {file_path}")
            xmp_file.close_file()


def parse_args():
    parser = argparse.ArgumentParser(description="Process files and display XMP data.")
    parser.add_argument("directory", help="Directory to process files from.")
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose logging."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    process_files(args.directory, args.verbose)
    return 0
