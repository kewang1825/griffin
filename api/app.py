from flask import Flask, make_response
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return make_response('OK', 200)


@app.route('/start/<string:app_name>', methods=['POST'])
def start(app_name):
    try:
        data = open('{0}.json'.format(app_name), 'rb').read()
    except:
        return make_response('cannot start application [{0}] which is not defined.'.format(app_name), 404)

    # The resource URL for the marathon action.
    marathon_url = 'http://localhost/marathon/v2/apps'

    # Set request headers.
    headers = {
        'Content-Type': 'application/json'
    }

    print('POST {0}'.format(marathon_url))
    response = requests.post(url=marathon_url, headers=headers, data=data)
    return make_response(response.text, response.status_code)


@app.route('/stop/<string:app_name>', methods=['POST'])
def stop(app_name):
    # The resource URL for the marathon action.
    marathon_url = 'http://localhost/marathon/v2/apps/{0}'.format(app_name)

    print('DELETE {0}'.format(marathon_url))
    response = requests.delete(url=marathon_url)
    return make_response(response.text, response.status_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

