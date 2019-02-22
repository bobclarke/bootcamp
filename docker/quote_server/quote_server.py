from flask import Flask
import pymongo

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test Hello World!"

@app.route("/quote")
def quote():
	all_results = ""
	myclient = pymongo.MongoClient("mongodb://mongo:27017/")
	mydb = myclient["quotes_db"]
	mycol = mydb["quotes_col"]
	myquery = { "type": "quote" }
	results = mycol.find(myquery)
	for result in results:
		all_results += str(result)+'<br>'

	return all_results 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
