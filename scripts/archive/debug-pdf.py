#!/usr/bin/env python3
"""PDF 텍스트 구조 디버깅"""
import fitz

PDF_PATH = '/home/user/dev/data-dict/KBO 운영통합관리(OPS) 테이블 명세서_20251118.pdf'

doc = fitz.open(PDF_PATH)

# 페이지 1-3, 6-8, 30-31 텍스트 확인
for page_num in [0, 1, 2, 5, 6, 7, 8, 29, 30, 61, 62]:
    if page_num >= len(doc):
        continue
    page = doc[page_num]
    text = page.get_text()
    print(f"\n{'='*60}")
    print(f"PAGE {page_num + 1}")
    print(f"{'='*60}")
    print(text[:2000])
    print("...")

doc.close()
