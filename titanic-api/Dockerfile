# 1. Baza - Python
FROM python:3.10-slim

# 2. Radni direktorijum unutar kontejnera
WORKDIR /app

# 3. Kopiranje svih fajlova u kontejner
COPY . .

# 4. Instalacija Python biblioteka
RUN pip install --no-cache-dir -r requirements.txt

# 5. Otvori port 5000
EXPOSE 5000

# 6. Pokreni app.py
CMD ["python", "app.py"]