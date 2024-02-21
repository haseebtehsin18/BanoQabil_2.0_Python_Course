import pygame
import sys
import os

class Button():
    def __init__(self, text, font, color, pos):
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.rect = self.font.render(text, True, color).get_rect(center=pos)

    def draw(self, screen):
        shadow_offset = (5, 5)  # Adjust the shadow offset
        shadow_color = (0, 0, 0, 150)  # Opacity: 57%

        # Render shadow
        shadow_surface = self.font.render(self.text, True, shadow_color)
        shadow_rect = shadow_surface.get_rect(center=(self.pos[0] + shadow_offset[0], self.pos[1] + shadow_offset[1]))
        screen.blit(shadow_surface, shadow_rect)

        # Render text without stroke
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.pos)
        screen.blit(text_surface, text_rect)

    def check_click(self, position):
        return self.rect.collidepoint(position)

def game_over_menu(screen, score):
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    SKY_BLUE = (135, 206, 235)  # Sky Blue color
    custom_font_game_over = pygame.font.Font(os.path.join("assets", "font.ttf"), 100)  # Double the size for "Game Over"
    custom_font_others = pygame.font.Font(os.path.join("assets", "font.ttf"), 40)  # Smaller size for other text
    main_menu_button = Button("Main Menu", custom_font_others, GREEN, (400, 450))
    restart_button = Button("Restart", custom_font_others, GREEN, (400, 350))
    score_button = Button(f"Your Score: {score}", custom_font_others, SKY_BLUE, (400, 300))  # Changed color to sky blue
    background = pygame.transform.scale(pygame.image.load("assets/Gobackground.png").convert(), (800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.check_click(pygame.mouse.get_pos()):
                    return False
                if restart_button.check_click(pygame.mouse.get_pos()):
                    return True
        
        screen.blit(background, (0, 0))
        draw_text(screen, "Game Over", custom_font_game_over, RED, (400, 150))
        score_button.draw(screen)
        main_menu_button.draw(screen)
        restart_button.draw(screen)
        pygame.display.update()

def draw_text(screen, text, font, color, pos):
    shadow_offset = (5, 5)  # Adjust the shadow offset
    shadow_color = (255, 255, 255, 150)  # White with 57% opacity

    # Render shadow
    shadow_surface = font.render(text, True, shadow_color)
    shadow_rect = shadow_surface.get_rect(center=(pos[0] + shadow_offset[0], pos[1] + shadow_offset[1]))
    screen.blit(shadow_surface, shadow_rect)

    # Render text
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)

def main_menu(screen):
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake Game - Game Over Menu")
    score = 0
    while True:
        if not game_over_menu(screen, score):
            main_menu(screen)

if __name__ == "__main__":
    main()
