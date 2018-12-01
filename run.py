from board import Board
from BoardElements import BoardElement, Platform, Cloud, Win, Pit, Pit2
from tunnel import Tunnel
from coins import Coins
from brick import Brick
from ememy import Enemy
from characters import Characters
from mario import Mario
import os
from utils import Get, input_to
import sys, subprocess
# elements,coins
getch = Get()

board = Board(34,400)
P = Platform(2,4)
Win = Win(3,8)
superMario = Mario("Mario", 2,4)
superMario.NewPosition(board, 26,1)

os.system("clear")

P.addelements(board,28,34,0,396)
P.addelements(board,0,6,208,396)
Win.youWin(board)

clouds = []
for _ in range(0, 15):
    clouds.append(Cloud(3, 7))
    clouds[_].addCloud(board)

tunnels = []
for _ in range(0, 10):
    tunnels.append(Tunnel(3, 5))
    tunnels[_].placeTunnel(board)

bricks = []
for i in range(0, 30):
    bricks.append(Brick(2, 4))
    bricks[i].placeBrick(board)

pits = []
for i in range(0, 10):
    pits.append(Pit(2, 4))
    pits[i].addPit(board)

pits2 = []
for i in range(0, 10):
    pits2.append(Pit2(2, 4))
    pits2[i].addPit2(board)

coins = []
for _ in range(0, 10):
    coins.append(Coins(2, 4))
    coins[_].placeCoin(board)

enemies = []
for i in range(0, 10):
    enemies.append(Enemy('enemy',2, 4))
    enemies[i].addEnemy(board)

NoEnemies = 10
NoCoins = 10
NoBricks = 30

print(board.returnStringBoard(superMario))
potential = 0
kinetic= 0
loop = 0
jump = 0

def play_mp3(path):
    subprocess.Popen(['open', path])

play_mp3('./SuperMarioBros.mp3')

while True:
    loop += 1
    input = input_to(getch)
    print(input)
    os.system('clear')
    print(board.returnStringBoard(superMario))
    print(potential)
    if input == 'q':
        subprocess.Popen(['osascript', './stopscript'])
        # subprocess.run(['kill', music])
        os.system('clear')
        sys.exit()

    if potential == 0 and loop % 2 ==0:
        kinetic -=1 
        if superMario.Down(board) == 1:
            jump -= 1 if jump else 0
            kinetic = 0
    
    if potential:
        kinetic += 1 
        potential -= 1
        superMario.Up(board)

    if input == 'w' and jump < 2:
        jump += 1
        potential += 3
        kinetic += 0
    
    if input == 'a':
        superMario.Left(board)
    
    if input == 'd':
        superMario.Right(board)

    for enemy in enemies:
        enemy.randomMove(board,superMario)
    
    superMario.checkDeath(enemies,pits, pits2,board)

    enemies = [e for e in enemies if not e.checkKill(superMario, board)]
    coins = [e for e in coins if not e.checkKill(superMario, board)]
    bricks = [e for e in bricks if not e.checkKill(superMario, board)]
    
    Win.checkKill(superMario,board)
