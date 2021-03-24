def linearSearch(x, y, list_i):
    i = ARRAY[list_i]
    num = 23
    box = pygame.Rect(x + (BOX_SIZE+5)*(list_i+1), y, (BOX_SIZE+5), BOX_SIZE)
    color = GREEN if i == num else RED
    pygame.draw.rect(SCREEN, color, box, 1)
