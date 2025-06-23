
# 📚 Application de Gestion des Absences et Retards – Projet Microservice (Flask + Docker)

## 🧠 Contexte du projet

Ce projet est une **application web de gestion des absences et des retards** des étudiants. L’objectif est de permettre l’enregistrement des absences et retards via une interface simple.

L’application est conçue dans une **architecture microservice**, avec :

- un backend développé en **Flask** (Python),
- un frontend en **HTML/CSS**,
- une **containerisation via Docker**, avec **Docker Compose** pour l’orchestration,


## ⚙️ Technologies utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML / CSS
- **Containerisation** : Docker
- **Orchestration** : Docker Compose
- **Notification** : Envoi d’e-mail via SMTP

## 🗂️ Architecture du projet

```
ges_abs_ret/
│
├── app/                      
│   ├── templates/            
│   ├── static/               
│   ├── routes.py             
│   ├── venv
│   ├── Dockerfile                
│   ├── docker-compose.yml        
│   ├── requirements.txt          
│   ├── app.py
│   ├── config.py
│   ├── create_etudiant.py
│   ├── Jenkinsfile
│   ├── models.py
│   ├── run.py 
│
└── README.md                 # Ce fichier de documentation
```

## 🔐 Configuration requise 
Lancer un environnemnet virtuel et telecharger les requirements

## 🚀 Étapes pour exécuter le projet

### ✅ Prérequis

Assurez-vous d’avoir installé sur votre machine :

Docker

### ▶️ Lancer l'application

Dans le terminal, placez-vous à gestion_presence_app exécutez :

```bash
docker-compose up --build
```

Cela va :

1. Construire l’image Docker à partir du `Dockerfile`.
2. Démarrer le conteneur avec **Gunicorn** en production.
3. Exposer l’application à l’adresse : [http://localhost:5000](http://localhost:5000)


## 🔁 Commandes utiles

| Commande Docker                  | Description                                |
|----------------------------------|--------------------------------------------|
| `docker-compose up --build`     | Construction et démarrage du service        |
| `docker-compose down`           | Arrêt et suppression des conteneurs         |
| `docker-compose logs`           | Affichage des logs du backend               |
| `docker ps`                     | Vérification des conteneurs en cours        |


## 👥 Auteurs du projet

- **Votre Nom** – Développement backend & dockerisation  
- **Autres membres** – Frontend, intégration des emails, tests

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de le modifier, réutiliser ou le partager, avec mention des auteurs d’origine.

## 📷 Capture d’écran (à ajouter)

> Vous pouvez insérer ici des captures d’écran de l’interface utilisateur.

## ✅ Résumé

| Élément                    | Description                                     |
|----------------------------|-------------------------------------------------|
| But                        | Gérer les absences et retards des étudiants     |
| Backend                    | Flask (Python)                                  |
| Frontend                   | HTML/CSS                                        |
| Déploiement local          | Docker & Docker Compose                         |
| Email au professeur        | Automatisé via SMTP                             |
| Lancement                  | `docker-compose up --build`                     |
| Interface                  | [http://localhost:5000](http://localhost:5000)  |


## 🧪 Étapes détaillées pour utiliser l'application

Voici les étapes à suivre, **une par une**, pour exécuter l'application de gestion des absences et retards :

### Cloner le projet depuis le dépôt Git

Si vous n'avez pas encore le projet sur votre machine, exécutez dans le terminal :

```bash
git clone https://github.com/Falilou-MFD/ges_abs_ret.git
cd ges_abs_ret/gestion_presence_app
```

Lancer un environnemnet virtuel et telecharger les requirements

### Vérifier les fichiers `Dockerfile` et `docker-compose.yml`

Assurez-vous que le `Dockerfile` et le `docker-compose.yml` sont bien présents. Si ce n’est pas le cas, demandez à votre responsable technique ou récupérez-les depuis le dépôt officiel du projet.

### Lancer Docker Desktop (ou votre service Docker préféré)

Avant d’exécuter les commandes suivantes, ouvrez votre service Docker. Sur Windows cela signifie démarrer **Docker Desktop**.

### Construire et exécuter les conteneurs avec Docker Compose

```bash
docker-compose up --build
```

Cette commande :
- construit l'image Docker à partir du `Dockerfile`,
- lit la configuration de `docker-compose.yml`,
- démarre le serveur Flask via Gunicorn dans un conteneur.

### Accéder à l'application dans le navigateur

Une fois les services démarrés, ouvrez votre navigateur à l’adresse suivante :

👉 [http://localhost:5000](http://localhost:5000)

Vous devriez voir l’interface de soumission des absences et retards.


## ✅ Bonnes pratiques

- Toujours faire `docker-compose down` pour arrêter les services une fois terminé.

