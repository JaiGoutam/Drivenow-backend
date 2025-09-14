from django.db import models
from datetime import datetime


class BaseQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        return super().update(
            r_status="D",
            updated_by=user,
            updated_on=datetime.now()
        )

    def update(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        kwargs["updated_by"] = user
        kwargs["updated_on"] = datetime.now()
        return super().update(*args, **kwargs)

    def create(self, *args, **kwargs):
        instance = self.model(*args, **kwargs)
        instance.save()
        return instance


class BaseManager(models.Manager):
    def get_queryset(self, apply_status_filter=True):
        qs = BaseQuerySet(self.model, using=self._db)
        return qs.filter(r_status="A") if apply_status_filter else qs

    def get(self, *args, **kwargs):
        apply_status_filter = kwargs.pop('apply_status_filter', True)
        return self.get_queryset(apply_status_filter).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        apply_status_filter = kwargs.pop('apply_status_filter', True)
        return self.get_queryset(apply_status_filter).filter(*args, **kwargs)

    def create(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        instance = self.model(*args, **kwargs)
        instance.save(user=user)
        return instance


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    r_status = models.CharField(max_length=1, choices=[('A', 'Active'), ('D', 'Deleted')], default='A')

    objects = BaseManager()

    IMMUTABLE_FIELDS = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_state = {
            field: getattr(self, field) for field in self.IMMUTABLE_FIELDS
        }

    def save(self, *args, **kwargs):
        user = kwargs.pop("user", None)

        if self.pk is not None:
            for field_name in self.IMMUTABLE_FIELDS:
                current_value = getattr(self, field_name)
                original_value = self._original_state.get(field_name)
                if current_value != original_value:
                    raise ValueError(f"Cannot update immutable field: {field_name}")

        if not self.created_by and user:
            self.created_by = user
        if user:
            self.updated_by = user

        if not self.r_status:
            self.r_status = "A"

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.r_status = "D"
        self.save(*args, **kwargs)

    class Meta:
        abstract = True
