from flask import Flask, render_template, request
from typograf import typograf

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']
    processed_text = typograf(text)
    return render_template('form.html', content=processed_text)


if __name__ == "__main__":
    app.run()
