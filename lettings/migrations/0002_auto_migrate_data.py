from django.db import migrations


def migrate_data(apps, schema_editor):
    Letting = apps.get_model('lettings', 'Letting')
    Address = apps.get_model('lettings', 'Address')
    old_lettings = apps.get_model('oc_lettings_site', 'Letting')

    # Exemple de migration de données des anciennes tables vers les nouvelles
    for old_letting in old_lettings.objects.all():
        # Exemple de création d'une nouvelle adresse basée sur les données existantes
        address = Address.objects.create(
            number=old_letting.address_number,
            street=old_letting.address_street,
            city=old_letting.address_city,
            state=old_letting.address_state,
            zip_code=old_letting.address_zip_code,
            country_iso_code=old_letting.address_country_iso_code,
        )

        Letting.objects.create(
            title=old_letting.title,
            address=address,
        )


class Migration(migrations.Migration):

    dependencies = [
        # La migration initiale qui crée les nouveaux modèles
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
