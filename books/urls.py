from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('<uuid:pk>', views.BookDetail.as_view(), name='book_detail'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
]
