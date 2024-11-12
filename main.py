from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('pagina1.html')


@app.route('/pagina2')
def form2():
    return render_template('pagina2.html')


@app.route('/pagina3')
def form3():
    return render_template('pagina3.html')


if __name__ == '__main__':
    app.run()
