from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Trainer(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name
