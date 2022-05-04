# Generated by Django 3.2.13 on 2022-05-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0018_auto_20220503_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='dia',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='horario',
            unique_together={('horarios', 'dia', 'medico')},
        ),
        migrations.RemoveField(
            model_name='horario',
            name='agenda',
        ),
    ]