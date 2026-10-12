FROM python:3.12-slim

# Cài đặt user UID 1000 theo chuẩn Hugging Face Spaces
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PORT=7860 \
    PYTHONUNBUFFERED=1

WORKDIR $HOME/app

# Cài đặt thư viện Python
COPY --chown=user:user requirements.txt $HOME/app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Sao chép mã nguồn
COPY --chown=user:user . $HOME/app/

# Mở cổng 7860 theo chuẩn Hugging Face
EXPOSE 7860

# Khởi chạy server
CMD ["python", "scripts/reader_server.py"]
