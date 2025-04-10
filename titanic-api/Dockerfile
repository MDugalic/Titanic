# 1. Baza - uzimamo Python 3.10

FROM python:3.10-slim

# 2. Postavljamo radni direktorijum
WORKDIR /app

# 3. Kopiramo sve fajlove u kontejner

COPY .. 

# 4. Instaliramo zavisnosti

RUN pip install --no-cache -r requirements.txt

# 5. Expose-ujemo port na kojem Flask radi
EXPOSE 5000

# 6. Pokrecemo aplikaciju
CMD ["python","app.py"]