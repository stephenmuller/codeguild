"""sub_todo Views."""

from . import logic
from django.shortcuts import render

def render_todo_list(request):
    main_task = logic.get_all_main_tasks()
    template_data = {
        'main_item': main_task,
    }
    render(request, 'sub_todo/todo_list.html', template_data)

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
#
# def render_playlist(request, playlist_id):
#     playlist = logic.get_playlist_by_id(playlist_id)
#     songs = logic.get_all_songs_for_playlist(playlist)
#
#     template_args = {
#         'playlist': playlist,
#         'songs': songs,
#     }
#     return render(request, 'playlists/playlist.html', template_args)
# / shows the todo list.
# /add shows a form to add to the list.
# /submit is POSTed a new main item, and shows the ack page.
# /MAIN_ITEM_ID/add shows the form for adding a new sub-item to that main item.
# /MAIN_ITEM_ID/submit is POSTed a new sub-item, and shows the ack page.
# /MAIN_ITEM_ID/SUB_ITEM_ID/delete when GET, will delete that sub-item and possibly the main item if empty.