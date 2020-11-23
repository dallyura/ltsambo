from django.urls import path
from . import views
from .views  import HomeView, PanelDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView,CategoryListView


urlpatterns = [

    # path('',views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('tel307/<int:pk>', PanelDetailView.as_view(), name='panel_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('tel307/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('tel307/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('change_password/',views.change_password, name='change_password'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('N101/',AddPostView.as_view(), name='N101'),
    path('N102/',views.Site_N102, name='N102'),
    path('N103/',views.Site_N103, name='N103'),
    path('N106/',views.Site_N106, name='N106'),
    path('N109/',views.Site_N109, name='N109'),


    # path('', CSVFileView, name='export_csv'),

]

