from django.db import models
from .validators import validate_is_audio

# Create your models here.
class PlayModel(models.Model):

  title = models.CharField(max_length=50,null=True)
  m_file = models.FileField(verbose_name="音楽ファイル",null=True, upload_to='sound', validators=[validate_is_audio])

  def __str__(self):
    return self.title