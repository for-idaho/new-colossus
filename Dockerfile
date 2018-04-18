FROM python:3.6-alpine

RUN adduser -D newcolossus

WORKDIR /home/newcolossus

COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY newColossus.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP newColossus.py

RUN chown -R newcolossus:newcolossus ./
USER newcolossus

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
