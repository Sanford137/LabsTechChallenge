from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/skm2159', methods=['GET'])
def sanford_miller():
    return render_template('sanford-miller.html')

if __name__ == '__main__':
    app.run()
