from django.contrib import admin

# Register your models here.

from .models import UserProfile, BlogPost, Comment, Product, Store, Question, Choice, ContactMessage

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'bio')
	list_display_links = ('id', 'user')
	search_fields = ('user', 'bio')

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'content', 'author')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'author', 'content')
	list_display_links = ('id', 'post')
	search_fields = ('post', 'content')


class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'price')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'description')


class StoreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'question_text')
	list_display_links = ('id', 'question_text')


class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'question', 'choice_text', 'votes')
	list_display_links = ('id', 'question')
	search_fields = ('question', 'choice_text')


class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'content')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'content')





admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)