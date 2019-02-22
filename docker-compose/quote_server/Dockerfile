FROM python:3
RUN pip install flask
RUN pip install pymongo

WORKDIR /usr/src/app

COPY quote_server.py ./

EXPOSE 5000

CMD [ "python", "quote_server.py" ]
