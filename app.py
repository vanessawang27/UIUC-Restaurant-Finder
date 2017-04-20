import os
from flask import Flask, render_template
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')

app = Flask(__name__, template_folder = template_dir )


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# @app.route('/search/<input>', methods=['POST'])
# def search(input):   
#
#   return 

@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run()

