import os
import time
from google import genai
from google.genai import errors

# Cấu hình Gemini - Sử dụng bản 2.0 chuẩn của năm 2026
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def generate_with_retry(model, contents, max_retries=3):
    """Hàm hỗ trợ gọi API với cơ chế tự động thử lại nếu bị quá tải (429)"""
    for i in range(max_retries):
        try:
            response = client.models.generate_content(model=model, contents=contents)
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                if "limit: 0" in error_msg:
                    print("!!! LỖI NGHIÊM TRỌNG: Hạn mức (Quota) của Key này đã bị Google đưa về 0.")
                    print("!!! Vùi lòng ĐỔI API KEY mới từ một tài khoản/project khác để tiếp tục.")
                    raise e
                if i < max_retries - 1:
                    wait_time = 30  # Đợi 30 giây nếu bị quá tải tạm thời
                    print(f"Bị quá tải (429). Đang đợi {wait_time}s trước khi thử lại lần {i+1}...")
                    time.sleep(wait_time)
                    continue
            raise e

def run_pipeline():
    # 1. Đọc file input
    with open('input/eng.txt', 'r', encoding='utf-8') as f: eng_text = f.read()
    with open('input/kor.txt', 'r', encoding='utf-8') as f: kor_text = f.read()
    
    # 2. Bước 1: Dịch (Sử dụng Gemini 2.0 Flash)
    print("Đang tiến hành dịch bản thảo (Gemini 2.0 Flash)...")
    draft = generate_with_retry(
        model='gemini-2.0-flash', 
        contents=f"Translate to Vietnamese: {eng_text}"
    )
    time.sleep(10)
    
    # 3. Bước 2: Review (Sử dụng Gemini 2.0 Flash)
    print("Đang tiến hành Review...")
    report = generate_with_retry(
        model='gemini-2.0-flash', 
        contents=f"Review this translation: {draft} against {kor_text}"
    )
    time.sleep(10)
    
    # 4. Bước 3: Refine
    print("Đang hoàn tất bản dịch...")
    final = generate_with_retry(
        model='gemini-2.0-flash', 
        contents=f"Fix this translation: {draft} based on this report: {report}"
    )
    
    # 5. Lưu kết quả
    with open('output/vi_final.txt', 'w', encoding='utf-8') as f: f.write(final)
    print("Đã lưu kết quả thành công!")

if __name__ == "__main__":
    run_pipeline()

