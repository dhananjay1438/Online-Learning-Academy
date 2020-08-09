from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html', title="Home")

@app.route('/teenager_prayer')
def teenager_prayer():
    return render_template('teenager_prayer.html')

@app.route('/be_smart')
def be_smart():
    return render_template('be_smart.html')

@app.route('/degree_of_comparison')
def degree_of_comparison():
    return render_template('degree_of_comparison.html')

@app.route('/language_study')
def language_study():
    return render_template('language_study.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)