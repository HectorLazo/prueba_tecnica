import uuid
from django.db import models

# Create your models here.

class UsuarioManager(models.Manager):
	""" 
		Manager para usuarios
	"""

	def create_usuario(self, email, fecha_nacimiento):
		if not email:
			raise ValueError('Usuario debe tener un email')

		email = self.normalize_email(email)
		usuario = self.model(email=email)

		usuario.save(using=self._db)

		return user



class Usuario(models.Model):
	"""
		Modelo para usuarios
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)
	fecha_nacimiento = models.DateField()

	objects = UsuarioManager()