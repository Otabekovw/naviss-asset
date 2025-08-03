from django.urls import path
from . import views

urlpatterns = [
    path('partner/', views.PartnerAPIView.as_view(), name='partners-list'),
    path('news/', views.NewsAPIView.as_view(), name='news-list'),
    path('faq/', views.FAQAPIView.as_view(), name='faq-list'),
    path('feedback/', views.FeedbackAPIView.as_view(), name='feedback-list'),

]

