from app import app
from models import db, Utilisateur, Enseignant, Etudiant
from werkzeug.security import generate_password_hash

# === Modifier ces valeurs selon le type d'utilisateur à créer ===
role = 'enseignant'  # ou 'etudiant'
email = 'prof@example.com'
mot_de_passe = 'monmotdepasse'

with app.app_context():
    # Vérifie si l'utilisateur existe déjà
    if Utilisateur.query.filter_by(email=email).first():
        print("❌ Utilisateur déjà existant.")
    else:
        if role == 'enseignant':
            enseignant = Enseignant(nom='Dupont', prenom='Jean', email=email)
            db.session.add(enseignant)
            db.session.commit()

            utilisateur = Utilisateur(
                email=email,
                mot_de_passe=generate_password_hash(mot_de_passe),
                role='enseignant',
                id_enseignant=enseignant.id_enseignant
            )
        elif role == 'etudiant':
            etudiant = Etudiant(id_etudiant='E001', nom='Durand', prenom='Lucie', email=email)
            db.session.add(etudiant)
            db.session.commit()

            utilisateur = Utilisateur(
                email=email,
                mot_de_passe=generate_password_hash(mot_de_passe),
                role='etudiant',
                id_etudiant=etudiant.id_etudiant
            )
        else:
            print("❌ Rôle invalide.")
            exit()

        db.session.add(utilisateur)
        db.session.commit()
        print(f"✅ Utilisateur {email} ({role}) créé avec succès.")
