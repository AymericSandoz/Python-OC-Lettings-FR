Guide de démarrage rapide
=========================

Lancez le projet localement avec Docker :

1. Assurez-vous que Docker Desktop est actif.
2. Construisez l'image Docker :
   .. code-block:: bash

      docker build -t python-oc-lettings .

3. Lancez un conteneur :
   .. code-block:: bash

      docker run -p 8000:8000 python-oc-lettings

Accédez à l'application sur [http://localhost:8000](http://localhost:8000).
