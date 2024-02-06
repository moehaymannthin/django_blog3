from django.urls import path
from my_blog.views import *

urlpatterns = [
    path('list/', postlist, name="postlist"),
    path('create/', postcreate, name="postcreate"),
    path('detail/<int:p_id>/', postdetail, name="postdetail"),
    path('delete/<int:p_id>/', postdelete, name="postdelete"),
    path('update/<int:p_id>/', postupdate, name="postupdate"),
    path('cmt/delete/<int:p_id>/<int:c_id>/', cmtdelete, name="cmtdelete"),
    path('cmt/update/<int:p_id>/<int:c_id>/', cmtupdate, name="cmtupdate")
]