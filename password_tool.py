import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')

import random
import string
import requests
import hashlib
from colorama import Fore, Style, init

# Initialisation de colorama pour bien fonctionner sur tous les systèmes
init()

def generate_password(length=12, use_special=True):
    """Génère un mot de passe sécurisé."""
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    """Vérifie la force du mot de passe."""
    strength = {
        'length': len(password) >= 12,
        'lowercase': any(c.islower() for c in password),
        'uppercase': any(c.isupper() for c in password),
        'digits': any(c.isdigit() for c in password),
        'special': any(c in string.punctuation for c in password),
    }
    score = sum(strength.values())
    
    if score < 3:
        return "Faible"
    elif score < 5:
        return "Moyenne"
    else:
        return "Forte"

def check_if_compromised(password):
    """Vérifie si le mot de passe est dans une base de données de mots de passe compromis."""
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError("Erreur avec l'API PwnedPasswords.")
    
    hashes = response.text.splitlines()
    for h in hashes:
        hash_suffix, count = h.split(":")
        if suffix == hash_suffix:
            return True
    return False

if __name__ == "__main__":
    print(Fore.GREEN + "Bienvenue dans l'outil de mot de passe." + Style.RESET_ALL)
    choice = input(Fore.GREEN + "1: Générer un mot de passe\n2: Vérifier un mot de passe\nChoisissez une option: " + Style.RESET_ALL)
    
    if choice == "1":
        length = int(input(Fore.GREEN + "Longueur du mot de passe : " + Style.RESET_ALL))
        use_special = input(Fore.GREEN + "Inclure des caractères spéciaux ? (y/n) " + Style.RESET_ALL).lower() == "y"
        print(Fore.GREEN + f"Mot de passe généré : {generate_password(length, use_special)}" + Style.RESET_ALL)
    elif choice == "2":
        password = input(Fore.GREEN + "Entrez le mot de passe à vérifier : " + Style.RESET_ALL)
        print(Fore.GREEN + f"Force : {check_password_strength(password)}" + Style.RESET_ALL)
        try:
            if check_if_compromised(password):
                print(Fore.RED + "⚠️ Ce mot de passe est compromis !" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "✅ Ce mot de passe n'est pas compromis." + Style.RESET_ALL)
        except RuntimeError as e:
            print(Fore.RED + f"Erreur : {e}" + Style.RESET_ALL)
