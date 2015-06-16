FROM marina/python-web:1.0.1
# The base image brings with it Python 2.7, gevent, and uwsgi.

ADD requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

ADD . /src
WORKDIR /src

# Run
CMD ["/usr/local/bin/uwsgi", "--ini", "/src/uwsgi.ini"]
