from docling.document_converter import DocumentConverter

def read_pdf(path):
    try:
        converter = DocumentConverter()
        result = converter.convert(path)
        return result.document.export_to_markdown()
    except Exception as e:
        print("PDF Error:", e)
        return ""