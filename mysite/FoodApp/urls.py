from . import views
from django.urls import path

app_name = 'FoodApp'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    # add item
    path('add/', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:id>', views.update_item, name='update_item'),
    #delete item
    path('delete/<int:id>', views.delete_item, name = 'delete_item'),
    path('contactus/',views.PostContactInfoView.as_view(),name='contact_us'),
    path('thankyou/',views.thanks_page,name='thanks_page'),
]
