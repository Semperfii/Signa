def compute_scoring(users, matchs):
    users_indexed = {}
    for user in users:
        user['score'] = 0
        user['matches'] = 0
        user['victories'] = 0
        user['looses'] = 0
        user['goal_average'] = 0
        users_indexed[user['id']] = user

    for match in matchs:
        if not match['contested']:
            teamAB = [match['playerA'], match['playerB']]
            teamCD = [match['playerC'], match['playerD']]
            if match['scoreAB'] == 0:
                # AB has loosed
                loosers = teamAB
                winners = teamCD
                useful_score = match['scoreCD']
            elif match['scoreCD'] == 0:
                # CD has loosed
                loosers = teamCD
                winners = teamAB
                useful_score = match['scoreAB']
            else:
                raise Exception

            if useful_score == 1:
                goal_loosers = 2
                goal_winners = 3
            elif 2 <= useful_score <= 4:
                goal_loosers = 1
                goal_winners = 3
            elif 5 <= useful_score <= 7:
                goal_loosers = 1
                goal_winners = 4
            elif 8 <= useful_score <= 10:
                goal_loosers = 1
                goal_winners = 5
            else:
                raise Exception

            for player in loosers:
                users_indexed[player]['score'] += goal_loosers
                users_indexed[player]['matches'] += 1
                users_indexed[player]['looses'] += 1
                users_indexed[player]['goal_average'] -= useful_score
            for player in winners:
                users_indexed[player]['score'] += goal_winners
                users_indexed[player]['matches'] += 1
                users_indexed[player]['victories'] += 1
                users_indexed[player]['goal_average'] += useful_score

    users = []
    for id in users_indexed.keys():
        user = users_indexed[id]
        if user['matches'] > 0:
            users.append(user)

    return sorted(users, key=lambda x: (x['score'], -1 * x['matches'], x['victories'], x['goal_average']), reverse=True)
