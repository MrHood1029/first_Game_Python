import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Уклоняйся от метеоров")

# Игрок
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 10

# Метеоры
meteors = []
meteor_speed = 4
score = 0
level = 1


def spawn_meteor():
    x = random.randint(0, SCREEN_WIDTH - 50)
    meteor_type = random.choice(['normal', 'fast', 'slow'])
    meteors.append([x, 0, meteor_type])


def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, PLAYER_WIDTH, PLAYER_HEIGHT))


def draw_meteors():
    for meteor in meteors:
        color = WHITE if meteor[2] == 'normal' else RED if meteor[2] == 'fast' else BLUE
        pygame.draw.rect(screen, color, (meteor[0], meteor[1], 50, 50))


def move_meteors():
    global score
    for meteor in meteors:
        if meteor[2] == 'normal':
            meteor[1] += meteor_speed
        elif meteor[2] == 'fast':
            meteor[1] += meteor_speed + 1
        else:  # slow
            meteor[1] += meteor_speed - 1

        # Увеличение очков за прохождение метеора
        if meteor[1] > SCREEN_HEIGHT:
            score += 1
            meteors.remove(meteor)

def adjust_difficulty():
    global meteor_speed
    meteor_speed += 1  # Увеличиваем скорость метеоров


def check_collision():
    for meteor in meteors:
        if meteor[1] < player_y + PLAYER_HEIGHT and meteor[1] + 50 > player_y and meteor[
            0] < player_x + PLAYER_WIDTH and meteor[0] + 50 > player_x:
            return True
    return False


# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y += player_speed

    if random.randint(1, 30) == 1:
        spawn_meteor()

    move_meteors()

    if check_collision():
        print(f"Игре конец(! Ваши счёт: {score}")
        running = False

    screen.fill((0, 0, 0))
    draw_player(player_x, player_y)
    draw_meteors()

    # Отображение счета и уровня
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Очки: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()