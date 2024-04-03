import pygame


pygame.init()


width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Barák")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 100, 200), (100, 200, 600, 300))
    pygame.draw.polygon(window, (200, 0, 200), [(100, 200), (700, 200), (400, 100)])
    pygame.draw.rect(window, (0, 200, 200), (200, 250, 100, 50))
    pygame.draw.rect(window, (0, 200, 200), (200, 350, 100, 50))
    pygame.draw.rect(window, (0, 200, 200), (500, 250, 100, 50))
    pygame.draw.rect(window, (0, 200, 200), (500, 350, 100, 50))
    pygame.draw.rect(window, (200, 200, 200), (350, 350, 100, 150))
    pygame.draw.circle(window, (0, 0, 0), (360, 430), 8)
    pygame.draw.rect(window, (50, 50, 50), (250, 100, 30, 100))
    
    pygame.display.update()

pygame.quit()