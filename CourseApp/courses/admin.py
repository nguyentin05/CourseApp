from unittest import case

from django.contrib import admin
from .models import Category,Course,Lesson
from django import forms
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }

    form = LessonForm
    list_display = ['id', 'subject', 'course']
    search_fields = ['subject']
    list_filter = ['subject', 'course__subject']
    readonly_fields = ['avatar']

    def avatar(self,lesson):
        return mark_safe("<img src='/static/{img_url}' alt ='{alt}'/>".format(img_url=lesson.image.name,alt=lesson.subject))

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson,LessonAdmin)
