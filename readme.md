# **LITReview v1.0.0**

Application Web permettant de demander ou publier des critiques de livres ou d’articles.

## **Initialisation de l'environnement**

### 1. Cloner la branche Main vers un répertoire local

- Créer un dossier sur votre ordinateur pour y disposer les fichiers présents sous GitHub

- Ouvrir un terminal (Ex: Windows PowerShell) et se positionner dans le dossier en question avec la commande cd, par exemple:

```
cd d:
cd -- "D:\mon_dossier"
```

### 2. Créer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- Créer l'environnement:


`python -m venv tournament`

- Activer l'environnement (L'environnement est activé une fois son nom affiché dans le terminal) : 

    - Windows:

    `tournament/Scripts/Activate.ps1` 

    - Inux et MacOS:  

    `source tournament/bin/activate`

- Installer les librairies : 

`pip install -r requirements.txt`


## **Lancement du projet**

### 1. Lancer le serveur Django sous l'environnement virtuel, dans le terminal:

Se positionner dans l'application LITReview:

`cd litreview`

Lancer le serveur :

`py manage.py runserver`

### 2. Accéder à l'application:

Dans votre navigateur préféré, allez à l'adresse suivante :

http://127.0.0.1:8000/


## ** Fonctionnement de l'application **

### 1. Connexion

Pour vous connecter à l'application vous avez besoin de créer un compte ou bien d'utiliser un compte déjà enregistrer.

Compte disponible pour l'exemple :
```
Identifiant : openclassrooms

Mot de passe : litreview123
```

Sinon en cliquant sur `S'inscrire` vous pourrez créer un compte afin de vous identifier.
Lorsque vous serez connecté, vous serez redirigé vers votre page d'accueil.

### 2. Environnement utilisateur

### Flux

Cet espace est dédié aux articles et critiques dont vous êtes l'auteur ou bien des utilisateurs auxquels vous vous êtes abonné.
Les publications sont affichés par ordre chronologique, du plus récent au plus ancien.

A partir de cette catégorie vous pourrez :
  - Créer un ticket : En cliquant sur le bouton en dessous de la barre de navigation `Demander une critique`
  - Créer une critique sans répondre à un ticket : En cliquant sur le bouton en dessous de la barre de navigation `Créer une critique`
  - Créer une critique en réponse à un ticket : en cliquant sur le bouton `Créer une critique` à l'intérieur du ticket affiché
  
Un ticket ne peut posséder qu'une seule critique, par conséquent le bouton `Créer une critique` ne sera plus disponible sur le ticket correspondant.

Le flux affiche un maximum de 6 publications par page, vous pouvez changer de page à partir de la pagination en bas de page.

 ### Posts
 
 Cet espace répertorie l'ensemble de vos publications où il sera possible de les modifier ou supprimer.
 
 ### Abonnement
 
 Vous avez la possibilité de vous abonner à d'autres personnes afin de suivre leurs publications.
 
 Pour se faire il suffit de saisir le nom de l'utilisateur et de cliquer sur envoyer.
 
 Pour vous désabonner d'un utilisateur il suffit de cliquer sur le bouton `Désabonner` correspondant.
 
 Voici une liste d'utilisateurs déjà inscrits sur l'application:
  - sarahj
  - jean_5679
  - severine123
  - openclassrooms
  
### Déconnexion

Pour changer de compte, il suffit de se déconnecter en cliquant sur le bouton `Se déconnecter` de la barre de navigation.
Vous serez ensuite redirigé vers la page pour vous inscrire ou vous connecter.


  



