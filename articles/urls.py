from django.conf.urls import patterns, include, url
from articles import views
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.commentList, name='comments'),
    url(r'^(?P<pk>\d+)/form/$', views.NewCommentView.as_view(), name='commentForm'),
    url(r'^(?P<pk>\d+)/add/$', views.addComment, name='addComment'),
    url(r'^signup/$', views.signupView, name='signupView'),
    url(r'^success/$', views.signup, name='signup'),
    url(r'^login/$', views.loginView, name='loginView'),
    url(r'^login/success/$', views.loginLink, name='loginHere'),
    url(r'^logout/$', views.logoutLink, name='logoutLink'),






)
