from flask import Flask,render_template,url_for,flash, redirect
from jason_web_server import app,db,bcrypt
from jason_web_server.forms import RegistrationForm, LoginForm
from jason_web_server.models import User,Post
from flask_login import login_user, current_user, logout_user



posts = [
    {
        'author':'smile',
        'title':'hello world',
        'content':'This is a hello world post',
        'date_posted':'2019 8 8'
    },
    {
        'author':'smile',
        'title':'hello world',
        'content':'This is a hello world post',
        'date_posted':'2019 8 8'
    },
    {
        'author':'smile',
        'title':'hello world',
        'content':'This is a hello world post',
        'date_posted':'2019 8 8'
    },
    {
        'author':'smile',
        'title':'hello world',
        'content':'This is a hello world post',
        'date_posted':'2019 8 8'
    }
]
@app.route('/')
def index():
    return render_template('main.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="关于我们")


@app.route('/echo/<msg>')
def echo(msg):
    return '<h1>Hello I am a echo website. I can eho everything: {}</h1>'.format(msg)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # db.create_all()
        db.session.add(user)
        db.session.commit()
        flash(f'您的账号已经成功注册了~欢迎【{form.username.data}】加入乐学', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="注册界面", form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("index"))
        else:
            flash("登录失败，请确定账号和密码是否正确", "danger")
    return render_template('login.html', title="登录界面", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))