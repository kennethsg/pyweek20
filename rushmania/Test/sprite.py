import cocos

class sprite(cocos.sprite.Sprite):
    #def __init__(self, image, position = (...), rotation = 0, scale = 1, opacity = 255, color = (...), anchor = None):
     #   return super(sprite, self).__init__(image, position, rotation, scale, opacity, color, anchor)

     def __init__(self, image, position = (...), rotation = 0, scale = 1, opacity = 255, color = (...), anchor = None):
        super(sprite, self).__init__()