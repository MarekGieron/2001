import random


def main():
    """
    Main function that runs the game.
    """
    player_points = 0
    computer_points = 0

    while player_points < 2001 and computer_points < 2001:
        # Wait for user to press Enter to roll the dice
        input("Press Enter to roll the dice...")

        # Roll dice for player and add points
        player_roll = roll_dice()
        print("Player rolled", player_roll)
        player_points += player_roll

        # Apply special rules for certain rolls
        if player_roll == 7:
            player_points //= 7
        elif player_roll == 11:
            player_points *= 11

        # Check if player has won
        if player_points >= 2001:
            break

        # Roll dice for computer and add points
        computer_roll = roll_dice()
        print("Computer rolled", computer_roll)
        computer_points += computer_roll

        # Apply special rules for certain rolls
        if computer_roll == 7:
            computer_points //= 7
        elif computer_roll == 11:
            computer_points *= 11

        # Print current scores
        print("Player's current points:", player_points)
        print("Computer's current points:", computer_points)

    # Check who won the game
    if player_points >= 2001:
        print("Player wins!")
    else:
        print("Computer wins!")


def roll_dice():
    """
    Simulates rolling two dice and returns the sum of the rolls.
    """
    return random.randint(1, 6) + random.randint(1, 6)


if __name__ == '__main__':
    main()
