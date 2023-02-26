import random


def main():
    """
    Plays the game until either the player or computer reaches 2001 points or more.
    Prints the winner at the end of the game.
    """
    player_points = 0
    computer_points = 0

    while player_points < 2001 and computer_points < 2001:
        # Player's turn
        player_dice = get_player_dice()
        input("Press Enter to roll the dice...")
        player_roll = roll_dice(player_dice)
        print("Player rolled", player_roll)
        player_points += player_roll

        # Check if player rolled a 7 or 11 and apply the appropriate bonus or penalty
        if player_roll == 7:
            player_points //= 7
        elif player_roll == 11:
            player_points *= 11

        # Check if the player has reached 2001 points or more and end the game if so
        if player_points >= 2001:
            break

        # Computer's turn
        computer_dice = get_computer_dice()
        computer_roll = roll_dice(computer_dice)
        print("Computer rolled", computer_roll)
        computer_points += computer_roll

        # Check if computer rolled a 7 or 11 and apply the appropriate bonus or penalty
        if computer_roll == 7:
            computer_points //= 7
        elif computer_roll == 11:
            computer_points *= 11

        # Print the current score
        print("Player points:", player_points)
        print("Computer points:", computer_points)

    # Print the winner of the game
    if player_points >= 2001:
        print("Player wins!")
    else:
        print("Computer wins!")


def get_player_dice():
    """
    Asks the player to choose two dice from a list of options.
    Returns a list of the sides of the chosen dice.
    """
    while True:
        dice_string = input(
            "Choose two dice from the following options: D3, D4, D6, D8, D10, D12, D20, D100 (separated by commas): ")
        dice = dice_string.split(",")
        if len(dice) != 2:
            print("Invalid number of dice. Please try again.")
        else:
            try:
                sides = [int(d[1:]) for d in dice]
                if all(s in [3, 4, 6, 8, 10, 12, 20, 100] for s in sides):
                    return sides
                else:
                    print("Invalid number of sides. Please try again.")
            except ValueError:
                print("Invalid dice format. Please try again.")


def get_computer_dice():
    """
    Randomly chooses a pair of dice from a list of options.
    Returns a list of the sides of the chosen dice.
    """
    dice_options = [[3, 3], [3, 4], [4, 4], [4, 6], [6, 6], [6, 8], [8, 8], [8, 10], [10, 10], [10, 12], [12, 12],
                    [12, 20], [20, 20], [10, 100], [20, 100]]
    return random.choice(dice_options)


def roll_dice(dice):
    """
    Rolls each die in the list of dice and returns the sum of the rolls.
    """
    rolls = [random.randint(1, sides) for sides in dice]
    return sum(rolls)


if __name__ == '__main__':
    main()
