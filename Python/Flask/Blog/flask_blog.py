from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Zhangda Xu',
        'title': 'Blog Post 1',
        'content': 'First post!',
        'date_posted': 'May 1, 2020'
    },
    {
        'author': 'Yanming Zhou',
        'title': 'Blog Post 2',
        'content': 'Second post!',
        'date_posted': 'May 1, 2020'
    }


]


@app.route("/")     # root page
@app.route("/home")  # home page
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")    # about page
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
