from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
	path("", views.home, name="home" ),
        path("login/", views.loginUser, name="login"),
        path("logout/", views.logoutUser, name="logout"),
        path("apply/final/", views.final, name="final"),
        path("apply/stage1/", views.form, name="form"),
        path("apply/stage2/", views.employ, name="employ"),
        path("apply/stage3/", views.loan, name="loan"),
        path("dashboard/", views.dash, name="loan"),
        path("apply/verify/", views.verifyPayment, name="verify"),

        path("privacy/", views.privacy),
        path("about/", views.about),
        path("contact/", views.contact),
        path("tos/", views.tos),
        path("offices/", views.offices)
]


urlpatterns += staticfiles_urlpatterns()
