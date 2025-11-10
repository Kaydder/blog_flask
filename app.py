from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {

        'id' : 1,
        'title' : 'First post',
        'content' : 'This is my first post using Flask templates.',
        'author' : 'Kayder'
    },
    {
        'id': 2,
        'title': 'Learning Flask',
        'content': 'Flask makes it easy to create web apps with Python.',
        'author': 'Kayder'
    },
    {
        'id': 3,
        'title': 'API RESTful project',
        'content': 'Next step: building RESTful APIs using Flask and JSON.',
        'author' : 'Kayder'
    }
]

@app.route("/")
def home():
    name = "Kayder"
    return render_template("home.html", name=name, posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)
