import pygame
from random import randint, choice
from gameobject import GameObject
from board import speed_increase_value, lanes

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500:
      self.reset()

  def reset(self):
    self.x = -64
    self.y = choice(lanes)


  def increase_speed(self):
    self.dx += speed_increase_value

