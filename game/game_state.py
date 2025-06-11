import pygame
from enum import Enum

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    HIGH_SCORES = "high_scores"

class GameStateManager:
    def __init__(self):
        """Khởi tạo Game State Manager"""
        self.current_state = GameState.MENU
        self.previous_state = None
        
    def change_state(self, new_state):
        """Thay đổi state của game"""
        self.previous_state = self.current_state
        self.current_state = new_state
        
    def get_current_state(self):
        """Lấy state hiện tại"""
        return self.current_state
        
    def get_previous_state(self):
        """Lấy state trước đó"""
        return self.previous_state
        
    def is_state(self, state):
        """Kiểm tra xem có đang ở state này không"""
        return self.current_state == state 