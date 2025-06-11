import pygame
import random
from .constants import *

class Food:
    def __init__(self, grid_width, grid_height):
        """Khởi tạo Food"""
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = None
        self.special_food = False
        self.special_timer = 0
        self.spawn()
    
    def spawn(self, avoid_positions=None):
        """Tạo food mới tại vị trí random, tránh các vị trí trong avoid_positions"""
        if avoid_positions is None:
            avoid_positions = []
        
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in avoid_positions:
                self.position = (x, y)
                break
        
        # 10% chance tạo special food
        self.special_food = random.random() < 0.1
        if self.special_food:
            self.special_timer = 100  # Special food tồn tại 100 frames
    
    def update(self):
        """Update food state"""
        if self.special_food:
            self.special_timer -= 1
            if self.special_timer <= 0:
                self.special_food = False
    
    def get_position(self):
        """Lấy vị trí của food"""
        return self.position
    
    def is_special(self):
        """Kiểm tra xem có phải special food không"""
        return self.special_food
    
    def get_score_value(self):
        """Lấy điểm số khi ăn food này"""
        return FOOD_SCORE * 2 if self.special_food else FOOD_SCORE
    
    def draw(self, screen):
        """Vẽ food lên screen"""
        if self.position:
            x, y = self.position
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            if self.special_food:
                # Special food có hiệu ứng nhấp nháy
                alpha = 100 + int(55 * abs(pygame.time.get_ticks() % 1000 - 500) / 500)
                color = (*YELLOW, alpha) if self.special_timer % 10 < 5 else (*PURPLE, alpha)
                pygame.draw.rect(screen, color[:3], rect)
                pygame.draw.rect(screen, WHITE, rect, 2)
            else:
                # Normal food
                pygame.draw.rect(screen, RED, rect)
                pygame.draw.rect(screen, WHITE, rect, 1) 