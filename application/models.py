from application import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(300), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'Question: ', self.question, '\r\n',
            'Answer: ', self.answer, '\r\n'
            'ID: ', str(self.id), '\r\n'
            ])



class Quizzes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False, unique=True)
    question_id_1=db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=True)
    question_id_2=db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=True)
    question_id_3=db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=True)
    date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return ''.join([
            'Title: ', self.title, '\r\n',
            'Questions: ', self.question_id_1, '\r\n', self.question_id_2, '\r\n', self.question_id_3, '\r\n'
            ])
