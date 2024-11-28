import pygame

# Load an image from file and return it
def load_image(image_path, scale_width=None, scale_height=None):
    """Load an image from the given path and optionally scale it."""
    image = pygame.image.load(image_path)
    if scale_width and scale_height:
        image = pygame.transform.scale(image, (scale_width, scale_height))
    return image

# Load a sound from file and return it
def load_sound(sound_path):
    """Load a sound file."""
    return pygame.mixer.Sound(sound_path)

# Draw a button with text
def draw_button(screen, x, y, width, height, color, text, font, text_color):
    """Draw a button on the screen."""
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

# Display a temporary message in the game window
def display_message(screen, message, font, color, x, y):
    """Display a temporary message on the screen."""
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

# Check if mouse click is inside a button
def is_button_clicked(mouse_pos, button_rect):
    """Check if the mouse click is inside a button rectangle."""
    x, y = mouse_pos
    button_x, button_y, button_width, button_height = button_rect
    return button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height
