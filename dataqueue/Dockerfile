FROM python:3
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=./dataqueue/app.py \
    FLASK_ENV=development \
    INTAKE_API_KEY=intake_key_placeholder \
    OUTTAKE_API_KEY=outtake_key_placeholder
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "flask", "run", "--host=0.0.0.0" ]