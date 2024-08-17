from ..database import db

class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
    details = db.Column(db.String, nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String, nullable=False)
    
    __table_args__ = (db.UniqueConstraint('id', 'title', name='_id_title_uc'),)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user_id': self.user_id,
            'details': self.details,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'status': self.status
        }
