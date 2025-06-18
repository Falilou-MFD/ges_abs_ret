from app import app, db
from models import Etudiant

# Crée un étudiant selon la structure de ta base
with app.app_context():
    nouvel_etudiant = Etudiant(
        id_etudiant="ETU1234",
        nom="Jean",
        prenom="Dupont",
        email="jean.dupont@example.com"
    )

    db.session.add(nouvel_etudiant)
    db.session.commit()
    print("✅ Étudiant ajouté avec succès.")
