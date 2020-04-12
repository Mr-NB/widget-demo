#Monitor-Probe
#
#VERSION 1.0

FROM python:3.7
LABEL AUTHOR="Niu Ben<v-beniu@microsoft.com>"
USER root

WORKDIR /usr/src/test
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wget vim
COPY . .

CMD ["python", "main.py"]