from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth

from post import Post
from comment import Comment
from category import Category
from user import User

app = Flask(__name__)
auth = HTTPBasicAuth()


@app.route('/')
def hello_world():
    return redirect("/categories")


@app.route('/posts')
def list_posts():
    return render_template('posts.html', posts=Post.all())


@app.route('/posts/<int:id>')
def show_post(id):
    post = Post.find(id)

    return render_template('post.html', post=post)


@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.find(id)
    if request.method == 'GET':
        return render_template(
            'edit_post.html',
            post=post,
            categories=Category.all()
        )
    elif request.method == 'POST':
        post.name = request.form['name']
        post.author = request.form['author']
        post.content = request.form['content']
        post.category = Category.find(request.form['category_id'])
        post.save()
        return redirect(url_for('show_post', id=post.id))


@app.route('/posts/new', methods=['GET', 'POST'])
@auth.login_required
def new_post():
    if request.method == 'GET':
        return render_template('new_post.html', categories=Category.all())
    elif request.method == 'POST':
        categ = Category.find(request.form['category_id'])
        values = (
            None,
            request.form['name'],
            request.form['author'],
            request.form['content'],
            categ
        )
        Post(*values).create()

        return redirect('/')


@app.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    post = Post.find(id)
    post.delete()

    return redirect('/')


@app.route('/comments/new', methods=['POST'])
def new_comment():
    if request.method == 'POST':
        post = Post.find(request.form['post_id'])
        values = (None, post, request.form['message'])
        Comment(*values).create()

        return redirect(url_for('show_post', id=post.id))


@app.route('/categories')
def get_categories():
    return render_template("categories.html", categories=Category.all())


@app.route('/categories/new', methods=["GET", "POST"])
def new_category():
    if request.method == "GET":
        return render_template("new_category.html")
    elif request.method == "POST":
        category = Category(None, request.form["name"])
        category.create()
        return redirect("/categories")


@app.route('/categories/<int:id>')
def get_category(id):
    return render_template("category.html", category=Category.find(id))


@app.route('/categories/<int:id>/delete')
def delete_category(id):
    Category.find(id).delete()
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        values = (None, request.form['username'], User.hash_password(request.form['password']))

        User(*values).create()
        return redirect('/')

@auth.verify_password
def verify_password(username, password):
    user = User.find_by_username(username)

    if not user:
        return False

    return user.verify_password(password)