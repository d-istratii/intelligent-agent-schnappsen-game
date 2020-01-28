"""
MyBot - Describe here
"""

# Import the API objects
from api import State
from api import Deck
import random


class Bot:

    def __init__(self):
        pass

    def findNextSmallestCardOfSameSuit(self, state):
        highestRank = None
        position = None
        moves = state.moves()

        # Opponents card rank
        opponentsCardRank = Deck.get_rank(state.get_opponents_played_card())
        # Opponents card suit
        opponentsCardSuit = Deck.get_suit(state.get_opponents_played_card())

        moves_trump_suit = []

        # Get all trump suit moves available
        for index, move in enumerate(moves):

            if moves[index][0] is not None and Deck.get_suit(moves[index][0]) == opponentsCardSuit:
                moves_trump_suit.append(move)

        # Check your hand for same suit cards as opponent
        # If opponent's card rank is '10' check for 'A' and play it
        if len(moves_trump_suit) > 0:
            if opponentsCardRank == "10":
                for index, move in enumerate(moves_trump_suit):
                    if Deck.get_rank(moves_trump_suit[index][0]) == "A" \
                            and Deck.get_suit(moves_trump_suit[index][0] == opponentsCardSuit):
                        highestRank = "A"
                        break

            # else if rank is 'K' look for '10' and play it else, look for 'A' and keep looking in the pack maybe '10' will be found later
            elif opponentsCardRank == "K":
                for index, move in enumerate(moves_trump_suit):
                    if Deck.get_rank(moves_trump_suit[index][0]) == "10" \
                            and Deck.get_suit(moves_trump_suit[index][0] == opponentsCardSuit):
                        highestRank = "10"
                        break

            elif opponentsCardRank == "Q":
                for index, move in enumerate(moves_trump_suit):
                    if Deck.get_rank(moves_trump_suit[index][0]) == "K" \
                            and Deck.get_suit(moves_trump_suit[index][0] == opponentsCardSuit):
                        highestRank = "K"
                        break

            elif opponentsCardRank == "J":
                for index, move in enumerate(moves_trump_suit):
                    if Deck.get_rank(moves_trump_suit[index][0]) == "Q" \
                            and Deck.get_suit(moves_trump_suit[index][0] == opponentsCardSuit):
                        highestRank = "Q"
                        position = index
                        break

                    elif Deck.get_rank(moves_trump_suit[index][0]) == "K" \
                            and Deck.get_suit(moves_trump_suit[index][0] == opponentsCardSuit):
                        highestRank = "K"

        for index, move in enumerate(moves):
            if Deck.get_rank(moves[index][0]) == highestRank \
                    and Deck.get_suit(moves[index][0]) == opponentsCardSuit:
                position = index
                break

        return position

    def findLowestCardOfSameSuit(self, state):
        lowestRank = None
        position = None
        moves = state.moves()

        # Opponents card suit
        opponentsCardSuit = Deck.get_suit(state.get_opponents_played_card())

        moves_trump_suit = []

        # Get all trump suit moves available
        for index, move in enumerate(moves):

            if moves[index][0] is not None and Deck.get_suit(moves[index][0]) == opponentsCardSuit:
                moves_trump_suit.append(move)

        # Check your hand for same suit cards as opponent
        # If opponent's card rank is '10' check for 'A' and play it
        if len(moves_trump_suit) > 0:
            for index, move in enumerate(moves_trump_suit):
                if Deck.get_rank(moves_trump_suit[index][0]) == "J" \
                        and Deck.get_suit(moves_trump_suit[index][0]) == opponentsCardSuit:
                    lowestRank = "J"
                    break

                elif Deck.get_rank(moves_trump_suit[index][0]) == "Q" \
                        and Deck.get_suit(moves_trump_suit[index][0]) == opponentsCardSuit:
                    lowestRank = "Q"

                elif Deck.get_rank(moves_trump_suit[index][0]) == "K" \
                        and Deck.get_suit(moves_trump_suit[index][0]) == opponentsCardSuit \
                        and lowestRank != "Q":
                    lowestRank = "K"

        for index, move in enumerate(moves):
            if Deck.get_rank(moves[index][0]) == lowestRank \
                    and Deck.get_suit(moves[index][0]) == opponentsCardSuit:
                position = index
                break

        return position

    def findLowestTrumpCard(self, state):
        lowestRank = None
        position = None
        moves = state.moves()
        # Opponents card rank
        opponentsCardRank = Deck.get_rank(state.get_opponents_played_card())
        trumpSuit = state.get_trump_suit()
        # Opponents card suit

        moves_trump_suit = []

        # Get all trump suit moves available
        for index, move in enumerate(moves):

            if moves[index][0] is not None and Deck.get_suit(moves[index][0]) == trumpSuit:
                moves_trump_suit.append(move)

        # Check your hand for same suit cards as opponent
        # If opponent's card rank is '10' check for 'A' and play it
        if len(moves_trump_suit) > 0:
            if opponentsCardRank == "10" or opponentsCardRank == "A":
                for index, move in enumerate(moves_trump_suit):
                    if moves_trump_suit[index][0] is not None and Deck.get_rank(moves_trump_suit[index][0]) == "J":
                        lowestRank = "J"
                        break

                    elif moves_trump_suit[index][0] is not None and Deck.get_rank(moves_trump_suit[index][0]) == "Q":
                        lowestRank = "Q"

                    elif moves_trump_suit[index][0] is not None \
                            and Deck.get_rank(moves_trump_suit[index][0]) == "K" \
                            and lowestRank != "Q":
                        lowestRank = "K"

                    elif moves_trump_suit[index][0] is not None \
                            and Deck.get_rank(moves_trump_suit[index][0]) == "10" \
                            and lowestRank != "K" and lowestRank != "Q":
                        lowestRank = "10"

                    elif moves_trump_suit[index][0] is not None \
                            and Deck.get_rank(moves_trump_suit[index][0]) == "A" \
                            and lowestRank != "10" and lowestRank != "K" and lowestRank != "Q":
                        lowestRank = "A"

            else:
                for index, move in enumerate(moves_trump_suit):
                    if moves_trump_suit[index][0] is not None and Deck.get_rank(moves_trump_suit[index][0]) == "J":
                        lowestRank = "J"
                        break

                    elif moves_trump_suit[index][0] is not None and Deck.get_rank(
                            moves_trump_suit[index][0]) == "Q":
                        lowestRank = "Q"

                    elif moves_trump_suit[index][0] is not None \
                            and Deck.get_rank(moves_trump_suit[index][0]) == "K" \
                            and lowestRank != "Q":
                        lowestRank = "K"


        for index, move in enumerate(moves):
            if Deck.get_rank(moves[index][0]) == lowestRank and Deck.get_suit(moves[index][0]) == trumpSuit:
                position = index
                break

        return position

    def findLowestPointsCard(self, state):
        smallestRank = None
        possibleRanks = ["A", "10", "K", "Q", "J"]
        position = None
        moves = state.moves()
        moves_trump_suit = []

        # Check your hand for same suit cards as opponent
        # If opponent's card rank is '10' check for 'A' and play it
        # Get all trump suit moves available

        if len(moves) > 0:

            for index, move in enumerate(moves):

                # Check whether 'J' is in your hand, if so play the card
                if Deck.get_rank(moves[index][0]) == possibleRanks[4]:
                    smallestRank = possibleRanks[4]
                    position = index
                    break
                elif Deck.get_rank(moves[index][0]) == possibleRanks[3]:
                    smallestRank = possibleRanks[3]
                    position = index
                elif Deck.get_rank(moves[index][0]) == possibleRanks[2] and smallestRank != possibleRanks[3]:
                    smallestRank = possibleRanks[2]
                    position = index
                elif Deck.get_rank(moves[index][0]) == possibleRanks[1] and smallestRank != possibleRanks[
                    2] and smallestRank != possibleRanks[3]:
                    smallestRank = possibleRanks[3]
                    position = index
                elif Deck.get_rank(moves[index][0]) == possibleRanks[0] and smallestRank != possibleRanks[
                    1] and smallestRank != possibleRanks[2] and smallestRank != possibleRanks[3]:
                    smallestRank = possibleRanks[4]
                    position = index
        # print("smallestrank: ", smallestRank)
        return position

    def findLowestPointsCardThatIsNotTrump(self, state):
        # print("lowest card acum")
        moves = state.moves()
        smallestRank = None
        possibleRanks = ["A", "10", "K", "Q", "J"]
        position = None

        trumpSuit = state.get_trump_suit()
        moves_trump_suit = []

        # Get all trump suit moves available
        for index, move in enumerate(moves):

            if moves[index][0] is not None and Deck.get_suit(moves[index][0]) != trumpSuit:
                moves_trump_suit.append(move[0])

        if len(moves_trump_suit) > 0:

            for index, move in enumerate(moves_trump_suit):

                # Check whether 'J' is in your hand, if so play the card
                if Deck.get_rank(moves_trump_suit[index]) == possibleRanks[4]:
                    smallestRank = possibleRanks[4]
                    break

                elif Deck.get_rank(moves_trump_suit[index]) == possibleRanks[3]:
                    smallestRank = possibleRanks[3]

                elif Deck.get_rank(moves_trump_suit[index]) == possibleRanks[2] \
                        and smallestRank != possibleRanks[4] \
                        and smallestRank != possibleRanks[3]:
                    smallestRank = possibleRanks[2]

                elif Deck.get_rank(moves_trump_suit[index]) == possibleRanks[1] \
                        and smallestRank != possibleRanks[4] \
                        and smallestRank != possibleRanks[3] \
                        and smallestRank != possibleRanks[2]:
                    smallestRank = possibleRanks[1]

                elif Deck.get_rank(moves_trump_suit[index]) == possibleRanks[0] \
                        and smallestRank != possibleRanks[4] \
                        and smallestRank != possibleRanks[3] \
                        and smallestRank != possibleRanks[2] \
                        and smallestRank != possibleRanks[1]:
                    smallestRank = possibleRanks[0]

        for index, move in enumerate(moves):

            if moves[index][0] is not None and Deck.get_rank(moves[index][0]) == smallestRank \
                    and Deck.get_suit(moves[index][0]) != trumpSuit:
                position = index

        return position

    def checkForMarriage(self, state):

        position = None
        moves = state.moves()
        chosen_suit = []
        trumpSuit = state.get_trump_suit()
        queens = []
        kings = []

        # Get all trump suit moves available
        for index, move in enumerate(moves):

            if moves[index][0] is not None and Deck.get_rank(moves[index][0]) == "Q":
                queens.append(move[0])
            elif moves[index][0] is not None and Deck.get_rank(moves[index][0]) == "K":
                kings.append(move[0])

        isLooping = True

        if len(queens) and len(kings) > 0:
            for index, move in enumerate(queens):
                for index2, move2 in enumerate(kings):
                    if Deck.get_suit(queens[index]) == Deck.get_suit(kings[index2]) and Deck.get_suit(queens[index]) == trumpSuit:
                        chosen_suit = Deck.get_suit(queens[index])
                        isLooping = False
                        break


                    elif Deck.get_suit(queens[index]) == Deck.get_suit(kings[index2]):
                        chosen_suit = Deck.get_suit(queens[index])
                        isLooping = False
                        break

                if isLooping == False:
                    break

        for index, move in enumerate(moves):

            if moves[index][0] is not None \
                    and Deck.get_suit(moves[index][0]) == chosen_suit \
                    and Deck.get_rank(moves[index][0]) == "Q":
                position = index

        return position

    def checkForTrumpExchange(self, state):
        moves = state.moves()
        trumpSuit = state.get_trump_suit()

        for index, move in enumerate(moves):
            if moves[index][0] is not None \
                    and Deck.get_rank(moves[index][0]) == "J" \
                    and Deck.get_suit(moves[index][0]) == trumpSuit:
                position = index
                Deck.exchange_trump(self, position)
                break




    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
        Function that gets called every turn. This is where to implement the strategies.
        Be sure to make a legal move. Illegal moves, like giving an index of a card you
        don't own or proposing an illegal mariage, will lose you the game.
       	TODO: add some more explanation
        :param State state: An object representing the gamestate. This includes a link to
            the states of all the cards, the trick and the points.
        :return: A tuple of integers or a tuple of an integer and None,
            indicating a move; the first indicates the card played in the trick, the second a
            potential spouse.
        """

        moves = state.moves()
        trumpSuit = state.get_trump_suit()
        chosen_move = moves[0]
        whosTurn = state.leader()

        if state.get_opponents_played_card() is not None:
            # 1
            # Overtake with the next smallest suit card
            if self.findNextSmallestCardOfSameSuit(state) is not None:
                chosen_rank = self.findNextSmallestCardOfSameSuit(state)
                # chosen_move = moves[self.checkHandKnowSuit(moves, chosen_rank, opponentsCardSuit)]
                chosen_move = moves[chosen_rank]
                # print(chosen_move)
                return chosen_move

            # 2
            # Overtake with the smallest trump
            elif self.findLowestTrumpCard(state) is not None:
                chosen_rank = self.findLowestTrumpCard(state)
                chosen_move = moves[chosen_rank]
                # print(chosen_move)
                return chosen_move

            # 3
            # Play the smallest suit card

            elif self.findLowestCardOfSameSuit(state) is not None:
                chosen_rank = self.findLowestCardOfSameSuit(state)
                chosen_move = moves[chosen_rank]
                # chosen_move = moves[self.checkHandUnknowSuit(moves, chosen_rank)]
                # print(chosen_move)
                return chosen_move

            # 4
            # Play the smallest available card in the hand that is not a trump
            elif self.findLowestPointsCardThatIsNotTrump(state) is not None:
                chosen_rank = self.findLowestPointsCardThatIsNotTrump(state)
                chosen_move = moves[chosen_rank]
                # chosen_move = moves[self.checkHandUnknowSuit(moves, chosen_rank)]
                # print(chosen_move)
                return chosen_move

        elif whosTurn == 2:
            #check for trump exchange
            if state.get_phase() == 1:
                self.checkForTrumpExchange(state)

            # check for marriage
            if self.checkForMarriage(state) is not None:
                chosen_rank = self.checkForMarriage(state)
                chosen_move = moves[chosen_rank]
                return chosen_move

            elif self.findLowestPointsCardThatIsNotTrump(state) is not None:
                chosen_rank = self.findLowestPointsCardThatIsNotTrump(state)
                chosen_move = moves[chosen_rank]
                # print(chosen_move)
                return chosen_move

            elif self.findLowestPointsCard(state) is not None:
                chosen_rank = self.findLowestPointsCard(state)
                chosen_move = moves[chosen_rank]
                # print(chosen_move)
                return chosen_move

        return chosen_move
