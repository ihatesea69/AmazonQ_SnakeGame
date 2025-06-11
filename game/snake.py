import pygame
from .constants import *

class Snake:
    def __init__(self, x, y):
        """Khởi tạo Snake tại vị trí (x, y)"""
        self.body = [(x, y)]
        self.direction = RIGHT
        self.grow_pending = False
        
    def move(self):
        """Di chuyển snake theo direction hiện tại"""
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Thêm head mới
        self.body.insert(0, new_head)
        
        # Xóa tail nếu không grow
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def grow(self):
        """Đánh dấu snake sẽ grow ở lần move tiếp theo"""
        self.grow_pending = True
    
    def change_direction(self, new_direction):
        """Thay đổi direction, không cho phép đi ngược lại"""
        # Không cho phép đi ngược direction hiện tại
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def check_wall_collision(self, grid_width, grid_height):
        """Kiểm tra va chạm với tường"""
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= grid_width or head_y < 0 or head_y >= grid_height
    
    def check_self_collision(self):
        """Kiểm tra va chạm với chính mình"""
        head = self.body[0]
        return head in self.body[1:]
    
    def get_head_position(self):
        """Lấy vị trí của đầu snake"""
        return self.body[0]
    
    def get_length(self):
        """Lấy độ dài của snake"""
        return len(self.body)
    
    def draw(self, screen):
        """Vẽ snake lên screen"""
        for i, segment in enumerate(self.body):
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            # Head có màu khác với body
            if i == 0:
                pygame.draw.rect(screen, GREEN, rect)
                pygame.draw.rect(screen, WHITE, rect, 2)
            else:
                pygame.draw.rect(screen, GREEN, rect)
                pygame.draw.rect(screen, BLACK, rect, 1) 