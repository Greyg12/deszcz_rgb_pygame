import pygame
import random

pygame.init()
pygame.mixer.init()

# Ustawienia szerokości i wysokości ekranu
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Wczytanie i odtworzenie dźwięku deszczu
try:
    pygame.mixer.music.load('rain_sound.mp3')  # Upewnij się, że plik 'rain_sound.mp3' jest w tym samym katalogu
    pygame.mixer.music.set_volume(0.05) # Ustawienie poziomu głośności wartosci z przedziału [0, 1]
    pygame.mixer.music.play(-1)  # -1 oznacza nieskończone powtarzanie
except pygame.error:
    print('Nie udało się wczytać pliku dźwiękowego. Upewnij się, że plik istnieje i jest w poprawnym formacie.')

# Zdefiniowanie liczby kropli deszczu do symulacji
num_raindrops = 100

# Zdefiniowanie prędkości kropli deszczu
raindrop_speed = 0.3

# Zdefiniowanie kolorów kropli deszczu
raindrop_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (127, 127, 9)]

class Raindrop:
    def __init__(self):
        # Inicjalizacja pozycji kropli deszczu losowo
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)

        # Ustawienie prędkości kropli
        self.speed = raindrop_speed

        # Wybór losowego koloru kropli deszczu
        self.color = random.choice(raindrop_colors)

    def fall(self):
        # Aktualizacja pozycji kropli w osi Y w zależności od prędkości
        self.y += self.speed

        # Jeśli kropla spadnie poniżej ekranu, resetuje swoją pozycję
        if self.y > screen_height:
            self.y = 0
            self.x = random.randint(0, screen_width)

# Tworzenie listy kropli deszczu raz, przed główną pętlą gry
raindrops = [Raindrop() for _ in range(num_raindrops)]

# Główna pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wypełnienie ekranu kolorem tła
    screen.fill((0, 0, 0))  # Czarny kolor tła (ciemne niebo)

    # Rysowanie i aktualizowanie każdej kropli
    for raindrop in raindrops:
        # Rysowanie kropli jako linii na ekranie
        pygame.draw.line(screen, raindrop.color, (raindrop.x, raindrop.y), (raindrop.x, raindrop.y + 5), 2)
        raindrop.fall()  # Aktualizacja pozycji kropli (spadanie)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zatrzymanie odtwarzania muzyki i zakończenie działania Pygame
pygame.mixer.music.stop()
pygame.quit()
