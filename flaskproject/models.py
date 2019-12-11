
from datetime import datetime
from sqlalchemy import DateTime
from flaskproject import app, db


class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self, content, data_created):
        return '<Task %i>' % self.id
