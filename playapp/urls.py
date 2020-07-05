from .views import PlayView, PlayViewList, PlayViewDelete, PlayViewUpdate
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('create/', PlayView.as_view(), name="create"),
    path('list/', PlayViewList.as_view(), name="list"),
    path('delete/<int:pk>', PlayViewDelete.as_view(), name="delete"),
    path('update/<int:pk>', PlayViewUpdate.as_view(), name="update"),
]