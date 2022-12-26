from flask import Flask
import Utils

app = Flask(__name__)




@app.route("/")
def show_score():
    score = Utils.get_score()
    if score == -1:
        return f'''<html>
               <head>
               <title>Scores Game</title>
               </head>
               <body>
               <h1><div id="score" style="color:red">{score}</div></h1>
               </body>
               </html>'''
    else:
        return f'''<html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score">{score}</div></h1>
        </body>
        </html>'''
