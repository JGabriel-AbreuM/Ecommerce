from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validacao_porcentagem(valor):
    if 0 >= valor or valor > 100:
        raise ValidationError(
            _('%(value)s não é um número válido.'),
            params={'value': valor},
        )