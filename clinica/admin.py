from django.contrib import admin
from .models import Agenda, Horario, Medico, Consulta
from django import forms


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'crm', 'email', 'created_at', 'updated_at']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['horarios', 'created_at', 'updated_at']


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    # horarios = HorarioAdmin
    list_display = ['dia', 'medico', 'created_at', 'updated_at']
    date_hierarchy = 'dia'


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['agenda_id', 'horario', 'data_agendamento']
    # 'medico'
