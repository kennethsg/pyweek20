from cocos.director import director
import scene1
from pyglet.window import key
import player_controller
import sprite1

def main():
    global keyboard
    director.init()
    the_scene = scene1.Scene1()
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)
    director.run(the_scene)
    
if __name__ == '__main__':
    main()