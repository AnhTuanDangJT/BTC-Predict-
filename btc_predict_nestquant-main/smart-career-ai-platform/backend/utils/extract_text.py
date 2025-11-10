from pdfminer.high_level import extract_text
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using pdfminer.six
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

def extract_text_from_pdf_bytes(pdf_bytes):
    """
    Extract text from PDF bytes
    """
    try:
        resource_manager = PDFResourceManager()
        fake_file_handle = StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        
        from io import BytesIO
        pdf_file = BytesIO(pdf_bytes)
        
        for page in PDFPage.get_pages(pdf_file, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        
        text = fake_file_handle.getvalue()
        
        converter.close()
        fake_file_handle.close()
        
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF bytes: {str(e)}")

