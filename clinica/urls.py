from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (MedicoViewSet,
                    AgendaAlphaViewSet,
                    ConsultaAlphaViewSet)


router = SimpleRouter()
# teste
router.register('agendas', AgendaAlphaViewSet)
router.register('consultas', ConsultaAlphaViewSet)

router.register('medicos', MedicoViewSet)
# router.register('agendas', HorarioViewSet)
# router.register('consulta', ConsultaViewSet)

urlpatterns = [
    # path('consultas/(?P<crm>.+)/$', ConsultaAlphaViewSet.as_view()),
    # path('agendas/', AgendaAlphaViewSet.as_view(), name='agendas'),
    # path('agendas/<int:pk>/', AgendaAPIView.as_view(), name='agenda'),
]
