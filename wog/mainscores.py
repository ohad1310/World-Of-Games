from flask import Flask


app = Flask(__name__)


@app.route('/')
def score_server(scores):
    try:
        score = open("scores.txt", "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + ERROR_MESSAGE + str(scores) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8777)