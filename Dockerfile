FROM python:3.6.5-alpine

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src

CMD python manage.py run -h 0.0.0.0