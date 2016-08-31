"""sub_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_todo_list, name='todo_list'),
    url(r'^add', views.render_add, name='add'),
    url(r'^submit', views.render_submit_new_main, name='submit_new_main'),
    url(r'^(?P<main_item_id>.+)/add', views.render_add_item_to_main_item, name='add_item_to_main_item'),
    url(r'^(?P<main_item_id>.+)/submit', views.render_ack_sub_item_submit, name='ack_sub_item_submit'),
    url(r'^(?P<main_item_id>.+)/(?P<sub_item_id>.+)/delete', views.render_sub_item_delete, name='sub_item_delete')
]




# / shows the todo list.
# /add shows a form to add to the list.
# /submit is POSTed a new main item, and shows the ack page.
# /MAIN_ITEM_ID/add shows the form for adding a new sub-item to that main item.
# /MAIN_ITEM_ID/submit is POSTed a new sub-item, and shows the ack page.
# /MAIN_ITEM_ID/SUB_ITEM_ID/delete when GET, will delete that sub-item and possibly the main item if empty.
