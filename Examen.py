
# exercice3
Reponse aux question suivantes:
1=faux
2=vrai
3=vrai
4=vrai
5=faux

#NOTION DE PROGRAMMATION ORIENTE Objets
    # Exo2
import random

class Personne:
    def __init__(self, nom, prob_infection=0.0):
        self.nom = nom
        self.prob_infection = prob_infection
        self.infecte = False
    
    def s_infecter(self):
        if not self.infecte and random.random() < self.prob_infection:
            self.infecte = True

class Population:
    def __init__(self, taille, prob_infection=0.5):
        self.individus = [Personne(f'Individu_{i}', prob_infection) for i in range(taille)]
    
    def initialiser_infection(self, nb_infectes):
        infectes = random.sample(self.individus, nb_infectes)
        for personne in infectes:
            personne.infecte = True
    
    def propager_infection(self):
        for personne in self.individus:
            personne.s_infecter()
    
    def afficher_etat(self, jour):
        nb_infectes = sum(1 for p in self.individus if p.infecte)
        print(f"Jour {jour} : {nb_infectes}/{len(self.individus)} infectés")
    
    def simuler(self, jours):
        for jour in range(1, jours + 1):
            self.propager_infection()
            self.afficher_etat(jour)

# Simulation
taille_population = 1000
nb_infectes_initiaux = 10
jours_simulation = 30

population = Population(taille_population)
population.initialiser_infection(nb_infectes_initiaux)
population.simuler(jours_simulation)


        #EXo 1
import csv
import matplotlib.pyplot as plt

# Tâche 1 : Lecture du fichier CSV
def lire_csv(nom_fichier):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires.
    """
    donnees = []
    with open(nom_fichier, mode='r') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        for ligne in lecteur:
            # Conversion des nombres en entiers
            ligne['Cas'] = int(ligne['Cas'])
            ligne['Dèces'] = int(ligne['Dèces'])
            donnees.append(ligne)
    return donnees

# Tâche 2 : Calculs statistiques
def calculer_statistiques(donnees):
    ""
    Calcule les totaux et taux de mortalité par préfecture.
    Retourne un dictionnaire {préfecture: {cas, deces, taux}}.
    ""
    stats = {}
    for entree in donnees:
        pref = entree['Préfecture']
        if pref not in stats:
            stats[pref] = {'cas': 0, 'deces': 0}
        stats[pref]['cas'] += entree['Cas']
        stats[pref]['deces'] += entree['Dèces']
    
    # Calcul du taux de mortalités
    for pref in stats:
        cas = stats[pref]['cas']
        deces = stats[pref]['deces']
        stats[pref]['taux'] = deces / cas if cas > 0 else 0.0
    return stats

# Tâche 3 : Visualisations
def visualiser_donnees(stats):
    
    Génère deux diagrammes à barres : cas totaux et taux de mortalité.
    "
    prefectures = list(stats.keys())
    cas = [stats[pref]['cas'] for pref in prefectures]
    taux = [stats[pref]['taux'] for pref in prefectures]

    # Diagramme des cas
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, cas, color='skyblue')
    plt.title('Nombre total de cas par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Cas')

    # Diagramme du taux de mortalité
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, taux, color='salmon')
    plt.title('Taux de mortalité par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux (Décès/Cas)')
    plt.ylim(0, 1) 
     # Limite pour une meilleure lisibilité

    plt.show()

# Exécution principale
if __name__ == "__main__":
    donnees = lire_csv('ebola_guinea.csv')
    stats = calculer_statistiques(donnees)
    visualiser_donnees(stats)
