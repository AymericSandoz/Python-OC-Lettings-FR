===================================
Structure de la Base de Données
===================================

Ce projet repose sur trois modèles principaux : **Profile**, **Address**, et **Letting**. Chaque modèle représente une entité spécifique et inclut des relations et attributs adaptés.

Profile
=======

Le modèle **Profile** représente un profil utilisateur associé à un compte existant dans le modèle intégré ``User`` de Django.

.. code-block:: python

    from django.db import models
    from django.contrib.auth.models import User

    class Profile(models.Model):
        """
        Modèle représentant un profil utilisateur.

        Attributs :
            - user (User) : Relation One-to-One avec le modèle User.
            - favorite_city (str) : La ville préférée de l'utilisateur.

        Relations :
            - user (User) : Association avec un utilisateur unique.
        """
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        favorite_city = models.CharField(max_length=64, blank=True)

        def __str__(self):
            return self.user.username

Address
=======

Le modèle **Address** définit les informations relatives à une adresse.

.. code-block:: python

    from django.db import models
    from django.core.validators import MaxValueValidator, MinLengthValidator

    class Address(models.Model):
        """
        Modèle représentant une adresse.

        Attributs :
            - number (int) : Numéro de rue (max 4 chiffres).
            - street (str) : Nom de la rue.
            - city (str) : Nom de la ville.
            - state (str) : Abréviation de l'état (exactement 2 caractères).
            - zip_code (int) : Code postal (max 5 chiffres).
            - country_iso_code (str) : Code ISO du pays (exactement 3 caractères).

        Relations :
            - Aucune.
        """
        number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
        zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
        country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

        class Meta:
            verbose_name = "adresse"
            verbose_name_plural = "adresses"

        def __str__(self):
            return f"{self.number} {self.street}"

Letting
=======

Le modèle **Letting** représente une location associée à une adresse spécifique.

.. code-block:: python

    class Letting(models.Model):
        """
        Modèle représentant une location.

        Attributs :
            - title (str) : Titre de la location.
            - address (Address) : Adresse associée à la location.

        Relations :
            - address (Address) : Relation One-to-One avec une adresse.
        """
        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

        def __str__(self):
            return self.title

Relations Entre Modèles
=======================

- **Profile** : Relation **One-to-One** avec le modèle intégré ``User``.
- **Address** : Ne possède aucune relation directe mais est utilisé par ``Letting``.
- **Letting** : Relation **One-to-One** avec une adresse unique via ``Address``.

Notes Importantes
=================

- **Classe Meta** :
  - Le paramètre ``verbose_name`` permet de définir un nom lisible dans l'interface d'administration Django.
  - Les noms au pluriel sont définis via ``verbose_name_plural``.

- **Méthodes ``__str__``** :
  - Ces méthodes offrent une représentation textuelle lisible pour les objets.

- **Migration des Données** :
  - Les ajustements complexes peuvent nécessiter des scripts de migration personnalisés pour déplacer ou copier les données sans affecter l'application en production.

Ces modèles sont prêts pour une utilisation dans Django Admin, des API ou d'autres services.
