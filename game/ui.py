import pygame
from .constants import *
from .game_state import GameState

class UI:
    def __init__(self, screen):
        """Khởi tạo UI"""
        self.screen = screen
        pygame.font.init()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw_text(self, text, font, color, x, y, center=False):
        """Vẽ text lên screen"""
        text_surface = font.render(text, True, color)
        if center:
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.screen.blit(text_surface, text_rect)
        else:
            self.screen.blit(text_surface, (x, y))
        return text_surface.get_rect()
    
    def draw_menu(self):
        """Vẽ main menu"""
        self.screen.fill(BLACK)
        
        # Title
        self.draw_text("SNAKE GAME", self.font_large, GREEN, WINDOW_WIDTH // 2, 150, center=True)
        self.draw_text("Built with Amazon Q CLI", self.font_small, WHITE, WINDOW_WIDTH // 2, 200, center=True)
        
        # Menu options
        self.draw_text("SPACE - Start Game", self.font_medium, WHITE, WINDOW_WIDTH // 2, 300, center=True)
        self.draw_text("H - High Scores", self.font_medium, WHITE, WINDOW_WIDTH // 2, 350, center=True)
        self.draw_text("ESC - Quit", self.font_medium, WHITE, WINDOW_WIDTH // 2, 400, center=True)
        
        # Instructions
        self.draw_text("Use Arrow Keys to Move", self.font_small, YELLOW, WINDOW_WIDTH // 2, 500, center=True)
        self.draw_text("P - Pause | R - Restart", self.font_small, YELLOW, WINDOW_WIDTH // 2, 530, center=True)
    
    def draw_game_ui(self, score, high_score, level):
        """Vẽ UI trong lúc chơi game"""
        # Score
        self.draw_text(f"Score: {score}", self.font_medium, WHITE, 10, 10)
        self.draw_text(f"High: {high_score}", self.font_medium, WHITE, 10, 50)
        self.draw_text(f"Level: {level}", self.font_medium, WHITE, 10, 90)
        
        # Draw grid lines (optional)
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (20, 20, 20), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (20, 20, 20), (0, y), (WINDOW_WIDTH, y))
    
    def draw_pause_screen(self):
        """Vẽ pause screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        self.draw_text("PAUSED", self.font_large, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, center=True)
        self.draw_text("Press P to Continue", self.font_medium, YELLOW, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20, center=True)
        self.draw_text("Press ESC to Main Menu", self.font_medium, YELLOW, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60, center=True)
    
    def draw_game_over(self, final_score, is_high_score):
        """Vẽ game over screen"""
        self.screen.fill(BLACK)
        
        self.draw_text("GAME OVER", self.font_large, RED, WINDOW_WIDTH // 2, 200, center=True)
        self.draw_text(f"Final Score: {final_score}", self.font_medium, WHITE, WINDOW_WIDTH // 2, 280, center=True)
        
        if is_high_score:
            self.draw_text("NEW HIGH SCORE!", self.font_medium, YELLOW, WINDOW_WIDTH // 2, 320, center=True)
        
        self.draw_text("SPACE - Play Again", self.font_medium, GREEN, WINDOW_WIDTH // 2, 400, center=True)
        self.draw_text("ESC - Main Menu", self.font_medium, WHITE, WINDOW_WIDTH // 2, 440, center=True)
    
    def draw_high_scores(self, high_scores):
        """Vẽ high scores screen"""
        self.screen.fill(BLACK)
        
        self.draw_text("HIGH SCORES", self.font_large, YELLOW, WINDOW_WIDTH // 2, 50, center=True)
        
        y_start = 150
        for i, score_entry in enumerate(high_scores[:10]):
            rank = i + 1
            score = score_entry["score"]
            player = score_entry["player"]
            date = score_entry["date"][:10]  # Chỉ lấy ngày
            
            color = GREEN if rank <= 3 else WHITE
            self.draw_text(f"{rank:2d}. {player:10s} {score:6d} {date}", 
                          self.font_small, color, WINDOW_WIDTH // 2, y_start + i * 30, center=True)
        
        self.draw_text("ESC - Back to Menu", self.font_medium, WHITE, WINDOW_WIDTH // 2, 500, center=True) 