FROM mongo

WORKDIR /my_work_dir

COPY load_quotes.js .
COPY start_and_load_mongo.sh .

CMD ["/opt/start_and_load_mongo.sh"]

