'''Test application for UDACITY class'''
# pylint: disable-msg=C0103
import datetime
import logging
from datetime import timezone

from flask import Flask, json

app = Flask(__name__)
time_start = datetime.datetime.now(timezone.utc)
main_cnt = 0
status_cnt = 0
metrics_cnt = 0

# Stream logs to a file, and set the default log level to DEBUG
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s - %(levelname)-8s - %(message)s' )

# default REST route
@app.route("/")
def hello():
    '''default REST route'''
    global main_cnt
    main_cnt += 1
    # Logging a CUSTOM message
    app.logger.info('Main request successful')
    return "Hello World!"

# status REST route.
# Will return "OK - healthy" if the application is running
@app.route("/status")
def status():
    '''
    status REST route.
    Will return "OK - healthy" if the application is running
    '''
    global status_cnt
    status_cnt += 1
    response = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info('status request successful response=' + json.dumps(response.json))
    return response

# metrics REST route.
# will return the number of times each endpoint has been accessed. Plus the uptime for the
# application.
@app.route("/metrics")
def metrics():
    '''
    metrics REST route.
    will return the number of times each endpoint has been accessed. Plus the uptime for the
    application.
    '''
    global metrics_cnt
    metrics_cnt += 1
    current_time = datetime.datetime.now(timezone.utc)
    response = app.response_class(
        response = json.dumps({"status":"success",
            "code": 0,
            "data":{"main_cnt":main_cnt,"status_cnt":status_cnt,"metrics_cnt":metrics_cnt},
            "uptime":str(current_time-time_start)}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.debug('metrics request successful response=' + json.dumps(response.json))
    return response

if __name__ == "__main__":
    app.logger.debug('app application starting')
    app.run(host = '0.0.0.0')
    #app.run(host='0.0.0.0', port=8080)
    app.logger.debug('app application finished')

# pylint: enable-msg=C0103
