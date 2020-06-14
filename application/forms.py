from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class QuestionForm(FlaskForm):
    question = StringField('Question: ',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    answer  = StringField('Answer: ',
        validators = [
            DataRequired(),
            Length(min=1, max=100)
        ]  
        )
    submit = SubmitField('Add!')


class QuizForm(FlaskForm):
    title=StringField('Title',
            validators=[
                DataRequired(),
                Length(min=1, max=100)
        ]
        )
    
    submit = SubmitField('Add!')

