Procédures de déploiement
=========================

Pipeline CI/CD
--------------

1. Configurez les secrets GitHub :
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`

2. Déployez automatiquement avec GitHub Actions :
   - Push sur la branche `main` pour déclencher le workflow.
   - Accédez à l'application sur Render après déploiement.

Déploiement local
-----------------

Pour déployer localement :
.. code-block:: bash

   docker run -p 8000:8000 python-oc-lettings
