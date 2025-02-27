import re
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    confirmar_senha = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'nome', 'password', 'confirmar_senha']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_nome(self, value):
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', value):
            raise serializers.ValidationError("O nome deve conter apenas letras.")
        return value

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("E-mail inválido.")
        return value

    def validate_password(self, value):
        if len(value) < 8 or not re.search(r'[A-Z]', value) or not re.search(r'\d', value) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("A senha deve ter no mínimo 8 caracteres, 1 número, 1 caractere especial e 1 letra maiúscula.")
        return value

    def validate(self, data):
        if data['password'] != data['confirmar_senha']:
            raise serializers.ValidationError({"confirmar_senha": "As senhas não coincidem."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirmar_senha')  # Removendo para evitar erro na criação do usuário
        user = User.objects.create_user(**validated_data)
        return user
