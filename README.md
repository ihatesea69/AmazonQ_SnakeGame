# 🐍 Snake Game - Built with Amazon Q CLI

![Snake Game](https://img.shields.io/badge/Game-Snake-green) ![Python](https://img.shields.io/badge/Python-3.7+-blue) ![PyGame](https://img.shields.io/badge/PyGame-2.5+-red)

Một game Snake cổ điển được xây dựng hoàn toàn bằng Python và PyGame, được phát triển với sự hỗ trợ của Amazon Q CLI.

## 🎮 Tính Năng

### Core Features:
- ✅ **Classic Snake Gameplay** - Di chuyển rắn ăn thức ăn và lớn dần
- ✅ **Collision Detection** - Va chạm với tường và chính mình
- ✅ **Score System** - Hệ thống tính điểm với high scores
- ✅ **Level Progression** - Tăng tốc độ theo level
- ✅ **Game States** - Menu, Playing, Paused, Game Over, High Scores

### Advanced Features:
- 🎵 **Sound Effects** - Âm thanh khi ăn thức ăn và game over
- ⭐ **Special Food** - Thức ăn đặc biệt với điểm số cao hơn
- 💾 **High Score Save** - Lưu top 10 điểm cao nhất
- 🎨 **Clean UI** - Giao diện đẹp với multiple screens
- ⏸️ **Pause Function** - Tạm dừng game bất cứ lúc nào

## 🚀 Cài Đặt và Chạy

### Bước 1: Clone Repository
```bash
git clone <repository-url>
cd AmazonQGame
```

### Bước 2: Cài Đặt Dependencies
```bash
pip install -r requirements.txt
```

### Bước 3: Chạy Game
```bash
python main.py
```

## 🎯 Cách Chơi

### Điều Khiển:
- **🔼 Arrow Keys** - Di chuyển rắn (Lên/Xuống/Trái/Phải)
- **SPACE** - Bắt đầu game mới / Chơi lại
- **P** - Tạm dừng/Tiếp tục
- **H** - Xem bảng điểm cao
- **R** - Restart game hiện tại
- **ESC** - Về menu chính / Thoát game

### Mục Tiêu:
1. Điều khiển rắn ăn thức ăn (hình vuông đỏ)
2. Mỗi lần ăn, rắn sẽ dài ra và bạn được điểm
3. Tránh va chạm với tường và thân rắn
4. Thu thập thức ăn đặc biệt (màu vàng/tím) để được điểm cao hơn
5. Cố gắng đạt điểm cao nhất!

## 📁 Cấu Trúc Project

```
AmazonQGame/
├── main.py                     # Entry point chính
├── requirements.txt            # Dependencies
├── README.md                   # Tài liệu hướng dẫn
├── BUILD_GAMES_WITH_AMAZON_Q_CLI_GUIDE.md  # Campaign guide
├── high_scores.json           # File lưu high scores (auto-generated)
└── game/                      # Game package
    ├── __init__.py           # Package initializer
    ├── constants.py          # Game constants và settings
    ├── snake.py              # Snake class logic
    ├── food.py               # Food class logic
    ├── game_state.py         # Game state management
    ├── score_manager.py      # Score và high scores
    ├── sound_manager.py      # Sound effects
    └── ui.py                 # UI rendering
```

## 🎨 Game Components

### 1. Snake (`game/snake.py`)
- Movement logic với direction control
- Growth mechanism
- Collision detection (wall & self)
- Visual rendering với head/body distinction

### 2. Food (`game/food.py`)
- Random spawning tránh snake body
- Special food với bonus points
- Visual effects (blinking cho special food)

### 3. Game State Management (`game/game_state.py`)
- State machine: Menu → Playing → Paused/GameOver
- Clean transitions giữa các states

### 4. Score System (`game/score_manager.py`)
- Current score tracking
- High scores persistence (JSON file)
- Top 10 leaderboard với timestamps

### 5. Sound Effects (`game/sound_manager.py`)
- Procedural sound generation
- Different tones cho different events
- Volume control và toggle

### 6. UI System (`game/ui.py`)
- Multiple screens rendering
- Text rendering với multiple fonts
- Visual feedback và instructions

## 🔧 Technical Details

### Requirements:
- **Python 3.7+**
- **PyGame 2.5+**
- **NumPy 1.24+** (cho sound generation)

### Performance:
- **60 FPS** rendering
- **Grid-based** movement system
- **Efficient** collision detection
- **Minimal** memory footprint

### Code Quality:
- **Object-oriented** design
- **Modular** architecture
- **Type hints** support
- **Comprehensive** error handling
- **Vietnamese comments** cho dễ hiểu

## 🎯 Game Mechanics

### Scoring:
- **Normal Food**: 10 điểm
- **Special Food**: 20 điểm
- **Level Up**: Mỗi 50 điểm tăng 1 level

### Difficulty:
- **Speed**: Tăng theo level (max 3x tốc độ ban đầu)
- **Special Food**: 10% chance spawn
- **Collision**: Instant game over

### Features:
- **Persistent High Scores**: Lưu trong `high_scores.json`
- **Game Pause**: Không mất progress
- **Restart**: Bắt đầu lại ngay lập tức
- **Clean Exit**: Proper cleanup khi thoát

## 🛠️ Development với Amazon Q CLI

Game này được phát triển hoàn toàn với sự hỗ trợ của Amazon Q CLI, demonstrating:

### AI-Assisted Development:
- **Code Generation**: Tạo boilerplate và structure
- **Logic Implementation**: Collision detection, game mechanics
- **Error Handling**: Robust exception handling
- **Optimization**: Performance improvements

### Best Practices được AI suggest:
- **Modular Design**: Separate concerns
- **State Management**: Clean state transitions
- **Resource Management**: Proper cleanup
- **User Experience**: Intuitive controls

## 🏆 High Scores

Game tự động lưu top 10 điểm cao nhất vào file `high_scores.json`. Format:
```json
[
  {
    "score": 150,
    "player": "Player",
    "date": "2025-01-XX XX:XX:XX"
  }
]
```

## 🎮 Screenshots

*Game sẽ hiển thị:*
- **Main Menu**: Với options và instructions
- **Gameplay**: Grid-based với snake (xanh) và food (đỏ/vàng)
- **Pause Screen**: Overlay trong suốt
- **Game Over**: Final score và high score notification
- **High Scores**: Top 10 leaderboard

## 🤝 Contributing

Game này được tạo cho campaign "Build Games with Amazon Q CLI". 

Để tham gia campaign:
1. Build game của bạn với Amazon Q CLI
2. Viết blog hoặc quay video về trải nghiệm
3. Đăng với hashtag **#AmazonQCLI**
4. Redeem T-shirt miễn phí!

## 📄 License

Created for educational purposes and Amazon Q CLI campaign demonstration.

## 🎉 Acknowledgments

- **Amazon Q CLI** - AI coding assistant
- **PyGame Community** - Game development framework
- **Open Source** - Making game development accessible

---

**Enjoy the game and happy coding with Amazon Q CLI! 🐍🎮** 