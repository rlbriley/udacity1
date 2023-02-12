from flask import Flask
from flask import json
import logging
import datetime
from datetime import timezone

from flask import Flask
app = Flask(__name__)
timeStart = datetime.datetime.now(timezone.utc)
mainCount=0
statusCount=0
metricsCount=0

# Stream logs to a file, and set the default log level to DEBUG
#logging.basicConfig(filename='app.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)-8s - %(message)s' )
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)-8s - %(message)s' )


@app.route("/")
def hello():
    global mainCount
    mainCount+=1
    # Logging a CUSTOM message
    app.logger.info('Main request successful')
    return "Hello World!"

@app.route("/status")
def status():
    global statusCount
    statusCount+=1
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('status request successful response=' + json.dumps(response.json))
    return response

@app.route("/metrics")
def metrics():
    global mainCount
    global statusCount
    global metricsCount
    global timeStart
    metricsCount+=1
    timeCurrent=datetime.datetime.now(timezone.utc)
    response = app.response_class(
        response=json.dumps({"status":"success",
            "code": 0,
            "data":{"MainCount":mainCount,"StatusCount":statusCount,"MetricsCount":metricsCount},
            "uptime":str(timeCurrent-timeStart)}),
        status=200,
        mimetype='application/json'
    )
    app.logger.debug('metrics request successful response=' + json.dumps(response.json))
    return response

if __name__ == "__main__":
  app.logger.debug('app application starting')
  app.run(host='0.0.0.0')
  #app.run(host='0.0.0.0', port=8080)
  app.logger.debug('app application finished')

