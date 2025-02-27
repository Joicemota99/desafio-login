from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, nome, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Removendo username padrão
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'  # Login será feito pelo e-mail
    REQUIRED_FIELDS = ['nome']  # Nome agora é obrigatório

    objects = CustomUserManager()  # Define o UserManager personalizado

    def __str__(self):
        return self.email
