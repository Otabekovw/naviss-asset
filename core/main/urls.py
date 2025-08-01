from django.urls import path
from . import views

urlpatterns = [
    path('partners/', views.PartnersAPIView.as_view(), name='partners-list'),
    path('partners/create/', views.PartnersCreateAPIView.as_view(), name='partners-create'),
    path('partners/update/<int:pk>/', views.PartnersUpdateAPIView.as_view(), name='partners-update'),
    path('partners/delete/<int:pk>/', views.PartnersDeleteAPIView.as_view(), name='partners-delete'),

    path('news/', views.NewsAPIView.as_view(), name='news-list'),
    path('contacts/', views.ContactAPIView.as_view(), name='contacts-list'),
    path('applications/', views.ApplicationsAPIView.as_view(), name='applications-list'),
    path('reviews/', views.ReviewAPIView.as_view(), name='review-list'),
    path('detailednews/', views.DetailednewsAPIView.as_view(), name='detailednews-list'),
    path('detailednews/<int:pk>/', views.DetailednewsDetailAPIView.as_view(), name='detailednews-detail'),
]
