import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船、一个子弹编组、一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")
    # 创建存储游戏统计数据信息的实例，并创建记分牌
    
    sb = Scoreboard(ai_settings,screen,stats)
    # 开始游戏的主循环
    while True:
         # 监视键盘和鼠标事件
         gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)
         if stats.game_avtive:
            ship.update()
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb) 
         # 每次循环时都重绘屏幕,并让最近绘制的屏幕可见
         gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)
run_game()
