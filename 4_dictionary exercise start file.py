# This program uses a dictionary as a deck of cards.

def main():
    # Create a deck of cards.
    deck = create_deck() #creates dictionary of deck of cards

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))


    # Deal the cards.
    deal_cards(deck, num_cards)
    #deal_cards doesnt return anything - dont have to put a variable to save it into because its not a value returning function
    #first one has to be a dictionary, second has to be an integer



#create_deck is a value returning function
# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    #keys of a dictionary have to be unique - name of card is unique which is why its the key instead of value
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck 



# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number):
    #deck = dictionary, number = integer
    # Initialize an accumulator for the hand value.
    handValue = 0
    


    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > 52: #incase the user tries to use more than 52 cards - it will restart
        number = 52
    
    
    '''
    # Deal the cards and accumulate their values.
    for count in range(number):
        card,value = deck.popitem()
        print(card)
        handValue += value 

    '''

    import random
    for count in range(number): #number is the number of cards the user asks for 
        card = [random.choice(list(deck))] #will pick a random key from my list of keys in deck dictionary
        print(card)
        value = deck[card] #way we get value - call dictionary(deck)
        handValue += value 
    #this repeats as many times as user picks cards

    # Display the value of the hand.
    print('the value of the hand is', handValue)
    
    

# Call the main function.
main()
