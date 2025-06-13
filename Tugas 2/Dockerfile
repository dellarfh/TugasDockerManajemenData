# Gunakan image Python resmi
FROM python:3.9

# Set work directory
WORKDIR /app

# Copy semua file ke dalam docker image
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi
CMD ["python", "app.py"]