# Created by kaikobud at ২১/৭/২০
from django.urls import path
from snippets import views

urlpatterns = [
    path('snippet/', views.snippet_list),
    path('snippet/<int:pk>', views.snippet_details),
]