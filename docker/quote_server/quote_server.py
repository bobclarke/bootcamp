from flask import Flask
import pymongo
import sys
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test Hello World!"

@app.route("/quote")
def quote():
	all_results = '<html><head><style> ' 
	all_results += 'tr:nth-child(even){background-color: #f2f2f2} ' 
	all_results += 'th {  background-color: #4CAF50; color: white;} ' 
	all_results += 'table {border-collapse: collapse;} ' 
	all_results += 'th, td {padding: 8px;} ' 
	all_results += '</style></head><body>' 
	all_results += '<p>Quote Server</p>' 
	all_results += '<table><tr><th> Quote </th></tr>'

	myclient = pymongo.MongoClient("mongodb://" + os.getenv('MONGO_SVC', 'db-svc.bootcamp.svc.cluster.local') + ":" + os.getenv('MONGO_PORT', '27017') +  "/")
	mydb = myclient["test"]
	mycol = mydb["quotes_col"]
	myquery = { "type": "quote" }
	results = mycol.find(myquery)
	for result in results:
		all_results += '<tr><td>' + str(result['text']) + '</td></tr>'

	all_results += '</table>'
	all_results += '</body></html>'
	return all_results 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
