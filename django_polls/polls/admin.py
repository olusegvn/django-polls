from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question",               {'fields': ['question']}),
        ('Date information', {'fields': [], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

