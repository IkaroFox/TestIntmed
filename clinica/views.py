from rest_framework import viewsets, mixins, generics ,serializers
# from django.shortcuts import get_object_or_404


# from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Medico, Agenda, Horario, Consulta
from .serializers import (MedicoSerializer,
                          AgendaSerializer,
                          AgendaGetSerializer,
                          ConsultaGetSerializer,
                        #   ConsultaSerializer
                          )


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class ConsultaAlphaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaGetSerializer

# metodo que possibilita puxar as avaliacoes de um curso
    # def get_queryset(self):
    #     if self.kwargs.get('crm'):
    #         return self.queryset.filter(crm=self.kwargs.get('crm'))
    #     return self.queryset.all()
    
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['agenda_id', 'horario']


class AgendaAlphaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AgendaSerializer
        return AgendaGetSerializer

