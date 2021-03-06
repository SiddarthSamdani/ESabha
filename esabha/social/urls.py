from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
      path('home/', views.HomeView.as_view()),
      path('about/', views.AboutView.as_view()),
      path('contact/', views.ContactView.as_view()),
      path('', RedirectView.as_view(url='home/')),

        # path('mylist/', views.MyList.as_view()),
        # path('question/create', views.QuestionCreate.as_view(success_url="/college/home")),
        # path('notice/', views.NoticeListView.as_view()),
        # path('notice/<int:pk>', views.NoticeDetailView.as_view()),
        # path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/college/home")),

]
