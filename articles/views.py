# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from articles.models import Article, Comment

class IndexView(generic.ListView):
	template_name = 'articles/article_list.html'
	context_object_name = 'articles'
	def get_queryset(self):
		return Article.objects.order_by('-pub_date')

"""class DetailView(generic.DetailView):
	template_name = 'articles/comments.html'
	context_object_name = 'article'
	def get_queryset(self):
		article = get_object_or_404(Article, article_id=pk)
		return article.comment_set.order_by('-pub_date')
"""
class NewCommentView(generic.DetailView):
	template_name = 'articles/newcomment.html'
	context_object_name = 'article'
	model = Article

def addComment(request, pk):
	comment = Comment(content=request.POST['content'], article_id=pk, user=request.user.username);
	comment.save()
	return HttpResponseRedirect(reverse('articles:comments', args=(comment.article_id)))	

def commentList(request, pk):
	article = get_object_or_404(Article, id=pk)
	comments = article.comment_set.order_by('-pub_date')
	return render(request, 'articles/comments.html', { 'comments':comments })

def signupView(request):
	return render(request, 'articles/signup.html')

def signup(request):
	user = User.objects.create_user(request.POST['username'], "NULL", request.POST['password'])
	userCheck = authenticate(username=request.POST['username'], password=request.POST['password'])
	login(request, userCheck)
	return render(request, 'articles/signupSuccess.html', { 'username':request.POST['username'] })

def loginView(request):
	return render(request, 'articles/login.html')

def loginLink(request):
	form = AuthenticationForm(data=request.POST)
	if form.is_valid():
		login(request, form.get_user())
		return HttpResponseRedirect(reverse('articles:index'))

def logoutLink(request):
	logout(request)
	return HttpResponseRedirect(reverse('articles:index'))
