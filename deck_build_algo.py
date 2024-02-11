# algorithm for quantity of lands provided by Frank Karsten 
# https://www.channelfireball.com/article/How-Many-Lands-Do-You-Need-in-Your-Deck-An-Updated-Analysis/cd1c1a24-d439-4a8e-b369-b936edb0b38a/


def land_count(avg_mana_cost, num_cheap_draw_ramp):
  num_lands = 31.42 + 3.13 * avg_mana_cost – 0.28 * num_cheap_draw_ramp
  return num_lands

