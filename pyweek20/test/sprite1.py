import cocos
#import pyglet.window.key.KeyStateHandler
from pyglet.window import key
from cocos import actions
import player_controller
from cocos.actions.move_actions import Move

class Sprite1(cocos.sprite.Sprite):
    def __init__(self):
        super(Sprite1, self).__init__('rectangle_blue.png')

        self.position = (0, 100)
        self.scale = 0.5
        
        self.velocity = (0, 0)
        #self.do(Move())
        
        the_player_controller = player_controller.PlayerController()
        self.do(the_player_controller)
        
        #self.key_handler = key.KeyStateHandler()

        