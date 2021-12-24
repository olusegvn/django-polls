from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question",               {'fields': ['question']}),
        ('Date information', {'fields': [], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'publish_date', 'was_published_recenetly')
    list_filter = ['publish_date']
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

