import random


def play(player1, player2, num_games, verbose=False):
  p1_prev_play = ""
  p2_prev_play = ""
  results = {"p1": 0, "p2": 0, "tie": 0}

  for _ in range(num_games):
    p1_play = player1(p2_prev_play)
    p2_play = player2(p1_prev_play)

    if p1_play == p2_play:
      results["tie"] += 1
      winner = "Tie."
    elif (p1_play == "P"
          and p2_play == "R") or (p1_play == "R"
                                  and p2_play == "S") or (p1_play == "S"
                                                          and p2_play == "P"):
      results["p1"] += 1
      winner = "Player 1 wins."
    elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
      results["p2"] += 1
      winner = "Player 2 wins."

    if verbose:
      print("Player 1:", p1_play, "| Player 2:", p2_play)
      print(winner)
      print()

    p1_prev_play = p1_play
    p2_prev_play = p2_play

  games_won = results['p2'] + results['p1']

  if games_won == 0:
    win_rate = 0
  else:
    win_rate = results['p1'] / games_won * 100

  print("Final results:", results)
  print(f"Player 1 win rate: {win_rate}%")

  return (win_rate)


def peter(prev_opponent_play):
  if prev_opponent_play == 'R':
    r = random.choice(['P', 'S'])
  elif prev_opponent_play == 'P':
    r = random.choice(['R', 'S'])
  elif prev_opponent_play == 'S':
    r = random.choice(['P', 'R'])
  else:
    return random.choice(['R', 'P', 'S'])
  return r


def miles(prev_opponent_play):

  if prev_opponent_play is None:
    prev_opponent_play = 'R'
  counter = {'P': 'R', 'R': 'S', 'S': 'P'}
  return counter.get(prev_opponent_play, "R")


def gwen(prev_opponent_play, opponent_history=[]):
  opponent_history.append(prev_opponent_play)
  last_ten = opponent_history[-10:]
  most_used = max(set(last_ten), key=last_ten.count)

  if most_used is None:
    most_used = "R"

  counter = {'P': 'R', 'R': 'S', 'S': 'P'}
  return counter.get(most_used, "R")


def mj(prev_opponent_play, opponent_history=[]):
  opponent_history.append(prev_opponent_play)
  last_ten = opponent_history[-10:]
  least_used = min(set(last_ten), key=last_ten.count)

  if least_used is None:
    least_used = "P"

  counter = {'P': 'R', 'R': 'S', 'S': 'P'}
  return counter.get(least_used, "P")
