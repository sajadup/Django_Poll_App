from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Poll App Admin"
admin.site.site_title = "Poll App Admin Area"
admin.site.index_title = "Welcome to Poll App"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)