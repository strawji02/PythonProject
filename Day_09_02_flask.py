
from flask import Flask, render_template
import Day_08_01_lambda


app = Flask(__name__)

@app.route('/')
def index():
    return 'hellow, flask!'

@app.route('/randoms')
def randoms():
    a = Day_08_01_lambda.makerandoms(10)
    return str(a)


@app.route('/randoms/<int:count>')
def randomsCouts(count):
    a = Day_08_01_lambda.makerandoms(int(count))
    return str(a)

@app.route('/html')
def html():
    return render_template('randoms.html')

if __name__ == '__main__':
    app.run(debug=True)







