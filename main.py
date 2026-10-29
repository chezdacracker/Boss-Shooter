@namespace
class SpriteKind:
    gun = SpriteKind.create()
@namespace
class StatusBarKind:
    Ammo = StatusBarKind.create()

def on_b_pressed():
    global ammo
    statusbar.set_bar_size(60, 8)
    for index in range(15):
        statusbar.value += -1
        pause(100)
    pause(100)
    statusbar.set_bar_size(0, 0)
    ammo = 16
    info.set_score(16)
    statusbar.value = 15
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global ammo, bullet
    if ammo > 0:
        Glock_19.set_image(assets.image("""
            Glock 19 fired
            """))
        music.play(music.create_song(assets.song("""
                Glock Sound
                """)),
            music.PlaybackMode.IN_BACKGROUND)
        ammo += -1
        info.change_score_by(-1)
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . 4 5 5 4 . . . . . . . . . . .
                4 5 2 b b b b . . . . . . . . .
                2 4 b b b b b b b b . . . . . .
                4 . b b b b b b b b b b . . . .
                . . b b b b b b b b b b b . . .
                . . b b b b b b b b b b b b . .
                . . b b b b b b b b b b b b b .
                . . b b b b b b b b b b b b b .
                . . b b b b b b b b b b b b . .
                . . b b b b b b b b b b b . . .
                . . b b b b b b b b b b . . . .
                2 4 b b b b b b b b . . . . . .
                4 2 5 b b b b . . . . . . . . .
                . 4 2 5 4 . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            Glock_19,
            500,
            0)
        bullet.scale = 0.5
        pause(50)
        Glock_19.set_image(assets.image("""
            Glock 19
            """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_zero(status):
    game.game_over(True)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(bullet)
    statusbar2.value += -1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

bullet: Sprite = None
statusbar2: StatusBarSprite = None
statusbar: StatusBarSprite = None
ammo = 0
Glock_19: Sprite = None
scene.set_background_color(9)
info.set_score(16)
gamer = sprites.create(img("""
        ................................................
        ....ffffff......................................
        ..ffeeeef2f.....................................
        .ffeeeef222f....................................
        .feeeffeeeef....................................
        .ffffee2222ef...................................
        .fe222ffffe2f...................................
        fffffffeeeff....................................
        ffe44ebf44e.....................................
        fee4d41fdde.....................................
        .feee4ddded.....................................
        ..ffee44e4dde...................................
        ...f222244ee....................................
        ...f2222e2f.....................................
        ...f444455f.....................................
        ....ffffff......................................
        .....fff........................................
        ................................................
        ................................................
        ................................................
        ................................................
        ................................................
        ................................................
        ................................................
        """),
    SpriteKind.player)
controller.move_sprite(gamer, 0, 80)
gamer.set_position(30, randint(2, 118))
gamer.set_stay_in_screen(True)
Glock_19 = sprites.create(assets.image("""
    Glock 19
    """), SpriteKind.gun)
Glock_19.scale = 0.7
Glock_19.set_position(30, 55)
Glock_19.follow(gamer, 1000)
badguy = sprites.create(img("""
        . . . b 5 b . . . . . . . . . .
        . . . . b 5 b . . . . . . . . .
        . . . . b b b b b b . . . . . .
        . . . b 5 5 5 5 5 b b . . . . .
        . . f d 5 5 f 1 d 5 b b . . . .
        . . c 4 d 5 f f 1 5 5 b . . . .
        . . 4 4 d d b f d 5 5 b . . . .
        b 4 4 4 4 4 5 5 5 5 5 d b b b .
        . b 4 4 4 4 4 5 5 d b b d d d b
        . . b 5 5 5 5 5 5 b 5 5 5 d b b
        . b 5 5 5 5 5 5 d 5 5 5 5 c d c
        . b 5 5 5 5 5 5 b 5 5 d c d b c
        . b d 5 5 5 5 5 d b c c d d c .
        . . b b 5 5 5 d d d d d b c . .
        . . . b b c c c c c c c c . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.enemy)
badguy.set_bounce_on_wall(True)
badguy.set_position(140, 52)
ammo = 16
statusbar = statusbars.create(60, 8, StatusBarKind.Ammo)
statusbar.max = 15
statusbar.value = 15
statusbar.position_direction(CollisionDirection.BOTTOM)
statusbar.set_bar_size(0, 0)
pause(1)
statusbar2 = statusbars.create(60, 8, StatusBarKind.health)
statusbar2.position_direction(CollisionDirection.TOP)
statusbar2.max = 100
statusbar2.value = 100

def on_update_interval():
    badguy.set_velocity(0, randint(-100, 100))
game.on_update_interval(100, on_update_interval)
