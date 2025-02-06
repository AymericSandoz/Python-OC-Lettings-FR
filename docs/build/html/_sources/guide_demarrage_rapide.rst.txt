Guide de démarrage rapide
=========================

Lancez le projet avec manage.py
-------------------------------

1. Activez votre environnement virtuel :
   
.. code-block:: console

      venv\Scripts\activate

2. Lancez le serveur de développement :
   
.. code-block:: console

      python manage.py runserver

Lancez le projet localement avec Docker :
-----------------------------------------


1. Assurez-vous que Docker Desktop est actif.
2. Télécharger l'image Docker (sauf si vous avez déjà téléchargé l'image. Sha1 correspond à la version du commit git) :

.. code-block:: console

      docker pull sandozaymeric/oc-lettings-app-test:{sha1}

3. Lancez un conteneur (adaptez le nom de l'image si vous avez construit l'image avec un autre nom) :

.. code-block:: console

      docker run -p 8000:8000 python-oc-lettings

Accédez à l'application sur `http://localhost:8000 <http://localhost:8000>`_.


Il est aussi possible de lancer le projet avec le débugger de Visual Studio Code.