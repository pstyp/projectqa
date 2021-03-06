from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Questions, Quizzes
from application.forms import QuestionForm, QuizForm 



@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')



@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    quizData=Quizzes.query.all()
    form=QuizForm()
    if form.validate_on_submit():
        quizData=Quizzes(
                title=form.title.data)
        db.session.add(quizData)
        db.session.commit()
        return redirect(url_for('quiz'))
    else:
        print(form.errors)

    return render_template('quiz.html', title='quizzes', form=form, quizzes=quizData)

@app.route('/questions',  methods=['GET', 'POST'])
def questions():
    questionData=Questions.query.all()
    form = QuestionForm()
    if form.validate_on_submit():
        questionData = Questions(
            question = form.question.data,
            answer = form.answer.data,
                    )

        db.session.add(questionData)
        db.session.commit()

        return redirect(url_for('questions'))
    else:
        print(form.errors)
        
    return render_template('questions.html', title='questions', questions=questionData, form=form)


@app.route('/update_question/<int:id>', methods=['GET', 'POST'])
def update_question(id):
    quest=Questions.query.filter_by(id=id).first()
    form = QuestionForm()
    if form.validate_on_submit():
        quest.question=form.question.data
        quest.answer=form.answer.data
        db.session.commit()
        return redirect(url_for('questions'))
    elif request.method=='GET':
        form.question.data=quest.question
        form.answer.data=quest.answer

    return render_template('update_question.html', title='Update question', form=form, id=id)




@app.route('/delete_question/<int:id>', methods=['GET', 'POST'])
def delete_question(id):
    quest=Questions.query.filter_by(id=id).first()
    db.session.delete(quest)
    db.session.commit()
    return redirect(url_for('questions'))


#@app.route('add_question_to_quiz/<int:id>', methods=['GET', 'POST'])
#def add_question_to_quiz(id):
 #   quest=Questions.query.filter_by(id=id).first()




