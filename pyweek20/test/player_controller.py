from cocos import actions
from pyglet.window import key

class PlayerController(actions.Move):
    def step(self, dt):
        super(PlayerController, self).step(dt)
        global keyboard
        keyboard = key.KeyStateHandler()
        # Determine velocity based on keyboard inputs.
        velocity_x = 100 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
        velocity_y = 100 * (keyboard[key.UP] - keyboard[key.DOWN])
    
        # Set the object's velocity.
        self.target.velocity = (velocity_x, velocity_y)
