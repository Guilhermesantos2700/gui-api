from rest_framework import serializers
from empresa.models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id','nome','email','senha','cnpj','telefone','endereso','cep']