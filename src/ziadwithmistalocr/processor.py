import os
import time
import logging
from .utils import encode_pdf, ensure_directory
from .core import OCRClient


class BatchOCR:
    def __init__(self, api_key: str, max_retries: int = 5, backoff: int = 1):
        self.client = OCRClient(api_key)
        self.max_retries = max_retries
        self.initial_backoff = backoff

    def process_folder(self, input_dir: str, output_dir: str):
        ensure_directory(output_dir)

        pdf_files = self._get_pdf_files(input_dir)

        for pdf in pdf_files:
            self._process_single_file(pdf, input_dir, output_dir)

    def _get_pdf_files(self, directory: str):
        pdf_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(".pdf"):
                    rel_path = os.path.relpath(
                        os.path.join(root, file), directory
                    )
                    pdf_files.append(rel_path)
        return pdf_files

    def _process_single_file(self, pdf_filename, input_dir, output_dir):
        full_path = os.path.join(input_dir, pdf_filename)
        attempts = 0
        backoff = self.initial_backoff

        while attempts < self.max_retries:
            try:
                b64 = encode_pdf(full_path)
                response = self.client.process_pdf_base64(b64)

                output_name = pdf_filename.rsplit(".", 1)[0] + ".md"
                output_path = os.path.join(output_dir, output_name)

                ensure_directory(os.path.dirname(output_path))

                with open(output_path, "w", encoding="utf-8") as md_file:
                    for page in response.pages:
                        md_file.write(f"## Page {page.index + 1}\n\n")
                        md_file.write(page.markdown + "\n\n")

                return

            except Exception as e:
                attempts += 1
                logging.error(f"{pdf_filename} failed attempt {attempts}: {e}")
                time.sleep(backoff)
                backoff *= 2

        raise RuntimeError(f"Failed to process {pdf_filename}")
