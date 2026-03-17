import os
import base64


def encode_pdf(pdf_path: str) -> str:
    with open(pdf_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode("utf-8")


def ensure_directory(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
