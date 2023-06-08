def player(prev_play, opponent_history=[]):
  if prev_play is None:
    prev_play = 'R'
  counter = {'P': 'S', 'R': 'P', 'S': 'R'}
  return counter.get(prev_play, "R")
