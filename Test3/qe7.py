Game_leaderboard = [49,39,29,19,9,50]
for i in range(len(Game_leaderboard)):
    for j in range(len(Game_leaderboard) - i - 1):
        if Game_leaderboard[j] < Game_leaderboard[j + 1]:
            Game_leaderboard[j], Game_leaderboard[j + 1] = Game_leaderboard[j + 1], Game_leaderboard[j]
print("Sorted Game_leaderboard:", Game_leaderboard)