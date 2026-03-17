````markdown
# ZiadWithMistralOcr

**ZiadWithMistralOcr** is a Python library for performing batch OCR (Optical Character Recognition) on PDF documents using the [Mistral API](https://mistralai.com/). It allows you to process multiple PDF files in a folder and export the results as Markdown files efficiently.

---

## Features

- Process entire folders of PDFs in batch.
- Converts PDFs to Markdown format.
- Handles multi-page PDFs.
- Supports logging and retry mechanism for API errors.
- Easy integration with Python projects.

---

## Installation

You can install the library directly from PyPI:

```bash
pip install ziad-with-mistral-ocr
````

> For testing, you can also use Test PyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ ziad-with-mistral-ocr
```

---

## Usage

### 1. Import and initialize

```python
from ziadwithmistalocr import BatchOCR
import os

# Initialize with your Mistral API key
ocr = BatchOCR(api_key=os.getenv("MISTRAL_API_KEY"))
```

### 2. Process a folder of PDFs

```python
ocr.process_folder("docs_import", "docs_exports")
```

* `docs_import`: Folder containing input PDF files.
* `docs_exports`: Folder where Markdown files will be saved.

---

### Example:

```python
from ziadwithmistalocr import BatchOCR
import os

ocr = BatchOCR(api_key=os.getenv("MISTRAL_API_KEY"))
ocr.process_folder("sample_pdfs", "output_markdown")
```

This will convert all PDFs in `sample_pdfs` into Markdown files in `output_markdown`.

---

## Environment Variables

It's recommended to store your API key in an environment variable:

```bash
export MISTRAL_API_KEY="your_api_key_here"   # Linux/macOS
setx MISTRAL_API_KEY "your_api_key_here"     # Windows
```

Then access it in Python using:

```python
import os
api_key = os.getenv("MISTRAL_API_KEY")
```

---

## Logging

* All processing attempts, errors, and statuses are logged in `conversion.log`.
* A CSV database (`processed_files.csv`) is also maintained to keep track of processed files and retries.

---

## Requirements

* Python >= 3.9
* [mistralai](https://pypi.org/project/mistralai/)
* python-dotenv (optional, for environment variable management)

Install dependencies:

```bash
pip install mistralai python-dotenv
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions are welcome! Please create issues or pull requests on GitHub.

---

## Contact

Created by Ziad. For questions, reach me at [riseappsriseapps.@gmail.com](mailto:riseappsriseapps.@gmail.com).

