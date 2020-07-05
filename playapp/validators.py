import os
from django.core.exceptions import ValidationError

def validate_is_audio(value):
  # splittextはピリオドで分割します
  ext = os.path.splitext(value.name)[1]
  if not ext.lower() in ['.wav', '.mp3', '.acc']:
    raise ValidationError('音声ファイルしか受付ないよ！')