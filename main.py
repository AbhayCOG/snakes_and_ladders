import random 

grid = int(input("Enter the grid size: "))
max_num = grid*grid

print()
player1=[]
player2=[]
player3=[]
player4=[]

p1_dice_roll_history = []
p2_dice_roll_history = []
p3_dice_roll_history = []
p4_dice_roll_history = []

pl1 = 0
pl2 = 0
pl3 = 0
pl4 = 0

while pl1<max_num or pl2<max_num or pl3<max_num or pl4<max_num:
    p1_dice_roll = random.randint(1,6)
    if pl1+p1_dice_roll < max_num:
        p1_dice_roll_history.append(p1_dice_roll)
        pl1 = pl1+p1_dice_roll
        player1.append(pl1)
    elif pl1+p1_dice_roll > max_num:
        p1_dice_roll_history.append(p1_dice_roll)
        player1.append(pl1)
    else:
        p1_dice_roll_history.append(p1_dice_roll)
        pl1 = pl1+p1_dice_roll
        player1.append(pl1)
        print("Player 1 is the Winner")
        break
    
    p2_dice_roll = random.randint(1,6)
    if pl2+p2_dice_roll < max_num:
        p2_dice_roll_history.append(p2_dice_roll)
        pl2 = pl2+p2_dice_roll
        player2.append(pl2)
    elif pl2+p2_dice_roll > max_num:
        p2_dice_roll_history.append(p2_dice_roll)
        player2.append(pl2)
    else:
        p2_dice_roll_history.append(p2_dice_roll)
        pl2 = pl2+p2_dice_roll
        player2.append(pl2)
        print("Player 2 is the Winner")
        break
    
    p3_dice_roll = random.randint(1,6)
    if pl3+p3_dice_roll < max_num:
        p3_dice_roll_history.append(p3_dice_roll)
        pl3 = pl3+p3_dice_roll
        player3.append(pl3)
    elif pl3+p3_dice_roll > max_num:
        p3_dice_roll_history.append(p3_dice_roll)
        player3.append(pl3)
    else:
        p3_dice_roll_history.append(p3_dice_roll)
        pl3 = pl3+p3_dice_roll
        player3.append(pl3)
        print("Player 3 is the Winner")
        break
    
    p4_dice_roll = random.randint(1,6)
    if pl4+p4_dice_roll < max_num:
        p4_dice_roll_history.append(p4_dice_roll)
        pl4 = pl4+p4_dice_roll
        player4.append(pl4)
    elif pl4+p4_dice_roll > max_num:
        p4_dice_roll_history.append(p4_dice_roll)
        player4.append(pl4)
    else:
        p4_dice_roll_history.append(p4_dice_roll)
        pl4 = pl4+p4_dice_roll
        player4.append(pl4)
        print("Player 4 is the Winner")
        break

print(f"Player 1 positions: {player1} \nPlayer 1 dice rolls: {p1_dice_roll_history}\n")
print(f"Player 2 positions: {player2} \nPlayer 2 dice rolls: {p2_dice_roll_history}\n")
print(f"Player 3 positions: {player3} \nPlayer 3 dice rolls: {p3_dice_roll_history}\n")
print(f"Player 4 positions: {player4} \nPlayer 4 dice rolls: {p4_dice_roll_history}\n")
