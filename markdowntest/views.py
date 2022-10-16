from django.views.generic import ListView

from .models import Post


class MarkdownListView(ListView):
    model = Post
    template_name = 'post_list.html'
