# SHIP CLASS   #
import pygame
from pygame.sprite import Sprite
class Ship:
    def __init__(self):
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen = pygame.display.set_mode(500,600)
        self.rect.midbottom = self.screen_rect.midbottom
        self.lasers = pygame.sprite.Group()
        self.velocity=Vector(0,0)
        self.speed = 2
    def center_ship(self):
        return (self.rect.x/2, self.rect.y/2)
    def fire(self):
        self.lasers.add()
    def remove_lasers(self):
        self.lasers.remove()
    def move(self):
        key_up_down = [pygame.KEYDOWN, pygame.KEYUP]
        movement = {K_RIGHT : Vector(1, 0), K_LIFE : Vector(-1, 0), K_UP : Vector(0, -1), K_RIGHT : Vector(0, 1)}
        translate = {K_d:K_RIGHT, K_a:K_LEFT, K_w:K_UP, K_s:K_DOWN}
        for event in pygame.event.get():
            e_type = event.type
            if e_type in key_up_down:
                k = event.type
                if k in translate.keys() or k in translate.values():
                    if k in translate.keys():
                        k= translate[k]
                    self.velocity = self.speed * movement[k]

        self.rect.left+=self.velocity.x
        self.rect.top += self.velocity.y
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.move()
        self.draw()



#   vector  #

 class Vector:
     def __init__(self, x=0.0, y=0.0):
         self.x=x
         self.y=y
     def __repr__(self):
         return “Vector({}, {})”.format(self.x, self.y)
     def __add__(self, other):
         return Vector(self.x + other.x, self.y+other.y)
     def __sub__(self, other):
        return self.__add__(-1*other)
     def __rmul__(self, k: float): pass
        return  Vector(k * self.x,k*self.y)
     def __mul__(self, k: float): pass
        return __rmul__(k)
     def __truediv__(self, k: float): pass
        return self.__rmul__(1.0/k)
     def __neg__(self): pass
        self.x *= -1
        self.y *= -1
     def __eq__(self): pass
        return self.x == other.x and self.y == other.y


 @staticmethod
 def test():  # feel free to change the test code
     v = Vector(x=5, y=5)
     u = Vector(x=4, y=4)
     print(‘v is {}’.format(v))
     print(‘u is {}’.format(u))
     print(‘uplusv is {}’.format(u + v))
     print(‘uminusv is {}.format(u – v))
     print(‘ku is {}’.format(3 * u))
     print(‘-u is {}’.format(-1 * u))

     def main():
         Vector.test()