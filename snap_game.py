import random

def ask_input(): 
    print("Welcome to SNAP game!")
    question1 = "Please choose how many packs you want to use(1~3).\
                \nAnswer: "
    question2 = "Which of the following conditions to trigger SNAP?\
                \n(1)When value of the card maches.\
                \n(2)When the suit maches.\
                \n(3)When bothlue and suit maches.\
                \nAnswer: "
    packs_qty = None
    rule = None
    while packs_qty is None:
        packs_qty = ""
        packs_qty = input(question1)
        packs_qty = int(packs_qty)
        if packs_qty in [1, 2, 3]:
            break
        else:
            print("Your input: {} is not illegal, please input again.".format(packs_qty) )  
            packs_qty = None
            continue
    while rule is None:
        rule = ""
        rule = input(question2)
        rule = int(rule)
        if rule in [1, 2, 3]:
            break
        else:
            print("Your input: {} is not illegal, please input again.".format(rule) )
            rule = None
            continue
    return packs_qty, rule

def shuffle():
    #generate cards
    cards = []
    for i in range(1, packs_qty + 1):
        for suit in ['A', 'B', 'C', 'D']:
            numbers = ["{:02}".format(i) for i in range(1, 14)] #01,02,03...13
            card_suit = [str(i) + suit + num for num in numbers]   #1A01,1A02,1A03...1B01,1B02...
            cards += card_suit
        
    #shuffle and divide to users
    user1 = []
    user2 = []
    while len(cards) > 0:        
        card = random.choice(cards)
        user1.append(card)
        cards.remove(card)
        card = random.choice(cards)
        user2.append(card)
        cards.remove(card)
    
    return cards, user1, user2

def game():
    cards, user1, user2 = shuffle()
    public = []
    user_snap_cnt = {'user1':0, 'user2':0}
    l_cnt = 0
    
    while len(user1) > 0 and len(user2) > 0:
        l_cnt += 1
        print("\nRound {}".format(l_cnt))
        snap = False
        user1, user1_choice = play_card(user1)
        print("user1 choose {}".format(user1_choice))
        public.append(user1_choice)
        if len(user2) > 0:
            user2, user2_choice = play_card(user2)
            public.append(user2_choice)
            print("user2 choose {}".format(user2_choice))
        else:
            break
        #compare if SNAP
        if   rule == 1:   #(1)When value of the card maches.
            if user1_choice[-2:] == user2_choice[-2:]:
                snap = True
        elif rule == 2:   #(2)When the suit maches.\
            if user1_choice[1] == user2_choice[1]:
                snap = True
        elif rule == 3:   #(3)When both value and suit maches.
            if user1_choice[1:] == user2_choice[1:]:
                snap = True
        if snap:
            random_user = random.choice(['user1', 'user2'])
            if random_user == 'user1':
                user1 += public
            elif random_user =='user2':
                user2 += public
            user_snap_cnt[random_user] += 1
            print("This round {} takes SNAP!".format(random_user))
            public = []
        print("User1 have {} cards, {} times SNAP!".format(len(user1),user_snap_cnt['user1']))
        print("User2 have {} cards, {} times SNAP!".format(len(user2), user_snap_cnt['user2']))
            
    if len(user1) == 0:
        print("user1's have no card. user2 wins!")
    elif len(user2) == 0:
        print("user2's have no card. user1 wins!")
        
def play_card(user):
    user_choice = random.choice(user)
    user.remove(user_choice)
    
    return user, user_choice
    
if __name__ == '__main__':
    packs_qty, rule = ask_input()
    game()
    
