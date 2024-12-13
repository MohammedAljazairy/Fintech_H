FROM python:3.9-slim

WORKDIR usr/src/app
COPY . .
RUN pip install numpy
Run pip install Flask
RUN pip install scikit-learn
EXPOSE 8000
CMD [ "python","endpoint.py" ]