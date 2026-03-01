import os
import google.generativeai as genai

# Cấu hình Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model_flash = genai.GenerativeModel('gemini-1.5-flash') # Dùng để dịch (Rẻ/Nhanh)
model_pro = genai.GenerativeModel('gemini-1.5-pro')     # Dùng để Review (Thông minh)

def run_pipeline():
    # 1. Đọc file input
    with open('input/eng.txt', 'r') as f: eng_text = f.read()
    with open('input/kor.txt', 'r') as f: kor_text = f.read()
    
    # 2. Bước 1: Dịch (Sử dụng Gemini Flash)
    # (Thêm logic prompt và glossary tại đây)
    draft = model_flash.generate_content(f"Translate to Vietnamese: {eng_text}").text
    
    # 3. Bước 2: Review (Sử dụng Gemini Pro)
    report = model_pro.generate_content(f"Review this translation: {draft} against {kor_text}").text
    
    # 4. Bước 3: Refine
    final = model_pro.generate_content(f"Fix this translation: {draft} based on this report: {report}").text
    
    # 5. Lưu kết quả
    with open('output/vi_final.txt', 'w') as f: f.write(final)

if __name__ == "__main__":
    run_pipeline()

