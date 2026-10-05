# Menggunakan image Python sebagai base image
FROM python:3.12-slim

# Menentukan folder kerja di dalam container
WORKDIR /app

# Menyalin file program thread ke container
COPY thread_sum.py .

# Menjalankan program ketika container dimulai
CMD ["python", "thread_sum.py"]