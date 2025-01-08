## 🔑 **Vérificateur et Générateur de Mots de Passe Sécurisés**

Un outil en Python qui combine deux fonctionnalités essentielles pour la gestion des mots de passe :  
1. **Génération de mots de passe sécurisés** selon des critères définis (longueur et caractères spéciaux).  
2. **Vérification de la robustesse et de la compromission des mots de passe** à l'aide de plusieurs tests de sécurité et de l'API Have I Been Pwned.

---

### 📋 **Fonctionnalités**  

1. **Générateur de mots de passe**  
   - Permet de générer des mots de passe aléatoires.  
   - Options disponibles :  
     - Longueur personnalisée.  
     - Inclusion ou exclusion des caractères spéciaux.  
   - Les mots de passe générés sont conçus pour être robustes face aux attaques courantes.  

2. **Vérificateur de mots de passe**  
   - Évalue la robustesse du mot de passe en fonction de plusieurs critères :  
     - Longueur (>= 12 caractères).  
     - Présence de lettres majuscules et minuscules.  
     - Inclusion de chiffres et de caractères spéciaux.  
   - Vérifie si le mot de passe est compromis en utilisant l'API [Have I Been Pwned](https://haveibeenpwned.com/).  

---

### 🛠️ **Installation et Prérequis**  

1. **Python 3.x** doit être installé sur votre machine. Vous pouvez le télécharger [ici](https://www.python.org/downloads/).  
2. Installez les dépendances nécessaires avec la commande :  
   ```bash
   pip install requests colorama
   ```

---

### 🚀 **Utilisation**  

1. **Cloner le dépôt GitHub** :  
   ```bash
   git clone https://github.com/Negr170/password_tool.git
   cd nom-du-repo
   ```

2. **Exécuter le script** :  
   ```bash
   python3 password_tool.py
   ```

3. **Options disponibles** :  
   - **Générer un mot de passe** : Créez un mot de passe en précisant la longueur et l'inclusion de caractères spéciaux.  
   - **Vérifier un mot de passe** : Analysez la robustesse et vérifiez si le mot de passe est compromis.  

---

### 💡 **Exemple de fonctionnement**  

**Génération d'un mot de passe** :  
```bash
Bienvenue dans l'outil de mot de passe.
1: Générer un mot de passe
2: Vérifier un mot de passe
Choisissez une option: 1
Longueur du mot de passe : 16
Inclure des caractères spéciaux ? (y/n) y
Mot de passe généré : w3r@!dP&9*L#xTbU
```

**Vérification d'un mot de passe** :  
```bash
Bienvenue dans l'outil de mot de passe.
1: Générer un mot de passe
2: Vérifier un mot de passe
Choisissez une option: 2
Entrez le mot de passe à vérifier : w3r@!dP&9*L#xTbU
Force : Forte
✅ Ce mot de passe n'est pas compromis.
```

---

### ⚠️ **Limitations connues**  
- Le script affiche un avertissement lié à la version de **LibreSSL** sur macOS, mais cela n'affecte pas son fonctionnement.  
- Si vous utilisez une ancienne version de `pip`, il est recommandé de la mettre à jour :  
  ```bash
  python3 -m pip install --upgrade pip
  ```

---

### 🛡️ **Avertissement**  

Ce projet est conçu à des fins éducatives et personnelles. Bien que l'outil aide à créer et vérifier des mots de passe sécurisés, il est toujours recommandé d'utiliser un gestionnaire de mots de passe professionnel pour un usage critique.  

---
