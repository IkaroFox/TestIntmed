# Generated by Django 3.2.13 on 2022-05-03 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0021_horario_agenda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='agenda',
        ),
        migrations.AddField(
            model_name='agenda',
            name='agenda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to='clinica.horario'),
        ),
    ]
