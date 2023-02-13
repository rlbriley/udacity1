FROM python:3.11
# Maintainer label is deprecated.
LABEL maintainer="Richard L. Briley Jr."
LABEL version="0.1.1"
COPY ./exercises/python-helloworld /app
WORKDIR /app
EXPOSE 5111:5000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD wget http://localhost:5000/status
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]