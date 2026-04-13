from django.contrib import admin
from .models import uploadCV, JDKeyword, Rematch

@admin.register(uploadCV)
class uploadCVAdmin(admin.ModelAdmin):
    list_display = ('id', 'cv_file', 'uploaded_at')
    readonly_fields = ('extracted_text',)

@admin.register(JDKeyword)
class JDKeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword',)

@admin.register(Rematch)
class RematchAdmin(admin.ModelAdmin):
    list_display=('id', 'ats_score', 'uploaded_at')
    readonly_fields = ('ideal_text',)