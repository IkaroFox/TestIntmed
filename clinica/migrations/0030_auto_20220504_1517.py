# Generated by Django 3.2.13 on 2022-05-04 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0029_auto_20220504_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='agenda',
            new_name='agenda_id',
        ),
        migrations.AlterUniqueTogether(
            name='consulta',
            unique_together={('horario', 'agenda_id')},
        ),
    ]
