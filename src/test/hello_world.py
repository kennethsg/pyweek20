import cocos
from cocos.actions import *
import pyglet
from pyglet.window import key
from pyglet.window.key import KeyStateHandler

class HelloWorld(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super( HelloWorld, self ).__init__()

        self.sprite = cocos.sprite.Sprite('rectangle_blue.png')

        '''
        label = cocos.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=32,
                          anchor_x='center', anchor_y='center')

        label.position = 320,240

        self.add( label )
        '''

        # similar to cocos.text.Label, a cocos.sprite.Sprite
        # is a subclass of pyglet.sprite.Sprite with the befits of
        # being a CocosNode.
        #sprite = cocos.sprite.Sprite('rectangle_blue.png')

        # sprite in the center of the screen (default is 0,0)
        self.sprite.position = 0, 100

        # sprite scale attribute starts with 3 (default 1 )
        self.sprite.scale = 0.5

        # add the sprite as a child, but with z=1 (default is z=0).
        # this means that the sprite will be drawn on top of the label
        self.add(self.sprite, z=1)

        #key_display = KeyDisplay()
        #keys_pressed = KeyDisplay.init()
        # Move a sprite 50 pixels to the right, and 100 pixel to the top in 2 seconds.
        #sprite.do( MoveBy( (500,0), duration=2 ) )

        
        #print(self.update_keys())    
        
        #self.key_handler = key.KeyStateHandler()
        
       # if self.key_handler[key.RIGHT]:   
       #     print ('RIGHT')
       
        

    '''
    def update_position(self):
        #print(self.update_keys()) 
        print("'RIGHT'" in self.keys_pressed)
        for i in self.keys_pressed:
            if i is 'RIGHT':
                self.sprite.do( MoveBy( (500,0), duration=2 ) )
    '''


    def on_key_press(self, k, modifiers):
        #This function is called when a key is pressed.
        
        #self.keys_pressed.add(key)
        #self.update_text()
        #self.update_position()
        if k == key.RIGHT:
            print ('RIGHT')
            self.sprite.do( MoveBy( (500,0), duration=2 ) )
        #self.sprite.do( MoveBy( (500,0), duration=2 ) )
    
    '''
    def on_key_release(self, key, modifiers):
        """This function is called when a key is released.
        
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)

        Constants are the ones from pyglet.window.key

        Sometimes a key release can arrive without a previous 'press' event, so discard
        is used instead of remove.

        This can happen in Windows by example when you 'press ALT, release ALT, press B,
        release B'; the events received are 'pressed ALT, released ALT, released B'.

        This may depend on the pyglet version, here pyglet from repo at may 2014 was used.
        """
        #self.keys_pressed.discard(key)
        #self.update_text()
        #self.update_position()
    '''

    '''
    def update_keys(self):
        key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        return key_names
    '''



if __name__ == "__main__":

    cocos.director.director.init()

    hello_layer = HelloWorld()

    #events_layer = KeyDisplay()

    main_scene = cocos.scene.Scene (hello_layer)

    cocos.director.director.run (main_scene)