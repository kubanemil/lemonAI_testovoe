FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]