# Generated by Django 4.2.4 on 2023-09-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapplication', '0003_infosession_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infosession',
            name='categorie',
        ),
        migrations.AddField(
            model_name='infoetudiant',
            name='categorie',
            field=models.CharField(choices=[('Tous', 'Tous'), ('Licence 1', 'Licence 1'), ('Licence 2', 'Licence 3'), ('Licence 3', 'Licence3')], default='Tous', max_length=15),
        ),
    ]
