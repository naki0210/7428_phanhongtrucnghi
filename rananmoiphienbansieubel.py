import pygame
import random
import os

# Cài đặt
WIDTH, HEIGHT = 900, 600
PLAYER_INIT_RADIUS = 25
FOOD_RADIUS = 8
FOOD_COUNT = 25
PLAYER_SPEED = 2.5

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chấm tròn ăn mồi - Mini Agar.io")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)

# Skin: "dot" hoặc "crocodile"
SKINS = ["dot", "crocodile"]
current_skin = 0

# Load ảnh cá sấu (đổi tên file nếu cần)
if os.path.exists("crocodile.png"):
    crocodile_img = pygame.image.load("crocodile.png")
    crocodile_img = pygame.transform.scale(crocodile_img, (PLAYER_INIT_RADIUS*2, PLAYER_INIT_RADIUS*2))
else:
    crocodile_img = None

def random_color():
    colors = [(30,214,251),(255,31,143),(243,233,20),(255,171,0),(21,245,135),(74,60,255),(255,63,52)]
    return random.choice(colors)

def spawn_food():
    return [
        {
            "x": random.randint(FOOD_RADIUS, WIDTH-FOOD_RADIUS),
            "y": random.randint(FOOD_RADIUS, HEIGHT-FOOD_RADIUS),
            "color": random_color()
        }
        for _ in range(FOOD_COUNT)
    ]

# Khởi tạo người chơi và mồi
player = {"x": WIDTH//2, "y": HEIGHT//2, "r": PLAYER_INIT_RADIUS, "color": (58,217,58)}
foods = spawn_food()

def draw_player():
    if SKINS[current_skin] == "dot":
        pygame.draw.circle(screen, player["color"], (int(player["x"]), int(player["y"])), int(player["r"]))
        pygame.draw.circle(screen, (255,230,0), (int(player["x"]), int(player["y"])), int(player["r"]), 3)
        label = font.render("naki", True, (255,255,255))
        screen.blit(label, (player["x"]-label.get_width()//2, player["y"]-label.get_height()//2))
    elif SKINS[current_skin] == "crocodile" and crocodile_img:
        scale = int(player["r"]*2)
        img = pygame.transform.scale(crocodile_img, (scale, scale))
        screen.blit(img, (player["x"]-player["r"], player["y"]-player["r"]))
    else:
        pygame.draw.circle(screen, player["color"], (int(player["x"]), int(player["y"])), int(player["r"]))

def draw_foods():
    for f in foods:
        pygame.draw.circle(screen, f["color"], (f["x"], f["y"]), FOOD_RADIUS)

def eat_food():
    global foods
    new_foods = []
    for f in foods:
        dx = f["x"] - player["x"]
        dy = f["y"] - player["y
