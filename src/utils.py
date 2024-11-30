import pygame

def load_image(image_path, scale_width=None, scale_height=None):
    image = pygame.image.load(image_path)
    if scale_width and scale_height:
        image = pygame.transform.scale(image, (scale_width, scale_height))
    return image

def load_sound(sound_path):
    return pygame.mixer.Sound(sound_path)

def draw_button(screen, x, y, width, height, color, text, font, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

def display_message(screen, message, font, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

def is_button_clicked(mouse_pos, button_rect):
    x, y = mouse_pos
    button_x, button_y, button_width, button_height = button_rect
    return button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height
