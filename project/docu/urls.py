from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url=staticfiles_storage.url("index.html"))),
    path('api/', views.getData),
    path('api/info', views.info),
    path('api/token/signup/', views.signupToken, name='token_signup'),
    path('api/token/', views.loginToken, name='token_obtain_pair'),
    path('api/token/refresh/', views.refreshToken, name='token_refresh'),
    path('api/token/logout/', views.logoutToken, name='token_logout'),
    path('api/tokens/list/', views.getTokens, name='tokens_list'),
    path('about/', views.about),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
]
