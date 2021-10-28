from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

class postDetailView(DetailView):
	model = Post
	template_name = 'postDetails.html'

def humorView(request):
	return render(request, 'humor.html')

def authorView(request):
	return render(request, 'author.html')

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'addComment.html'
	success_url = reverse_lazy('home')	
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)