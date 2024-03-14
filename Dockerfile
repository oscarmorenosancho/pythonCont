FROM python:3.9

RUN mkdir /home/project/
COPY project /home/project/

WORKDIR /home/project/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["python", "/home/project/manage.py", "runserver"]