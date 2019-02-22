#!/bin/bash

# Start mongo
mongod &

# Load data
sleep 10
mongo < /my_work_dir/load_quotes.js

while true
do
	sleep 1000
done
