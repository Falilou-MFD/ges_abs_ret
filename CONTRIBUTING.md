# Guide de Contribution - Application de gestion des absences et des retards

Bienvenue dans notre projet ! Ce guide vous accompagnera pas à pas pour contribuer efficacement au développement de l'application.

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- Git
- Visual Studio Code (VSCode)
- Python 3.8+ (si applicable au projet)
- Node.js (si applicable au projet)

## 🚀 Démarrage rapide

### 1. Cloner le repository


# Cloner le repository
git clone https://github.com/Falilou-MFD/ges_abs_ret.git

# Se déplacer dans le dossier du projet
cd application-gestion-absences-retards


### 2. Ouvrir le projet dans VSCode


# Ouvrir le projet dans VSCode
code .


Ou bien ouvrez VSCode et utilisez `File > Open Folder` pour sélectionner le dossier du projet.

### 3. Créer et se déplacer sur votre branche de travail

**⚠️ IMPORTANT : Chaque développeur doit travailler sur sa propre branche !**




### 4. Configuration de l'environnement de développement

#### 4.1 Créer un environnement virtuel (Python)

Si le projet utilise Python :

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur macOS/Linux :
source venv/bin/activate
```

## 💻 Flux de travail de développement

### 1. Avant de commencer à coder

```bash
# S'assurer d'être sur votre branche
git branch

# Récupérer les dernières modifications du main
git checkout main
git pull origin main
git checkout votre-branche
git merge main
```

### 2. Développement et commits

#### Règles pour les commits :

- **Faites des commits fréquents** : Même pour une seule ligne ajoutée !
- **Messages clairs et descriptifs** : Décrivez précisément ce qui a été fait



#### Exemples de bons commits :

```bash
git add .
git commit -m "feat: Ajoute le bouton de connexion"

git add .
git commit -m "feat: Ajoute la validation du champ mot de passe"

git add .
git commit -m "fix: Corrige l'affichage des dates d'absence"

git add .
git commit -m "docs: Ajoute la documentation de l'API"

git add .
git commit -m "style: Améliore le style du formulaire de connexion"
```

### 3. Pousser vos modifications

```bash
# Pousser votre branche vers le repository distant
git push origin votre-branche
```

### 4. Créer une Pull Request

1. Allez sur GitHub
2. Cliquez sur "Compare & pull request"
3. Rédigez une description claire de vos modifications
4. Assignez au moins un reviewer
5. Attendez la validation avant le merge

## 🔒 Règles de sécurité et bonnes pratiques

### Protection de la branche main

- ✅ Les merges directs sur `master` sont interdits
- ✅ Une Pull Request avec validation est obligatoire
- ✅ Au moins un reviewer doit approuver les changements


### Sécurité des données

- 🚫 **JAMAIS** de mots de passe ou clés API dans le code

# Vérifier le formatting du code
black .           # Pour Python
prettier .        # Pour JavaScript
```



*Pour toute question ou suggestion d'amélioration de ce guide, n'hésitez pas à ouvrir une issue.*
