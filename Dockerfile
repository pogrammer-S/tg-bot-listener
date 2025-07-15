FROM python
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt   
ENTRYPOINT ["python", "main_rename.py"]