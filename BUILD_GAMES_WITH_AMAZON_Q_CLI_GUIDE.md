# 🎮 Hướng Dẫn Xây Dựng Game với Amazon Q CLI

## 📋 Giới Thiệu Campaign

Campaign **"Build Games with Amazon Q CLI"** là cơ hội tuyệt vời để bạn trải nghiệm thực tế với AI coding assistant và phát huy sức sáng tạo để tạo ra những game mới sử dụng Amazon Q CLI.

**⏰ Thời gian:** 20 tháng 5 - 20 tháng 6, 2025  
**🌏 Khu vực:** Chỉ dành cho người tham gia từ khu vực Châu Á - Thái Bình Dương, Nhật Bản và Trung Quốc

### 🎁 Cách Nhận T-shirt Amazon Q

1. **Xây dựng game** sử dụng Amazon Q CLI
2. **Viết blog** hoặc **quay video** về trải nghiệm và đăng lên mạng xã hội
3. **Đăng ký nhận** T-shirt Amazon Q branded

---

## 🚀 Hướng Dẫn Từng Bước

### BƯỚC 1: Đăng Ký AWS Builder ID

1. Truy cập [AWS Builder ID](https://community.aws) để đăng ký
2. Tạo username unique trên community.aws
3. Tham gia Discord server để kết nối với cộng đồng builders

### BƯỚC 2: Cài Đặt Amazon Q CLI

#### Cài Đặt Trên Windows:

```powershell
# Cài đặt Amazon Q CLI
pip install amazon-q-cli

# Hoặc sử dụng npm
npm install -g @aws/amazon-q-cli

# Kiểm tra cài đặt
q --version
```

#### Cài Đặt PyGame (Thư Viện Game):

```bash
pip install pygame
pip install numpy
pip install matplotlib
```

#### Thiết Lập Ban Đầu:

```bash
# Khởi tạo Amazon Q CLI
q init

# Đăng nhập với AWS Builder ID
q auth login
```

### BƯỚC 3: Bắt Đầu Chat Với Amazon Q CLI

#### Khởi Tạo Session Chat:

```bash
# Bắt đầu chat session
q chat

# Hoặc tạo project mới
q create-project --name my-game --template pygame
```

#### Ví Dụ Prompts Hiệu Quả:

**🎯 Prompt Khởi Tạo Game:**
```
"Tôi muốn tạo một game Snake đơn giản bằng Python và PyGame. 
Hãy tạo cấu trúc project với:
- File main.py để chạy game
- Class Snake để quản lý rắn
- Class Food để quản lý thức ăn
- Game loop với collision detection
- Score system
- Game over screen"
```

**🎯 Prompt Cải Tiến Game:**
```
"Hãy thêm các tính năng sau vào game Snake:
- Sound effects khi ăn thức ăn và game over
- High score system lưu vào file
- Tăng tốc độ theo level
- Power-ups đặc biệt
- Menu chính với options"
```

**🎯 Prompt Tối Ưu Code:**
```
"Hãy review và tối ưu code game của tôi:
- Refactor để clean code hơn
- Thêm comments và documentation
- Implement design patterns phù hợp
- Optimize performance
- Add error handling"
```

---

## 🎮 Ví Dụ Các Loại Game Có Thể Xây Dựng

### 1. **Classic Arcade Games**
- **Snake Game**: Game rắn săn mồi cổ điển
- **Tetris**: Game xếp khối
- **Pong**: Game bóng bàn 2D
- **Pacman**: Game ăn đậu trong mê cung

### 2. **Puzzle Games**
- **2048**: Game ghép số
- **Sudoku Solver**: Trò chơi giải Sudoku
- **Memory Match**: Game lật thẻ ghi nhớ
- **Sliding Puzzle**: Game ghép hình trượt

### 3. **Action Games**
- **Space Invaders**: Game bắn phi thuyền
- **Flappy Bird**: Game điều khiển chim bay
- **Platformer**: Game nhảy cầu đơn giản
- **Tower Defense**: Game phòng thủ tháp

### 4. **Strategy Games**
- **Tic Tac Toe AI**: Cờ ca rô với AI
- **Chess Engine**: Động cơ cờ vua
- **Connect Four**: Game nối 4
- **Minesweeper**: Game dò mìn

---

## 💡 Kỹ Thuật Prompting Hiệu Quả

### 🔥 Best Practices cho Prompts:

1. **Mô Tả Chi Tiết:**
```
❌ "Tạo game"
✅ "Tạo game platformer 2D với character có thể jump, run, collect coins và có enemy AI"
```

2. **Chỉ Định Technical Requirements:**
```
✅ "Sử dụng PyGame, 60 FPS, resolution 800x600, với sprite animations"
```

3. **Yêu Cầu Code Structure:**
```
✅ "Organize code với separate classes cho Player, Enemy, Level, GameManager"
```

4. **Iterative Development:**
```
✅ "Trước tiên tạo basic movement, sau đó thêm gravity, collision detection, rồi enemies"
```

### 🎯 Prompts Cho Các Giai Đoạn Phát Triển:

#### **Giai Đoạn 1: Prototype**
```
"Tạo prototype đơn giản của [tên game] với core mechanics cơ bản. 
Chỉ cần basic graphics và minimum viable product."
```

#### **Giai Đoạn 2: Features**
```
"Thêm các features sau vào game:
- [Feature 1]: [mô tả chi tiết]
- [Feature 2]: [mô tả chi tiết]
Đảm bảo code maintainable và có comments"
```

#### **Giai Đoạn 3: Polish**
```
"Polish game với:
- Improved graphics và animations
- Sound effects và background music
- Smooth transitions và particle effects
- Settings menu và save/load system"
```

---

## 🛠️ Ví Dụ Development Workflow

### Workflow Xây Dựng Snake Game:

```bash
# Bước 1: Khởi tạo project
q chat "Tạo cấu trúc folder cho Snake game với PyGame"

# Bước 2: Tạo basic game loop
q chat "Tạo main.py với basic game loop: init, handle events, update, draw"

# Bước 3: Implement Snake
q chat "Tạo Snake class với movement, growth, collision detection"

# Bước 4: Add Food system
q chat "Tạo Food class spawn random positions, avoid snake body"

# Bước 5: Game mechanics
q chat "Implement score system, game over conditions, restart functionality"

# Bước 6: UI và Polish
q chat "Thêm start menu, high score display, sound effects"
```

---

## 📝 Code Examples và AI Solutions

### Example 1: AI-Generated Snake Game Structure

```python
# main.py - AI generated with Amazon Q CLI
import pygame
import sys
import random
from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = Direction.RIGHT
        self.grow_pending = False
    
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        self.body.insert(0, new_head)
        
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def grow(self):
        self.grow_pending = True
    
    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        
        # Wall collision
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return True
        
        # Self collision
        if (head_x, head_y) in self.body[1:]:
            return True
        
        return False

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width = 20
        self.height = 15
        self.cell_size = 30
        self.screen = pygame.display.set_mode(
            (self.width * self.cell_size, self.height * self.cell_size)
        )
        pygame.display.set_caption("Snake Game - Built with Amazon Q CLI")
        
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.width // 2, self.height // 2)
        self.food = self.spawn_food()
        self.score = 0
        self.running = True
    
    def spawn_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake.body:
                return (x, y)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
                    self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
                    self.snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
                    self.snake.direction = Direction.RIGHT
    
    def update(self):
        self.snake.move()
        
        # Check food collision
        if self.snake.body[0] == self.food:
            self.snake.grow()
            self.food = self.spawn_food()
            self.score += 10
        
        # Check game over
        if self.snake.check_collision(self.width, self.height):
            self.running = False
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # Draw snake
        for segment in self.snake.body:
            x, y = segment
            rect = pygame.Rect(
                x * self.cell_size, y * self.cell_size,
                self.cell_size, self.cell_size
            )
            pygame.draw.rect(self.screen, (0, 255, 0), rect)
        
        # Draw food
        food_x, food_y = self.food
        food_rect = pygame.Rect(
            food_x * self.cell_size, food_y * self.cell_size,
            self.cell_size, self.cell_size
        )
        pygame.draw.rect(self.screen, (255, 0, 0), food_rect)
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
```

### Example 2: AI Automation Đã Tiết Kiệm Thời Gian

```bash
# Thay vì viết manual, AI tự động generate:

# 1. Project structure
q chat "Setup complete pygame project structure with assets folder, sounds, fonts"

# 2. Boilerplate code
q chat "Generate game template với settings.py, utils.py, constants.py"

# 3. Asset management
q chat "Create asset loader class tự động load sprites, sounds, fonts"

# 4. Game states management
q chat "Implement state machine cho menu, gameplay, pause, game over"
```

---

## 🎥 Hướng Dẫn Tạo Blog/Video

### 📝 Template Blog Post:

```markdown
# Xây Dựng [Tên Game] với Amazon Q CLI - Trải Nghiệm AI Coding

## 🎮 Game Tôi Đã Chọn
- **Tên game:** [Tên game]
- **Lý do chọn:** [Tại sao chọn game này]
- **Mục tiêu:** [Những gì muốn đạt được]

## 🤖 Kỹ Thuật Prompting Hiệu Quả
- **Prompts khởi tạo:** [Ví dụ prompts]
- **Iterative development:** [Cách phát triển từng bước]
- **Debugging với AI:** [Cách AI giúp debug]

## 💡 AI Xử Lý Challenges Như Thế Nào
- **Collision detection:** [AI approach]
- **Game physics:** [AI solutions]
- **Performance optimization:** [AI suggestions]

## ⚡ Automation Tiết Kiệm Thời Gian
- **Code generation:** [Ví dụ auto-gen]
- **Boilerplate reduction:** [Template auto-create]
- **Testing automation:** [AI test cases]

## 🔧 Code Examples Thú Vị
```python
# Paste interesting AI-generated code here
```

## 📸 Screenshots & Gameplay
[Thêm screenshots và video gameplay]

## 🎯 Kết Luận
[Tổng kết trải nghiệm và học được gì]

#AmazonQCLI #GameDevelopment #AI #Coding
```

### 🎬 Video Content Structure:

1. **Intro (30s):** Giới thiệu bản thân và game
2. **Demo Game (1-2 phút):** Chơi thử game đã build
3. **Development Process (3-4 phút):** 
   - Show prompts sử dụng
   - Live coding với Q CLI
   - Explain challenges và solutions
4. **Code Review (2 phút):** Highlight interesting AI-generated code
5. **Lessons Learned (1 phút):** Những gì học được
6. **Outro (30s):** Kêu gọi like, share với hashtag #AmazonQCLI

---

## 🎁 Bước 5: Redeem T-shirt

### 📋 Yêu Cầu Blog/Video:

Đảm bảo nội dung bao gồm:
- ✅ Game bạn chọn và lý do
- ✅ Kỹ thuật prompting hiệu quả
- ✅ Cách AI xử lý programming challenges
- ✅ Ví dụ development automation
- ✅ Code examples thú vị từ AI
- ✅ Screenshots hoặc gameplay footage

### 📝 Redeem Form:
Sau khi đăng blog/video với hashtag **#AmazonQCLI**, điền form redeem T-shirt.

### 🌏 Quốc Gia Đủ Điều Kiện:
Australia, Bangladesh, Bhutan, Brunei, Cambodia, China, Fiji, Hong Kong, India, Indonesia, Japan, Laos, Malaysia, Maldives, Myanmar, Nepal, New Zealand, Pakistan, Papua New Guinea, Philippines, Singapore, South Korea, Sri Lanka, Taiwan, Thailand, **Vietnam**

---

## 🚀 Game Ideas Để Bắt Đầu

### 🎯 Beginner Level:
- **Rock Paper Scissors** với AI opponent
- **Number Guessing Game** với hints
- **Simple Calculator** với GUI
- **Digital Clock** với alarm

### 🎮 Intermediate Level:
- **Snake Game** với power-ups
- **Tetris Clone** với scoring
- **Pong Game** với AI paddle
- **Memory Card Game** với themes

### 🏆 Advanced Level:
- **Tower Defense** với multiple enemies
- **Platformer** với level editor
- **RPG Battle System** với turn-based combat
- **Racing Game** với physics

---

## 📚 Tài Nguyên Bổ Sung

### 🔗 Links Hữu Ích:
- [Amazon Q CLI Self Service Workshop](workshop-link)
- [Derek Bingham's Blog](blog-link)
- [Haowen Huang's Guide](guide-link)
- [Discord Community](discord-link)

### 📖 Learning Resources:
- PyGame Documentation
- Game Development Patterns
- AI Prompting Best Practices
- Game Design Principles

---

## ❓ FAQ

**Q: Tôi có thể viết code bằng tiếng Việt không?**  
A: Có! Bạn có thể prompt và comment bằng tiếng Việt, nhưng nên giữ tên variables và functions bằng tiếng Anh.

**Q: Game phải hoàn thiện 100% không?**  
A: Không! Prototype hoặc MVP cũng được chấp nhận, miễn là thể hiện được quá trình sử dụng AI.

**Q: Có thể collaborate với bạn bè không?**  
A: Có thể, nhưng mỗi người chỉ nhận được 1 T-shirt.

**Q: Deadline submit như thế nào?**  
A: T-shirt được ship mỗi thứ 6, submissions phải nộp trước thứ 4 của tuần đó.

---

## 🎉 Kết Luận

Campaign này là cơ hội tuyệt vời để:
- 🤖 Trải nghiệm AI coding assistant
- 🎮 Phát triển kỹ năng game development  
- 📝 Chia sẻ kiến thức với cộng đồng
- 🎁 Nhận được swag cool từ AWS

**Chúc bạn build game thành công và có những trải nghiệm thú vị với Amazon Q CLI!** 🚀

---

*Tài liệu này được tạo để hỗ trợ campaign "Build Games with Amazon Q CLI". Mọi thông tin chi tiết vui lòng tham khảo thông báo chính thức từ AWS.* 