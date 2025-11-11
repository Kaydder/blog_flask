from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import NewPostForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-this"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"

@app.route("/")
def home():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("home.html", name="Kayder", posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)

@app.route("/new", methods=["GET", "POST"])
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new = Post(
            title=form.title.data,
            content=form.content.data,
            author=form.author.data
        )
        db.session.add(new)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new_post.html", form=form)

@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = NewPostForm(obj=post) 

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.author = form.author.data
        db.session.commit()
        flash(f"Post '{post.title}' updated successfully!", "success")
        return redirect(url_for("post_detail", post_id=post.id))

    return render_template("edit_post.html", form=form, post=post)

@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post '{post.title}' deleted successfully!", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
