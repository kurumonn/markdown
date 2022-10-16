from django.urls import path

from .views import MarkdownListView

urlpatterns = [
    path('', MarkdownListView.as_view(), name='markdown_list'),
]