# Generated by Django 3.2.13 on 2022-05-03 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0020_alter_horario_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='agenda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dias', to='clinica.agenda'),
        ),
    ]
