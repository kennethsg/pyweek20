import cocos
import sprite1



class Layer1 (cocos.layer.Layer):
    
    is_event_handler = True

    def __init__(self):
        super(Layer1, self).__init__()
        the_sprite = sprite1.Sprite1()
        self.add(the_sprite, z = 1)
        
