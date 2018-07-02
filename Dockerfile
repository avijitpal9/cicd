FROM python:2.7
MAINTAINER avijitpal.1987@gmail.com
RUN pip install flask
ADD dist/myapp-0.1.tar.gz /opt/
