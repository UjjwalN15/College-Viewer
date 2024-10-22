# from django.db import models
# from django.utils.translation import gettext as _

# # Create your models here.

# class Colleges(models.Model):
#     name = models.CharField(_("colege"), max_length=300)
#     location = models.CharField(_("location"),max_length=500)
#     university = models.CharField(_("university"),max_length=300)
#     courses = models.CharField(_("courses"),max_length=300)
#     ownership = models.CharField(_("ownership"),max_length=300)
#     phone_number = models.CharField(_("phone_number"),max_length=300)
#     email = models.EmailField(_("email"),)

from django.db import models

class College(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    university = models.CharField(max_length=500)
    course_offered = models.CharField(max_length=500)
    ownership_type = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.name
