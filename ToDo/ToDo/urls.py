
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from tasks.views import signup, login_view, main_page

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('api/', include(router.urls)),
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='main_page'),
    path('main/', main_page, name='main_page'),
]
