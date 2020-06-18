
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

"""
router=DefaultRouter() 
router.register('userdetail',views.UserDetailViewSet,basename='userdetail')


detail_list_view=views.UserDetailViewSet.as_view(
    {'get':'list'}
)
"""
urlpatterns = [
    #path('',include(router.urls)),
    path('',views.profile,name='profile'),
    #path('',detail_list_view),
    path('user_detail/<int:pk>/',views.user_detail,name='user_detail'),
    path('favourite/',views.favourite,name='favourite')
    #path('userdetail/',views.userdetail,name='userdetail'),
]
