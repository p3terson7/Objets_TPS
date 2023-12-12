# Run: python -m flask --app myapp run
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = '1738'  # Clé secrète

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin): # Classe utilisateur
    def __init__(self, password_hash):
        self.id = 'user'
        self.password_hash = password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

user = User(generate_password_hash('1212'))  # Utilisateur avec mot de passe 1212

@login_manager.user_loader
def load_user(user_id): # Charge l'utilisateur
    if user_id == user.id:
        return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login(): # Page de connexion
    if request.method == 'POST':
        password = request.form['password']
        if len(password) == 4 and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Mot de passe invalide!')
    return render_template('login.html')

data = [
    {
        "Temperature": "21.1",
        "Humidity": "54.1",
    }
]

@app.route('/')
@login_required # Force la connexion
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
