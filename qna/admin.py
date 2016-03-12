from django.contrib import admin

from .models import Question, Answer, QuestionComment, AnswerComment, Stream, Category, Heart

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(QuestionComment)
admin.site.register(Answer)
admin.site.register(AnswerComment)
admin.site.register(Stream)
admin.site.register(Category)
admin.site.register(Heart)
