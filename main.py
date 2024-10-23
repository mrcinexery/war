"""
Module represents the flow of the card game war.
"""
from deck import Deck
from game import Game
from player import Player

if __name__ == "__main__":
    deck = Deck()
    deck.init_deck()
    player1 = Player('Player1')
    player2 = Player('Player2')
    #game.player2.input_name()
    player1.set_name("Marc")
    player2.set_name("Anika")
    game = Game(player1, player2)
    game.print_rules()
    #game.player1.input_name()

    GAME_IS_RUNNING = True

    while True:

        deck.init_deck()
        player1.set_deck(deck.get_first_half_deck())
        player2.set_deck(deck.get_second_half_deck())
        ROUND_COUNTER = 0

        while GAME_IS_RUNNING:

            print(f'No. of rounds: {ROUND_COUNTER}')

            print(f'Deck size: {player1.get_deck_size()}')
            print(f'Deck size: {player2.get_deck_size()}')

            if player1.get_deck().get_size() == 0:
                print(f'{player1.get_name()} has no cards left.')
                print(f'{player2.get_name()} has won.!')
                player2.increment_score()
                break

            if player2.get_deck().get_size() == 0:
                print(f'{player2.get_name()} has no cards left.')
                print(f'{player1.get_name()} has won.!')
                player1.increment_score()
                break

            if game.is_cyclic():
                print(
                    "Cyclic distribution discovered! Game will be abborted!.")
                break


            card_pl1 = player1.get_deck().get_top_card()
            card_pl2 = player2.get_deck().get_top_card()

            game.print_battle(card_pl1, card_pl2)

            if card_pl1 is not None and card_pl2 is not None:

                if card_pl1.get_value() > card_pl2.get_value():
                    print(
                        f'{card_pl1.get_name()} beats'
                        f'{card_pl2.get_name()}...')

                    player1.put_under_deck(card_pl1)
                    player1.put_under_deck(card_pl2)
                    (player1.put_under_deck
                     (game.get_distributed_side_decks()))

                elif card_pl1.get_value() < card_pl2.get_value():
                    print(
                        f'{card_pl2.get_name()} beats'
                        f'{card_pl1.get_name()}...')
                    player2.put_under_deck(card_pl1)
                    player2.put_under_deck(card_pl2)

                    (player2.put_under_deck
                     (game.get_distributed_side_decks()))

                else:
                    print(f'{card_pl2.get_name()} and {card_pl1.get_name()}'
                          f' are equal strong...')
                    player1.put_on_side_deck(card_pl1)
                    player2.put_on_side_deck(card_pl2)

            ROUND_COUNTER += 1

        if not game.new_game():
            break
