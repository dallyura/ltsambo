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


def home(request):
    return render(request,"home.html", {})

def video(request):
    obj=Item.objects.all()
    return render(request,'about.html',{'obj':obj})

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
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board_n101 = Board_N101(Site=Site, Operator=Operator, Panel_No=Panel_No, Activity=Activity,  Bite=Bite, Depth=Depth, Geo_Type=Geo_Type, Tooth_Qty=Tooth_Qty, Memo=Memo)
        board_n101.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n101.html')


def Site_N101_delete(request, id):
    board_n101 = Board_N101.objects.get(id=id)
    board_n101.delete()
    return redirect("/N101")


def N101_Info(request):
    return render(request, "N101_info.html", {})



def Site_N102(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'N102.html', boards)

def Post_N102(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board = Board(Site=Site, Operator=Operator, Panel_No=Panel_No,  Activity=Activity, Bite=Bite, Depth=Depth, Geo_Type=Geo_Type, Tooth_Qty=Tooth_Qty, Memo=Memo)
        board.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n102.html')


def Site_N102_delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect("/N102")


def Site_N103(request):
    boards_n103 = {'boards_n103': Board_N103.objects.all()}
    return render(request, 'N103.html', boards_n103)


def Post_N103(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board_n103 = Board_N103(Site=Site, Operator=Operator, Panel_No=Panel_No,  Activity=Activity, Bite=Bite, Depth=Depth, Geo_Type=Geo_Type, Tooth_Qty=Tooth_Qty, Memo=Memo)
        board_n103.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n103.html')

def Site_N103_delete(request, id):
    board_n103 = Board_N103.objects.get(id=id)
    board_n103.delete()
    return redirect("/N103")

def Site_N106(request):
    boards_n106 = {'boards_n106': Board_N106.objects.all()}
    return render(request, 'N106.html', boards_n106)


def Post_N106(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board_n106 = Board_N106(Site=Site, Operator=Operator, Panel_No=Panel_No,  Activity=Activity,  Bite=Bite, Depth=Depth, Geo_Type=Geo_Type,Tooth_Qty=Tooth_Qty,  Memo=Memo)
        board_n106.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n106.html')


def Site_N106_delete(request, id):
    board_n106 = Board_N106.objects.get(id=id)
    board_n106.delete()
    return redirect("/N106")

def Site_N109(request):
    boards_n109 = {'boards_n109': Board_N109.objects.all()}
    return render(request, 'N109.html', boards_n109)


def Post_N109(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board_n109 = Board_N109(Site=Site, Operator=Operator, Panel_No=Panel_No, Activity=Activity,  Bite=Bite, Depth=Depth, Geo_Type=Geo_Type,Tooth_Qty=Tooth_Qty,  Memo=Memo)
        board_n109.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_n109.html')


def Site_N109_delete(request, id):
    board_n109 = Board_N109.objects.get(id=id)
    board_n109.delete()
    return redirect("/N109")


def Site_T316(request):
    boards_t316 = {'boards_t316': Board_T316.objects.all()}
    return render(request, 'T316.html', boards_t316)


def Post_T316(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board_t316 = Board_T316(Site=Site, Operator=Operator, Panel_No=Panel_No, Activity=Activity,  Bite=Bite, Depth=Depth, Geo_Type=Geo_Type, Tooth_Qty=Tooth_Qty, Memo=Memo)
        board_t316.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_t316.html')


def Site_T316_delete(request, id):
    board_t316 = Board_T316.objects.get(id=id)
    board_t316.delete()
    return redirect("/T316")

def Site_Labrador_BC1(request):
    boards_labrador_BC1 = {'boards_labrador_BC1': Board_Labrador_BC1.objects.all()}
    return render(request, 'Labrador_BC1.html', boards_labrador_BC1)


def Post_Labrador_BC1(request):
    if request.method == "POST":
        Site = request.POST['Site']
        Operator = request.POST['Operator']
        Panel_No = request.POST['Panel_No']
        Activity = request.POST['Activity']
        Bite = request.POST['Bite']
        Depth = request.POST['Depth']
        Geo_Type = request.POST['Geo_Type']
        Tooth_Qty = request.POST['Tooth_Qty']
        Memo = request.POST['Memo']

        board_labrador_BC1 = Board_Labrador_BC1(Site=Site, Operator=Operator, Panel_No=Panel_No, Activity=Activity,  Bite=Bite, Depth=Depth, Geo_Type=Geo_Type, Tooth_Qty=Tooth_Qty, Memo=Memo)
        board_labrador_BC1.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post_labrador_BC1.html')


def Site_Labrador_BC1_delete(request, id):
    board_labrador_BC1 = Board_Labrador_BC1.objects.get(id=id)
    board_labrador_BC1.delete()
    return redirect("/Labrador_BC1")




# def Site_N106(request):
#     return render(request, "N106.html", {})
#
#
# def Site_N109(request):
#     return render(request, "N109.html", {})
#


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
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity',  'Bite', 'Depth', 'Geo_Type', 'Tooth_Qty',  'Memo'])

    for board_n101 in Board_N101.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth', 'Geo_Type','Tooth_Qty', 'Memo'):
        writer.writerow(board_n101)

    response['Content-Disposition'] = 'attachment; filename="CSV_N101.csv"'

    return response


def export_N102_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type', 'Tooth_Qty','Memo'])

    for board in Board.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth', 'Geo_Type','Tooth_Qty','Memo'):
        writer.writerow(board)

    response['Content-Disposition'] = 'attachment; filename="CSV_N102.csv"'

    return response

def export_N103_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity', 'Bite', 'Depth', 'Geo_Type','Tooth_Qty','Memo'])

    for board_n103 in Board_N103.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type', 'Tooth_Qty','Memo'):
        writer.writerow(board_n103)

    response['Content-Disposition'] = 'attachment; filename="CSV_N103.csv"'

    return response

def export_N106_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type', 'Tooth_Qty','Memo'])

    for board_n106 in Board_N106.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type','Tooth_Qty', 'Memo'):
        writer.writerow(board_n106)

    response['Content-Disposition'] = 'attachment; filename="CSV_N106.csv"'

    return response

def export_N109_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity',  'Bite', 'Depth', 'Geo_Type','Tooth_Qty','Memo'])

    for board_n109 in Board_N109.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type', 'Tooth_Qty','Memo'):
        writer.writerow(board_n109)

    response['Content-Disposition'] = 'attachment; filename="CSV_N109.csv"'

    return response


def export_T316_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity', 'Bite', 'Depth', 'Geo_Type','Tooth_Qty','Memo'])

    for board_t316 in Board_T316.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type', 'Tooth_Qty','Memo'):
        writer.writerow(board_t316)

    response['Content-Disposition'] = 'attachment; filename="CSV_T316.csv"'

    return response

def export_Labrador_BC1_csv(request):

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Site','Time', 'Operator',  'Panel_No', 'Activity', 'Bite', 'Depth', 'Geo_Type','Tooth_Qty','Memo'])

    for board_labrador_BC1 in Board_Labrador_BC1.objects.all().values_list('Site','created_date', 'Operator', 'Panel_No', 'Activity', 'Bite', 'Depth','Geo_Type', 'Tooth_Qty','Memo'):
        writer.writerow(board_labrador_BC1)

    response['Content-Disposition'] = 'attachment; filename="CSV_Labrador_BC1.csv"'

    return response

