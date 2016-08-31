from flask import Flask, make_response, request
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return make_response('OK', 200)


@app.route('/start/<string:app_name>/<string:app_tag>', methods=['POST', 'PUT'])
def start(app_name, app_tag):
    try:
        data = open('{0}.json'.format(app_name), 'r').read()
    except:
        return make_response('cannot start application [{0}] which is not defined.'.format(app_name), 404)

    # The resource URL for the marathon action.
    if app_name[-6:] == "-group":
        marathon_url = 'http://localhost/marathon/v2/groups'
    else:
        marathon_url = 'http://localhost/marathon/v2/apps'

    if request.method == 'PUT':
        marathon_url += '/{0}'.format(app_name)

    print('{0} {1}'.format(request.method, marathon_url))

    # Set request headers.
    headers = {
        'Content-Type': 'application/json'
    }

    # Set request data.
    data = data.replace('#app_tag', app_tag)

    if request.method == 'POST':
        response = requests.post(url=marathon_url, headers=headers, data=data, params=request.args)
    else:
        response = requests.put(url=marathon_url, headers=headers, data=data, params=request.args)

    return make_response(response.text, response.status_code)


@app.route('/stop/<string:app_name>', methods=['POST'])
def stop(app_name):
    # The resource URL for the marathon action.
    if app_name[-6:] == "-group":
        marathon_url = 'http://localhost/marathon/v2/groups/{0}'.format(app_name)
    else:
        marathon_url = 'http://localhost/marathon/v2/apps/{0}'.format(app_name)

    print('DELETE {0}'.format(marathon_url))
    response = requests.delete(url=marathon_url)
    return make_response(response.text, response.status_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

