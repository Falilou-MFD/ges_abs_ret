from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Etudiant(db.Model):
    id_etudiant = db.Column(db.String(10), primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)

class Enseignant(db.Model):
    id_enseignant = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)

class Cours(db.Model):
    nom_cours = db.Column(db.String(100), primary_key=True)
    id_enseignant = db.Column(db.Integer, db.ForeignKey('enseignant.id_enseignant'))
    date_cours = db.Column(db.Date)

class Absence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_etudiant = db.Column(db.String(10), db.ForeignKey('etudiant.id_etudiant'))
    nom_cours = db.Column(db.String(100), db.ForeignKey('cours.nom_cours'))
    date_absence = db.Column(db.Date)
    motif = db.Column(db.Text)

class Retard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_etudiant = db.Column(db.String(10), db.ForeignKey('etudiant.id_etudiant'))
    nom_cours = db.Column(db.String(100), db.ForeignKey('cours.nom_cours'))
    date_retard = db.Column(db.Date)
    duree_minutes = db.Column(db.Integer)

class Utilisateur(db.Model):
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20))
    id_etudiant = db.Column(db.String(10), db.ForeignKey('etudiant.id_etudiant'), nullable=True)
    id_enseignant = db.Column(db.Integer, db.ForeignKey('enseignant.id_enseignant'), nullable=True)