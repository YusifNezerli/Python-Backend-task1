from flask import Flask, render_template, request

app =  Flask(__name__)


# @app.route('/home')
# def home():
#     return render_template("home.html")

# @app.route('/about')
# def home():
#     return render_template('about.html')

# @app.route('/')
# def home():

# @app.route('/all-page')
# def all():
#     our_page = request.args.get('page')
#     return render_template(our_page)

@app.route('/all-page')
def all():
    name = request.args.get('name')
    return render_template('introduction.html', namee=name)
