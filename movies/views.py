from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import context
from django.views import generic
from .models import Movie, Review, Comment
from .forms import MovieModelForm, ReviewModelForm, CommentModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
	template_name = "registration/signup.html"
	form_class = CustomUserCreationForm

	def get_success_url(self):
		return reverse ("login")


class LandingPageView(generic.TemplateView):
	template_name = "landing.html"

class MovieListView(LoginRequiredMixin, generic.ListView):
	template_name = "leads/lead_list.html"
	queryset = Movie.objects.all()
	context_object_name = "movies"

def movie_create(request):
	if request.method == 'POST':
		print('Recieving a post request', request.FILES)


		# notice how I passed request.FILES. It is compulsory when you're receiving files

		# Your generic view function also works. I just want to show you how it would be written using just the 
		# normal function
		form = MovieModelForm(request.POST, request.FILES)
		if form.is_valid():
			print("The form is valid")
			print(form.cleaned_data)
			title = form.cleaned_data['title']
			date_released = form.cleaned_data['date_released']
			rating = form.cleaned_data['rating']
			poster = form.cleaned_data['poster']
			
			movie = Movie.objects.create(
				title=title,
				date_released=date_released,
				rating=rating,
				poster = poster
			)
			print(movie.poster.url)
		return redirect("/movies")	
	context = {
		"form": MovieModelForm()
	}
	return render(request, "movies/movie_create.html", context)



# class MovieCreateView(LoginRequiredMixin, generic.CreateView):
# 	template_name = "movies/movie_create.html"
# 	form_class  = MovieModelForm

# 	def get_success_url(self):
# 		return reverse ("movies:movie-list")

# 	def form_valid(self, form):
# 		# TODO send email
# 		send_mail(
# 			subject="A movie has been added to the list",
# 			message="Click the link below to see details of the movie",
# 			from_email="emekamba10@gmail.com",
# 			recipient_list=["admin@yemreviews.com"]
# 		)
		# return super(MovieCreateView, self).form_valid(form)


def movie_detail(request, pk):
	movies = Movie.objects.get(id=pk)
	reviews = Review.objects.filter(title=movies)
	comments = Comment.objects.all()
	context = {
        "movies": movies,
		"reviews": reviews,
		"comments": comments
    }
	return render(request, "movies/movie_detail.html", context)

class MovieUpdateView(LoginRequiredMixin, generic.UpdateView):
	template_name = "movies/movie_update.html"
	queryset = Movie.objects.all()
	form_class  = MovieModelForm

	def get_success_url(self):
		return reverse ("movies:movie-list")


class MovieDeleteView(LoginRequiredMixin, generic.DeleteView):
	template_name = "movies/movie_delete.html"
	queryset = Movie.objects.all()

	def get_success_url(self):
		return reverse ("movies:movie-list")

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
	template_name = "movies/review_create.html"
	form_class = ReviewModelForm

	def get_success_url(self):
		return reverse ("movies:movie-list")

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
	template_name = "movies/comment_create.html"
	form_class = CommentModelForm

	def get_success_url(self):
		return reverse ("movies:movie-detail")

class LogoutView(generic.TemplateView):
	template_name = "logout.html"































































#--------------------------------------------------

# #def movie_create(request):
# 	if request.method == 'POST':
# 		print('Recieving a post request')
# 		form = MovieForm(request.POST)
# 		if form.is_valid():
# 			print("The form is valid")
# 			print(form.cleaned_data)
# 			title = form.cleaned_data['title']
# 			date_released = form.cleaned_data['date_released']
# 			rating = form.cleaned_data['rating']
			
# 			Movie.objects.create(
# 				title=title,
# 				date_released=date_released,
# 				rating=rating
# 			)
# 		return redirect("/movies")	
# 	context = {
# 		"form": MovieForm()
# 	}
# 	return render(request, "movies/movie_create.html", context)

# def movie_list(request):
# 	movies = Movie.objects.all()
# 	context = {
#         "movies": movies
#     }
# 	return render(request, "movies/movie_list.html", context)

# def movie_detail(request, pk):
# 	movies = Movie.objects.get(id=pk)
# 	reviews = Review.objects.filter(title=movies)
# 	context = {
#         "movies": movies,
# 		"reviews": reviews
#     }
# 	return render(request, "movies/movie_detail.html", context)

# def movie_create(request):
# 	if request.method == 'POST':
# 		print('Recieving a post request')
# 		form = MovieModelForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("/movies")	
# 	context = {
# 		"form": MovieModelForm()
# 	}
# 	return render(request, "movies/movie_create.html", context)

# def movie_update(request, pk):
# 	movie = Movie.objects.get(id=pk)
# 	form = MovieModelForm(instance=movie)
# 	if request.method == "POST":
# 		form = MovieModelForm(request.POST, instance=movie)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("/movies")
# 	context = {
# 		"form": form,
# 		"movie": movie
# 	}
# 	return render(request, "movies/movie_update.html", context)

# def movie_delete(request, pk):
# 	movie = Movie.objects.get(id=pk)
# 	movie.delete()
# 	context = {
# 		"movie" : movie
# 	}
# 	return render(request, "movies/movie_delete.html", context)


# def landing_page(request):
# 	return render(request, "landing.html")

# def review_create(request, pk):
# 	movie = Movie.objects.get(id=pk)
# 	if request.method == 'POST':
# 		print('Recieving a post request')
# 		form = ReviewForm(request.POST)
# 		if form.is_valid():
# 			print("The form is valid")
# 			print(form.cleaned_data)
# 			movie.title = form.cleaned_data['title']
# 			author = form.cleaned_data['author']
# 			details = form.cleaned_data['details']
# 			Review.objects.create(
# 				title=movie.title,
# 				author=author,
# 				details=details
# 			)
# 		return redirect("/movies")	
# 	context = {
# 		"movie": movie,
# 		"form": ReviewForm()
# 	}
# 	return render(request, "movies/review_create.html", context)

# ----

# class ReviewDetailView(generic.DetailView):
# 	template_name = "movies/movie_detail.html"
# 	queryset = Review.objects.all()
# 	context_object_name = "reviews"

# # class CommentDetailView(generic.DetailView):
# # 	template_name = "movies/movie_detail.html"
# # 	queryset = Comment.objects.all()
# # 	context_object_name = "comments"

# def comment_list(request):
# 	comments = Comment.objects.all()
# 	context = {
#         "comments": comments
#     }
# 	return render(request, "movies/movie_detail.html", context)
