import os
import time
from google import genai
from google.genai import errors

# Cấu hình Gemini - Ép sử dụng v1 API để ổn định hơn
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"],
    http_options={'api_version': 'v1'}
)

def generate_with_retry(model, contents, max_retries=3):
    """Hàm hỗ trợ gọi API với cơ chế tự động thử lại nếu bị quá tải (429)"""
    for i in range(max_retries):
        try:
            # Ưu tiên sử dụng bản 1.5-flash vì nó có quota miễn phí lớn nhất
            response = client.models.generate_content(model=model, contents=contents)
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg and i < max_retries - 1:
                wait_time = 20  # Đợi 20 giây nếu bị quá tải
                print(f"Bị quá tải (429). Đang đợi {wait_time}s trước khi thử lại lần {i+1}...")
                time.sleep(wait_time)
                continue
            # Nếu lỗi 404 (không tìm thấy model 2.0), thử chuyển xuống 1.5-flash
            if "404" in error_msg and "2.0" in model:
                print("Model 2.0 không khả dụng, đang thử chuyển sang 1.5-flash...")
                return generate_with_retry("gemini-1.5-flash", contents, max_retries)
            raise e

def run_pipeline():
    # 1. Đọc file input
    with open('input/eng.txt', 'r', encoding='utf-8') as f: eng_text = f.read()
    with open('input/kor.txt', 'r', encoding='utf-8') as f: kor_text = f.read()
    
    # 2. Bước 1: Dịch (Sử dụng Gemini 1.5 Flash - Hạn mức cao nhất)
    print("Đang tiến hành dịch bản thảo (Gemini 1.5 Flash)...")
    draft = generate_with_retry(
        model='gemini-1.5-flash', 
        contents=f"Translate to Vietnamese: {eng_text}"
    )
    time.sleep(10)  # Nghỉ 10 giây để tránh bị lock quota
    
    # 3. Bước 2: Review (Sử dụng Gemini 1.5 Flash cho an toàn quota)
    print("Đang tiến hành Review...")
    report = generate_with_retry(
        model='gemini-1.5-flash', 
        contents=f"Review this translation: {draft} against {kor_text}"
    )
    time.sleep(10)
    
    # 4. Bước 3: Refine
    print("Đang hoàn tất bản dịch...")
    final = generate_with_retry(
        model='gemini-1.5-flash', 
        contents=f"Fix this translation: {draft} based on this report: {report}"
    )
    
    # 5. Lưu kết quả
    with open('output/vi_final.txt', 'w', encoding='utf-8') as f: f.write(final)
    print("Đã lưu kết quả thành công!")

if __name__ == "__main__":
    run_pipeline()

