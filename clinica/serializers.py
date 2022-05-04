from rest_framework import serializers
from django.http import HttpResponse
from django.db.models import Avg
from json import JSONEncoder
import json

from .models import Agenda, Medico, Horario, Consulta


class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico

        fields = (
            'id',
            'crm',
            'nome',
            'email',
        )


class HorariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horario
        fields = [
            'horarios',
        ]


class AgendaSerializer(serializers.ModelSerializer):

    medico = serializers.PrimaryKeyRelatedField(queryset=Medico.objects.all())
    horarios = HorariosSerializer(many=True)

    class Meta:
        model = Agenda
        fields = [
            'id',
            'medico',
            'dia',
            'horarios',
        ]

    def create(self, validated_data):
        horaios_data = validated_data.pop('horarios')
        instance = Agenda.objects.create(**validated_data)
        for horaio_data in horaios_data:
            print(horaio_data)
            Horario.objects.create(
                agenda=instance, horarios=horaio_data['horarios'])
        return instance

    def to_representation(self, instance):
        self.fields['medico'] = MedicoSerializer()
        return super(AgendaSerializer, self).to_representation(instance)


class AgendaGetSerializer(serializers.ModelSerializer):

    medico = serializers.PrimaryKeyRelatedField(queryset=Medico.objects.all())
    horarios = serializers.SlugRelatedField(many=True,
                                            queryset=Horario.objects.all(),
                                            slug_field="horarios",
                                            required=False,)

    class Meta:
        model = Agenda
        fields = [
            'id',
            'medico',
            'dia',
            'horarios',
        ]
        # depth = 0

    def to_representation(self, instance):
        self.fields['medico'] = MedicoSerializer()
        return super(AgendaGetSerializer, self).to_representation(instance)


class AgendaCustomSerializer(serializers.ModelSerializer):

    medico = MedicoSerializer()

    class Meta:
        model = Agenda
        fields = ['medico']


class ConsultaGetSerializer(serializers.ModelSerializer):

    agenda_id = serializers.PrimaryKeyRelatedField(queryset=Agenda.objects.all(), write_only=True)

    horario = serializers.SlugRelatedField(many=False,
                                           queryset=Horario.objects.all(),
                                           slug_field="horarios",
                                           required=False,)

    medico = serializers.SerializerMethodField('get_madic')

    dia = serializers.SerializerMethodField('is_named')

    class Meta:
        model = Consulta
        extra_kwargs = {'agenda_id': {'write_only': True}}
        fields = [
            'id',
            'dia',
            'agenda_id',
            'horario',
            'data_agendamento',
            'medico',
        ]

    def is_named(self, foo):
        return foo.agenda_id.dia

    def get_madic(self, foo):
        m = {
            'id': foo.agenda_id.medico.id,
            'nome': foo.agenda_id.medico.nome,
            'crm': foo.agenda_id.medico.crm,
            'email': foo.agenda_id.medico.email,
        }
        return m
    
    # def create(self, validated_data):
    #     data_agenda = validated_data.pop('agenda_id')
    #     data_horarios = validated_data.pop('horario')
    #     # agenda_data = validated_data.pop('agenda')
    #     instance = Consulta.objects.create(
    #         agenda=data_agenda,
    #         horario=data_horarios
    #     )
    #     return instance


# class ConsultaSerializer(serializers.ModelSerializer):

#     horario = serializers.SlugRelatedField(many=False,
#                                            queryset=Horario.objects.all(),
#                                            slug_field="horarios",
#                                            required=False,)

#     medico = serializers.SerializerMethodField('get_madic')

#     dia = serializers.SerializerMethodField('is_named')

#     class Meta:
#         model = Consulta
#         fields = [
#             'id',
#             'dia',
#             'horario',
#             'data_agendamento',
#             'medico',
#         ]

#     def is_named(self, foo):
#         return foo.agenda.dia

#     def get_madic(self, foo):
#         m = {
#             'id': foo.agenda.medico.id,
#             'nome': foo.agenda.medico.nome,
#             'crm': foo.agenda.medico.crm,
#             'email': foo.agenda.medico.email,
#         }
#         return m

#     def create(self, validated_data):
#         data = validated_data.pop(0)
#         # agenda_data = validated_data.pop('agenda')
#         instance = Consulta.objects.create(
#             agenda=data['agenda'],
#             horario=data['horario']
#         )
#         return instance
