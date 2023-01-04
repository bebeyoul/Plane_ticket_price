from flask import Flask
import pandas as pd
from flask import Flask, render_template
import openpyxl

# instance de l'application Flask
app = Flask(__name__)
@app.route('/')

# def home():
#     prout = 'Super interface'
#     return render_template('page.html', title=prout)


def home():
    # Lire le dataset avec Pandas
    df = pd.read_csv('C:/Users/julie/OneDrive/Documents/GitHub/Plane_ticket_price/data/final_dataset.csv')

    # Sélectionner les colonnes à afficher
    columns_to_display = ["VPN", 'Date', 'Depart', 'Arrivé', 'Prix', 'Temps de vol','Heure de départ', "Heure d'arrivé", "Nombre d'escales", 'Compagnies', 'PIB par habitant ($)']
    data = df[columns_to_display]

    # Passer les données à la page HTML en utilisant Jinja2
    return render_template('page.html', data=data)

# Executer l'application
if __name__ == '__main__':
    app.run()