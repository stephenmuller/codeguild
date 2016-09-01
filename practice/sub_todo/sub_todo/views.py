"""sub_todo Views."""

from . import logic
from django.shortcuts import render
from django.http import HttpResponse


def render_todo_list(request):
    tasks = logic.get_all_tasks()
    template_data = {
        'main_tasks': tasks,
    }
    return render(request, 'sub_todo/todo_list.html', template_data)


def render_add_main_item(request):
    """   ... """
    return render(request, 'sub_todo/add.html')

def render_ack_submit_new_main(request):
    new_task = request.POST['new_main_task']
    logic.create_new_main_item(new_task)
    return render(request, 'sub_todo/ack_new_main.html')


def render_add_sub_item(request, main_item_id):
    template_data = {
        'main_item_id': main_item_id
    }
    return render(request, 'sub_todo/add_sub_item.html', template_data)



def render_ack_sub_item_submit(request, main_item_id):
    new_task = request.POST['new_sub_task']
    logic.create_sub_task(new_task, logic.get_main_item_by_id(main_item_id))
    return render(request, 'sub_todo/ack_sub_item_submit.html')


def render_sub_item_delete(request, main_item_id, sub_item_id):
    logic.delete_sub_item(sub_item_id, main_item_id)
    return HttpResponse('Deleted subtask {}'.format(sub_item_id))


# /add shows a form to add to the list.
# /submit is POSTed a new main item, and shows the ack page.
# /MAIN_ITEM_ID/add shows the form for adding a new sub-item to that main item.
# /MAIN_ITEM_ID/submit is POSTed a new sub-item, and shows the ack page.
# /MAIN_ITEM_ID/SUB_ITEM_ID/delete when GET, will delete that sub-item and possibly the main item if empty.