from rest_framework import serializers
import TEST.models as TestModels

class SerialJugador(serializers.ModelSerializer):
	sala_id = serializers.SerializerMethodField('trae_sala_id')

	def trae_sala_id(self, objeto):
		return u"%s" %(objeto.sala.id)
	class Meta:
		model = TestModels.jugador
		fields = ('id','nombre', 'sala_id')