namespace SpriteKind {
    export const gun = SpriteKind.create()
}
namespace StatusBarKind {
    export const Ammo = StatusBarKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    statusbar.setBarSize(60, 6)
    for (let index = 0; index < 10; index++) {
        statusbar.value += -1
        pause(100)
    }
    statusbar.setBarSize(0, 0)
    ammo = 16
    info.setScore(16)
    statusbar.value = 10
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (statusbar2.value >= 0) {
        if (ammo > 0) {
            Glock_19.setImage(assets.image`Glock 19 Fired Update`)
            music.play(music.createSong(assets.song`Glock Sound`), music.PlaybackMode.InBackground)
            ammo += -1
            info.changeScoreBy(-1)
            bullet = sprites.createProjectileFromSprite(assets.image`bullet`, Glock_19, 500, 0)
            bullet.scale = 0.5
            pause(50)
            Glock_19.setImage(assets.image`Glock 19 Update`)
        }
    }
})
info.onCountdownEnd(function () {
    game.gameOver(false)
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    statusbar2.setBarSize(0, 0)
    sprites.destroy(badguy)
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(bullet)
    statusbar2.value += -1
})
let bullet: Sprite = null
let statusbar2: StatusBarSprite = null
let statusbar: StatusBarSprite = null
let ammo = 0
let badguy: Sprite = null
let Glock_19: Sprite = null
game.splash("Boss fight!!", "B to reload and A to shoot")
info.startCountdown(120)
scene.setBackgroundImage(assets.image`bg`)
info.setScore(16)
let gamer = sprites.create(assets.image`player`, SpriteKind.Player)
controller.moveSprite(gamer, 0, 80)
gamer.setPosition(30, randint(2, 118))
gamer.setStayInScreen(true)
Glock_19 = sprites.create(assets.image`Glock 19 Update`, SpriteKind.gun)
Glock_19.scale = 0.7
Glock_19.setPosition(30, 55)
Glock_19.follow(gamer, 1000)
badguy = sprites.create(assets.image`badguy`, SpriteKind.Enemy)
badguy.setBounceOnWall(true)
badguy.setPosition(140, 52)
ammo = 16
statusbar = statusbars.create(60, 6, StatusBarKind.Ammo)
statusbar.max = 10
statusbar.value = 10
statusbar.positionDirection(CollisionDirection.Bottom)
statusbar.setBarSize(0, 0)
pause(1)
statusbar2 = statusbars.create(60, 8, StatusBarKind.Health)
statusbar2.positionDirection(CollisionDirection.Top)
statusbar2.max = 100
statusbar2.value = 100
statusbar2.y = 15
game.onUpdateInterval(400, function () {
    badguy.setVelocity(0, randint(randint(-100, -50), randint(100, 50)))
})
