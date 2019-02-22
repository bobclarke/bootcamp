FROM mongo

WORKDIR /my_work_dir

COPY load_quotes.js .
COPY start_and_load_mongo.sh .
RUN chmod +x start_and_load_mongo.sh

CMD ["/my_work_dir/start_and_load_mongo.sh"]

