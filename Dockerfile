FROM python:3.8-slim-buster

WORKDIR /app

COPY ./MainScores.py /app/
COPY ./Utils.py /app/
COPY ./Score.py /app/

RUN pip install Flask
RUN echo '8' >> Scores.txt
CMD flask --app MainScores run --host=0.0.0.0