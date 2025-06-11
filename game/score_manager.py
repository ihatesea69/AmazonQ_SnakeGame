import json
import os
from datetime import datetime

class ScoreManager:
    def __init__(self, filename="high_scores.json"):
        """Khởi tạo Score Manager"""
        self.filename = filename
        self.current_score = 0
        self.high_scores = self.load_high_scores()
    
    def load_high_scores(self):
        """Load high scores từ file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    return json.load(f)
            else:
                return []
        except:
            return []
    
    def save_high_scores(self):
        """Lưu high scores vào file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.high_scores, f, indent=2)
        except:
            pass
    
    def add_score(self, score, player_name="Player"):
        """Thêm score mới vào high scores"""
        score_entry = {
            "score": score,
            "player": player_name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.high_scores.append(score_entry)
        self.high_scores.sort(key=lambda x: x["score"], reverse=True)
        
        # Chỉ giữ top 10
        self.high_scores = self.high_scores[:10]
        self.save_high_scores()
    
    def is_high_score(self, score):
        """Kiểm tra xem score có phải là high score không"""
        if len(self.high_scores) < 10:
            return True
        return score > self.high_scores[-1]["score"]
    
    def get_high_scores(self):
        """Lấy danh sách high scores"""
        return self.high_scores
    
    def get_highest_score(self):
        """Lấy điểm cao nhất"""
        if self.high_scores:
            return self.high_scores[0]["score"]
        return 0
    
    def reset_current_score(self):
        """Reset điểm hiện tại"""
        self.current_score = 0
    
    def add_points(self, points):
        """Thêm điểm vào score hiện tại"""
        self.current_score += points
    
    def get_current_score(self):
        """Lấy điểm hiện tại"""
        return self.current_score 