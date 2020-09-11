class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Параметры корабля
        self.ship_speed_factor = float(1.5)
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
