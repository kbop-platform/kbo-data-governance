#!/usr/bin/env python3
"""Extract full text from the KBO OPS table specification PDF."""

import fitz  # PyMuPDF

PDF_PATH = "/home/user/dev/data-dict/KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf"

doc = fitz.open(PDF_PATH)
total_pages = len(doc)
print(f"=== Total pages: {total_pages} ===\n")

for page_num in range(total_pages):
    page = doc[page_num]
    text = page.get_text()
    print(f"--- Page {page_num + 1} of {total_pages} ---")
    print(text)
    print()

doc.close()
print("=== END OF DOCUMENT ===")
