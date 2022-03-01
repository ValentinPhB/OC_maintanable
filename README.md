# OC_Maintanable
# Complétion du fichier README initial

## Table des matières 

1. [Résumé](#1-résumé)
2. [Développement local](#2-développement-local)
3. [Fonctionnement du Pipeline](#3-fonctionnement-du-pipeline)
4. [Approche du monitoring avec Sentry](#4-approche-du-monitoring-avec-sentry)
5. [Auteurs](#5-auteurs)

## 1. Résumé

Site web d'Orange County Lettings.
Réduction de la dette technique, architecture modulaire, création d'un pipeline avec circle Ci (compilation, tests, contenerisation et déploiement sur heroku) et monitoring de l'application avec Sentry.

## 2. Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le dépôt

- `cd /path/to/put/project/in`
- `git clone https://github.com/ValentinPhB/OC_maintanable.git`

#### Créer l'environnement virtuel

- `cd /path/to/OC_maintanable`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/OC_maintanable`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/OC_maintanable`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/OC_maintanable`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/OC_maintanable`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info($NOM_DE_TABLE);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  $NOM_DE_TABLE where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## 3. Fonctionnement du Pipeline

jobs:
- build : construit un environnement pour exécuter l'application.
- tests : exécute flake8 et pytest.
- containerization : pousse une image vers DokerHub.
- heroku/deploy-via-git : déploie le site avec Heroku.

Lors de chaque modification du projet poussée sur GitHub et sur toutes les branches qui le compose, le pipeline sera déclanché pour les jobs "build" et "tests".
Seul les modifications du projet poussée sur la branche principale (main) délancheront égalemenent les jobs "containerization" et "heroku/deploy-via-git".

### Prérequis
- Avoir un compte [GitHub](https://github.com/).
- Avoir un compte Compte [DokerHub](https://hub.docker.com/).
- Se connecter à [Circle Ci](https://circleci.com/signup?return-to=https%3A%2F%2Fapp.circleci.com%2Fprojects%2F) avec son compte GitHub.
- Avoir une compte [Heroku](https://signup.heroku.com/login).
- Installer [Docker](https://docs.docker.com/get-docker/) sur votre poste.

### Connexions :

- Clonez le dépôt actuel dans le dossier de votre choix sur votre poste puis poussez le dans un de vos dépôt personnel créé sur votre Github et nommé selon votre choix en changeant url Origin :
```
git remote set-url origin http://github.com/YOU/YOUR_REPO
```

- Dans DockerHub créez un dépôt du nom de votre choix.

- Dans Circle CI (connecté à votre GitHub) allez dans le menu PROJET et cliquez sur "Set up project" à coté du nom de votre dépôt GitHub (réplique du dépôt courant). Le premier choix est déjà séléctionné par défault, ne le modifiez pas et cliquez encore sur "Set up project".

- Dans heroku, une fois connecté, créez une nouvelle app en cliquant sur "new" puis "create new app" et nommez la selon votre choix.

- Installez [heroku](https://devcenter.heroku.com/articles/heroku-cli) sur votre poste et effectuez les commandes suivantes pour récupérer votre token heroku :

- `cd /path/to/YOURREPOSITORY`
- `heroku login` # Suivez les instructions de votre navigateur pour vous connecter.
- `heroku auth:token` # un token s'affichera.

- Copiez le et gardez le.

### Créations du context dans Circle CI (variables d'environnement) :

- Dans Circle CI allez dans le menu ORGANIZATION SETTINGS et cliquez sur "create context" et nommez le *OC-P13*.
- Ajoutez-y, une à une, les variables suivantes :
  -  DOCKERHUB_USERNAME      (value = votre nom d'utilisateur DockerHub)
  -  DOCKERHUB_PASSWORD      (value = votre mot de passe DockerHub)
  -  HEROKU_API_KEY          (value = le token heroku copié)
  -  HEROKU_APP_NAME         (value = le nom de votre application Heroku)
  -  REPO_NAME               (value = le nom de votre depôt sur DockerHub)

- Ce context est indispensable au fonctionnement du pipeline.
- À chaque fois que vous pousserez votre les modifications de votre dépôt local sur le votre dépôt GitHub le pipeline s'executera. Si les ciritères de tests sont remplis et que la branche poussée est la branche principale (main) alors la contenerisation et le déploiement s'effecturont.

### Accès au site déployer 

- Si toutes les étapes du pipeline ont été parcourus avec succès (affichage dans circle CI) vous pouvez naviguer sur votre application déployée à l'adresse suivante : https://NOM_DE_VOTRE_APP_HEROKU.herokuapp.com/

### Récupération des image de dockerHub en local

- Pour récupérer les images poussées dans votre DockerHub et les lancer localement il suffit d'aller sur votre compte dockerHub dans le dépot correspondant.
Ensuite, récupérez le nom de l'image et, sur votre machine, exécutez les commandes suivantes :

- `docker run -p 8000:8000 $NOMIMAGE`

- Ensuite il vous suffira d'ouvrir, dans votre navigateur, le lien proposé à la suite de l'éxécution de cette commande pour parcourir l'application.

## 4. Approche du monitoring avec Sentry

### Fonctionnement 

- Créez vous une compte [Sentry](https://sentry.io/signup/)
- Créez un projet, sélectionnez django, sélectionnez "Alert me on every issue", enfin cliquez sur "Create Project".
-  Une fenètre dans votre navigateur s'ouvre la seule information à récupérer est la chaine string suivant dsn= car votre projet est déja configuré à l'exeption de cette donnée qui permettra la récupération de ces "ISSUES".
-  Ainsi copie-z cette chaine de caractère et collez la dans votre projet (branche principale), à sa place, dans le fichier settings.py de votre projet.
-  Dans votre fichier settings.py la valeur 
```python
dsn=''
```
- Ne doit plus être vide.

- Poussez vos modifications de la branche principale sur votre dépôt distant pour actionner le pipeline.


### Utilisation 

- Une fois la configuration effectuée, et le pipeline passé avec succès, Sentry est utilisable.
- Lorsque l'application est déployée et qu'un requète sur l'url "https://NOM_DE_VOTRE_APP_HEROKU.herokuapp.com/sentry-debug/" est formulée, la fonction nommée "trigger_error" (définie aupréalablement dans le ficher url.py du projet) est exécutée, rapportant une ZeroDivisionError "issue" à sentry.
- Pour voir le rapport d'"Issue" il vous suffit ensuite de vous connecter sur [Sentry](https://sentry.io/) et d'aller dans le menu "ISSUES".

## 5. Auteurs

- Openclassrooms
- Valentin Pheulpin
