from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')
# app.run(debug=True)


@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify({
        'working': 'yes!!',
    })



