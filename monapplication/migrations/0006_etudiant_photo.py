# Generated by Django 4.2.4 on 2023-09-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapplication', '0005_infosession_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='photo',
            field=models.FileField(blank=True, upload_to='photoEtudiant'),
        ),
    ]