FROM python

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./notessite/manage.py", "runserver", "0.0.0.0:8000"]
