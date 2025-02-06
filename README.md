## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Cette section explique le processus de déploiement de l'application via GitHub Actions, qui est automatisé pour garantir que l'application soit déployée correctement à chaque mise à jour. Le processus de déploiement repose sur un pipeline CI/CD en trois étapes : **tests**, **construction et push de l'image Docker**, et **déploiement sur Render**.

### Fonctionnement du déploiement

Le pipeline CI/CD est configuré dans le fichier `config.yml` et est déclenché par un **push** ou une **pull request** sur la branche `master`. L'objectif est d'assurer que le code est testé, validé, puis déployé sur la plateforme Render de manière automatique et fiable.

Le pipeline se compose de trois principaux workflows :

1. **Tests** : Cette étape vérifie la stabilité du code en exécutant des tests unitaires et en s'assurant que le code respecte les bonnes pratiques (linting).
2. **Build and Push** : Si les tests passent, une image Docker de l'application est construite et envoyée sur Docker Hub.
3. **Déploiement** : Une fois l'image Docker disponible, le job de déploiement s'assure que l'application est déployée sur Render.

### Configuration requise

Pour que le déploiement fonctionne correctement, plusieurs configurations et secrets sont nécessaires. Voici ce qui doit être en place :

- **GitHub Actions** : Le dépôt GitHub doit être configuré pour utiliser GitHub Actions avec un fichier `config.yml` adéquat.
- **Secrets GitHub** : Les secrets suivants doivent être configurés dans les paramètres du dépôt GitHub pour sécuriser les informations sensibles :
  - `DOCKERHUB_USERNAME` : Nom d'utilisateur Docker Hub.
  - `DOCKERHUB_TOKEN` : Jeton d'accès Docker Hub pour se connecter et pousser des images.
  - `RENDER_SERVICE_ID` : Identifiant du service Render où l'application sera déployée.
  - `RENDER_API_KEY` : Clé API Render pour interagir avec l'API Render et déployer l'application.

### Étapes du déploiement

Voici les étapes détaillées pour effectuer le déploiement :

1. **Configurer les secrets GitHub.**

   - Allez dans les paramètres de votre dépôt GitHub, puis dans **Secrets** pour ajouter les secrets nécessaires :
     - `DOCKERHUB_USERNAME`
     - `DOCKERHUB_TOKEN`
     - `RENDER_SERVICE_ID`
     - `RENDER_API_KEY`

2. **Lancer le pipeline CI/CD.**

   - Lorsque vous poussez du code sur la branche `master` ou que vous soumettez une pull request, le pipeline GitHub Actions est automatiquement déclenché. Ce pipeline effectuera les trois étapes :
     1. **Tests** : Exécution des tests pour vérifier la qualité du code.
     2. **Build and Push** : Construction de l'image Docker et envoi vers Docker Hub.
     3. **Deploy** : Déploiement de l'application sur Render.

3. **Vérification de l'URL de l'application déployée.**
   - Une fois le déploiement terminé, l'application sera accessible à l'URL suivante :
     ```
     https://python-oc-lettings-fr-dqfq.onrender.com/
     ```

### Conseils pour le déploiement

- **Suivi des logs** : Si le pipeline échoue, vérifiez les logs sur GitHub Actions pour comprendre ce qui a échoué et corriger les problèmes.
- **Tests locaux** : Avant de pousser des modifications, il est recommandé d'exécuter les tests et de construire l'image Docker en local pour éviter les erreurs de déploiement.
- **Mises à jour de configuration** : Si des modifications sont nécessaires dans le pipeline (par exemple, ajout de nouvelles étapes ou mise à jour des dépendances), n'oubliez pas de modifier le fichier `config.yml`.

## Sentry : Journalisation des logs

Afin d'optimiser l'application et d'assurer un suivi précis des erreurs, nous avons choisi d'intégrer **Sentry**, un outil de surveillance des erreurs et des performances. Sentry nous permet de détecter les erreurs en temps réel et d'améliorer la stabilité de l'application en facilitant le diagnostic des problèmes.

Pour que sentry fonctionne, assurez vous de créer un fichier .env à la racine du projet contenant le DSN que vous pourrez retrouver sur votre interface sentry dans settings/client keys(DSN)

```
SENTRY_DSN=https://PUBLIC_KEY.ingest.de.sentry.io/PROJECT_ID

```

Vous pourrez ainsi visualiser les logs de l'application sur l'interface sentry.

Il est aussi possible de configurer la variable ENVIRONMENT dans votre fichier .env et sur votre plateforme de déploiement pour configurer l'environment sur lequel les logs sentry sont enregistrés.
