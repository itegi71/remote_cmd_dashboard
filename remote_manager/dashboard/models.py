from django.db import models


class Commandlog(models.Model):
    """
    model to log executed SSH commands """

    server_ip=models.GenericIPAddressField()
    command=models.TextField()
    output=models.TextField()
    executed_at=models.DateTimeField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Server_ip} - {self.command} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# Create your models here.
