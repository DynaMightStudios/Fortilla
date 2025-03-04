from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from fort import Fort

app = Ursina()


# Initialize FirstPersonController
player = FirstPersonController()
player.speed = 15
player.jump_height = 4
player.height = 10

crouching = False
sprinting = False


def update():
    global crouching, sprinting
    print(held_keys['c'])
    if held_keys['c'] == 1:
        player.speed = 8.9
        crouching = True
    else:
        player.speed = 15
        crouching = False

plane = Entity(model='plane', texture='beach', scale=180, rotation = 0.2, collider='box')

Fort_ = Fort
Fort_.create()

Sky(texture='Skyy')

  
app.run()
