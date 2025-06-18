from flask import Blueprint, render_template, request, session
from models import Absence, db
from datetime import datetime  # ✅ Import nécessaire pour convertir la date

prof_bp = Blueprint('prof', __name__, url_prefix='/prof')

@prof_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session.get('role') != 'enseignant':
        return "Accès interdit"

    if request.method == 'POST':
        id_etudiant = request.form['id_etudiant']
        nom_cours = request.form['nom_cours']
        date_str = request.form['date']  # On garde la chaîne temporairement
        motif = request.form['motif']

        try:
            # ✅ Convertir en objet date Python
            date_absence = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return "Format de date invalide. Utilisez AAAA-MM-JJ."

        # Enregistrement de l'absence
        absence = Absence(
            id_etudiant=id_etudiant,
            nom_cours=nom_cours,
            date_absence=date_absence,  # ✅ Type correct
            motif=motif
        )
        db.session.add(absence)
        db.session.commit()

    return render_template('dashboard_prof.html')
