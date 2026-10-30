@namespace
class SpriteKind:
    gun = SpriteKind.create()
@namespace
class StatusBarKind:
    Ammo = StatusBarKind.create()

def on_b_pressed():
    global ammo
    statusbar.set_bar_size(60, 6)
    for index in range(10):
        statusbar.value += -1
        pause(100)
    statusbar.set_bar_size(0, 0)
    ammo = 16
    info.set_score(16)
    statusbar.value = 10
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global ammo, bullet
    if statusbar2.value >= 0:
        if ammo > 0:
            Glock_19.set_image(assets.image("""
                Glock 19 Fired Update
                """))
            music.play(music.create_song(assets.song("""
                    Glock Sound
                    """)),
                music.PlaybackMode.IN_BACKGROUND)
            ammo += -1
            info.change_score_by(-1)
            bullet = sprites.create_projectile_from_sprite(assets.image("""
                bullet
                """), Glock_19, 500, 0)
            bullet.scale = 0.5
            pause(50)
            Glock_19.set_image(assets.image("""
                Glock 19 Update
                """))
        else:
            music.play(music.create_song(assets.song("""
                    No bullets
                    """)),
                music.PlaybackMode.IN_BACKGROUND)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.game_over(False)
info.on_countdown_end(on_countdown_end)

def on_on_zero(status):
    statusbar2.set_bar_size(0, 0)
    sprites.destroy(badguy)
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
badguy: Sprite = None
Glock_19: Sprite = None
game.splash("Boss fight!!", "B to reload and A to shoot")
info.start_countdown(120)
scene.set_background_image(assets.image("""
    bg
    """))
info.set_score(16)
gamer = sprites.create(assets.image("""
    player
    """), SpriteKind.player)
controller.move_sprite(gamer, 0, 80)
gamer.set_position(30, randint(2, 118))
gamer.set_stay_in_screen(True)
Glock_19 = sprites.create(assets.image("""
        Glock 19 Update
        """),
    SpriteKind.gun)
Glock_19.scale = 0.7
Glock_19.set_position(30, 55)
Glock_19.follow(gamer, 1000)
badguy = sprites.create(assets.image("""
    badguy
    """), SpriteKind.enemy)
badguy.set_bounce_on_wall(True)
badguy.set_position(140, 52)
ammo = 16
statusbar = statusbars.create(60, 6, StatusBarKind.Ammo)
statusbar.max = 10
statusbar.value = 10
statusbar.position_direction(CollisionDirection.BOTTOM)
statusbar.set_bar_size(0, 0)
pause(1)
statusbar2 = statusbars.create(60, 8, StatusBarKind.health)
statusbar2.position_direction(CollisionDirection.TOP)
statusbar2.max = 100
statusbar2.value = 100
statusbar2.y = 15

def on_update_interval():
    badguy.set_velocity(0, randint(randint(-100, -50), randint(100, 50)))
game.on_update_interval(400, on_update_interval)

def on_forever():
    if True:
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            if True:
                                if True:
                                    if True:
                                        if True:
                                            if True:
                                                if True:
                                                    if True:
                                                        if True:
                                                            if True:
                                                                if True:
                                                                    if True:
                                                                        if True:
                                                                            if True:
                                                                                if True:
                                                                                    if True:
                                                                                        if True:
                                                                                            if True:
                                                                                                if True:
                                                                                                    if True:
                                                                                                        if True:
                                                                                                            if True:
                                                                                                                if True:
                                                                                                                    if True:
                                                                                                                        if True:
                                                                                                                            if True:
                                                                                                                                if True:
                                                                                                                                    pass
forever(on_forever)
