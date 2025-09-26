
import pygame
pygame.init()

## variabel global
scene_lebar = 600
scene_tinggi = 400
scene_judul = "pingpong seru  seruan"
gambar_bakgron = "backgron.png"
gambar_bola = "bola.png"
gambar_p1 = "player1.png"
gambar_p2 = "player2.png"
musik_bakgron = "energy.mp3"
GAME_ON = True
GAME_OVER = False

## scene
scene = pygame.display.set_mode((scene_lebar, scene_tinggi))
pygame.display.set_caption(scene_judul)
background = pygame.transform.scale(pygame.image.load(gambar_bakgron),
    (scene_lebar, scene_tinggi))

## tambah kelas untuk sprite
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, cepat):
        super().__init__()
        self.lebar = lebar
        self.tinggi = tinggi
        self.gambar = pygame.transform.scale(pygame.image.load(gambar),
            (self.lebar, self.tinggi))
        self.rect = self.gambar.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cepat = cepat
    def tampilkan(self):
        scene.blit(self.gambar, (self.rect.x, self.rect.y))
class Pemain(GameSprite):
    def gerak_p1(self):
        TOMBOL = pygame.key.get_pressed()
        if TOMBOL[pygame.K_a]: # ke atas
            self.rect.y -= self.cepat
        if TOMBOL[pygame.K_d]: # ke bawah
            self.rect.y += self.cepat
    def gerak_p2(self):
        TOMBOL = pygame.key.get_pressed()
        if TOMBOL[pygame.K_j]: # ke atas
            self.rect.y -= self.cepat
        if TOMBOL[pygame.K_l]: # ke bawah
            self.rect.y += self.cepat

## buat objek sprite
p1 = Pemain(gambar_p1, 50, 50, 50, 100, 20)
p2 = Pemain(gambar_p2, 450, 50, 50, 100, 20)
bola = GameSprite(gambar_bola, 250, 150, 50, 50, 10)

## buat game loop
FPS = pygame.time.Clock()
while GAME_ON:
    ## buat event quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False

    ## tampilkan yang perlu ditampilkan
    scene.blit(background, (0,0))
    p1.tampilkan()
    p2.tampilkan()
    bola.tampilkan()
    ## untuk pergerakkan
    p1.gerak_p1()
    p2.gerak_p2()

    ## bagian penting
    FPS.tick(60)
    pygame.display.update()









