# algorithm for quantity of lands provided by Frank Karsten 
# https://www.channelfireball.com/article/How-Many-Lands-Do-You-Need-in-Your-Deck-An-Updated-Analysis/cd1c1a24-d439-4a8e-b369-b936edb0b38a/


def land_count(avg_mana_cost, num_cheap_draw_ramp):
    num_lands = 31.42 + 3.13 * avg_mana_cost - 0.28 * num_cheap_draw_ramp
    return num_lands

# data for mana count vs sources provided by Frank Karsten. The empty fields were estimated by me
# https://www.channelfireball.com/article/How-Many-Sources-Do-You-Need-to-Consistently-Cast-Your-Spells-A-2022-Update/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/

def num_of_sources(mana_value, num_of_symbols):
    """Function that takes in the cheapest card that has the greatest number of mana symbols of a single color 
        that the player wants to cast on time (turn = n = mana value). Returns the number of sources the deck
        should have in order to cast that spell on time
        mana_color: STR - mana color of the card
        mana_value: INT - mana value of the card
        num_of_symbols: INT - how many symbols of the given color are there
        Returns: INT - the number of symbols of the given color needed"""

    val_to_sym_hash = {
             1: {1: 19},
             2: {1: 19, 2: 30},
             3: {1: 18, 2: 28, 3: 36},
             4: {1: 16, 2: 26, 3: 33, 4: 39},
             5: {1: 15, 2: 23, 3: 30, 4: 36},
             6: {1: 14, 2: 22, 3: 28, 4: 33},
             7: {1: 13, 2: 20, 3: 26, 4: 30}
             }

    # it's impossible to have a card with greater mana_symbols than value, so return False if so.
    # I don't have data on symbols >= 5, so until I get the time to get that, this will be the limit
    if num_of_symbols > mana_value or num_of_symbols > 4:
        return 101

    # model only goes up to 7, and that should be sufficient for 99.9% of deck cases.
    if mana_value > 7:
        return 201

    value = val_to_sym_hash[mana_value][num_of_symbols]

    return value

  
