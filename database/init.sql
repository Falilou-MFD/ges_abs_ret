-- Table des étudiants
CREATE TABLE Etudiant (
    id_etudiant VARCHAR(10) PRIMARY KEY, 
    nom VARCHAR(50),
    prenom VARCHAR(50),
    email VARCHAR(100) UNIQUE,
);

-- Table des enseignants
CREATE TABLE Enseignant (
    id_enseignant VARCHAR PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

-- Table des cours
CREATE TABLE Cours (
    nom_cours VARCHAR(100) PRIMARY KEY,
    id_enseignant INTEGER REFERENCES Enseignant(id_enseignant)
    date_cours DATE
);

-- Table des absences
CREATE TABLE Absence (
    id_etudiant VARCHAR(10) REFERENCES Etudiant(id_etudiant),
    nom_cours INTEGER REFERENCES Cours(nom_cours),
    date_absence DATE,
    motif TEXT
);

-- Table des retards
CREATE TABLE Retard (
    id_etudiant VARCHAR(10) REFERENCES Etudiant(id_etudiant),
    nom_cours INTEGER REFERENCES Cours(nom_cours),
    date_retard DATE,
    duree_minutes INTEGER
);

-- Table des utilisateurs (authentification)
CREATE TABLE Utilisateur (
    id_utilisateur SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('etudiant', 'enseignant')),
    id_etudiant VARCHAR(10),
    id_enseignant INTEGER,
    FOREIGN KEY (id_etudiant) REFERENCES Etudiant(id_etudiant),
    FOREIGN KEY (id_enseignant) REFERENCES Enseignant(id_enseignant)
);

