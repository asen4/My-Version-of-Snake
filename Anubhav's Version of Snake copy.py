import pygame
import random
pygame.init()

def instruction_screen():
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    DARK_GREEN = (45, 75, 15)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # The following line of code creates a window/surface. 
    screen = pygame.display.set_mode([1920, 965])

    # The following line of code gives the window a caption. 
    pygame.display.set_caption("Ankur's Version of Snake")

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)
    # font = pygame.font.SysFont('Calibri', 30, True, False)   
    clock = pygame.time.Clock()
    done = False
    display_instructions = True
    instruction_page = 1

    border = pygame.Surface([1800, 845])
    border.fill(BLACK)
     
    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
        # Set the screen background
        screen.fill(DARK_GREEN)
        screen.blit(border, (60, 60))
     
        if instruction_page == 1:
            # Draw instructions, page 1
            # This could also load an image created in another program.
            # That could be both easier and more flexible.

            text = font.render("Anubhav's Version of Snake", True, WHITE)
            screen.blit(text, [860, 20])
     
            text = font.render("INSTRUCTIONS: Please press the SPACEBAR in order to begin the game.", True, WHITE)
            screen.blit(text, [75, 75])

            text = font.render("If you want to pause the game while you are playing, please press P.", True, WHITE)
            screen.blit(text, [75, 110])

            text = font.render("You have the option of using the arrow keys or WASD keys to control the snake's movements.", True, WHITE)
            screen.blit(text, [75, 145])

            text = font.render("The rules of the usual game of Snake still apply in this game.", True, WHITE)
            screen.blit(text, [75, 180])
     
            text = font.render("However, there are few add-ons in this verison of Snake:", True, WHITE)
            screen.blit(text, [75, 215])

            text = font.render("1. There are a few yellow-colored obstacles in random locations on the screen.", True, WHITE)
            screen.blit(text, [100, 250])

            text = font.render("If the snake hits an obstacle, it will bounce off the obstacle and will head in a new direction.", True, WHITE)
            screen.blit(text, [100, 285])

            text = font.render("2. In addition to apples as the snake's food, there are blueberries as well.", True, WHITE)
            screen.blit(text, [100, 355])

            text = font.render("Apples increase the length of the snake by 4. Blueberries increase the length of the snake by 2.", True, WHITE)
            screen.blit(text, [100, 390])

            text = font.render("Enjoy!", True, WHITE)
            screen.blit(text, [75, 460])
     
        # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        if instruction_page == 1:
            display_instructions = False

def play_again_A():
    main()

def main():
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    DARK_GREEN = (45, 75, 15)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    # The following line of code creates a window/surface. 
    screen = pygame.display.set_mode([1920, 965])

    # The following line of code gives the window a caption. 
    pygame.display.set_caption("Ankur's Version of Snake")
    
    play_again = True
    while play_again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_again = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    # Set the width and height of each snake segment
                    segment_width = 15
                    segment_height = 15

                    # Margin between each segment
                    segment_margin = 3
                     
                    # Set initial speed
                    x_change = segment_width + segment_margin
                    y_change = 0

                    border = pygame.Surface([1800, 845])
                    border.fill(BLACK)
                    
                    class Segment (pygame.sprite.Sprite):
                        """ Class to represent one segment of the snake. """
                        # -- Methods
                        # Constructor function
                        def __init__ (self, x, y):
                            # Call the parent's constructor
                            super().__init__()
                     
                            # Set height, width
                            self.image = pygame.Surface([segment_width, segment_height])
                            self.image.fill(GREEN)
                     
                            # Make our top-left corner the passed-in location.
                            self.rect = self.image.get_rect()
                            self.rect.x = x
                            self.rect.y = y

                        def Coord_Snake_HeadX():
                            image = pygame.Surface([segment_width, segment_height])

                            rect = image.get_rect()
                            rect.x = x
                            rect.y = y
                            return rect.x

                        def Coord_Snake_HeadY():
                            image = pygame.Surface([segment_width, segment_height])

                            rect = image.get_rect()
                            rect.x = x
                            rect.y = y
                            return rect.y

                    class High_Score():
                        def get_high_score():
                            # Default high score
                            high_score = 0
                         
                            # Try to read the high score from a file
                            try:
                                high_score_file = open("high_score_Snake.txt", "r")
                                high_score = int(high_score_file.read())
                                high_score_file.close()
                            except IOError:
                                # Error reading file, no high score
                                print("There is no high score yet.")
                            except ValueError:
                                # There's a file there, but we don't understand the number.
                                print("I'm confused. Starting with no high score.")
                         
                            return high_score
                         
                         
                        def save_high_score(new_high_score):
                            try:
                                # Write the file to disk
                                high_score_file = open("high_score_Snake.txt", "w")
                                high_score_file.write(str(new_high_score))
                                high_score_file.close()
                            except IOError:
                                # Hm, can't write it.
                                print("Unable to save the high score.")

                    class Obstacles (pygame.sprite.Sprite):
                        def __init__ (self, x, y):
                            super().__init__()

                            self.image = pygame.Surface([segment_width, segment_height])
                            self.image.fill(YELLOW)

                            self.rect = self.image.get_rect()
                            self.rect.x = x
                            self.rect.y = y

                        def moveRandomDirection():
                            image = pygame.Surface([segment_width, segment_height])

                            rect = image.get_rect()
                            x = rect.x
                            y = rect.y
                            
                    class Apple (pygame.sprite.Sprite):
                        def __init__ (self):
                            super().__init__()

                            self.image = pygame.Surface([segment_width, segment_height])
                            self.image.fill(RED)
                            
                            self.rect = self.image.get_rect()
                            self.rect.x = random.randrange(60, 1716, 18)
                            self.rect.y = random.randrange(60, 780, 18)

                    class Blueberry (pygame.sprite.Sprite):
                        def __init__ (self):
                            super().__init__()

                            self.image = pygame.Surface([10, 10])
                            self.image.fill(BLUE)
                            
                            self.rect = self.image.get_rect()
                            self.rect.x = random.randrange(60, 1716, 18)
                            self.rect.y = random.randrange(60, 780, 18)

                    class Pause():
                        def pause():
                            paused = True

                            while paused:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        play_again = False
                                        pygame.display.quit()
                                        pygame.quit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            done = True
                                            play_again = False
                                            pygame.display.quit()
                                            pygame.quit()
                                        if event.key == pygame.K_c:
                                          paused = False

                                screen.fill(DARK_GREEN)
                                
                                border = pygame.Surface([1800, 845])
                                border.fill(BLACK)
                                screen.blit(border, (60, 60))
                                
                                font = pygame.font.Font(None, 36)
                                text = font.render("The game is currently PAUSED. Press C to CONTINUE or Q to QUIT THE GAME.", True, WHITE)
                                screen.blit(text, [75, 75])

                                pygame.display.update()

                    all_snake_segments_list = pygame.sprite.Group()
                    apple_container = pygame.sprite.GroupSingle()
                    blueberry_container = pygame.sprite.GroupSingle()
                    obstacle_container = pygame.sprite.Group()
                     
                    # Create an initial snake
                    snake_segments = []
                    for i in range(3):
                        x = 960 - (segment_width + segment_margin) * i
                        y = 474
                        segment = Segment(x, y)
                        snake_segments.append(segment)
                        all_snake_segments_list.add(segment)

                    obstacle_array = []
                    for i in range(25):
                        x = random.randrange(60, 1716, 18)
                        y = random.randrange(60, 780, 18)
                        obstacle = Obstacles(x, y)
                        obstacle_array.append(obstacle)
                        obstacle_container.add(obstacle)

                    # Creating the first apple
                    apple = Apple()
                    apple_container.add(apple)
                    
                    blueberry = Blueberry()
                    blueberry_container.add(blueberry)
                    
                    clock = pygame.time.Clock()
                    done = False

                    direction = "right"
                    
                    while not done:
                        
                        for event in pygame.event.get():
                            # Set the speed based on the key pressed
                            # We want the speed to be enough that we move a full
                            # segment, plus the margin.
                            if event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                                    x_change = (segment_width + segment_margin) * -1
                                    y_change = 0
                                    direction = "left"
                                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                                    x_change = (segment_width + segment_margin)
                                    y_change = 0
                                    direction = "right"
                                if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                                    x_change = 0
                                    y_change = (segment_height + segment_margin) * -1
                                    direction = "up"
                                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                                    x_change = 0
                                    y_change = (segment_height + segment_margin)
                                    direction = "down"
                                if event.key == pygame.K_p:
                                    Pause.pause()
                                     
                        # Get rid of last segment of the snake
                        # .pop() command removes last item in list
                        old_segment = snake_segments.pop()
                        all_snake_segments_list.remove(old_segment)
                     
                        # Figure out where new segment will be
                        x = snake_segments[0].rect.x + x_change
                        y = snake_segments[0].rect.y + y_change
                        segment = Segment(x, y)
                     
                        # Insert new segment into the list
                        snake_segments.insert(0, segment)
                        all_snake_segments_list.add(segment)
                        '''
                        for i in range (4):
                            random_value = random.randint(1, 4)

                            if random_value == 1:
                                x_change_ob = (segment_width + segment_margin) * -1
                                y_change_ob = 0
                            if random_value == 2:
                                x_change_ob = (segment_width + segment_margin)
                                y_change_ob = 0
                            if random_value == 3:
                                x_change_ob = 0
                                y_change_ob = (segment_height + segment_margin) * -1
                            if random_value == 4:
                                x_change_ob = 0
                                y_change_ob = (segment_height + segment_margin)

                            #old_obstacle = obstacle_array.pop()
                            #obstacle_container.remove(old_obstacle)

                            x = obstacle_array[i].rect.x + x_change_ob
                            y = obstacle_array[i].rect.y + y_change_ob
                            obstacle = Obstacles(x, y)

                            #obstacle_array.insert(0, obstacle)
                            #obstacle_container.add(obstacle)
                        '''
                        # The following piece of code checks if the snake collides with the boundaries. 
                        coord_X = Segment.Coord_Snake_HeadX()
                        coord_Y = Segment.Coord_Snake_HeadY()
                        # print("(",coord_X,", ",coord_Y,")")
                        if coord_X <= 55 or coord_X >= 1845 or coord_Y <= 55 or coord_Y >= 890:
                            border.fill(BLACK)
                            instruction_page = 1
                                 
                            # -------- Instruction Page Loop -----------
                            while not done or display_instructions:                             
                                # Set the screen background
                                screen.fill(DARK_GREEN)
                                screen.blit(border, (60, 60))

                                if instruction_page == 1:
                                    # Draw instructions, page 1
                                    # This could also load an image created in another program.
                                    # That could be both easier and more flexible.
                                 
                                    text = font.render("GAME OVER! You lost because you collided with the boundaries!", True, WHITE)
                                    screen.blit(text, [75, 75])

                                    text = font.render("Press the SPACEBAR to play again.", True, WHITE)
                                    screen.blit(text, [75, 110])

                                    text = font.render("If you want to quit the game, press Q or the X button at the top-left corner of the window.", True, WHITE)
                                    screen.blit(text, [75, 145])
                   
                                # Limit to 60 frames per second
                                clock.tick(60)
                                 
                                # Go ahead and update the screen with what we've drawn.
                                pygame.display.update()
        

                                if instruction_page == 1:
                                    display_instructions = False

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        done = True
                                        play_again = False
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                            done = True
                                            play_again = False
                                    else:
                                        play_again_A()
                    
                        # The following piece of code checks if the snake collides with itself.         
                        for i in range (1, len(snake_segments)):
                            if pygame.sprite.collide_rect(snake_segments[0], snake_segments[i]):
                                border.fill(BLACK)
                                instruction_page = 1
                                 
                                # -------- Instruction Page Loop -----------
                                while not done or display_instructions:                             
                                    # Set the screen background
                                    screen.fill(DARK_GREEN)
                                    screen.blit(border, (60, 60))

                                    if instruction_page == 1:
                                        # Draw instructions, page 1
                                        # This could also load an image created in another program.
                                        # That could be both easier and more flexible.
                                 
                                        text = font.render("GAME OVER! You lost because you collided with yourself!", True, WHITE)
                                        screen.blit(text, [75, 75])

                                        text = font.render("Press the SPACEBAR to play again.", True, WHITE)
                                        screen.blit(text, [75, 110])

                                        text = font.render("If you want to quit the game, press Q or the X button at the top-left corner of the window.", True, WHITE)
                                        screen.blit(text, [75, 145])
                   
                                    # Limit to 60 frames per second
                                    clock.tick(60)
                                 
                                    # Go ahead and update the screen with what we've drawn.
                                    pygame.display.update()
        

                                    if instruction_page == 1:
                                        display_instructions = False

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            done = True
                                            play_again = False
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_q:
                                                done = True
                                                play_again = False
                                        else:
                                            play_again_A()
                                                
                        if pygame.sprite.spritecollide(snake_segments[0], apple_container, False):
                            # This while loop makes sure the apple does not appear on the snake's body or on the obstacles.
                            while pygame.sprite.groupcollide(apple_container, all_snake_segments_list, False, False) or pygame.sprite.groupcollide(obstacle_container, apple_container, False, False):
                                apple = Apple()
                                apple_container.add(apple)
                                
                            # The following piece of code increases the length of the snake when it eats a apple. 
                            for i in range(4):
                                segment = Segment(x, y)
                                snake_segments.append(segment)
                                all_snake_segments_list.add(segment)

                        # Get the high score
                        high_score = High_Score.get_high_score()
                     
                        # Get the score from the current game
                        current_score = len(snake_segments)
                    
                        # See if we have a new high score
                        if current_score > high_score:
                            High_Score.save_high_score(current_score)
                        
                        if pygame.sprite.spritecollide(snake_segments[0], obstacle_container, False):
                            random_value = random.randint(1, 4)
                            if random_value == 1 and direction != "up":
                                x_change = 0
                                y_change = (segment_height + segment_margin)
                                direction = "down"
                            elif random_value == 2 and direction != "right":
                                x_change = (segment_width + segment_margin) * -1
                                y_change = 0
                                direction = "left"
                            elif random_value == 3 and direction != "left":
                                x_change = (segment_width + segment_margin)
                                y_change = 0
                                direction = "right"
                            elif random_value == 4 and direction != "down":
                                x_change = 0
                                y_change = (segment_height + segment_margin) * -1
                                direction = "up"
        
                            old_segment = snake_segments.pop()
                            all_snake_segments_list.remove(old_segment)
                     
                            # Figure out where new segment will be
                            x = snake_segments[0].rect.x + x_change
                            y = snake_segments[0].rect.y + y_change
                            segment = Segment(x, y)
                     
                            # Insert new segment into the list
                            snake_segments.insert(0, segment)
                            all_snake_segments_list.add(segment)
                            
                        
                        if pygame.sprite.spritecollide(snake_segments[0], blueberry_container, False):
                            while pygame.sprite.groupcollide(blueberry_container, all_snake_segments_list, False, False) or pygame.sprite.groupcollide(obstacle_container, blueberry_container, False, False):
                                blueberry = Blueberry()
                                blueberry_container.add(blueberry)

                                for i in range(2):
                                    segment = Segment(x, y)
                                    snake_segments.append(segment)
                                    all_snake_segments_list.add(segment)
                           

                        
                        # Draw Everything
                        # Clear Screen
                        screen.fill(DARK_GREEN)

                        font = pygame.font.Font(None, 36)
                        # font = pygame.font.SysFont('Calibri', 30, True, False)
                        text_title = font.render("Ankur's Version of Snake", True, WHITE)
                        text_score = font.render("Current Score: {0}".format(len(snake_segments)), True, WHITE)
                        text_high_score = font.render("High Score: {0}".format(high_score), True, WHITE)
                        
                        screen.blit(border, (60, 60))
                        screen.blit(text_title, [860, 25])
                        screen.blit(text_score, [1650, 926])
                        screen.blit(text_high_score, [70, 926])
                         
                        all_snake_segments_list.draw(screen)
                        apple_container.draw(screen)
                        blueberry_container.draw(screen)
                        obstacle_container.draw(screen)
                        
                        # Flip and Update Screen
                        pygame.display.flip()
                     
                        # Pause
                        clock.tick(15)
                        
                elif event.key == pygame.K_q:
                    play_again = False
                    
    pygame.display.quit()                              
    pygame.quit()

instruction_screen()
main()
