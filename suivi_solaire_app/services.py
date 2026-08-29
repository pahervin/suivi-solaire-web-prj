# monitoring/services.py
import requests

from suivi_solaire_web.settings import API_BASE_URL


def lire_puissances_installees():
    """Récupère les puissances max depuis /puissances-max."""
    try:
        response = requests.get(f"{API_BASE_URL}/puissance/installee/toutes", timeout=5)
        if response.status_code == 200:
            # Convertir la liste de couples en dictionnaire {nom: puissance}
            return response.json()
    except Exception as e:
        print(f"Erreur /puissances installées: {e}")
    return {'datation':0, 'onduleur':0, 'compteur':0}

def lire_puissances_instantanees():
    """Récupère les valeurs instantanées depuis /valeurs-instantanees."""
    try:
        response = requests.get(f"{API_BASE_URL}/puissance/instantanee/toutes", timeout=5)
        if response.status_code == 200:
            # Convertir la liste de couples en dictionnaire {nom: puissance}
            return response.json()
    except Exception as e:
        print(f"Erreur /puissances instantanees: {e}")
    return {'datation':0, 'onduleur':0, 'compteur':0}

def lire_energies_instantanees():
    """Récupère les valeurs instantanées depuis /valeurs-instantanees."""
    try:
        response = requests.get(f"{API_BASE_URL}/energie/instantanee/toutes", timeout=5)
        if response.status_code == 200:
            # Convertir la liste de couples en dictionnaire {nom: puissance}
            return response.json()
    except Exception as e:
        print(f"Erreur /energies instantanees: {e}")
    return {'datation':0, 'produite':100, 'prelevee':20, 'injectee':30}

def lire_energie_estimee():
    """Récupère la prévision d'énergie (à adapter si endpoint différent)."""
    try:
        response = requests.get(f"{API_BASE_URL}/energie/estimee/toutes", timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Erreur /forecast: {e}")
    return {}