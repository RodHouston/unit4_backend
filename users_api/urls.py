from django.urls import path
from . import views

urlpatterns = [
    path('api/users', views.UserList.as_view(), name='user_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/homes', views.HomeList.as_view(), name='home_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/homes/<int:pk>', views.HomeDetail.as_view(), name='home_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/photos', views.PhotoList.as_view(), name='photo_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
