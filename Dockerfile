FROM python:3.11

# Встановлення робочої директорії
WORKDIR /code

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код
COPY . .

# Відкриття порту
EXPOSE 8000

# Команда для запуску додатку
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
