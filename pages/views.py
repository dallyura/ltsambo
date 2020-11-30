from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
import csv
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
import datetime


# def home(request):
#     return render(request,"home.html", {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cats_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})


class PanelDetailView(DetailView):
    model = Post
    template_name = 'panel_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PanelDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['Panel_name','Operator_name','Depth']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def about(request):
    return render(request, "about.html", {})

def Site_N101(request):
    boards_n101 = {'boards_n101': Board_N101.objects.all()}
    return render(request, 'N101.html', boards_n101)


def Post_N101(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Memo = request.POST['Memo']

        board_n101 = Board_N101(Site=Site, Operator=Operator, Panel_No=Panel_No, Bite=Bite, Depth=Depth, Memo=Memo)
        board_n101.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n101.html')

def Site_N102(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'N102.html', boards)

def Post_N102(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Memo = request.POST['Memo']

        board = Board(Site=Site, Operator=Operator, Panel_No=Panel_No, Bite=Bite, Depth=Depth, Memo=Memo)
        board.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n102.html')


def Site_N103(request):
    return render(request, "N103.html", {})


def Site_N106(request):
    return render(request, "N106.html", {})


def Site_N109(request):
    return render(request, "N109.html", {})



def contact(request):
    return render(request, "contact.html", {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In !'))
            return redirect('home')

        else:
            messages.success(request, ('Error Logging In - Please Try Again...'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out ! '))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Registered ...'))
            return redirect('home')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profile ...'))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}

    return render(request, 'edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You Have Edited Your Password ...'))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'change_password.html', context)




def export_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Bite', 'Depth', 'Memo'])

    for board_n101 in Board_N101.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Bite', 'Depth', 'Memo'):
        writer.writerow(board_n101)

    response['Content-Disposition'] = 'attachment; filename="CSV_N101.csv"'

    return response


def export_N102_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Bite', 'Depth', 'Memo'])

    for board in Board.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Bite', 'Depth', 'Memo'):
        writer.writerow(board)

    response['Content-Disposition'] = 'attachment; filename="CSV_N102.csv"'

    return response




# class CSVFileView(HomeView):
#     def get(self, request, *args, **kwargs):
#         response = HttpResponse(content_type='text/csv')
#         cd = 'attachment; filename="{0}"' .format('report.csv')
#         request['Content-Disposition'] = cd
#
#         filenames = ('Panel_name', 'Site_name', 'Operator_name', 'Depth', 'post_date', 'category')
#         data = Post.objects.values(*filenames)
#         writer = csv.DictWriter(response, fieldnames=filenames)
#         writer.writeheader()
#
#         for row in data:
#             writer.writerow(row)
#
#         return response