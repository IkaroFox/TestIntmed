from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core import serializers


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Medico(Base):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Medico'
        unique_together = ['email', 'crm']
        ordering = ['-created_at']

    def __str__(self):
        return self.nome


class Agenda(Base):

    def validate_date(date):
        if date < timezone.now().date():
            raise ValidationError(
                ("Data não pode ser antiga"), code='invalid')

    medico = models.ForeignKey(
        Medico,
        related_name='medicos',
        on_delete=models.CASCADE,
        null=True)

    dia = models.DateField(
        validators=[validate_date]
    )

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        unique_together = [['medico', 'dia']]
        ordering = ['-dia']


class Horario(Base):
    horarios = models.TimeField(null=True)
    agenda = models.ForeignKey(Agenda,
                               related_name="horarios",
                               on_delete=models.CASCADE,
                               null=True,
                               )

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        unique_together = [['horarios', 'agenda']]
        ordering = ['-horarios']


class Consulta(models.Model):

    def validate_date(date):
        ag0 = Agenda.objects.all().filter(id=date)
        if ag0.values('dia')[0]['dia'] < timezone.now().date():
            raise ValidationError(
                ("Não pode ser Data antiga."), code='invalid')

    def validate_date_time(date):
        ag0 = Horario.objects.all().filter(id=date)
        if ag0.values('horarios')[0]['horarios'] < timezone.now().date():
            raise ValidationError(
                ("Não pode ser Horario antigo."), code='invalid')

    agenda_id = models.ForeignKey(
        Agenda,
        related_name="agenda_id",
        on_delete=models.CASCADE,
        null=True,
        validators=[validate_date]
    )
    horario = models.ForeignKey(
        Horario,
        related_name="consulta",
        on_delete=models.CASCADE,
        null=True,
        validators=[validate_date_time]
    )
    data_agendamento = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        unique_together = [['horario', 'agenda_id']]
        # ordering = ['-horario']
