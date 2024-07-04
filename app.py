from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('temp/home.html')  # This should point to your home.htmltemplate

if __name__ == '__main__':
    app.run(host='1.1',debug=True)
