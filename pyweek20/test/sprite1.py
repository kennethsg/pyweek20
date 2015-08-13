import cocos
import player_controller

class Sprite1(cocos.sprite.Sprite):
    def __init__(self):
        super(Sprite1, self).__init__('rectangle_blue.png')
        self.position = (0, 100)
        self.scale = 0.5
        self.velocity = (0, 0)
        self.do(player_controller.PlayerController())        