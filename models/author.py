from final_project.flask_blog.main import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return "<Author: {} - {}>".format(self.name, self.email)