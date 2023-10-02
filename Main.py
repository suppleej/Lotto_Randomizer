import random


def rand_list(game, plays):
    play_result = []
    if game == 'MM':
        max_white_ball = 70
        max_yellow_ball = 25
    elif game == 'PB':
        max_white_ball = 69
        max_yellow_ball = 26
    else:
        max_white_ball = 0
        max_yellow_ball = 0

    for num in range(plays):
        play_result.clear()

        # 5x white ball generator
        while len(play_result) < 5:
            ball = random.SystemRandom().randint(1, max_white_ball)
            if ball in play_result:
                continue
            else:
                play_result.append(ball)

        # PowerBall / MegaBall
        yellow_ball = random.SystemRandom().randint(1, max_yellow_ball)

        play_result.sort()
        play_result.append(game[0] + 'B: ' + str(yellow_ball))
        print(play_result)


program_running = True

while program_running:
    game_type = input('Mega Millions (MM) or Power Ball (PB)?\n')
    num_plays = int(input('How many plays?\n'))
    print(f'Game: {game_type}, Plays: {num_plays}.')
    rand_list(game_type.upper(), num_plays)

    response = input('Another? (Y/N)\n')
    if response.upper() == 'N':
        program_running = False
