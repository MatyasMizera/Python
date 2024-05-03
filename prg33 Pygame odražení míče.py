import pygame

bila = (255, 255, 255)
cerna = (0, 0, 0)
cervena = (255, 0, 0)

sirka = 800
vyska = 600
okno = pygame.display.set_mode((sirka, vyska))
pygame.display.set_caption("Odrážející se míč")

polomer = 20
x = sirka // 2
y = vyska // 2
dx = 1  # Nastavitelná rychlost vodorovně
dy = 1  # Nastavitelná rychlost svisle

bezi = True
while bezi:
  for udalost in pygame.event.get():
    if udalost.type == pygame.QUIT:
      bezi = False

  okno.fill(cerna)

  pygame.draw.circle(okno, cervena, (x, y), polomer)

  if x + polomer >= sirka or x - polomer <= 0:
    dx *= -1
  if y + polomer >= vyska or y - polomer <= 0:
    dy *= -1

  x += dx
  y += dy

  pygame.display.flip()

pygame.quit()
