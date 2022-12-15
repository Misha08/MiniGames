import pygame
import random
from Games.Game import Game

pygame.init()


class Snake(Game):

    '''

    The snake class that inherits from the main game class,
    in turn, the PyGame module is used here

    '''
    # Initialization method
    def __init__(self, count_of_players):
        '''

        The Snake class

        Here you can set the main parameters of the game by default:
        1) Colors of the main interactive elements
        2) Colors of the texts
        3) Colors of the backgrounds
        4) Width and Height of the play display
        5) Generate the display parameters
        6) Set the clock and ticks parameter
        7) Speed and the length a part of the snake
        8) Fonts for texts

        '''

        # Delegation
        super().__init__(count_of_players)

        # Colors
        # Colors of the main interactive elements
        self.snake_color = (93, 203, 46)
        self.food_color = (255, 0, 0)

        # Colors of the texts
        self.color_of_score_text = (255, 255, 255)
        self.color_of_lose_message = (219, 228, 233)

        # Colors of the backgrounds
        self.background_color_1 = (50, 153, 213)
        self.background_color_2 = (27, 108, 155)

        # Width and Height of the play display
        self.dis_width = 700
        self.dis_height = 400

        # Generate the display parameters
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption("Snake")

        # Set the clock and ticks parameter
        self.clock = pygame.time.Clock()

        # Speed and the length a part of the snake
        self.snake_block = 10
        self.snake_speed = 10

        # Fonts for texts
        self.font_style = pygame.font.SysFont("Helvetica", 22)
        self.score_font = pygame.font.SysFont("Helvetica", 35)

    # The function which shows how much food did you eat
    def your_score(self, score):
        score_message = self.score_font.render("Your score: " + str(score), True, self.color_of_score_text)
        self.dis.blit(score_message, [0, 0])

    # The function which shows which player is currently playing
    def player_display(self, player):
        display_player = self.score_font.render(str(player), True, self.color_of_score_text)
        self.dis.blit(display_player, [500, 0])

    # The function that describes a snake on the playing field
    def our_snake(self, snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.snake_color, [x[0], x[1], snake_block, snake_block])

    # The function which shows how much food did you eat
    def message(self, msg, color):
        message = self.font_style.render(msg, True, color)
        self.dis.blit(message, [self.dis_width / 6, self.dis_height / 2.2])

    # The main logical play function
    def play(self):
        '''

        The main logical "play" function



        1) Generation of the main parameters of the game and the interactive elements:
            a) The start coordinates of the snake
            b) Move parameters
            c) Coordinates of food
            d) The status of the game
        2) Then comes the creation of the main game loop, which ends only when the game process stops
        3) First, the algorithm recorded the output of the screen about the defeat,
           where, when processing events, the corresponding actions occur:
            a) When a key 'c' is pressed, an event 'K_c is triggered and the game for the current player is restarted
            with the initial parameters
            b) When a key 'q' is pressed, an event 'K_q is triggered and the game for the current player is ended
        4) The direction events are calculated depending on the triggered event, according to the pressed key
           as you can see, it increases and decreases by x or by y.
        5) The comparison of the position of the snake is triggered,
           and if it has gone beyond the boundaries of the playing field,
           then the internal game loop stops its work and it is considered that the current player has lost
        6) The snake moves across the playing field by adding the movement parameters
           to the current coordinates of its head.
        7) Creating a logical abstract snake body for further interaction and output
        8) Checking the integrity of the snake, when the snake comes into contact with its own body
           or for some reason it does not match,
           and specifically exceeds the logical length of the snake's body
        9) Update the display
        10) The case of eating food is calculated, when it is eaten,
            the length of the snake increases and one point is added, and the current user gets 100 points
        11) Tics occur

        '''

        # Loop through the list of players
        for player in self.players:

            # The start coordinates of the snake
            snake_x1 = round(random.randrange(0, self.dis_width - self.snake_block) / 20.0) * 10.0
            snake_y1 = round(random.randrange(0, self.dis_height - self.snake_block) / 20.0) * 10.0

            # Move parameters
            x1_move = 0
            y1_move = 0

            # Parameters of the snake
            snake_list = list()
            length_of_snake = 1

            # Coordinates of food
            food_x = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0

            # Define the status of the game
            game_over = False
            game_close = False

            # The play loop
            while not game_over:
                # The play loop
                while game_close:
                    # Display the end information
                    self.dis.fill(self.background_color_2)

                    self.message("You lose! press C - to play again или Q - to quit the game",
                                 self.color_of_lose_message)

                    # Display how much food have you eaten
                    self.your_score(length_of_snake - 1)

                    # Update the display
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:

                                # Changing the game status
                                game_over = True
                                game_close = False

                            if event.key == pygame.K_c:

                                # Restart the game
                                self.snake_speed = 10
                                self.play()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.get_players()
                        game_over = True
                    if event.type == pygame.KEYDOWN:

                        # Change of direction Buttons
                        # Change of direction on Left
                        if event.key == pygame.K_LEFT:
                            x1_move = self.snake_block * -1
                            y1_move = 0

                        # Change of direction on Right
                        elif event.key == pygame.K_RIGHT:
                            x1_move = self.snake_block
                            y1_move = 0

                        # Change of direction on Up
                        elif event.key == pygame.K_UP:
                            y1_move = self.snake_block * -1
                            x1_move = 0

                        # Change of direction on Down
                        elif event.key == pygame.K_DOWN:
                            y1_move = self.snake_block
                            x1_move = 0

                        # Checking for a button press to end the game
                        elif event.key == pygame.K_q:
                            game_close = True
                            game_over = True

                        # Checking buttons for changing speed
                        elif event.key == pygame.K_v:
                            self.snake_speed += 2
                        elif event.key == pygame.K_b:
                            # Negative speed check
                            if self.snake_speed - 2 > 0:
                                self.snake_speed -= 2

                # Finding a snake within the playing field
                if snake_x1 >= self.dis_width or snake_x1 < 0 or snake_y1 >= self.dis_height or snake_y1 < 0:
                    game_close = True

                # Adding the coordinates so that move
                snake_x1 += x1_move
                snake_y1 += y1_move

                # Color of the main playing field
                self.dis.fill(self.background_color_1)

                # Drawing food and the snake itself
                pygame.draw.rect(self.dis, self.food_color, [food_x, food_y, self.snake_block, self.snake_block])

                # Creating Logical Snake body
                snake_head = list()
                snake_head.append(snake_x1)
                snake_head.append(snake_y1)
                snake_list.append(snake_head)

                # Prevention of mismatch between the length of the snake and its logical body on the field
                if len(snake_list) > length_of_snake:
                    del snake_list[0]

                # Determining if a snake's head collides with its main body
                for elem_snake in snake_list[:-1]:
                    if elem_snake == snake_head:
                        game_close = True

                # Operations carried out with regard to the snake
                self.our_snake(self.snake_block, snake_list)
                self.your_score(length_of_snake - 1)
                self.player_display(player)

                # Update the display
                pygame.display.update()

                # Calculating the case when a snake eats food
                if snake_x1 == food_x and snake_y1 == food_y:
                    food_x = round(random.randrange(0, self.dis_width - self.snake_block) / 20.0) * 10.0
                    food_y = round(random.randrange(0, self.dis_height - self.snake_block) / 20.0) * 10.0
                    length_of_snake += 1

                # Determining the number of ticks depending on the speed of the snake
                self.clock.tick(self.snake_speed)

            # Scoring points for an active player
            player.add_score(length_of_snake - 1)

        # Call the function for getting info about the players
        self.get_players()

        # Close the game
        pygame.quit()


if __name__ == "__main__":
    s = Snake(2)
    s.play()
