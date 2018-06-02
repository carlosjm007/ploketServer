import json
from channels import Channel, Group
import TEST.models as TestModels

#####################
##  Documentacion de la libreria channels
##  https://channels.readthedocs.io/en/latest/
#####################

## Funcion que se ejecuta cuando un usuario se conecta por medio del socket
#  @param message Contiene la informacion del usuario se que conecta, ej: id usuario
def ws_connect(message, sala, id):
	print u"%s - %s"%(sala, id)
	message.reply_channel.send({'accept': True})
	Group(sala).add(message.reply_channel)

## Funcion que se ejecuta cuando un usuario envia un mensaje a traves del socket
## especificamente atiende casos de bloqueo, activacion y cierre de alerta e informa
## a otros usuario conectados
#  @param message Contiene la informacion del usuario se que conecta, ej: id usuario
def ws_receive(message, sala, id):
	try:
		Group(sala).send({"bytes": message.content["bytes"]})
	except:
		info = json.loads(message.content['text'])
		TestModels.jugador.objects.filter(id=info["id_disparado"]).update(estado=False)
		Group(sala).send({"text": message.content['text']})
    

## Funcion que se ejecuta cuando El socket es desconectado
#  @param message Contiene la informacion del usuario se que conecta, ej: id usuario
def ws_disconnect(message, sala, id):
	# Unsubscribe from any connected rooms
	#TestModels.jugador.objects.filter(id=id).update(estado=False)
	print u"Desconectado"