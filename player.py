from gameobject import GameObject


#
class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/player.png')
    self.dx = 0
    self.dy = 0
    self.reset()
  
  def left(self):
    self.dx -= 100
  
  def right(self):
    self.dx += 100

  def up(self):
    self.dy -= 100

  def down(self):
    self.dy += 100

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32