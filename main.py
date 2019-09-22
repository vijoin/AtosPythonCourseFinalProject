from flask import Flask, jsonify, abort, make_response, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

from final_project.flask_blog.models.post import *

posts = [{
            'id': 1,
            'author': 'Victor Inojosa',
            'email': 'vijoin@gmail.com',
            'date': '2019-10-03',
            'title': "Let's Begin",
            'body': """
                    <h2>Hi all!</h2>
                    <p>Welcome to the first class of Python Course.</p>
                    <p><img style="width: 50%;" src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"><br></p>
                    <p>Today it's a great day for all of us. I hope you learn from me as much as I will learn from you.</p>
                    <p>At the end of this course you'll be able to build an API REST and a simple but powerful Blog.</p>
                    <p>Please, feel free to make any suggestions!</p><p><b>Let's begin!</b></p>
            """,
        },
            {
            'id': 2,
            'author': 'Victor2 Inojosa2',
            'email': 'vijoin@gmail.com2',
            'date': '2019-10-04',
            'title': "Let's Begin2",
            'body': """"
                        <h2>Hi all!</h2>
                        <p>Welcome to the first class of Python Course.</p>
                        <p><img style="width: 50%;" src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"><br></p>
                        <p>Today it's a great day for all of us. I hope you learn from me as much as I will learn from you.</p>
                        <p>At the end of this course you'll be able to build an API REST and a simple but powerful Blog.</p>
                        <p>Please, feel free to make any suggestions!</p><p><b>Let's begin!</b></p>
                """,
            }]

@app.route('/')
def index():
    return "Hello World"

@app.route("/blog/api/v0.1/mock_posts/<int:post_id>", methods=['GET'])
def get_mock_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if not post:
        abort(404)
    return jsonify({'post': post[0]})

@app.route('/blog/api/v0.1/posts')
def get_all_posts():
    return jsonify({'posts': posts})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/blog/api/v0.1/mock_posts', methods=['POST'])
def create_mock_post():
    if not request.json or not 'title' in request.json:
        abort(400)
    post = {
        'id': posts[-1]['id'] + 1,
        'title': request.json['title'],
        'author_id': request.json.get('author', ""),
        'body': request.json.get('body', ""),
    }
    posts.append(post)
    return jsonify({'post': post}), 201

@app.route('/blog/api/v0.1/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json:
        abort(400)
    post = Post(title=request.json['title'],
                author_id=request.json.get('author', 1),
                body=request.json.get('body', "No Data"))
    db.session.add(post)
    db.session.commit()
    return jsonify({"post": {'id': post.id, 'title': post.title}})

@app.route('/blog/api/v0.1/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    return jsonify({'post': {
                        'id': post.id,
                        'title': post.title,
                        'author': post.author_id,
                        'body': post.body,
                            }
                    })

if __name__ == '__main__':
    app.run()
    db.create_all()