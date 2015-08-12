import cocos
from cocos.director import director
import layer1

class Scene(cocos.scene.Scene):
    def __init__(self):
        super(Scene, self).__init__()    
        #the_layer = layer1.Layer1()
        #self.add(the_layer)

if __name__ == "__main__":
    director.init()
    the_scene = Scene()
    the_layer = layer1.Layer1()
    the_scene.add(the_layer)
    #director.push(the_scene)
    director.run(the_scene)