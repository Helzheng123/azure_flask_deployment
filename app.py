from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

df = pd.read_csv('healthy_lifestyle_city_2021.csv')
@app.route('/data')
def data(data=df):
    data = data.head(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )