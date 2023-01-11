# Plane_ticket_price

Les objectifs de ce projet sont :
1. Proposer une interface conseillant les meilleurs prix pour une voyage, en précisant la position du VPN
2. Démontrer qu'il existe, ou non, une relation entre le PIB des pays où le VPN a été posé et les prix des vols proposés

Pour ce faire, nous avons :
- Scrapé les données PIB des pays (cf. PIB.ipynb)
- Scrapé les vols (9 voyages préfédini, les 15 premiers vols) en variant le VPN (cf. vols.ipynb)
- Puisque c'est un travail en duo, nous avons fusionné les datasets créés (cf. concatenation.ipynb)
- Fusionné le dataset des vols avec le dataset du PIB
- Analysé et visualisé les données (cf. analyse_de_donnees.ipynb)
- Créé une interface (python) pour la proposer les vols les plus malins (cf. launch_App.py)