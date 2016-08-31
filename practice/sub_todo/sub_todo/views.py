"""sub_todo Views."""


def render_add(request):
    pass


def render_submit_new_main(request):
    pass


def render_add_item_to_main(request):
    pass


def render_ack_sub_item_submit(request):
    pass


def render_sub_item_delete(request):
    pass


def render_add_item_to_main_item(request):
    pass


# / shows the todo list.
# /add shows a form to add to the list.
# /submit is POSTed a new main item, and shows the ack page.
# /MAIN_ITEM_ID/add shows the form for adding a new sub-item to that main item.
# /MAIN_ITEM_ID/submit is POSTed a new sub-item, and shows the ack page.
# /MAIN_ITEM_ID/SUB_ITEM_ID/delete when GET, will delete that sub-item and possibly the main item if empty.