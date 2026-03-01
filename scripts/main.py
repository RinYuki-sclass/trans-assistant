import os
from google import genai

# Cấu hình Gemini
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def run_pipeline():
    # 1. Đọc file input
    with open('input/eng.txt', 'r', encoding='utf-8') as f: eng_text = f.read()
    with open('input/kor.txt', 'r', encoding='utf-8') as f: kor_text = f.read()
    
    # 2. Bước 1: Dịch (Sử dụng Gemini Flash)
    # (Thêm logic prompt và glossary tại đây)
    draft = client.models.generate_content(
        model='gemini-2.0-flash', 
        contents=f"Translate to Vietnamese: {eng_text}"
    ).text
    
    # 3. Bước 2: Review (Sử dụng Gemini Pro)
    report = client.models.generate_content(
        model='gemini-2.0-pro', 
        contents=f"Review this translation: {draft} against {kor_text}"
    ).text
    
    # 4. Bước 3: Refine
    final = client.models.generate_content(
        model='gemini-2.0-pro', 
        contents=f"Fix this translation: {draft} based on this report: {report}"
    ).text
    
    # 5. Lưu kết quả
    with open('output/vi_final.txt', 'w', encoding='utf-8') as f: f.write(final)

if __name__ == "__main__":
    run_pipeline()

