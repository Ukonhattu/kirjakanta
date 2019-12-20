FROM python:3.4.2

WORKDIR /usr/app/
COPY . .
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python run.py