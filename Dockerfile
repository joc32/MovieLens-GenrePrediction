FROM python:3.7.5-slim
FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-devel
RUN pip install --upgrade pip
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD ["python3","setup.py"]