from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

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

@app.route("/blog/api/v0.1/posts/<int:post_id>", methods=['GET'])
def get_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if not post:
        abort(404)
    return jsonify({'post': post[0]})

@app.route('/blog/api/v0.1/posts')
def get_all_posts():
    return jsonify({'posts': posts})

if __name__ == '__main__':
    app.run()
    db.create_all()