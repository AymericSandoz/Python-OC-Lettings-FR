# Generated by Django 3.0 on 2024-10-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0004_auto_20241011_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='letting',
            name='test',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
