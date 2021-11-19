from random import randint, choice
from gameobject import GameObject

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500:
      self.reset()

  def reset(self):
    self.x = randint(50, 300)
    self.y = -64