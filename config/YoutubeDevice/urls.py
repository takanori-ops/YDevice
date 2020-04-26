from django.urls import path
from . import views

app_name = "YoutubeDevice"

urlpatterns = [
    path("",views.index,name="index"),
    path("home/",views.home,name="home"),
    path('signup/', views.signup, name='signup'), # 追加
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"), # 追加
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"), # 追加
    path("cards/", views.CardListView.as_view(), name="cards_list"),
    path("cards/create/", views.CardCreateView.as_view(), name="cards_create"),
    path("cards/<int:pk>/", views.CardDetailView.as_view(), name="cards_detail"),
    path("cards/<int:pk>/update/", views.CardUpdateView.as_view(), name="cards_update"),
    path("cards/<int:pk>/delete/", views.CardDeleteView.as_view(), name="cards_delete"),
]

