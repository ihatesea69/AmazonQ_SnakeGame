#!/usr/bin/env python3
"""
Snake Game - Built with Amazon Q CLI
Main entry point for the game
"""

import pygame
import sys
from game.constants import *
from game.snake import Snake
from game.food import Food
from game.game_state import GameState, GameStateManager
from game.score_manager import ScoreManager
from game.sound_manager import SoundManager
from game.ui import UI

class SnakeGame:
    def __init__(self):
        """Khởi tạo Snake Game"""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game - Built with Amazon Q CLI")
        self.clock = pygame.time.Clock()
        
        # Game components
        self.state_manager = GameStateManager()
        self.score_manager = ScoreManager()
        self.sound_manager = SoundManager()
        self.ui = UI(self.screen)
        
        # Game objects
        self.snake = None
        self.food = None
        self.level = 1
        self.speed = FPS
        
        # Game state
        self.running = True
        
    def init_game(self):
        """Khởi tạo game objects cho game mới"""
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = Snake(start_x, start_y)
        self.food = Food(GRID_WIDTH, GRID_HEIGHT)
        self.food.spawn(self.snake.body)
        self.score_manager.reset_current_score()
        self.level = 1
        self.speed = FPS
    
    def handle_events(self):
        """Xử lý events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)
    
    def _handle_keydown(self, key):
        """Xử lý keyboard input"""
        current_state = self.state_manager.get_current_state()
        
        if current_state == GameState.MENU:
            if key == pygame.K_SPACE:
                self.init_game()
                self.state_manager.change_state(GameState.PLAYING)
            elif key == pygame.K_h:
                self.state_manager.change_state(GameState.HIGH_SCORES)
            elif key == pygame.K_ESCAPE:
                self.running = False
        
        elif current_state == GameState.PLAYING:
            if key == pygame.K_UP:
                self.snake.change_direction(UP)
            elif key == pygame.K_DOWN:
                self.snake.change_direction(DOWN)
            elif key == pygame.K_LEFT:
                self.snake.change_direction(LEFT)
            elif key == pygame.K_RIGHT:
                self.snake.change_direction(RIGHT)
            elif key == pygame.K_p:
                self.state_manager.change_state(GameState.PAUSED)
            elif key == pygame.K_r:
                self.init_game()
            elif key == pygame.K_ESCAPE:
                self.state_manager.change_state(GameState.MENU)
        
        elif current_state == GameState.PAUSED:
            if key == pygame.K_p:
                self.state_manager.change_state(GameState.PLAYING)
            elif key == pygame.K_ESCAPE:
                self.state_manager.change_state(GameState.MENU)
        
        elif current_state == GameState.GAME_OVER:
            if key == pygame.K_SPACE:
                self.init_game()
                self.state_manager.change_state(GameState.PLAYING)
            elif key == pygame.K_ESCAPE:
                self.state_manager.change_state(GameState.MENU)
        
        elif current_state == GameState.HIGH_SCORES:
            if key == pygame.K_ESCAPE:
                self.state_manager.change_state(GameState.MENU)
    
    def update_game(self):
        """Update game logic"""
        if not self.state_manager.is_state(GameState.PLAYING):
            return
        
        # Move snake
        self.snake.move()
        
        # Check food collision
        if self.snake.get_head_position() == self.food.get_position():
            self.snake.grow()
            points = self.food.get_score_value()
            self.score_manager.add_points(points)
            
            # Play sound
            if self.food.is_special():
                self.sound_manager.play_sound('special')
            else:
                self.sound_manager.play_sound('eat')
            
            # Spawn new food
            self.food.spawn(self.snake.body)
            
            # Increase level và speed
            if self.score_manager.get_current_score() // 50 + 1 > self.level:
                self.level += 1
                self.speed = min(FPS + self.level * 2, FPS * 3)
        
        # Update food
        self.food.update()
        
        # Check collisions
        if (self.snake.check_wall_collision(GRID_WIDTH, GRID_HEIGHT) or 
            self.snake.check_self_collision()):
            self._game_over()
    
    def _game_over(self):
        """Xử lý game over"""
        self.sound_manager.play_sound('game_over')
        
        final_score = self.score_manager.get_current_score()
        if self.score_manager.is_high_score(final_score):
            self.score_manager.add_score(final_score)
        
        self.state_manager.change_state(GameState.GAME_OVER)
    
    def render(self):
        """Render game graphics"""
        current_state = self.state_manager.get_current_state()
        
        if current_state == GameState.MENU:
            self.ui.draw_menu()
        
        elif current_state == GameState.PLAYING:
            self.screen.fill(BLACK)
            
            # Draw game objects
            if self.snake:
                self.snake.draw(self.screen)
            if self.food:
                self.food.draw(self.screen)
            
            # Draw UI
            self.ui.draw_game_ui(
                self.score_manager.get_current_score(),
                self.score_manager.get_highest_score(),
                self.level
            )
        
        elif current_state == GameState.PAUSED:
            # Vẽ game ở background
            self.screen.fill(BLACK)
            if self.snake:
                self.snake.draw(self.screen)
            if self.food:
                self.food.draw(self.screen)
            
            self.ui.draw_game_ui(
                self.score_manager.get_current_score(),
                self.score_manager.get_highest_score(),
                self.level
            )
            
            # Vẽ pause overlay
            self.ui.draw_pause_screen()
        
        elif current_state == GameState.GAME_OVER:
            final_score = self.score_manager.get_current_score()
            is_high_score = self.score_manager.is_high_score(final_score)
            self.ui.draw_game_over(final_score, is_high_score)
        
        elif current_state == GameState.HIGH_SCORES:
            self.ui.draw_high_scores(self.score_manager.get_high_scores())
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        print("🐍 Snake Game - Built with Amazon Q CLI")
        print("Controls:")
        print("  Arrow Keys - Move")
        print("  SPACE - Start/Restart")
        print("  P - Pause")
        print("  H - High Scores")
        print("  ESC - Menu/Quit")
        print("\nStarting game...")
        
        while self.running:
            self.handle_events()
            self.update_game()
            self.render()
            self.clock.tick(self.speed)
        
        pygame.quit()
        sys.exit()

def main():
    """Entry point"""
    try:
        game = SnakeGame()
        game.run()
    except Exception as e:
        print(f"Error starting game: {e}")
        print("Make sure pygame is installed: pip install pygame")
        sys.exit(1)

if __name__ == "__main__":
    main() 