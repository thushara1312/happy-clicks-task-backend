import uuid
from django.db import models
from django.conf import settings
from django.db.models import Max

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="creator_%(app_label)s_%(class)s_objects",
        on_delete=models.CASCADE,
    )
    updater = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="updater_%(app_label)s_%(class)s_objects",
        on_delete=models.CASCADE,
    )
    deleter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="deleter_%(app_label)s_%(class)s_objects",
        on_delete=models.CASCADE,
    )
   
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.auto_id:
            max_auto_id = self.__class__.objects.aggregate(Max('auto_id'))['auto_id__max']
            self.auto_id = (max_auto_id or 0) + 1
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
