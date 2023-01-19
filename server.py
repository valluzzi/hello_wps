
import os
import flask

import pywps
from pywps import Service
from processes.sayhello import SayHello


app = flask.Flask(__name__)


# This is, how you start PyWPS instance
service = Service([SayHello()], ['pywps.cfg'])

@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return service


@app.route("/")
def hello():
    server_url = pywps.configuration.get_config_value("server", "url")
    request_url = flask.request.url
    return flask.render_template('index.html', request_url=request_url,
                                 server_url=server_url,
                                 #process_descriptor=process_descriptor
                                 )




if __name__ == "__main__":
    app.run(threaded=True,host='127.0.0.1')
