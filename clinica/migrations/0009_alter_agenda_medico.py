# Generated by Django 3.2.13 on 2022-05-02 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0008_alter_agenda_medico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='medico',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico'),
        ),
    ]
