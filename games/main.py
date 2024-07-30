import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self,image,x,y,spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)

        self.rect = self.image.get_rect()
        self.rect,x, self.rect,y

    def draw(self, surface):
        surface.blit(self.image,(self.rect.x, self.rect.y))

class TileMap():
    def __init__(self,filename, spritesheet):
    self.tile_size = 32
    self.start_x, self.star_y - 0, 0

