from rest_framework import serializers
import datetime
from datetime import date

from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = '__all__'

	def validate_fecha_nacimiento(self, value):
		if value:
			if value >= datetime.date.today():
				raise serializers.ValidationError("La fecha de nacimiento no puede ser mayor a hoy")
        
		return value
