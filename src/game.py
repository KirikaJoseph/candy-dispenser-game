import random
import pygame
import sys
from stack import Stack
from utils import load_image, load_sound, draw_button, display_message, is_button_clicked

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
BUTTON_HOVER = (0, 100, 255)



# Fonts and Sounds
FONT = pygame.font.Font(None, 36)
PUSH_SOUND = None
POP_SOUND = None
ERROR_SOUND = None
BUTTON_CLICK_SOUND = None

#background images
backgrounds = [
    {"name": "Back2", "image": "back2.jpg"},
    {"name": "Back4", "image": "back4.jpg"},
    {"name": "Back5", "image": "back5.jpg"},
    {"name": "Back6", "image": "back6.jpg"}
]

#Candies

candies = [
    {"name": "Red", "image": "candy.png"},
    {"name": "Purple", "image": "candy2.png"},
    {"name": "Light Blue", "image": "candy3.png"},
    {"name": "Green", "image": "candy4.png"},
    {"name": "Light Blue", "image": "candy5.png"},
    {"name": "Yellow", "image": "candy6.png"},
    {"name": "Orange", "image": "candy7.png"},
    {"name": "Red", "image": "candy8.png"}
]


# Initialize the stack
STACK_MAX_SIZE = 8
candy_stack = Stack(max_size=STACK_MAX_SIZE)

# Load assets
dispenser_image = None
spring_image = None
candy_image = None
background_image = None


def load_assets():
    global PUSH_SOUND, POP_SOUND, ERROR_SOUND, BUTTON_CLICK_SOUND
    global dispenser_image, spring_image, candy_images, background_image, background_images, current_background
    
    # Load sounds
    PUSH_SOUND = pygame.mixer.Sound("../assets/sounds/push.wav")
    POP_SOUND = pygame.mixer.Sound("../assets/sounds/pop.wav")
    ERROR_SOUND = pygame.mixer.Sound("../assets/sounds/error.wav")
    BUTTON_CLICK_SOUND = pygame.mixer.Sound("../assets/sounds/button_click2.wav")  # Load button click sound
    
    # Load images
    dispenser_image = pygame.image.load("../assets/images/dispenser.png")
    spring_image = pygame.image.load("../assets/images/spring.png")
    # candy_image = pygame.image.load("../assets/images/candy.png")
    # background_image = pygame.image.load("../assets/images/back2.jpg")  # Replace with your actual image path
    # background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    candy_images = {}
    for candy in candies:
        candy_images[candy["name"]] = pygame.image.load(f"../assets/images/{candy['image']}")

    # Load background images
    background_images = {}
    for background in backgrounds:
        try:
            background_images[background["name"]] = pygame.image.load(f"../assets/images/{background['image']}")
        except pygame.error as e:
            print(f"Error loading background image: {background['image']}, Error: {e}")
    
    # Randomly choose a background image at the start
    if background_images:
        current_background = random.choice(list(background_images.values()))
    else:
        print("No background images loaded!")

def draw_background(screen):
    """Draw the background image to the screen."""
    if current_background:
        # Scale the background image to fit the screen
        background = pygame.transform.scale(current_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background, (0, 0))  # Blit the background image to (0, 0) position

# def draw_background(screen):
#     """Draw the background image to the screen."""
#     screen.blit(background_image, (0, 0))  # Blit the background image to (0, 0) position

#def draw_background(screen):
   # """Draw a gradient background."""
    #for y in range(SCREEN_HEIGHT):
      #  color = (135 + y // 10, 206 + y // 20, 235)  # Sky blue gradient
       # pygame.draw.line(screen, color, (0, y), (SCREEN_WIDTH, y))

def draw_dispenser(screen, candies):
    """Draw the dispenser, candies, and the spring."""
    spring_height = 50 + len(candies) * 5
    screen.blit(dispenser_image, (230, -100 + spring_height))
 
    # The candies in the stack
    for i, candy in enumerate(candies):
        x = 430 # Candy x position
        y = 255 - (i * 30)  
        z=125
        candy_image = candy_images[candy]
        screen.blit(candy_image, (x, y+z))  
        z+10

    
    
    screen.blit(spring_image, (210, 300 + spring_height))


def draw_buttons(screen, mouse_pos):
    buttons = {
        "Push": (20, 100, 200, 50),
        "Pop": (20, 170, 200, 50),
        "Peek": (20, 240, 200, 50),
        "IsEmpty": (20, 310, 200, 50),
        "IsFull": (20, 380, 200, 50),
        "Length": (20, 450, 200, 50),
        "Reset": (20, 520, 200, 50),
        "Quit": (20, 590, 200, 50),
    }
    for label, (x, y, w, h) in buttons.items():
    
        color = BUTTON_HOVER if x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h else DARK_BLUE
        pygame.draw.rect(screen, color, (x, y, w, h), border_radius=10)
        pygame.draw.rect(screen, BLACK, (x, y, w, h), width=2, border_radius=10)

        text = FONT.render(label, True, WHITE)
        text_rect = text.get_rect(center=(x + w // 2, y + h // 2))
        screen.blit(text, text_rect)

def draw_horizontal_bar(screen):
    """Draw a horizontal bar at the bottom of the screen."""
    bar_height = 100
    bar_color = (0, 0, 0) 
    pygame.draw.rect(screen, bar_color, (0, SCREEN_HEIGHT - bar_height, SCREEN_WIDTH, bar_height))

    # Add text
    # text = FONT.render("Candy Dispenser Game", True, WHITE)
    # screen.blit(text, (20, SCREEN_HEIGHT - bar_height + 10))
def display_message(screen, message, color=WHITE):
    """Display a temporary message prominently on the screen."""
    
    msg = FONT.render(message, True, color)
    msg_rect = msg.get_rect(center=(SCREEN_WIDTH // 2, 50))

    
    pygame.draw.rect(screen, BLACK, msg_rect.inflate(20, 10), border_radius=10)
    pygame.draw.rect(screen, GRAY, msg_rect.inflate(20, 10), border_radius=10, width=2)

    
    screen.blit(msg, msg_rect)


# Main game loop
def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Candy Dispenser Stack Game")

    clock = pygame.time.Clock()
    load_assets()
    feedback_message = ""
    feedback_color = BLACK
    feedback_timer = 0

    background_change_timer = pygame.time.get_ticks()

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        # The background 
        draw_background(screen)
        draw_horizontal_bar(screen)
        
        

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # Handle button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
              x, y = pygame.mouse.get_pos()
    
              if 20 < x < 220 and 100 < y < 150:  # Push button
                  selected_candy = random.choice(candies)
                  if candy_stack.push(selected_candy["name"]):  # Add only the name
                       BUTTON_CLICK_SOUND.play()
                       feedback_message = f"Pushed {selected_candy['name']}!"
                       feedback_color = GREEN
                       feedback_timer = pygame.time.get_ticks()
                  else:
                       ERROR_SOUND.play()
                       feedback_message = "Stack is full!"
                       feedback_color = RED
                       feedback_timer = pygame.time.get_ticks()

              elif 20 < x < 220 and 170 < y < 220:  # Pop button
                   if candy_stack.pop():
                      POP_SOUND.play()
                      feedback_message = "Candy popped!"
                      feedback_color = GREEN
                      feedback_timer = pygame.time.get_ticks()
                   else:
                      ERROR_SOUND.play()
                      feedback_message = "Stack is empty!"
                      feedback_color = RED
                      feedback_timer = pygame.time.get_ticks()


              elif 20 < x < 220 and 240 < y < 290:  # Peek button
                   top_candy = candy_stack.peek()
                   if top_candy:
                     BUTTON_CLICK_SOUND.play()
                     feedback_message = f"Top candy: {top_candy}"
                     feedback_color = BLUE
                     feedback_timer = pygame.time.get_ticks()

                   else:
                     ERROR_SOUND.play()
                     feedback_message = "Stack is empty!"
                     feedback_color = RED
                     feedback_timer = pygame.time.get_ticks()


              elif 20 < x < 220 and 310 < y < 360:  # IsEmpty button
                   if candy_stack.is_empty():
                      BUTTON_CLICK_SOUND.play()
                      feedback_message = "Stack is empty!"
                      feedback_color = GREEN
                      feedback_timer = pygame.time.get_ticks()

                   else:
                     ERROR_SOUND.play()
                     feedback_message = "Stack is not empty!"
                     feedback_color = BLUE
                     feedback_timer = pygame.time.get_ticks()


              elif 20 < x < 220 and 380 < y < 430:# IsFull button
                if candy_stack.is_full():
                     BUTTON_CLICK_SOUND.play()
                     feedback_message = "Stack is full!"
                     feedback_color = GREEN
                     feedback_timer = pygame.time.get_ticks()

                else:
                    ERROR_SOUND.play()
                    feedback_message = "Stack is not full!"
                    feedback_color = BLUE
                    feedback_timer = pygame.time.get_ticks()


              elif 20 < x < 220 and 450 < y < 500:  # Length button
                    BUTTON_CLICK_SOUND.play()
                    feedback_message = f"Stack length: {len(candy_stack.stack)}"
                    feedback_color = WHITE
                    feedback_timer = pygame.time.get_ticks()


              elif 20 < x < 220 and 520 < y < 570:  # Reset button
                   candy_stack.clear()
                   BUTTON_CLICK_SOUND.play()
                   feedback_message = "Stack reset!"
                   feedback_color = GREEN
                   feedback_timer = pygame.time.get_ticks()


              elif 20 < x < 220 and 590 < y < 640:  # Quit button
                   BUTTON_CLICK_SOUND.play()
                   running = False

                   # Reset feedback timer
                   feedback_timer = pygame.time.get_ticks()

        
        draw_dispenser(screen, candy_stack.stack)
        draw_buttons(screen, mouse_pos)
        draw_horizontal_bar(screen)

       
        if pygame.time.get_ticks() - background_change_timer > 10000:  
            if background_images:  
                current_background = random.choice(list(background_images.values())) 
            background_change_timer = pygame.time.get_ticks()  

        # Feedback message
        if pygame.time.get_ticks() - feedback_timer < 1000:
            display_message(screen, feedback_message, feedback_color)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
