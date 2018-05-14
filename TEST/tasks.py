from background_task import background
from django.contrib.auth.models import User
import TEST.models as TestModels
from channels import Channel, Group
import json
@background()
def test(sala_id):
	print "task " + sala_id

@background(schedule=1)
def ordenar_jugadores(sala_id):
	angulo = 0
	diccionario = {}
	jugadores = TestModels.jugador.objects.filter(sala__id = sala_id)
	distancia = 360 / jugadores.count()
	for ju in jugadores:
		diccionario = {"id":ju.id,"angulo":angulo,"magnitud": 52.0}
		angulo = angulo + distancia
		Group(str(sala_id)).send({"text": json.dumps(diccionario)})

@background()
def cuenta_regresiva():
	salas_listas = TestModels.sala.objects.filter(cuenta__gte=1)
	diccionario = {}
	for sa in salas_listas:
		sa.cuenta = sa.cuenta - 1
		sa.save()
		if (sa.cuenta == 5):
			ordenar_jugadores(sa.id)
		diccionario = {"id":"Server", "cuenta": sa.cuenta}
		Group(str(sa.id)).send({"text": json.dumps(diccionario)})