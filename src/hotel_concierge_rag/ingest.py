import pandas as pd
from pypdf import PdfReader
def load_pdf_pages(pdf_path: str) -> pd.DataFrame:
    reader = PdfReader(pdf_path)
    rows = []
    for i, page in enumerate(reader.pages):
        lines = page.extract_text()
        rows.append({
            "source": pdf_path,             
            "text":lines, 
             "page_number" :i+1,
             "word_count" : len(lines.split())
        })

    pages = pd.DataFrame(rows)
    
    return pages
    



    