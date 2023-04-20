FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

COPY . .

CMD ["pyhton", "manage.py", "runserver", "0.0.0.0:7000"]