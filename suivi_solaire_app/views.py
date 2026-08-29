# monitoring/views.py
from datetime import datetime as dt

from django.shortcuts import render
from django.http import JsonResponse
from .services import lire_puissances_installees, lire_puissances_instantanees, lire_energie_estimee, \
    lire_energies_instantanees


def dashboard(request):
    """Écran principal avec synthèse des énergies et puissances."""
    puissances_installees = lire_puissances_installees()
    puissances_instantanees = lire_puissances_instantanees()
    energies_instantanees = lire_energies_instantanees()
    energie_estimee = lire_energie_estimee()

    # Calculer la puissance max installée (somme des max_power)
    puissance_totale_installee = sum(puissances_installees.values())

    # Calculer la puissance consommée totale (compteur + équipements)
    puissance_totale_utilisee = sum(puissances_instantanees.values())

    energie_utilisee = energies_instantanees['produite'] - energies_instantanees['injectee']
    energie_totale_estimee = sum(energie_estimee.values())


    context = {
        # Données de l'onduleur
        "puissance_onduleur": puissances_instantanees["onduleur"],
        # Données du compteur
        "puissance_compteur": puissances_instantanees["compteur"],
        # Puissances max
        "puissances_installees": puissances_installees,
        # Prévision d'énergie
        "energie_estimee": energie_estimee,
        # Puissance max installée
        "puissance_totale_installee": puissance_totale_installee,
        # Puissance consommée totale
        "puissance_totale_utilisee": puissance_totale_utilisee,
        # Datation des données
        "datation": dt.fromtimestamp(puissances_instantanees["datation"]),
        # Énergies de la journée
        "energie_utilisee": energie_utilisee,
        "energie_totale_estimee": energie_totale_estimee,
        "energie_produite": energies_instantanees["produite"],
        "energie_prelevee": energies_instantanees["prelevee"],
        "energie_injectee": energies_instantanees["injectee"],
    }
    return render(request, 'dashboard.html', context)

def get_live_data_json(request):
    """Endpoint pour AJAX (rafraîchissement automatique)."""
    puissances_instantanees = lire_puissances_instantanees()
    energies_instantanees = lire_energies_instantanees()
    energie_estimee = lire_energie_estimee()
    puissance_totale_utilisee = sum(puissances_instantanees.values())

    energie_totale_utilisee = sum(energies_instantanees.values())

    return JsonResponse({
        "onduleur": puissances_instantanees["onduleur"],
        "compteur": puissances_instantanees["compteur"],
        "devices": puissances_instantanees["devices"],
        "energie_estimee": energie_estimee,
        "puissance_totale_utilisee": puissance_totale_utilisee,
        "energie_produite": energies_instantanees["onduleur"],
        "energie_prelevee": energies_instantanees["prelevee"],
        "energie_injectee": energies_instantanees["injectee"],
    })