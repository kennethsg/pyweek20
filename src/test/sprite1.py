import cocos
#import pyglet.window.key.KeyStateHandler
from pyglet.window import key
import player_controller

class Sprite1(cocos.sprite.Sprite):
    #def __init__(self, image, position = (...), rotation = 0, scale = 1, opacity = 255, color = (...), anchor = None):
        #return super(sprite, self).__init__(image, position, rotation, scale, opacity, color, anchor)

    #===========================================================================
    # def __init__(self):
    #     super(Sprite, self).__init__('rectangle_blue.png', position = (0,100), scale = 0.5, anchor = 1)
    #===========================================================================

    def __init__(self):
        super(Sprite1, self).__init__('rectangle_blue.png')

        self.position = (0, 100)
        self.scale = 0.5
        
        
        #the_player_controller = player_controller.PlayerController()
        #self.do(the_player_controller)
        
        self.key_handler = key.KeyStateHandler()

        