from final_project.flask_blog.main import db
from final_project.flask_blog.models.author import Author

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(120))
    body = db.Column(db.Text(1200))

    author = db.relationship('Author', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post {} - {:.20}>'.format(self.id, self.title)

