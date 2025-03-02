===================================
API
===================================

1. **Application Lettings**
===================================

Cette application permet d'afficher la liste des logements et les détails d'un logement spécifique.

**Route principale :**

- **GET `https://python-oc-lettings-fr-dqfq.onrender.com/lettings/`**
  Affiche la liste de tous les logements. La vue associée récupère tous les objets de type `Letting` et les affiche sur la page d'accueil de la section des logements.

  **Vues associées :**
  - `index`: Affiche une liste des logements disponibles.

**Route des détails d'un logement :**

- **GET `https://python-oc-lettings-fr-dqfq.onrender.com/lettings/<int:letting_id>/`**  
  Affiche les détails d'un logement spécifique. Le `letting_id` est l'identifiant unique du logement dans la base de données. Cette route permet de récupérer un logement particulier et d'afficher ses informations détaillées sur une page dédiée.

  **Vues associées :**
  - `letting`: Affiche les détails du logement spécifié.

2. **Application Profiles**
===================================

Cette application permet d'afficher le profil des utilisateurs de l'application.

**Route principale :**

- **GET `https://python-oc-lettings-fr-dqfq.onrender.com/profiles/`**  
  Affiche la liste des profils des utilisateurs. Cette vue récupère les profils disponibles dans le système et les affiche sur une page dédiée.

  **Vues associées :**
  - `index`: Affiche une liste des profils des utilisateurs.

**Route du profil d'un utilisateur :**

- **GET `https://python-oc-lettings-fr-dqfq.onrender.com/profiles/<str:username>/`**  
  Affiche le profil d'un utilisateur spécifique basé sur son nom d'utilisateur. Cette route permet de visualiser les informations personnelles d'un utilisateur.

  **Vues associées :**
  - `profile`: Affiche les informations détaillées du profil de l'utilisateur spécifié.
