
class Render_manager:

    def __init__(self, game):
        self.game = game

    def render(self):
        render_data = self.game.level_manager.active_level
        background = render_data.background
        self.game.__SURFACE__.blit(background.texture.get_texture(), (0, 0))
        sorted_layers = sorted(render_data.loaded_objects.keys())
        for i in sorted_layers:
            for j in render_data.loaded_objects[i]:
                j.draw(self.game)
