from flask import Blueprint, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash
from models import Utilisateur

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        mdp = request.form['password']
        user = Utilisateur.query.filter_by(email=email).first()

        if user and check_password_hash(user.mot_de_passe, mdp):
            session['user_id'] = user.id_utilisateur
            session['role'] = user.role
            session['id_etudiant'] = user.id_etudiant
            session['id_enseignant'] = user.id_enseignant

            if user.role == 'enseignant':
                return redirect(url_for('prof.dashboard'))
            elif user.role == 'etudiant':
                return redirect(url_for('etudiant.dashboard'))
        else:
            return "Email ou mot de passe incorrect"

    return render_template('login.html')