from django.urls import path
from .views import HomeView, postDetailView, humorView, authorView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', postDetailView.as_view(), name="postDetails"),
    path('humor/', humorView, name="humor"),
    path('author/', authorView, name="author"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="addComment"),
]