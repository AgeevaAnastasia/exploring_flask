# Flask-SQLAlchemy

from flask import Flask, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from hw_3.models import db, User
from hw_3.forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# инициализация БД
db.init_app(app)

app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
# получение csrf - объекта для работы с формами
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'DB is running!'


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        second_name = form.second_name.data
        birth = form.birth.data
        sex = form.sex.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        existing_user = User.query.filter(User.email == email).first()

        if existing_user:
            error_msg = 'Such email already exists.'
            form.email.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(first_name=first_name,
                    second_name=second_name,
                    birth=birth,
                    sex=sex,
                    email=email,
                    password=password)
        db.session.add(user)
        db.session.commit()
        return 'Registration was successful!'
    return render_template('register.html', form=form)


@app.route('/get/')
def get():
    users = User.query.all()
    return render_template('register_db.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
