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
    df = pd.read_excel('PIB_annuel_et_PPA_par_pays_utile.xlsx')

    # Sélectionner les colonnes à afficher
    columns_to_display = ['Pays', 'PIB par habitant ($)']
    data = df[columns_to_display]

    # Passer les données à la page HTML en utilisant Jinja2
    return render_template('page.html', data=data)

# Executer l'application
if __name__ == '__main__':
    app.run()