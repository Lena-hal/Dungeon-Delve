# TODO
## GUI manager
add gui manager that handeles events of gui elements and renders them.
every event is sent to gui manager and he will resend those events to the coresponding gui elements. those elements will update their state based on these events. this event handeling will be called before every frame render.

game_class has:
gui_list = []
gui_render_list = []

gui_manager.update() -> this should update the states of ui -> SCRAPPED
gui_manager.process_events(event) -> this gets 1 event and the gui should get updated based on that update.
- this function is in the process of being added but i got stuck at processing events at singular menus because i don't have internet acess and i cant look on existing events to use 

