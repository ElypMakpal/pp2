import pygame
import os


pygame.init()
pygame.mixer.init()

# музыкаға апаратын жол
song_elements_path = r"C:\pp2\lab 7\song elements"

# кнопокалар
playb = pygame.image.load(os.path.join(song_elements_path, "play.png"))
pausb = pygame.image.load(os.path.join(song_elements_path, "pause.png"))
nextb = pygame.image.load(os.path.join(song_elements_path, "next.png"))
prevb = pygame.image.load(os.path.join(song_elements_path, "back.png"))
background = pygame.image.load(os.path.join(song_elements_path, "background.png"))

# кнопкалардың размерлері
playb = pygame.transform.scale(playb, (50, 50))
pausb = pygame.transform.scale(pausb, (50, 50))
nextb = pygame.transform.scale(nextb, (50, 50))
prevb = pygame.transform.scale(prevb, (50, 50))
background = pygame.transform.scale(background, (700, 600))

# муз файлдар
music_files = [
    os.path.join(song_elements_path, "song1.mp3"),
    os.path.join(song_elements_path, "song2.mp3"),
    os.path.join(song_elements_path, "song3.mp3")
]
current_song = 0
pygame.mixer.music.load(music_files[current_song])


# Окно размері
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Координаты кнопок
play_rect = pygame.Rect(300, 500, 50, 50)
pause_rect = pygame.Rect(400, 500, 50, 50)
next_rect = pygame.Rect(500, 500, 50, 50)
prev_rect = pygame.Rect(200, 500, 50, 50)

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(playb, play_rect.topleft)
    screen.blit(pausb, pause_rect.topleft)
    screen.blit(nextb, next_rect.topleft)
    screen.blit(prevb, prev_rect.topleft)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                pygame.mixer.music.play()
            elif pause_rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
            elif next_rect.collidepoint(event.pos):
                current_song = (current_song + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
            elif prev_rect.collidepoint(event.pos):
                current_song = (current_song - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song])
                pygame.mixer.music.play()
    
    pygame.display.flip()

pygame.quit()