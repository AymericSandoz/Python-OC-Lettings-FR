Déploiement
===========

Cette section détaille la configuration et les étapes nécessaires pour le déploiement automatisé de l'application via GitHub Actions. Le pipeline CI/CD est divisé en trois principaux workflows : les tests, la conteneurisation et le déploiement.

Pipeline CI/CD
--------------

Le pipeline est défini dans le fichier ``config.yml`` et est déclenché par des **push** ou **pull requests** sur la branche ``master``. Il se compose des jobs suivants :

1. **Test** : Vérifie que le code passe les tests unitaires et respecte les normes de qualité.
2. **Build and Push** : Construit une image Docker de l'application et la pousse sur Docker Hub.
3. **Deploy** : Déploie l'application sur la plateforme Render.

Job : Test
##########

Ce job garantit que le code est stable et respecte les normes de qualité avant tout déploiement. Voici les étapes principales :

- **Installation des dépendances** : Utilisation de ``pip`` pour installer les modules nécessaires spécifiés dans ``requirements.txt``.
- **Linting** : Analyse du code avec ``flake8`` pour identifier des problèmes de style ou syntaxe.
- **Tests unitaires** : Exécution des tests avec ``pytest`` et vérification de la couverture minimale requise (80 %).

Job : Build and Push
####################

Une fois les tests réussis, une image Docker de l'application est construite et poussée sur Docker Hub. Les étapes incluent :

- **Connexion à Docker Hub** : Utilisation des secrets GitHub pour les identifiants Docker Hub.
- **Construction et balisage** : Création d'une image Docker avec un tag basé sur le commit SHA actuel.
- **Push de l'image** : Envoi de l'image sur le registre Docker.

Job : Deploy
############

Le job de déploiement utilise Render comme plateforme d'hébergement. Voici les étapes clés :

- **Préparation** : Vérifie que l'image Docker est prête à être déployée.
- **Déploiement via Render API** : Utilisation de l'action ``render-deploy`` pour déclencher un déploiement.

Secrets GitHub
--------------

Pour sécuriser les identifiants et configurations sensibles, les secrets suivants doivent être configurés dans le dépôt GitHub :

- ``DOCKERHUB_USERNAME`` : Nom d'utilisateur Docker Hub.
- ``DOCKERHUB_TOKEN`` : Jeton d'accès Docker Hub.
- ``RENDER_SERVICE_ID`` : Identifiant du service Render.
- ``RENDER_API_KEY`` : Clé API Render.

URL de l'application
--------------------

Une fois le déploiement terminé, l'application sera accessible via l'URL suivante :

``https://python-oc-lettings-fr-dqfq.onrender.com/``

Conseils pour le déploiement
----------------------------

- **Suivi des logs** : Vérifiez les logs sur GitHub Actions pour identifier toute erreur dans le pipeline.
- **Tests locaux** : Exécutez les tests et construisez l'image Docker en local pour résoudre les problèmes avant le push.
- **Mises à jour de configuration** : Si des modifications sont nécessaires dans le pipeline, mettez à jour le fichier ``config.yml``.

