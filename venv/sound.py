import pygame.mixer

pygame.mixer.init()
current_volume = 0.5

def set_music_volume(volume):
    global current_volume
    current_volume = volume
    pygame.mixer.music.set_volume(current_volume)

def play_menu_music():
    pygame.mixer.music.load("sounds/menu_music.mp3")
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)  # Loop indefinitely

def play_gameplay_music():
    pygame.mixer.music.load("sounds/gameplay_music.mp3")
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)  # Loop indefinitely

def play_defeat_music():
    pygame.mixer.music.load("sounds/defeat_music.mp3")
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)  # Loop indefinitely

def stop_music():
    pygame.mixer.music.stop()