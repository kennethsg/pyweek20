import cocos
import layer1

class Scene1(cocos.scene.Scene):
    def __init__(self):
        super(Scene1, self).__init__()    
        the_layer = layer1.Layer1()
        self.add(the_layer)