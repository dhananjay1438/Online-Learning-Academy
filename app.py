from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html', title="Home")

@app.route('/teenager_prayer')
def teenager_prayer():
    return render_template('teenager_prayer.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)