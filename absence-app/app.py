from flask import Flask, render_template, request, redirect, url_for, session  # Importe les modules nécessaires de Flask pour gérer l'application web
from flask_sqlalchemy import SQLAlchemy  # Pour la gestion de la base de données avec SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash  # Pour sécuriser les mots de passe avec hachage
from flask.cli import with_appcontext  # Permet d'utiliser les commandes personnalisées avec le contexte de l'app Flask
import click  # Utilisé pour créer des commandes en ligne de commande personnalisées

app = Flask(__name__)  # Initialise l'application Flask
app.config['SECRET_KEY'] = 'ma-cle-secrete'  # Clé secrète pour gérer les sessions utilisateur
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Chemin de la base de données SQLite
db = SQLAlchemy(app)  # Initialise SQLAlchemy avec l'app Flask

# --- MODELES ---
class User(db.Model):  # Modèle pour les utilisateurs (professeurs)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Presence(db.Model):  # Modèle pour enregistrer les présences, absences et retards
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    matiere = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    statut = db.Column(db.String(20), nullable=False)  # Statut de présence

# --- ROUTES ---
@app.route('/')  # Redirige vers la page de connexion
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])  # Gère l'affichage et la soumission du formulaire de connexion
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id  # Connexion réussie, on enregistre l'ID utilisateur en session
            return redirect(url_for('index'))  # Redirige vers la page d'accueil (tableau de bord)
        else:
            error = "Identifiants incorrects."  # Affiche une erreur si les identifiants sont faux
    return render_template('login.html', error=error)

@app.route('/logout')  # Déconnecte l'utilisateur et le redirige vers la page de connexion
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route("/dashboard")  # Affiche le tableau de bord avec les statistiques et les filtres
def dashboard():
    if 'user_id' not in session:  # Redirige vers login si l'utilisateur n'est pas connecté
        return redirect(url_for('login'))

    matiere = request.args.get("matiere", "")  # Récupère la matière sélectionnée (si présente)
    date = request.args.get("date", "")  # Récupère la date sélectionnée (si présente)

    query = Presence.query  # Commence la requête sur les présences
    if matiere:
        query = query.filter_by(matiere=matiere)
    if date:
        query = query.filter_by(date=date)

    donnees = query.all()  # Exécute la requête et récupère les enregistrements

    stats = {  # Calcule les statistiques de présence
        'present': query.filter_by(statut="Présent").count(),
        'absent': query.filter_by(statut="Absent").count(),
        'retard': query.filter_by(statut="En retard").count()
    }

    matieres = db.session.query(Presence.matiere).distinct().all()  # Récupère toutes les matières distinctes
    matieres = [m[0] for m in matieres]  # Transforme en liste simple

    return render_template("dashboard.html",
                           donnees=donnees,
                           stats=stats,
                           matieres=matieres,
                           matiere_selectionnee=matiere,
                           date_selectionnee=date)

# --- COMMANDE POUR CREER ADMIN ---
@click.command('create-admin')  # Commande CLI pour créer un utilisateur admin
@click.argument('username')
@click.argument('password')
@with_appcontext  # Permet d’exécuter dans le contexte de l’app Flask
def create_admin(username, password):
    if User.query.filter_by(username=username).first():
        print("Utilisateur déjà existant.")  # Vérifie si l’utilisateur existe déjà
    else:
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')  # Hache le mot de passe
        new_user = User(username=username, password=hashed_password)  # Crée un nouvel utilisateur
        db.session.add(new_user)
        db.session.commit()
        print(f"Admin '{username}' créé avec succès.")  # Confirmation

app.cli.add_command(create_admin)  # Ajoute la commande à l’interface CLI Flask

# --- INIT ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables dans la base de données au démarrage si elles n’existent pas
    app.run(debug=True)  # Lance le serveur Flask en mode debug
