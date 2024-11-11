from django.db import migrations


def migrate_data(apps, schema_editor):
    # Récupérer l'ancien modèle dans oc_lettings_site
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    # Récupérer le modèle Profile dans l'application profiles
    Profile = apps.get_model('profiles', 'Profile')

    # Migrer les données : pour chaque profil dans l'ancienne table, créer un nouveau profil
    for old_profile in OldProfile.objects.all():
        # Créer un nouveau profil dans 'profiles' avec les données de l'ancien profil
        Profile.objects.create(
            user=old_profile.user,  # Vous récupérez l'utilisateur associé
            # Migrer la ville favorite (ou autres champs si nécessaire)
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):

    dependencies = [
        # Assurez-vous que le modèle Profile dans profiles est bien créé
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
