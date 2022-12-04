
options = {
    'X': {
        'type': 'rock',
        'score': 1
    },
    'Y': {
        'type': 'paper',
        'score': 2
    },
    'Z': {
        'type': 'scissors',
        'score': 3
    }
}

result_mapping = {
    'X': -1,
    'Y': 0,
    'Z': 1
}

opp_mapping = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

results = {
    'rock': {
        'rock': 0,
        'paper': -1,
        'scissors': 1
    },
    'paper': {
        'rock': 1,
        'paper': 0,
        'scissors': -1
    },
    'scissors': {
        'rock': -1,
        'paper': 1,
        'scissors': 0
    }
}

result_scores = {
    1: 6,
    0: 3,
    -1: 0
}

def game(player, opp, strategy: 0):
    ''' Play one game '''
    # get Opponents move
    opp_option = options[opp_mapping[opp]]

    # get Strategy option
    if strategy == 0:
        player_option = options[player]
    
    elif strategy == 1:
        player_option = get_reaction(player, opp)
    
    result = results[player_option['type']][opp_option['type']]

    return result_scores[result] + player_option['score']


def get_reaction(player, opp):
    ''' Get required reaction for the second strategy '''
    desired_result = result_mapping[player]
    opp_option = results[options[opp_mapping[opp]]['type']]
    player_option = [option for option in opp_option.keys() if opp_option[option] == -desired_result]
    player_option_detail = [options[key] for key in options if options[key]['type'] == player_option[0]]

    return player_option_detail[0]


path = '2022/02/input.txt'

with open(path, 'r') as file:
    input = file.read()

## get contests in usable format
contests = [contest.split(' ') for contest in input.split('\n')]

## sum scores of all individual games with strategy 1
score_1 = sum([game(contest[1], contest[0], 0) for contest in contests if contest[0] != ''])
print(score_1)

## sum scores of all individual games with strategy 2
score_2 = sum([game(contest[1], contest[0], 1) for contest in contests if contest[0] != ''])
print(score_2)
