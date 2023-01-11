# Plane_ticket_price

## Objectifs
Les objectifs de ce projet sont :
1. Proposer une interface conseillant les meilleurs prix pour un voyage, en précisant la position du VPN
2. Démontrer qu'il existe, ou non, une relation entre le PIB des pays où le VPN a été posé et les prix des vols proposés


## Etapes du projet
Pour ce faire, nous avons :
- Scrapé les données PIB des pays concernés (cf. PIB.ipynb)
- Scrapé les vols (8 voyages préfédini, les 15 premiers vols) en variant le VPN (cf. vols.ipynb)
- Puisque c'est un travail en duo, nous avons fusionné les datasets créés (cf. concatenation.ipynb)
- Fusionné le dataset des vols avec le dataset du PIB
- Analysé et visualisé les données (cf. analyse_de_donnees.ipynb)
- Créé une interface (python) pour la proposer les vols les plus malins (cf. launch_App.py)


## VPN
Pays où on pose le VPN (les 5 plus pauvres et plus riches) :
1. Cambodge
2. Bangladesh
3. Moldavie
4. Inde
5. Philippines
6. Luxembourg
7. Macao
8. Monaco
9. Qatar
10. Liechtenstein


## Voyages
Nous avons choisis les voyages suivants:
1.	Aéroport de Paris Charles de Gaulle, Paris, France – Aéroport international de Narita, Tokyo, Japon (France, Japon)
2.	Aéroport international Mohammed-V de Casablanca, Casablanca, Maroc – Aéroport international de Gatwick, Londres, Angleterre, Royaume-Uni (Maroc, Angleterre)
3.	Aéroport Léonard de Vinci de Rome-Fiumicino, Rome, Italie - Aéroport international OR Tambo, Johannesbourg, Afrique du sud (Italie, Afrique du sud)
4.	Aéroport international de Riga, Riga, Lettonie - Vienna Schwechat International Airport, Vienne, Autriche (Lettonie – Autriche)
5.	Aéroport international du Caire, Le Caire, Egypte - Chhatrapati Shivaji International Airport, Mumbai, Maharashtra, Inde (Egypte – Inde)
6.	Aéroport Adolfo-Suárez de Madrid-Barajas, Madrid, Madrid, Espagne – Aéroport international Reina Sofía de Tenerife Sud, Ténérife, Îles Canaries, Espagne (Espagne - îles Canarie - Espagne)
7.	Aéroport international John F. Kennedy, New York, NY, Etats-Unis – Aéroport international de Los Angeles, Los Angeles, CA, Etats-Unis (US - US)
8.	Aéroport de Paris Charles de Gaulle, Paris, France – Aéroport Kingsford Smith de Sydney, Sydney, Nouvelles Galles du Sud, Australie (France – Australie)