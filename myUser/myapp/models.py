from django.db import models
from django.conf import settings

# duplicate key value will violate unique constraint 
#  "myapp_userprofile_user_id_key"
class UserProfile(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE)

  questions = models.CharField(max_length=1024)
  
