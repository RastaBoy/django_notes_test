FROM python

WORKDIR /app

# Прикольно, в докере есть кэширование
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "./notessite/manage.py", "runserver", "0.0.0.0:8000"]
