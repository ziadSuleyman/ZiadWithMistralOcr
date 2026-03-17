from mistralai import Mistral


class OCRClient:
    def __init__(self, api_key: str):
        self.client = Mistral(api_key=api_key)

    def process_pdf_base64(self, b64_string: str):
        return self.client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": f"data:application/pdf;base64,{b64_string}"
            },
            include_image_base64=False
        )
