from rest_framework import serializers
from usuario.models import usuario


class usuarioSerializer(serializers.ModelSerializer):
    class meta:
        model = usuario
        fields = ['id','nome','email','senha','numero'.'nacimento']