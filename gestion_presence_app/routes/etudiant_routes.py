from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Etudiant, db
# from app import db

etudiant_bp = Blueprint('etudiant', __name__)

@etudiant_bp.route('/login-etudiant', methods=['GET', 'POST'])
def login_etudiant():
    if request.method == 'POST':
        matricule = request.form['matricule']
        mot_de_passe = request.form['mot_de_passe']
        etudiant = Etudiant.query.filter_by(matricule=matricule).first()

        if etudiant and etudiant.check_password(mot_de_passe):
            session['etudiant_id'] = etudiant.id
            return redirect(url_for('etudiant.dashboard_etudiant'))
        else:
            flash("Matricule ou mot de passe incorrect.", "danger")

    return render_template('login_etudiant.html')


@etudiant_bp.route('/dashboard-etudiant')
def dashboard_etudiant():
    if 'etudiant_id' not in session:
        return redirect(url_for('etudiant.login_etudiant'))

    etudiant = Etudiant.query.get(session['etudiant_id'])

    absences = etudiant.absences  # à condition d’avoir une relation entre Absence et Etudiant

    return render_template('dashboard_etudiant.html', etudiant=etudiant, absences=absences)
