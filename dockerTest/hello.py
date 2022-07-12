# REST APIs
#Request Method:
    # GET           Endpoint: www.godev.today/api/v1/helloApi, It returns message 'Hello World!'
    # POST
    # PATCH
    # DELETE

# localhost = 127.0.0.1
# Port number: 5004

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/v1/helloApi')
def testApp():
    return jsonify({'message':'Hello World!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    