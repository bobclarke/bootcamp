#!/bin/bash

# Start mongo
mongod &

# Load data
mongo < /opt/load_quotes.js
