from cocos.director import director
import scene1
from test.global_variables import keyboard

def main():
    director.init()
    the_scene = scene1.Scene1()
    director.window.push_handlers(keyboard)
    director.run(the_scene)
    
if __name__ == '__main__':
    main()