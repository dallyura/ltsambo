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
    path('N101/',views.Site_N101, name='N101'),
    path('post_n101/', views.Post_N101, name='post_n101'),
    path('delete/<int:id>', views.Site_N101_delete),
    path('edit/<int:id>', views.Site_N101_edit),
    path('N102/',views.Site_N102, name='N102'),
    path('post_n102/', views.Post_N102, name='post_n102'),
    path('delete_N102/<int:id>', views.Site_N102_delete),
    path('N103/',views.Site_N103, name='N103'),
    path('N106/',views.Site_N106, name='N106'),
    path('N109/',views.Site_N109, name='N109'),
    path('export_csv', views.export_csv, name='export-csv'),
    path('export_N102_csv', views.export_N102_csv, name='export-n102-csv'),


]

