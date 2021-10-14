from django.contrib import admin
from django.urls import include, path
from mineauth.views import LoginView
from mineauth.api import UserList, UserDetails, GroupList

urlpatterns = [
		path('admin/', admin.site.urls),
		path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
		path('accounts/login/', LoginView.as_view(template_name="registration/login.html")),
		# path('oauth/', include("mineauth.urls"))
		path('users/', UserList.as_view()),
		path('users/<pk>/', UserDetails.as_view()),
		path('groups/', GroupList.as_view()),
]
