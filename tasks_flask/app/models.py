from .app import db


class Tasks(db.Model):
    __tablename__ = 'tasks'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name):
        self.name = name
