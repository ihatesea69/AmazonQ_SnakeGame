import pygame
import os

class SoundManager:
    def __init__(self):
        """Khởi tạo Sound Manager"""
        pygame.mixer.init()
        self.sounds = {}
        self.music_playing = False
        self.sound_enabled = True
        
        # Tạo simple sound effects bằng pygame
        self.create_sound_effects()
    
    def create_sound_effects(self):
        """Tạo sound effects đơn giản bằng pygame"""
        try:
            # Tạo eat sound (tần số cao, ngắn)
            eat_sound = pygame.sndarray.make_sound(self._generate_tone(800, 0.1))
            self.sounds['eat'] = eat_sound
            
            # Tạo game over sound (tần số thấp, dài hơn)
            game_over_sound = pygame.sndarray.make_sound(self._generate_tone(200, 0.5))
            self.sounds['game_over'] = game_over_sound
            
            # Tạo special food sound (tần số biến đổi)
            special_sound = pygame.sndarray.make_sound(self._generate_special_tone())
            self.sounds['special'] = special_sound
            
        except:
            # Nếu không tạo được sound, tắt sound
            self.sound_enabled = False
    
    def _generate_tone(self, frequency, duration):
        """Tạo tone đơn giản"""
        import numpy as np
        sample_rate = 22050
        frames = int(duration * sample_rate)
        arr = np.zeros((frames, 2))
        
        for i in range(frames):
            wave = np.sin(2 * np.pi * frequency * i / sample_rate)
            arr[i] = [wave * 0.3, wave * 0.3]  # Volume 30%
        
        return (arr * 32767).astype(np.int16)
    
    def _generate_special_tone(self):
        """Tạo tone đặc biệt cho special food"""
        import numpy as np
        sample_rate = 22050
        duration = 0.3
        frames = int(duration * sample_rate)
        arr = np.zeros((frames, 2))
        
        for i in range(frames):
            # Tần số tăng dần
            frequency = 400 + (i / frames) * 400
            wave = np.sin(2 * np.pi * frequency * i / sample_rate)
            arr[i] = [wave * 0.2, wave * 0.2]
        
        return (arr * 32767).astype(np.int16)
    
    def play_sound(self, sound_name):
        """Phát sound effect"""
        if self.sound_enabled and sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except:
                pass
    
    def toggle_sound(self):
        """Bật/tắt sound"""
        self.sound_enabled = not self.sound_enabled
        return self.sound_enabled
    
    def set_volume(self, volume):
        """Đặt volume (0.0 - 1.0)"""
        pygame.mixer.set_volume(volume)
    
    def is_sound_enabled(self):
        """Kiểm tra sound có được bật không"""
        return self.sound_enabled 