from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UsuarioSerializer

from .models import Usuario

@api_view(['GET'])
def apiOverView(request):
	"""
		Listado de urls disponibles en la API

	"""

	api_urls = {
		'Listar': '/api/usuario-list/',
		'Crear':  '/api/usuario-create/',
		'Detalle': '/api/usuario-detail/<str:pk>',
		'Actualizar': '/api/usuario-update/<str:pk>',
		'Eliminar': '/api/usuario-delete/<str:pk>',
	}

	return Response(api_urls)


@api_view(['GET'])
def usuarioList(request):
	"""
		Retorna un listado de Usuarios creados en el sistema.
	"""

	usuarios = Usuario.objects.all()
	serializer = UsuarioSerializer(usuarios, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def usuarioDetail(request, pk):
	"""
		Si el request es correcto, se devuelve una instancia 'Usuario', dados los datos validados.

	"""

	if Usuario.objects.filter(pk=pk).exists():
		usuario = Usuario.objects.get(pk=pk)
	else:
		error_message = 'El usuario con id {} no existe'.format(pk)
		return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

	serializer = UsuarioSerializer(usuario, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def usuarioCreate(request):
	"""

		Crea y devuelva una instancia 'Usuario', dados los datos validados.

	"""

	serializer = UsuarioSerializer(data=request.data)

	if serializer.is_valid(raise_exception=True):
		serializer.save()

	return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
def usuarioUpdate(request, pk):
	"""
		
		Actualiza y devuelva una instancia `Usuario` existente, dados los datos validados.

	"""

	if Usuario.objects.filter(pk=pk).exists():
		usuario = Usuario.objects.get(pk=pk)
	else:
		error_message = 'El usuario con id {} no existe'.format(pk)
		return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

	partial_only = True if request.method == 'PATCH' else False

	serializer = UsuarioSerializer(instance=usuario, data=request.data, partial=partial_only)
	print(request.data)

	if serializer.is_valid(raise_exception=True):
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def usuarioDelete(request, pk):
	"""

		Permite Eliminar un usuario

	"""

	if Usuario.objects.filter(pk=pk).exists():
		usuario = Usuario.objects.get(pk=pk)
	else:
		error_message = 'El usuario con id {} no existe'.format(pk)
		return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

	usuario = Usuario.objects.get(pk=pk)
	usuario.delete()
	message = 'El usuario con id {} se ha eliminado exitosamente'.format(pk)

	return Response({'message': message})
