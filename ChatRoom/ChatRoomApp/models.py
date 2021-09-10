from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Messages(models.Model):
    """Класс сообщений"""
    author = models.EmailField(validators=[RegexValidator(regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
                                                          message='Username must be Alphanumeric',
                                                          code='invalid_username'), ])
    text = models.TextField(max_length=100, validators=[RegexValidator(regex='^(?!\s*$).+'), ])
    create_date = models.DateField(null=True)
    update_date = models.DateField(null=True)

    def __str__(self):
        return "{} {} {} {} ".format(self.author, self.text, self.create_date, self.update_date)




