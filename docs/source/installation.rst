Installation
============

Prérequis
---------

- Python 3.8 ou supérieur.
- Docker Desktop.
- Git.

Étapes d'installation
---------------------

1. Clonez le dépôt :
   .. code-block:: bash

      git clone https://github.com/AymericSandoz/Python-OC-Lettings-FR.git

2. Naviguez dans le répertoire du projet :
   .. code-block:: bash

      cd Python-OC-Lettings-FR

3. Créez un environnement virtuel et installez les dépendances :
   .. code-block:: bash

      python -m venv venv
      pip install -r requirements.txt

Installation avec Docker Hub
---------------------

1. Téléchargez l'image Docker présente sur Docker Hub :
   .. code-block:: bash

      docker pull sandozaymeric/oc-lettings-app-test:latest