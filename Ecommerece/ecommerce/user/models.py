from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    CHOICES = (
        ("VD", ("Vendedor")),
        ("CP", ("Comprador"))
    )

    type = models.CharField(max_length=10, choices=CHOICES, blank=False, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @classmethod
    def type_is(self, id):
        user = CustomUser.objects.get(id=id)
        
        return user.type  

    @classmethod
    def id_is(self, username):
        user = User.objects.get(username=username)

        return user.id