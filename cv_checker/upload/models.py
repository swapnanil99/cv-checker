from django.db import models

class uploadCV(models.Model):
  cv_file = models.FileField(upload_to="cvs/", max_length=255, null=True, default=None)
  extracted_text = models.TextField(blank=True)
  uploaded_at = models.DateTimeField(auto_now_add=True)
  ats_score = models.PositiveIntegerField(default=0)

  def __str__(self):
    return self.cv_file.name

class JDKeyword(models.Model):
  keyword = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.keyword
  
class Rematch(models.Model):
  ideal_text = models.TextField() 
  uploaded_at = models.DateTimeField(auto_now_add=True)
  ats_score = models.PositiveIntegerField(default=0)
  
  def __str__(self):
     return f"Ideal Text {self.id}"