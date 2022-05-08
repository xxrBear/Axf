from django.db import models


class AxfUser(models.Model):
    u_name = models.CharField(max_length=128)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(max_length=64)
    u_icon = models.ImageField(upload_to='icons')
    u_token = models.CharField(max_length=256)

    u_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_user'
