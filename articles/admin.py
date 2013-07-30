from django.contrib import admin
from articles.models import Article, Comment

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

admin.site.register(Article, ArticleAdmin)