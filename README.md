### INFORMATION POUR EXECUTER LE FICHIER 
Il est necessaire d'executer les lignes de commandes ( si ce n'est pas déjà fait ou si les packages ne sont pas déjà installés ). 
io est normalement déjà contenu dans l'installation python de base.
```
 pip install biopython
 pip install matplotlib
 pip install streamlit
```

### EXECUTION DE L'APPLICATION 
Pour pouvoir faire tourner l'interface utilisateur, ouvrez votre terminal en ayant ouvert ce dossier et tapez :
``` 
 python -m streamlit main.py
```

### QUE FAIT CETTE APPLICATION 
Cette application a pour but de permettre a un utilisateur prédire le profil d'hydrophobicité de sa protéine dans 3 échelles différentes : Kyte - Dootlittle, Cornette et Hopp-Woods
Les tailles d'échelles recommandés sont celle des valeurs par défaut. Chaque échelle a son but :
* Kyte - Dootlittle : Prédire les domaines transmembranaires
* Cornette : Trouver les hélices alpha et donc les zones amphiphiles
* Hopp-Woods : Prédire les régions épitopes des antigèns.