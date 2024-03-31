_author_ = "Ritika Joshi"
_credits_ = ["StackOverflow, github.com"]
_email_ = "joshirk@mail.uc.edu"
#Project_TextBased_Adventure_Game

import time
import random

shop_items = ["Miracle Legumes          - 5 coins",
              "Steel armour             - 40 coins",
              "Quarterly reports        - NFS!",
              "A Neon Light             - 30 coins",
              "Beaumont adams (gun)     - 60 coins",
              "Helmet                   - 20 coins",
              "Back to Scranton"]

player_items = ["Steel armour"]

gift_items = ["Leave"]

jan_items = []

bar_info_day = ["INFO: Don't go into the jungle un-prepared",
                "INFO: The Ceo likes reports",
                "INFO: Check out the contests at night too",
                "INFO: The office nests stronger enemies",
                "INFO: jungle is vast, explore out of options to "
                "find many things",
                "INFO: Did you know there is a legendary tomb in the jungle?",
                "INFO: Animals in jungle are faster than you"]

bar_info_night = ["INFO: jungle at night is dark. You may need fire source",
                  "INFO: Did you know that the jungle has a range "
                  "between 1 to 50",
                  "INFO: Jan likes flowers",
                  "INFO: check out the secret contests at night",
                  "INFO: Do not pick a fight with enemies stronger than you",
                  "INFO: The city next to us has been attacked by "
                  "Werewolves",
                  "INFO: Access to corporate is restricted at night",
                  "INFO: Sneaking into corporate at night time might "
                  "result in imprisonment",
                  "INFO: Having full life is always an advantage"]

scranton_locations = ["Steamtown mall",
                     "Schrute Farms",
                     "Contest arena",
                     "Corporate at NY",
                     "The Office",
                     "Shady jungle"]

corporate_locations_day = ["File Cabinet",
                      "Quaters",
                      "Jan Office",
                      "Central Hall",
                      "Go back to scranton"]

corporate_locations_night = ["File Cabinet",
                        "Quaters",
                        "Jan Office",
                        "Central Hall"]

contest_items = ["Unknown Key",
                 "Mystery Box"]

rewards_day = ["Special Prize: Unknown Key",
               "Deposit coins and win back Double",
               "Deposit 10 coins, Win back 50 coins"]

rewards_night = ["Special Prize: Mystery Box",
                 "Deposit coins and win back Double",
                 "Deposit no coins, Win 50 back coins"]

player_offense_moves = ["You step forward to slash the enemy",
                        "You rise high to deliver a mighty blow",
                        "You make a lunge and slash attack",
                        "You deliver an counter attack",
                        "A power blow was directed towads the enemy",
                        "You rain down a series of gun shots",
                        "A sharp delivery to penetrate the defense of enemy",
                        "You run towards the enemy at great speed",
                        "You duck down and deliver a low swing",
                        "You stand tall and attck the enemy from the front",
                        "You run around and penetrate the back of the enemy"]

player_defense_moves = ["You hold the gun to counter the enemy attck",
                        "The enemy attacks are repelled by you",
                        "The enemy jumps on you and you roll to the side",
                        "You shoot your gun in rythm to the enemy attacks",
                        "You step back away from the enemy",
                        "You dodge the enemy and are ready to attack"
                        ]

enemy_offense_moves = ["The enemy charges at you like a mad bull",
                       "The enemy has a arm streangth of a boulder",
                       "Enemy has great strategy to corner you",
                       "The enemy attacks from behind",
                       "The enemy rolls around and attacks",
                       "The enemy jumps on you",
                       "The enemy fights you head on"]

enemy_defense_moves = ["Enemy has a strong defense",
                       "Your enemy has brains to dodge your attacks",
                       "Your enemy has speed advantage to evade your attacks",
                       "Your enemy has a strength to with stand your attack",
                       "Enemy takes you head on",
                       "Your enemy is a formidable opponent"]

animal_offense_moves = ["The animal charges straight at you",
                        "The animal attacks you with ferocity and growls",
                        "The animal attacks you from behind",
                        "The animal tries to bite you",
                        "The animal jumps on you",
                        "The animal uses its claws"]

animal_defense_moves = ["The animal has a thick skin",
                        "The animal dodges your attacks",
                        "The animal has speed advantage",
                        "The animal deflects your attacks with claws",
                        "The animal steps back to counter"]

animal_list = ["Bear", "Bat", "Jungle Cat"]

strong_animal_list = ["Porcupine", "Tiger", "Werewolf"]

beast_list = ["Kevin",
                "Guard",
                "SHOPKEEPER",
                "Jim at the contest arena"]

# triggers and declarations to be used in the code, from line 133 - 181
player = ""
shop_count = 0
armour = "available"
beaumont_adams = "available"
reports = "available"
helmet = "available"
bar_count = 0
beets_available = ""
player_life = 100
coins = 50000
drink_count = 0
info_count = 0
time_zone = "day"
player_offense_min = 0
player_offense_max = 30
player_defense = 10
contest_day_count = 0
contest_night_count = 0
game_night_count = 0
glowing_lilies_day_count = 0
flowers_day_count = 0
beets_day_count = 0
Keyword_count = 0
jungle_explore_count = 0
jungle_trigger = "deactivate"
game_over = "deactivate"
beets_available = ""
holygrail_sequense = ""
darryl = "alive"
treasure_box = "not_opened"
chest = "not_opened"
toby = "alive"
huge_monster = "alive"
corporate_count = 0
toll_status = ""
inner_corporate_count = 0
corporate_access = "restricted"
phone = "deactivated"
cabinet_status = ""
jan_count = 0
jan_introduction = ""
name = ""
jan_quest_status = ""
player_status = ""
tomb_password = ""
hologram_room_count = 0
kings_status = ""


# function to print messages with a 1.2 second delay
def print_pause(message):
    print(message)
    time.sleep(1.5)

# function to display the 'items in the list' with a serial NUMBER
def list_serial(list):
    for index in range(len(list)):
        print(str(index+1) + ". " + list[index])
    print("\n")
    return ""


# function to remove a specific item from a list
def remove_item(list, item):
    new_list = []
    for index in range(len(list)):
        if list[index] != item:
            new_list.append(list[index])
    list = new_list
    return list


# function to increase player's life within the limit of 100
def life_increase(num):
    global player_life
    if player_life < 100 and player_life > 0:
        player_life += num
        if player_life > 100:
            player_life = 100
        return player_life


# function to decrease player's life within the threshold of 0
def life_decrease(life, num):
    if life > 0:
        life += num
        if life < 0:
            life = 0
        return life
    else:
        life = 0
        return life


# function to display a message whenever the coins is insufficient
def low_coins_message():
    global coins
    global player
    print_pause("\nNOTE: You do not have enough cash " + player + "!")
    print_pause("Your coins : " + coins)
    print_pause("\nNOTE: Try earning some in the town contest")


# ------------main function for the game-------------
def adventure_game():
    global player
    # input to ask for the player's name
    player = input("State your name: ")
    print_pause("\nGreetings " + player + "!\n")
    print_pause("This is a quest to kill the evil Beast of Scranton")
    print_pause("The People of Scranton need an agent like you to save them")
    print_pause("Note: The creator of this game is huge fan of the show 'The Office'")
    print_pause("Note: And that explains all the references in the game.")
    scranton()


# A branch sequence to the function 'adventure_game'
def scranton():
    # trigger to end the game from the function 'fight_sequence'
    if game_over == "activate":
        print_pause("\n\nGame over. Try again ........")
        exit()
    # scranton intro
    # player's choice
    print_pause("\nWelcome to Scranton, PA")
    
    print_pause("Where would you like to go?\n")
    # displays list of scranton locations in a serial list
    scranton_choice = input(list_serial(scranton_locations)).lower()
    # if player decides to enter into the mall
    if "mall" in scranton_choice:
        print_pause("\nYou have entered the Steamtown mall to make business\n")
        shop()
    # if player decides to enter into the farms
    elif "farms " in scranton_choice:
        print_pause("\nYou have checked into the Schrute Farms")
        farms ()
    # if player decides to enter into the contest arena
    elif "contest" in scranton_choice:
        print_pause("\nYou head towards the contest arena with curiosity")
        contest_arena()
    # if player decides to enter into the jungle
    elif "jungle" in scranton_choice:
        jungle()
    # if player decides to enter into the office
    elif "office" in scranton_choice:
        print_pause("You step into the darkness of the office courageously !!")
        print_pause("The office has multiple partitions in it.")
        office()
    # if player decides to enter into the castl
    elif "corporate" in scranton_choice:
        corporate()
    # if player decides to enter into the secret passage
    elif "secret" in scranton_choice and "Secret Passage" in scranton_locations:
        secret_passage()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter something like 'mall/contest/farms ..'")
        scranton()


# funtion to trigger shop sequence in the game
def shop():
    global coins
    global shop_items
    global player_items
    global player
    global player_status
    global player_offense_min
    global player_offense_max
    global player_defense
    global player_life
    global holygrail_sequense
    global armour
    global beaumont_adams
    global reports
    global helmet
    global gift_items
    global shop_count
    shop_count += 1
    # An introduction to be used only one time in the game
    if shop_count == 1:
        print_pause("SHOPKEEPER: Welcome to the Steamtown mall of trade and purchase.")
    # A message to be displayed only if the player is wanted
    elif player_status == "wanted":
        print_pause("SHOPKEEPER: I am not allowed to trade with "
                    "criminals " + player + ".")
        print_pause("SHOPKEEPER: But I can keep this as a "
                    "secret between us")
    # A message to be used throughout the game, if player revisit the shop
    else:
        print_pause("\nSHOPKEEPER: Welcome back " + player + " !!")
        print_pause("SHOPKEEPER: Let me see if I can find, what you need.")

    print_pause("SHOPKEEPER: What do you want to purchase? Name it.\n")
    # Displays shops items in a serial list and take desired input from player
    shop_choice = input(list_serial(shop_items)).lower()
    # if player wants to buy life potion in the shop
    if "legume" in shop_choice:
        if coins >= 5 and player_life < 100:
            print_pause("SHOPKEEPER: All thanks to James Trickington for these "
                        "All full life is always safe.")
            print_pause("coins: " + str(coins) + " - 5")
            coins -= 5
            print_pause("Your coins: " + str(coins))
            life_increase(25)
            print_pause("Your life increased +25, feel stronger now ?")
            print_pause("Your life: " + str(player_life))
        elif player_life == 100:
            print_pause("SHOPKEEPER: You already have full life! Buy it when you need it")
        elif coins < 5:
            low_coins_message()
        else:
            low_coins_message()
    # if player wants to buy 'steel armour' in the shop
    # by adding / armour == "available" / in the below statement-
    # player cannot buy this item, if the item is already sold out
    elif "armour" in shop_choice and armour == "available":
        if coins >= 40:
            print_pause("SHOPKEEPER: Shiny shiny!")
            print_pause("\nNOTE: Now you have 'Steel Armour' in your possession")
            shop_items = remove_item(shop_items,
                                     "Steel armour - Worth 40$")
            player_items.append("Steel armour")
            gift_items.append("Steel armour")
            armour = "not available"
            print_pause("coins: " + str(coins) + " - 40")
            coins -= 40
            print_pause("Your coins: " + str(coins))
        else:
            low_coins_message()
    # if player wants to buy 'neon light' in the shop
    elif "neon light" in shop_choice:
        if coins >= 30:
            print_pause("SHOPKEEPER: Use it wisely "+ player)
            print_pause("\nNOTE: The neon light adds light element to weapons")
            shop_items = remove_item(shop_items,
                                     "A neon light              - Worth 30$")
            player_items.append("neon light")
            print_pause("coins: " + str(coins) + " - 30")
            coins -= 30
            print_pause("Your coins: " + str(coins))
        else:
            low_coins_message()

    # if player wants to buy 'beaumont adams' in the shop
    # by adding / beaumont adams == "available" / in the below statement-
    # player cannot buy this item, if the item is already sold out
    elif "beaumont adams" in shop_choice and beaumont_adams == "available":
        if coins >= 60 and "Light Saber" not in player_items:
            print_pause("SHOPKEEPER: A great gun for the cool agent")
            print_pause("\nNOTE: You now possess the 'beaumont adams', a mighty gun")
            player_offense_min = 20
            player_offense_max = 50
            print_pause("\nNOTE: Your offense has increased "
                        "to: " + str(player_offense_max))
            print_pause("\nNOTE: You are more stronger now and")
            print_pause("      ready to fight stronger enemies.")
            shop_items = remove_item(shop_items,
                                     "beaumont adams,a mighty gun - Worth 60$")
            player_items.append("beaumont adams")
            beaumont_adams = "not available"
            print_pause("coins: " + str(coins) + " - 60")
            coins -= 60
            print_pause("Your coins: " + str(coins))
        elif "Light Saber" in player_items:
            print_pause("SHOPKEEPER: You already possess a more "
                        "powerful weapon")
            print_pause("SHOPKEEPER: These is no need to buy this gun")
        elif coins < 60:
          low_coins_message()
    # if player wants to buy 'reports' in the shop
    # by adding / reports == "available" / in the below statement-
    # player cannot buy this item, if the item is already sold out
    elif "reports" in shop_choice and reports == "available":
        # if the player has 'Holy Grail' in his possession
        if "Holy Grail" in player_items:
            print_pause("SHOPKEEPER: You found my lost 'Holy Grail' !!")
            print_pause("SHOPKEEPER: You have my thanks " + player + ".")
            print_pause("SHOPKEEPER: As agreed, I will trade you the "
                        "'Quarterly reports' for the 'Holy Grail' of mine.")
            print_pause("\nNOTE: You have the 'Quarterly reports' - "
                        "a present worthy of ceo, in your possession.")
            shop_items = remove_item(shop_items,
                                     "Quarterly reports         - NFS")
            player_items = remove_item(player_items, "Holy Grail")
            player_items.append("reports")
            reports = "not available"
    # if the player does not have Holy Grail in his possession
        else:
            print_pause("SHOPKEEPER: Not for sale " + player + "!")
            print_pause("SHOPKEEPER: But I'm willing to trade it ")
            print_pause("            for a personal artifact of mine")
            print_pause("SHOPKEEPER: I lost my holy grail, somewhere"
                        " in the town.")
            print_pause("SHOPKEEPER: It is the pact made by the Robery Dunder himself")
            print_pause("SHOPKEEPER: Find it and the reports are yours")
            holygrail_sequense = "initiated"
    # if player wants to buy 'steel helmet' in the shop
    # by adding / helmet == "available" / in the below statement-
    # player cannot buy this item, if the item is already sold out
    elif "helmet" in shop_choice and helmet == "available":
        if coins >= 20:
            print_pause("SHOPKEEPER: Better safe than sorry")
            print_pause("\nNOTE: You have accquired a 'Steel Helmet'")
            shop_items = remove_item(shop_items,
                                     "Steel Helmet            - Worth 20$")
            player_items.append("Steel Helmet")
            helmet = "not available"
            print_pause("coins: " + str(coins) + " - 20")
            coins -= 20
            print_pause("Your coins: " + str(coins) + "\n")
            print_pause("\nNOTE: Your defense has been increased")
            print_pause("Defense :" + str(player_defense) + " + 10")
            player_defense += 10
            print_pause("Player Defense increased to: " + str(player_defense))
        elif coins < 20:
            low_coins_message()
    # if player wants to get back to the scranton
    elif "scranton" in shop_choice:
        print_pause("You head back to the scranton")
        scranton()
    # if player gives an unrecognized input
    else:
        print_pause("SHOPKEEPER: I didn't get that, "
                    "Specify the item clearly")
        shop()
    # After trading, player has to get back to the scranton
    print_pause("\nYou head back to the scranton")
    scranton()


# a function to run 'inn' sequence
def farms ():
    inner_farms ()


# A branch sequence to the funtion 'farms '
def inner_farms ():
    # player's choice
    print_pause("What would you like to do?\n")
    farms_choice = input("1. Go to the Bar"
                       "\n2. Rent a Room"
                       "\n3. Scranton\n\n").lower()
    # if player chooses to enter the bar
    if "bar" in farms_choice:
        bar()
    # if player chooses to enter the room
    elif "room" in farms_choice:
        room()
    # if player chooses to enter the scranton
    elif "scranton" in farms_choice:
        scranton()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter a valid choice: Bar? Room? Scranton?")
        inner_farms ()


# A branch sequence to the funtion 'inner_farms '
def bar():
    global bar_count
    global info_count
    global player_items
    global beets_available
    global coins
    global time_zone
    print_pause("")
    print_pause("You are the Bar and you see Kevin\n")
    print_pause("Kevin: What would you like to have?\n")
    bar_choice = input("1. A drink "
                       "\n2. Info\n\n").lower()
    if "drink" in bar_choice:
        bar_count += 1
        # if player has sufficient money and timezone is day, he gets drunk
        if coins >= 10 and time_zone == "day":
            if bar_count == 1:
                print_pause("Kevin: Here's your drink")
                # wine/beets in Kevin's possession will be diminished
                beets_available = "no"
                drunk()
            elif bar_count > 1 and bar_count < 5:
                # if you have beets and Kevin dorsn't, you get free drink
                if "beets" in player_items and beets_available == "no":
                    print_pause("\nNOTE: beets are given to the Kevin")
                    print_pause("Kevin: As promised, next round is on"
                                " the house!")
                    player_items = remove_item(player_items, "beets")
                    # beets in your possession will be ransfered to Kevin
                    beets_available = "yes"
                    drunk()
                elif beets_available == "yes":
                    # if Kevin has beets, you get drunk
                    drunk()
                else:
                    # if both player and Kevin doen't not have beets
                    # he asks you to go fetch some from the jungle
                    print_pause("Kevin: We are out of wine now.")
                    print_pause("Kevin: If you are desparate, "
                                "you can run an errand for me.")
                    print_pause("Kevin: There are some wild beets "
                                "growing in the jungle")
                    print_pause("Kevin: It is dangerous for me to go "
                                "into jungle by myself")
                    print_pause("Kevin: Fetch some for me and next round "
                                "will be on the house")
            # After every 5 counts, beets in Kevins possession will be-
            # diminished and count is reset to 0
            elif bar_count >= 5:
                print_pause("Kevin: We are out of wine again!!")
                print_pause("Kevin: I'm afraid you gonna have to "
                            "bring some more beetsfrom the jungle")
                beets_available = "no"
                bar_count = 0
        # at night time, drinks are not served
        elif time_zone == "night":
            print_pause("Kevin is not serving drinks at night")
            print_pause("But you can hear extra gossips from him at night.")
        # if player does not have enough cash
        elif coins < 10:
            print_pause("Kevin: I'm afraid you don't have enough coins")
            print_pause("Kevin: Try to earn some coins in contest arena")
    # if player wants info from the Kevin
    elif "info" in bar_choice:
        info_count += 1
        # after getting info for more than 2 times,
        # player is sent back to the room to take rest
        if info_count > 2:
            info_count = 0
            print_pause("Kevin: Don't exert yourself, come back later")
            print_pause("Kevin: I suggest you take a room and "
                        "rest for the day")
            room()
        # random info is displayed during daytime
        elif time_zone == "day":
            print_pause(random.choice(bar_info_day))
            bar()
        # random info different from daytime is displayed during night time
        elif time_zone == "night":
            print_pause(random.choice(bar_info_night))
            bar()
    # code to deal with unrecognized input
    else:
        print_pause("Kevin: I'm sorry, I don't understand your language")
        bar()
    inner_farms ()


# A branch sequence to the funtion 'bar'
def drunk():
    global coins
    print_pause("You get drunk again!")
    print_pause("coins: " + str(coins) + " -10")
    coins -= 10
    print_pause("Your coins: " + str(coins))
    print_pause("You have no choice but to take a room\n")
    room()


# A branch sequence to the funtion 'inner_farms '
def room():
    global coins
    print_pause("\nYou enterd the room all tired and depraved of sleep")
    print_pause("You were charged 2 coins for the room")
    print_pause("coins: " + str(coins) + " -2")
    coins -= 2
    print_pause("Your coins: " + str(coins))
    room_sequense()


# A branch sequence to the funtion 'room'
def room_sequense():
    global player_items
    global holygrail_sequense
    print_pause("\nWhat would yo do now?")
    room_action = input("1. Crash on the bed"
                        "\n2. Scan the room\n").lower()
    # if player wants to sleep on bed
    if "bed" in room_action:
        print_pause("\nIt is time to rest your body")
        room_choice()
    # if player wants to scan the room
    elif "scan" in room_action:
        print_pause("\nYou scan the room throughly for any "
                    "possible anamoly")
        # if Holy Grail sequence initiated by the shopkeeper
        if holygrail_sequense == "initiated":
            print_pause("You find something eating dust behind the "
                        "closet")
            print_pause("You read it, out of curiosity...")
            print_pause("You have found some sort of 'Holy Grail'")
            player_items.append("Holy Grail")
            print_pause("\nIt is time to rest your body")
            holygrail_sequense = "end"
            room_choice()
        # if Holy Grail sequence initiated by the shopkeeper
        else:
            print_pause("You find nothing abnormal")
            print_pause("It is time to rest your body")
            room_choice()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter a valid action in words")
        room_sequense()


# A branch sequence to the funtion 'room_sequense'
def room_choice():
    global time_zone
    global flowers_day_count
    global beets_day_count
    global glowing_lilies_day_count
    global keyword_count
    global jungle_trigger
    global player_items
    global gift_items
    global phone

    print_pause("\nHow long do you need to sleep?")
    sleep_till = input("1. Wake up at night"
                       "\n2. Wake up at morning\n").lower()
    # if player wants to sleep till night and timezone is day
    if "night" in sleep_till and time_zone == "day":
        print_pause("You wake up at night")
        time_zone = "night"
        # increse player's life by 25 after some rest
        print_pause("Your life increased by 25")
        print_pause("life : " + str(player_life) + " + 25")
        life_increase(25)
        print_pause("Your life: " + str(player_life))
        print_pause("\nsome events are different at night, go check them out")
        print_pause("You come down to the Schrute Farms's entrance")
        farms()
    # if player wants to sleep till night and timezone is already night
    if "night" in sleep_till and time_zone == "night":
        print_pause("Its already night time")
        room_choice()
    # if player wants to sleep till morning of next day
    elif "morning" in sleep_till:
        keyword_count = 0
        jungle_trigger = "deactivate"
        flowers_day_count += 1
        beets_day_count += 1
        phone = "deactivated"
        # if player has flowers in his possession for more than 2 days
        if flowers_day_count > 2:
            print_pause("\nNOTE: Flowers in your possession are dried up.")
            print_pause("NOTE: They are no longer useful")
            player_items = remove_item(player_items, "Flowers")
            gift_items = remove_item(player_items, "Flowers")
        # if player has glowing lilies in his possession for more than 2 days
        if glowing_lilies_day_count > 2:
            print_pause("\nNOTE: Glowing lilies in your possession "
                        "are dried up.")
            print_pause("NOTE: They are no longer useful")
            player_items = remove_item(player_items, "Glowing lilies")
            gift_items = remove_item(player_items, "Glowing lilies")
        # if player has beets in his possession for more than 2 days
        if beets_day_count > 2:
            print_pause("\nNOTE: beets in your possession have gone bad")
            print_pause("NOTE: They are no longer useful.")
            player_items = remove_item(player_items, "beets")
            gift_items = remove_item(player_items, "beets")
        print_pause("\nYou wake Up in the morning fresh to resume "
                    "your journey")
        time_zone = "day"
        # increse player's life by 50 after plenty of rest
        print_pause("Your life increased by 50")
        print_pause("life : " + str(player_life) + " + 50")
        life_increase(50)
        print_pause("Your life: " + str(player_life))
        print_pause("\nYou head back to the Schrute Farms entrance")
        farms()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter a valid time zone. Night? or Morning?")
        room_choice()


# funtion to trigger the location 'contest arena' in the scranton
def contest_arena():
    global time_zone
    global contest_day_count
    global contest_night_count
    # if player visits 'contest arena' during daytime
    if time_zone == "day":
        contest_day_count += 1
        # intro to be used only once in the game
        if contest_day_count == 1:
            print_pause("Surpricingly people held contests in gambling")
        # if player visits more than once
        if contest_day_count >= 1:
            print_pause("Would you like to take part in the gambling?")
            contest_choice_day = input("1. Yes"
                                       "\n2. No\n").lower()
            if "yes" in contest_choice_day:
                game_day()
            elif "no" in contest_choice_day:
                print_pause("Jim: Farewell, stranger.")
                scranton()
            # condition to handle unrecognized inputs from the player
            else:
                print_pause("Jim: Make up your mind stranger. 'yes' "
                            "or 'no' ?")
                contest_arena()
    # if player visits 'contest arena' during night time
    elif time_zone == "night":
        contest_night_count += 1
        # intro to be used only once in the game
        if contest_night_count == 1:
            print_pause("Under the clock of shadows, the Arena conducts"
                        " battles")
            print_pause("Would you dare to confront the person "
                        "reponsible for the fights at night time?")
        # if player visits more than once
        if contest_night_count > 1:
            print_pause("Would you dare to take part in the fights?")
        # take input from the player
        contest_choice_night = input("1. Yes"
                                     "\n2. No\n").lower()
        if "yes" in contest_choice_night:
            game_night()
        elif "no" in contest_choice_night:
            print_pause("Perhaps you are not ready yet")
            print_pause("Do come back another time....")
            scranton()
        # condition to handle unrecognized inputs from the player
        else:
            print_pause("Jim: Make up your mind stranger. 'yes' or 'no' ?")
            contest_arena()


# A branch sequence to the funtion 'contest_arena'
def game_day():
    global coins
    global contest_items
    global rewards_day
    global contest_items
    global player_items
    global player_status
    # a trigger if the player is wanted
    if player_status == "wanted":
        print_pause("Leave stranger, you are gonna get me in trouble")
        print_pause("You are forced to leave the contest arena")
        print_pause("You head back to the Scranton")
        scranton()
    # choice to play different games
    print_pause("\nJim: welcome stranger, what would you like to play?")
    contest_day_choice = input("1. Evens & Odds"
                               "\n2. Double or nothing"
                               "\n3. Rewards\n").lower()
    # if player choose 'evens & odds' game
    if "even" in contest_day_choice:
        if coins >= 10:
            print_pause("Jim: Deposit 10 coins to play the game")
            print_pause("Your coins: " + str(coins) + " - 10")
            coins -= 10
            print_pause("Your coins: " + str(coins))
            value1, value2 = roll_dice()
            if (value1+value2) % 2 == 0:
                value = "even"
            else:
                value = "odd"

            print_pause(str(value1) + "+" + str(value2) + " "
                        "= " + str(value1 + value2) + ", " + value)

            if value == "even":
                print_pause("Jim: Evens it is! Congratulations stranger")
                print_pause("Jim: You win 50 coins")
                print_pause("Your coins: " + str(coins) + " + 50")
                coins += 50
                print_pause("Your coins: " + str(coins))
            else:
                print_pause("Jim: Odds are against you stranger.., "
                            "you lost your deposit")
        # if player does not have enough coins
        else:
            low_coins_message()
            scranton()
    # if player choose 'double or nothing' game
    elif "double" in contest_day_choice:
        print_pause("\nJim: Deposit coins as you desire")
        print_pause("Jim: If both dices are evens or odd , you win")
        print_pause("Jim: If you win - you get double deposit")
        print_pause("Jim: Lose - I keep the coins.")
        # if player has not win the special prize already
        if "Unknown Key" in contest_items:
            print_pause("Also I have a special prize waiting to be won...")
        # take a desired amount of bet from the player's input
        coins_deposited = int(input("How much would you like to bet: "))
        print_pause("Your coins: " + str(coins) + " - " + str(coins_deposited))
        coins -= coins_deposited
        if coins >= 0:
            print_pause("Your coins = " + str(coins))
            value1, value2 = roll_dice()
            print_pause("Dices : " + str(value1) + "," + str(value2))
            # if player wins
            if (value1 % 2) == (value2 % 2):
                # if player has not win the special prize already
                if "Unknown Key" in contest_items:
                    print_pause("Jim: Marvelous stranger! It's your"
                                " lucky day")
                    print_pause("Jim: I have just the rare item as the prize")
                    print_pause("\nNOTE: You have received an 'Unknown Key'.")
                    contest_items = remove_item(contest_items, "Unknown Key")
                    player_items.append("Unknown Key")
                    rewards_day = remove_item(rewards_day,
                                              "Special Prize: Unknown Key")
                    print_pause("Jim: I'll keep the deposit just this once")
                    print_pause("Jim: consider it an even trade for the "
                                "rare item")
                # if player has already won the special prize
                else:
                    print_pause("Jim: Congratulation, stranger! You win "
                                "this game")
                    coins_deposited = 2*coins_deposited
                    print_pause("Your coins: " + str(coins) + " , "
                                "+ " + str(coins_deposited))
                    coins += coins_deposited
                    print_pause("Your coins: " + str(coins))
            # if player loses
            else:
                print_pause("Jim: It is not as easy as it sounds stranger!!")
                print_pause("Jim: I get to keep the coins")
        # if player does not have enough coins
        else:
            low_coins_message()
            coins += coins_deposited
            print_pause("Your coins = " + str(coins))
            scranton()
    # if player wants to check the rewards before playing the game
    elif "reward" in contest_day_choice:
        print_pause(list_serial(rewards_day))
        game_day()
    # condition to deal unrecognized input
    else:
        print_pause("Jim: Say the correct words stranger")
        game_day()
    # choice to play the game again
    print_pause("\nJim: would you like to play again stranger ?")
    play_again = input("1.yes\n2.no\n").lower()
    if "yes" in play_again:
        game_day()
    # if player wants to leave the contest arena
    else:
        print_pause("Jim: Good bye, stranger")
        scranton()


# A branch sequence to the funtion 'game_day'
def roll_dice():
    print_pause("\nRolling Dice:")
    value1 = random.randint(1, 6)
    print_pause("Dice 1: " + str(value1))
    value2 = random.randint(1, 6)
    print_pause("Dice 2: " + str(value2))
    # returns a random NUMBER from each dice
    return value1, value2


# A branch sequence to the funtion 'contest_arena'
def game_night():
    global game_night_count
    game_night_count += 1
    print_pause("\nJim: Welcome Stranger")
    # an intro to be used only once in the game
    if game_night_count == 1:
        print_pause("Jim: What brings you here at this hour of time?")
        input("You can say anything: \n")
        # irrespective of player's input game moves forward
        print_pause("Jim: I see you knew about our little secret contests")
        print_pause("Jim: Can you handle the voilance?")
        game_forward = input("1. Yes"
                             "\n2. No\n").lower()
        if "yes" in game_forward:
            game_night_contest()
        elif "no" in game_forward:
            scranton()
        else:
            print_pause("Jim: Hmm... I don't understand. Better meet later")
            scranton()
    # if player visits more than once
    elif game_night_count > 1:
        game_night_contest()


# A branch sequence to the funtion 'game_night'
def game_night_contest():
    global coins
    global contest_items
    global player_items
    global player_status
    global rewards_day
    global rewards_night
    # a trigger is player is wanted for a crime
    if player_status == "wanted":
        print_pause("Jim: I see you got yourself in some trouble stranger !!")
        print_pause("Jim: I'm not gonna turn you in, feel free to come at "
                    "night time")
    # game choice to fight the desired enemy
    print_pause("what would you like to to stranger?")
    contest_night_choice = input("1. Fight dragon\n2. Fight a goblin\n"
                                 "3. View rewards\n").lower()
    # if player wants to fight dragon
    if "dragon" in contest_night_choice:
        print_pause("\nJim: Are you sure stranger?")
        print_pause("Jim: He is the best fighter around "
                    "all the nearby citys")
        print_pause("Jim: His strength rivals a chariot")
        fight_choice = input("1.yes"
                             "\n2.no\n").lower()
        # if player chooses to fight the dragon
        if "yes" in fight_choice:
            print_pause("\nJim: I hope you don't regret your choice "
                        "stranger!!")
            print_pause("Jim: Deposit coins as you desire")
            print_pause("Jim: If you win , you will have double the deposit")
            print_pause("Jim: Lose, I keep the coins.")
            # input to bet desired amount of coins
            coins_deposited = int(input("How much would you like to bet:"))
            print_pause("Your coins: " + str(coins) + " -"
                        " " + str(coins_deposited))
            coins -= coins_deposited
            print_pause("Your coins= " + str(coins))
            # if player does not have enough coins
            if coins < 0:
                low_coins_message()
                print_pause("You are sent back to the scranton")
                scranton()
            # if player has enough coins, game resumes
            print_pause("\n The battle begins ..... \n")
            fight_result = fight_sequence("dragon", 20, 50, 20)
            # if player wins
            if fight_result == "player wins":
                print_pause("You have emerged victorious in this battle")
                print_pause("The dragon kneels down before you\n")
                print_pause("Jim: A combat to remember by stranger!!")
                # if player has not won the special night prize before
                if "Mystery Box" in contest_items:
                    print_pause("Jim: You are the first to bring down my "
                                "dragon, stranger!!")
                    print_pause("Jim: Let me reward you with the best "
                                "prize in my possession")
                    contest_items = remove_item(contest_items, "Mystery Box")
                    player_items.append("Mystery Box")
                    rewards_day = remove_item(rewards_day, "Special Prize"
                                              ": Mystery Box")
                    print_pause("\nNOTE: You have received a 'Mystery Box'.")
                # if player has won the special night prize already
                else:
                    print_pause("Jim: Congratulation, stranger! you won "
                                "this battle")
                    print_pause("Jim: You earn the right to call yourself"
                                "- 'The strongest among the scranton'")
                    coins_deposited = 2*coins_deposited
                    print_pause("Your coins: " + str(coins) + " +"
                                " " + str(coins_deposited))
                    coins += coins_deposited
                    print_pause("Your coins: " + str(coins))
            # if player loses
            else:
                print_pause("Jim: It is no simple task to defeat "
                            " the dragon stranger!!")
        # if player chooses to fight the dragon
        elif "no" in fight_choice:
            print_pause("Jim: There is no shame in retreat, stranger")
            game_night_contest()
        # condition to deal unrecognized input
        else:
            print_pause("Jim: I don't understand your words stranger")
            game_night_contest()
    # if player wants to fight the goblin
    elif "goblin" in contest_night_choice:
        # a special situation for the player to raise coins if broken completely
        print_pause("\nJim: You don't have to Deposit any coins to "
                    "play the game")
        print_pause("Jim: You get 50 coins on win and nothing to lose")
        print_pause("Your coins: " + str(coins))
        print_pause("\n The battle begins ..... \n")
        fight_result = fight_sequence("goblin", 10, 30, 10)
        # if player wins
        if fight_result == "player wins":
            print_pause("Jim: Well done stranger!")
            print_pause("Jim: You are tougher than you look")
            print_pause("Jim: Perhaps you might have a chance to "
                        "defeat our dragon")
            print_pause("Jim: You have won 50 coins")
            print_pause("Your coins: " + str(coins) + " + 50")
            coins += 50
            print_pause("Your coins: " + str(coins))
        # if player loses
        else:
            print_pause("Jim: Arena is merciless stranger.., "
                        "you lost your deposit")
    # if player wants to check the reward before fighting
    elif "reward" in contest_night_choice:
        print_pause(list_serial(rewards_night))
        game_night_contest()
    # condition to deal unrecognized input
    else:
        print_pause("Jim: Say the correct words stranger")
        game_night_contest()
    # trigger to let the player compete again
    print_pause("Jim: would you like to fight again stranger ?")
    play_again = input("1.yes\n2.no\n").lower()
    if "yes" in play_again:
        game_night_contest()
    else:
        print_pause("Jim: Good bye, stranger")
        scranton()


# A branch sequence to the funtion 'game_night_contest'
def fight_sequence(enemy, enemy_offense_min, enemy_offense_max, enemy_defense):
    global player_life
    global player_offense_min
    global player_offense_max
    global player_defense
    global player_offense_moves
    global player_defense_moves
    global enemy_offense_moves
    global enemy_defense_moves
    global animal_offense_moves
    global animal_defense_moves
    global rewards_night
    global animal_list
    global strong_animal_list
    global game_over

    enemy_life = 100
    # a loop to let player and enemy deal random damage in each turn
    for turn in range(40):
        # if trun is even NUMBER and player is alive
        if turn % 2 == 0 and player_life > 0:
            print_pause("Player Attacks....//")
            # print random message from the list 'player_offense_moves'
            print_pause(random.choice(player_offense_moves))
            # if enemy is an animal
            if enemy in animal_list or enemy in strong_animal_list:
                # print random message from the list 'animal_defense_moves'
                print_pause(random.choice(animal_defense_moves))
            # if enemy is not an animal
            else:
                # print random message from the list 'enemy_defense_moves'
                print_pause(random.choice(enemy_defense_moves))
            # assign random NUMBER with in the range to player's offence
            player_offense = random.randint(player_offense_min,
                                            player_offense_max)
            enemy_damage = enemy_defense - player_offense
            # as damage decreases the life, it cannot be a positive NUMBER
            if enemy_damage > 0:
                enemy_damage = 0
            print_pause("Enemy damage : " + str(enemy_damage))
            # decrement enemy life based on damage
            enemy_life = life_decrease(enemy_life, enemy_damage)
            # display both player's and enemy's life
            print_pause("Your life: " + str(player_life))
            print_pause("Enemy life : " + str(enemy_life)+ "\n")
        # if trun is odd NUMBER and enemy is alive
        elif turn % 2 == 1 and enemy_life > 0:
            print_pause(enemy + " Attacks....//")
            # if enemy is an animal
            if enemy in animal_list or enemy in strong_animal_list:
                # print random message from the list 'animal_offense_moves'
                print_pause(random.choice(animal_offense_moves))
            # if enemy is not an animal
            else:
                # print random message from the list 'enemy_offense_moves'
                print_pause(random.choice(enemy_offense_moves))
            # print random message from the list 'player_defense_moves'
            print_pause(random.choice(player_defense_moves))
            # assign random NUMBER with in the range to enemy's offence
            enemy_offense = random.randint(enemy_offense_min,
                                           enemy_offense_max)
            player_damage = player_defense - enemy_offense
            # as damage decreases the life, it cannot be a positive NUMBER
            if player_damage > 0:
                player_damage = 0
            print_pause("Player damage: " + str(player_damage))
            # decrement player's life based on damage
            player_life = life_decrease(player_life, player_damage)
            # display both player's and enemy's life
            print_pause("Your life: " + str(player_life))
            print_pause("Enemy life : " + str(enemy_life) + "\n")
        # if enemy loses the battle
        if player_life > 0 and enemy_life <= 0:
            print_pause("You have successfully slain the " + enemy)
            print_pause("You emerge victorious !!")
            return "player wins"
        # if player loses the battle
        elif player_life <= 0 and enemy_life > 0:
            print_pause("You lost this battle....")
            # if the fight is in the contest arena
            # your life will be restored to bare minimum
            if enemy == "goblin" or enemy == "dragon":
                print_pause("\nNOTE: Your life restored to 10")
                print_pause("NOTE: Find a way to increase your life")
                player_life = 10
                print_pause("Your life: " + str(player_life) + "\n")
                return "enemy wins"
            # if the fight is not in the contest arena
            # game ends
            print_pause("You are dead.")
            game_over = "activate"
            scranton()


# funtion to trigger the location 'jungle' in the scranton
def jungle():
    global jungle_trigger
    global time_zone
    global player_items
    # if player got tired from exploring jungle
    if jungle_trigger == "activate":
        print_pause("You are tired, comeback tomorrow")
        scranton()
    # if player tries to enter jungle at night time
    if time_zone == "night":
        # player must have a light element to enter jungle at night time
        if "neon light" in player_items:
            print_pause("You go into the jungle tearing the shadows"
                        " with your light element.")
            jungle_choice()
        # if player does not have a light element, he must be rejected
        else:
            print_pause("The jungle is dark and dangerous at night")
            print_pause("You need a light source to move forward")
            print_pause("You head back to the scranton")
            scranton()
    # if player enters jungle at daytime
    # as we bypassed night time conditional statement,
    # no conditional statement is required to specify day time trigger
    print_pause("You go deep into the jungle")
    print_pause("The jungle is vast and home to all kinds of things."
                " Including wild animals...")
    jungle_choice()


# A branch sequence to the funtion 'jungle'
def jungle_choice():
    global time_zone
    global player_items
    global gift_items
    global beets_day_count
    global flowers_day_count
    global glowing_lilies_day_count

    print_pause("\nEnter the NUMBER to perform the desired action:")
    jungle_action = input("1. Flowers"
                          "\n2. Beets"
                          "\n3. Explore"
                          "\n4. Back to scranton\n")
    # if player chooses to collect flowers during daytime
    if jungle_action == "1" and time_zone == "day":
        # if player already possess flowers in his items
        if "Flowers" in player_items:
            print_pause("You already have flowers")
            jungle_choice()
        # if player doeas not have flowers in his items
        else:
            print_pause("You collect different kinds of flowers")
            flowers_day_count = 0
            player_items.append("Flowers")
            gift_items.append("Flowers")
            jungle_choice()
    # if player chooses to collect flowers during daytime
    # flowers are replaced bu glowing lilies during night time
    elif jungle_action == "1" and time_zone == "night":
        # if player already possess glowing lilies in his items
        if "Glowing lilies" in player_items:
            print_pause("You already have glowing lilies")
            jungle_choice()
        # if player doeas not have glowing lilies in his items
        else:
            print_pause("You witness flowers glowing in the dark")
            print_pause("You collected some glowing lilies")
            glowing_lilies_day_count = 0
            player_items.append("Glowing lilies")
            gift_items.append("Glowing lilies")
            jungle_choice()
    # if player chooses to collect beets irrespective of time
    elif jungle_action == "2":
        # if player already possess beets in his items
        if "beets" in player_items:
            print_pause("You already have beets in your inventory")
            jungle_choice()
        # if player does not possess beets in his items
        else:
            print_pause("You gather beets and pack them carefully.")
            beets_day_count = 0
            player_items.append("beets")
            gift_items.append("beets")
            jungle_choice()
    # if player chooses to explore jungle irrespective of time
    elif jungle_action == "3":
        print_pause("\nNOTE: The jungle is vast")
        print_pause("Enter the NUMBER of the location, you want to search:")
        jungle_explore()
    # if player chooses to return to the scranton
    elif jungle_action == "4":
        print_pause("You head back to the scranton")
        scranton()
    # condition to deal unrecognized input
    else:
        print_pause("Enter a valid number")
        jungle_choice()


# A branch sequence to the funtion 'jungle_choice'
def jungle_explore():
    global player_items
    global jungle_explore_count
    global jungle_trigger
    global animal_list
    global strong_animal_list
    # animal attack triggers at random with a probability of '1/4'
    animal_attack = random.choice(["no", "yes", "no", "no"])
    # if animal attack triggerd
    if animal_attack == "yes":
        # if animal attack is during daytime,
        # random animal is selected from 'animal_list'
        if time_zone == "day":
            animal = random.choice(animal_list)
            print_pause("You have been ambushed by " + animal)
            fight_result = fight_sequence(animal, 0, 30, 0)
        # if animal attack is during night time,
        # random animal is selected from 'strong_animal_list'
        else:
            animal = random.choice(strong_animal_list)
            print_pause("You have been ambushed by " + animal)
            fight_result = fight_sequence(animal, 20, 40, 10)
        # if player wins
        if fight_result == "player wins":
            print_pause("You have courageously fought the animal and"
                        " killed it")
            print_pause("You resume your search")
        # if player loses, the sequence is executed in 'fight_sequence'
    # allows the player to enter an input to explore the jungle
    
    jungle_explore_action = int(input("Location : "))
    jungle_explore_count += 1
    # if exlpore input/count is given more than 3 times,
    # player is restricted to enter untill the next day
    if jungle_explore_count > 3:
        print_pause("You are tired, come back tomorrow")
        print_pause("You have returned back to the scranton")
        jungle_trigger = "activate"
        scranton()
    if jungle_explore_action >= 1 and jungle_explore_action < 20:
        print_pause("\nNOTE: You find nothing in this location, "
                    "better look somewhere else")
    elif jungle_explore_action >= 20 and jungle_explore_action < 25:
        print_pause("\nNOTE: You sense something not far from here")
    elif jungle_explore_action >= 25 and jungle_explore_action < 28:
        print_pause("\nNOTE: You are close to finding something...")
    elif jungle_explore_action == 28:
        print_pause("You found the 'Lost Tomb of Robert Dunder'")
        print_pause("The tomb is sealed off and require a keyword password")
        tomb()
    elif jungle_explore_action > 28 and jungle_explore_action <= 32:
        print_pause("\nNOTE: You are close to finding something")
    elif jungle_explore_action > 32 and jungle_explore_action <= 36:
        print_pause("\nNOTE: You sense something not far from here")
    elif jungle_explore_action > 36:
        print_pause("\nNOTE: You find nothing in this location, "
                    "better look somewhere else")
    # condition to loop back to explore option
    else:
        print_pause("Enter a NUMBER to search the respective location")
        jungle_explore()
    jungle_explore()


# A branch sequence to the funtion 'jungle_explore'
def tomb():
    global player_items
    global player_offense_min
    global player_offense_max
    global Keyword_count

    tomb_keyword = input("Enter the keyword: ")
    # if the keyword input is correct
    if tomb_keyword == "joshirk":
        print_pause("\nThe Robert Dunder's Tomb gates open with crackling sound")
        print_pause("You enter thr tomb and inspect with utmost care")
        print_pause("The ceo Robert Dunder's body still holds the legendary"
                    " sword: The Light Saber")
        print_pause("You have accquired the Legendary sword: Light Saber")
        player_items.append("Light Saber")
        # player stats will be increased
        player_offense_min = 50
        player_offense_max = 80
        print_pause("\nNOTE: Your offense has increased "
                    "to: " + str(player_offense_max))
        print_pause("NOTE: You are now stronger than ever!!")
        print_pause("\nYou now head back to the scranton")
        scranton()
    # if the keyword input is not matched
    else:
        Keyword_count += 1
        # if number of tries is not exceeded
        if Keyword_count <= 3:
            print_pause("\nNOTE: Wrong password, try again")
            tomb()
        # if the keyword is mismatched 3 times in a row
        else:
            Keyword_count = 0
            print_pause("\nYou have exceeded the number of tries")
            print_pause("You have been locked out for the rest of the day")
            print_pause("come back tommorow to try again")
            print_pause("You head back to the Scranton")
            scranton()


# funtion to trigger the location 'office' in the scranton
def office():
    global darryl
    global player_items
    global coins
    global treasure_box
    global chest
    global toby
    # if the player have light element to enter the office
    if "neon light" not in player_items:
        print_pause("You need light element to explore the dark office")
        print_pause("You head back to the scranton.")
        scranton()
    print_pause("Enter the NUMBER of the route you want to take.")
    office_choice = input("\n1. Warehouse"
                        "\n2. Conference Room"
                        "\n3. Annex"
                        "\n4. Back to scranton\n")
    # if player wants to enter route 1
    if office_choice == "1":
        # if darryl gaurding the route 1 is alive
        if darryl == "alive":
            print_pause("This route is gaurded by Darryl")
            print_pause("darryl is a strong opponent with thick skin")
            print_pause("what would you do?")
            route1_choice = input("\n1. Fight"
                                  "\n2. Run away\n").lower()
            # if player chooses to fight the darryl
            if "fight" in route1_choice:
                print_pause("You decided to fight Darryl\n")
                fight_result = fight_sequence("darryl", 20, 40, 10)
                if fight_result == "player wins":
                    print_pause("You have triumphed over the darryl")
                    # trigger to skip this part if visited again
                    darryl = "defeated"
            # if player chooses to run
            elif "run" in route1_choice:
                print_pause("You have strategically with drawn from a "
                            "death battle")
                print_pause("You should head back to the scranton to "
                            "prepare for the battle, before trying again")
                office()
            # condition to deal with unrecognized input
            else:
                print_pause("\nNOTE: Don't sweat, camly select "
                            "the NUMBER of your choice")
                office()
        # if the darryl has been already slain
        else:
            print_pause("Darryl gaurding the route has been slain")
            print_pause("You can travel furthur deep into the route now")
        # After the darryl part
        print_pause("\nYou travel deep into the Warehouse\n")
        print_pause("There is Dwight's Treasure box at the center of the room")
        print_pause("Would you like to open it?")
        treasure_box = input("\n1. Yes"
                             "\n2. No\n").lower()
        # if player chooses to open the box
        if "yes" in treasure_box:
            # if the treasure has been already looted
            if treasure_box == "empty":
                print_pause("The Treasure Box is already looted by you")
                print_pause("There is nothing intersting here")
                print_pause("You head back to the office entrance\n")
                office()
            # if the treasure is not looted
            print_pause("Treasure Box is sealed with a peculiar lock")
            # if the player has the key accquired from jan
            if "private key" in player_items:
                print_pause("You use the 'private key' given by the "
                            "jan herself")
                print_pause("You opened the Treasure box and finds "
                            "a 'candle'")
                print_pause("This looks like some kind of Family Heirloom")
                print_pause("\nNOTE: You have accquired a 'Royal candle'")
                player_items.append("Royal candle")
                # trigger to indicate, the treasure has been looted
                treasure_box = "empty"
                print_pause("You head back to the office entrance\n")
                office()
            # if the player does not have the key
            else:
                print_pause("You head back to the office entrance\n")
                office()
        # if player chooses not to open the box/ gives unrecognized input
        else:
            print_pause("You head back to the office entrance\n")
            office()

    # if player wants to enter route 2
    elif office_choice == "2":
        print_pause("\nNOTE: The entrance to the office is locked and "
                    "requires a key to open")
        # if player has the key, won in the contest arena
        if "Unknown Key" in player_items:
            print_pause("Would you like to try the 'Unknown Key', "
                        "you have won in the contest arena?")
            route2_choice = input("\n1 Yes"
                                  "\n2. No\n").lower()
            # if player tries to open the door using unknown key
            if "yes" in route2_choice:
                print_pause("The key matches the lock")
                print_pause("You opened the door and head furthur deep "
                            "into Route2")
                print_pause("In the room you found a chest eating dust")
                print_pause("The chest looks old and dangerous")
                print_pause("What would you do ?")
                chest_choice = input("\n1. Open"
                                     "\n2. Head back\n")
                # if player wants to open the chest
                if "open" in chest_choice:
                    # if the chest is already looted
                    if chest == "empty":
                        print_pause("You greedily open the chest again")
                        print_pause("Unfortunately, the chest does not get "
                                    "filled with coins automatically")
                        print_pause("The chest is already looted by you")
                        print_pause("There is nothing to do here")
                        print_pause("You head back to the office entrance\n")
                        office()
                    # if the chest is not looted
                    print_pause("You reluctantly open the chest")
                    print_pause("Voila...!! Its a treasure chest "
                                "filled with coins....")
                    print_pause("\nNOTE: You received 20000 coins")
                    print_pause("coins: " + str(coins) + " + 20000")
                    coins += 20000
                    print_pause("Your coins: " + str(coins))
                    # trigger to indicate, the chest has been already looted
                    chest = "empty"
                    print_pause("You head back to the office entrance\n")
                    office()
                # if player do not want to open chest/gives unrecognized input
                else:
                    print_pause("You head back to the office entrance\n")
                    office()
            # if player do not want to open door/gives unrecognized input
            else:
                print_pause("You head back to the office entrance\n")
                office()
        # if player does not have the key, won in the contest arena
        else:
            print_pause("\nNOTE: Come back after you acccquired "
                        "the key to 'conference room'")
            print_pause("You head back to the office entrance\n")
            office()

    # if player wants to enter route 3
    elif office_choice == "3":
        print_pause("This looks like a man made cellar")
        print_pause("There is a red post depicting as restricted region")
        print_pause("The cellar entrance is locked")
        # if player has the cellar key stolen from ceos quaters
        if "Cellar Key" in player_items:
            print_pause("\nWould you like to open the cellar?")
            route3_choice = input("1. Yes\n2. No\n").lower()
            # if player wants to open the cellar door
            if "yes" in route3_choice:
                print_pause("\nYou enterd the cellar while staying on gaurd")
                print_pause("You go deep in inner section of the office")
                # if the toby is alive
                if toby == "alive":
                    print_pause("\nThere is Toby sleeping actross"
                                " the cellar, blocking the path")
                    print_pause("Toby gives off a deathly vibe and "
                                "extremely vicious")
                    print_pause("\nNOTE: This is a high level enemy")
                    print_pause("NOTE: You propably need a special "
                                "sword-Light Saber,")
                    print_pause("      equipped with light element to defeat"
                                " the toby")
                    print_pause("\nDecide what to do?")
                    toby_choice = input("1. Wake Toby"
                                           "\n2. Come back later\n").lower()
                    # if player chooses to wake the toby
                    if "wake" in toby_choice:
                        print_pause("\nYou courageously draws your sword, "
                                    "ready to fight the toby")
                        print_pause("Toby lunges at you with great "
                                    "ferocity")
                        fight_result = fight_sequence("toby", 30, 50, 20)
                        # if player wins the battle
                        if fight_result == "player wins":
                            # trigger to indicate moster is has been slain
                            toby = "defeated"
                            print_pause("\nYou gather strength and "
                                        "go furthur deep into the "
                                        "cellar\n")
                            cellar_rooms()
                        # if player loses the battle,
                        # result will be executed in the fight_sequence
                    # if player does not want to wake the toby
                    else:
                        print_pause("\nPerhaps you are not ready to face "
                                    "toby, come back later")
                        print_pause("You head back to office entrance\n")
                        office()
                # if toby has been slain
                elif toby == "defeated":
                    print_pause("\nThere's a monter lying dead in the middle of "
                                "the cellar")
                    print_pause("You move forward\n")
                    cellar_rooms()
            # if player does not want to open the cellar door
            # or give unrecognized input
            else:
                print_pause("\nYou are not sure about the choice")
                print_pause("Perhaps you should comeback later !")
                print_pause("You head back to the office entrance")
                office()
        # if player does not have the cellar key stolen from ceos quaters
        else:
            print_pause("\nNOTE: Come back after you have accquired"
                        " cellar key")
            print_pause("You head back to office entrance\n")
            office()

    # if player choose to head back to the scranton
    elif office_choice == "4":
        print_pause("You head back to the scranton\n")
        scranton()
    # condition to deal with unrecognized input
    else:
        print_pause("\nEnter a valid NUMBER")
        office()


# A branch sequence to the funtion 'office'
def cellar_rooms():
    global huge_monster
    global player_defense
    # allows the player to choose between two doors
    print_pause("\nYou find 2 doors- an blue door and a "
                "red door, at the end of the cellar")
    print_pause("\nWhat would you do?")
    door_choice = input("1. Open blue Door"
                        "\n2. Open red Door"
                        "\n3. Head back\n").lower()
    # if player chooses to opne the blue door
    if "blue" in door_choice:
        print_pause("\nYou enter the room with the blue Door")
        # if huge toby is already slain
        if huge_monster == "defeated":
            print_pause("There a monster corpse rotting in the corner of room")
            print_pause("There is nothing else in this room")
            print_pause("You head back")
            cellar_rooms()
        # if huge monster is not slain/ alive
        print_pause("Suddenly, a Huge Monster jumps between"
                    " you and the entrance")
        print_pause("You cannot escape, leaving you no "
                    "choice but to fight")
        fight_result = fight_sequence("Huge monster", 30, 60, 30)
        # if player wins the battle
        if fight_result == "player wins":
            print_pause("\nThe sudden battle made your boold rush to head")
            print_pause("With the monster defeatd you were able to "
                        "leave the room")
            # trigger to indicate, hume monster has been slain
            huge_monster = "defeated"
            cellar_rooms()
        # if player loses,
        # result will be executed in the fight_sequence
    # if player chooses to open red door
    elif "red" in door_choice:
        print_pause("\nThe room is very old and filled with corpses"
                    " of fighters")
        print_pause("It appears there were numerous attempts to defeat the "
                    "monster")
        print_pause("Apparently none of them succeded")
        # if steel cheild has not yet been collected
        if "Steel Sheild" not in player_items:
            print_pause("\nYou search the room and finds a steel shield,\n "
                        "in the hands of a dead commander")
            print_pause("\nNOTE: You have accquired 'Steel Sheild'")
            print_pause("NOTE: Your defense has been increased")
            print_pause("Defense :" + str(player_defense) + " + 40")
            # player stats increased
            player_defense += 40
            player_items.append("Steel Sheild")
            print_pause("Player Defense increased to: " + str(player_defense))
        # if steel cheild has already been collected
        print_pause("\nThere is nothing else execpt for the rotting corpses "
                    "in this room ")
        print_pause("You head back to the office entrance")
        office()
    # if player chooses to head back to the office entrance
    elif "back" in door_choice:
        print_pause("You head back to the office entrance")
        office()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter your speciific choice in words")
        cellar_rooms()


# funtion to trigger the location 'corporate' in the scranton
def corporate():
    global player_items
    global corporate_count
    global coins
    global time_zone
    global player_status
    global toll_status
    global ceos_status

    corporate_count += 1
    # if player tries to enter corporate at night time, he should be restricted
    if time_zone == "night":
        print_pause("The access to corporate is restricted at night time")
        print_pause("Come back later")
        print_pause("You head back to the scranton")
        scranton()
    # if ceos identity is revealed to the player, player should be
    # allowed into the corporate even if the player is wanted for the crime
    if ceos_status == "revealed":
        print_pause("You enter corporate building demading a meeting with the ceo")
        print_pause("You were allowed inside the inner halls of the corporate")
        inner_corporate()
    # player will be imprisoned, if he tries to
    # enter the corporate and is wanted foe a crime
    if player_status == "wanted":
        print_pause("It was not a wise choice to place yourself infront of "
                    "gaurds\n while wanted for tresspassing.")
        print_pause("You got caught and sent to prison")
        prison()
    # if corporate access is already granted to the player by the ceo
    if corporate_access == "granted":
        print_pause("You have entered inside the corporate")
        inner_corporate()
    # if player enter the corporate gates for the first time
    if corporate_count == 1:
        print_pause("Dunder Mifflin has a Magnificient corporate building")
        print_pause("You seek an audience with the ceo but was denied "
                    "by the Guard")
        print_pause("Guard: I'm afraid, I cannot let just anyone pass, kid")
        print_pause("Guard: But I will make an exemption for 500 coins, "
                    "what do you say :")
    # if player enters the corporate gate more than once
    if corporate_count > 1:
        print_pause("\nYou are at the corporate Gate")
        # if toll was already paid and possess reports
        if toll_status == "paid" and "reports" in player_items:
            print_pause("Guard: You may pass now kid")
            print_pause("You head inside the corporate")
            inner_corporate()
        # if toll was already paid and does not possess reports
        elif toll_status == "paid" and "reports" not in player_items:
            print_pause("Guard: Obtain a suitable gift to present "
                        "to the ceo first.")
            print_pause("Guard: Then come seek his audience, kid !")
            print_pause("\nYou head back to the scranton in search of the ")
            print_pause("worthy present to offer the ceo")
            scranton()
        # if toll is not paid
        print_pause("Guard: You have to pay the Toll kid")

    # prompted to pay the toll on first visit to the corporate gate
    print_pause("\nNOTE: Will you pay the TOll ? what do you choose to do ?")
    toll = input("1. Pay 500 coins"
                 "\n2. Deny"
                 "\n3. Persuade\n").lower()
    # if player chooses to pay the toll
    if "coins" in toll:
        # if player does not have enough coins to pay the toll
        if coins < 500:
            print_pause("\nNOTE: Low in coins")
            print_pause("Guard: Earn the coins, kid")
            print_pause("You are sent back to the scranton")
            scranton()
        # if player has enough coins to pay the toll
        print_pause("\nYou pay the toll")
        print_pause("coins: " + str(coins) + " - 500")
        coins -= 500
        print_pause("Your coins: " + str(coins))
        # trigger to indicate toll has been paid
        toll_status = "paid"
        print_pause("\nGuard: Good choice kid....but I cannot just "
                    "let you pass yet")
        print_pause("Guard: Do you really think I'll let you pass for "
                    "500 coins alone ? hahahhah..")
        print_pause("Guard: Can't really put you in his presense, "
                    "empty handed")
        # if player already has reports in his possession on first visit
        if "reports" in player_items:
            print_pause("You have the right gift in your possession "
                        "to present to the ceo")
            print_pause("You were allowed inside the corporate")
            inner_corporate()
        # if player does not have reports in his possession on first visit
        else:
            print_pause("Guard: Come back after you have the anything "
                        "worthy to give to a ceo")
            print_pause("You were sent back to the scranton")
            scranton()
    # if player chooses not to pay the toll
    elif "deny" in toll:
        print_pause("\nGuard: Fine then. I won't let you pass kid")
        print_pause("You were sent back to the scranton")
        scranton()
    # if player chooses to convince without paying the toll
    elif "persuade" in toll:
        # player must have reports in his possession to convince
        if "reports" in player_items:
            print_pause(player + ": I have some important reports from scranton branch")
            print_pause(player + ": Do you think its a good idea to stop "
                        "me?")
            print_pause("The Guard stays silent for a minute and "
                        "lets you pass in")
            inner_corporate()
        # if player does not have reports in his possession to convince
        else:
            print_pause("\nYou have nothing to bargain with the access "
                        "to the corporate")
            print_pause("\nNOTE: You either pay the TOLL or accquire certain "
                        "ITEM to persuade")
            print_pause("You head back to the scranton")
            scranton()
    # condition to deal with unrecognized input
    else:
        print_pause("Guard: Say the correct words kid")
        corporate()


# A branch sequence to the funtion 'corporate'
def inner_corporate():
    global player_items
    global time_zone
    global inner_corporate_count
    global phone
    global corporate_access
    global cabinet_status
    global ceos_status

    print_pause("\nYou are inside the corporate")
    print_pause("What do you choose :")
    # displays list of locations in a serial order, during daytime
    if time_zone == "day":
        inner_corporate_choice = input(list_serial(corporate_locations_day)).lower()
    # displays different list of locations in a serial, during night time
    elif time_zone == "night":
        inner_corporate_choice = input(list_serial(corporate_locations_night)).lower()
    # if player enters central hall during daytime
    if "hall" in inner_corporate_choice and time_zone == "day":
        inner_corporate_count += 1
        # intro to be triggered only once
        if inner_corporate_count == 1:
            print_pause("The central hall is filled with many "
                        "dignitaries and head office members")
            print_pause("In the middle is the ceo listening to a presentation")
            print_pause("You present yourself to the ceo bearing "
                        "the 'reports'")
            print_pause("The ceo is pleased and welcomes "
                        "you to corporate at NYC")
            print_pause("\nNOTE: You gain access to corporate")
            print_pause("NOTE: You gain access to the 'File cabinet' and 'Jan's office'")
            # trigger to give access to the corporate
            corporate_access = "granted"
            inner_corporate()
        # if player enters central hall more than once, during daytime
        if inner_corporate_count > 1:
            print_pause("The central hall is occupied as usaul with dignitaries")
            print_pause("They seemed to be busy.")
            # if ceos identity is revealed to the player by hologram
            if ceos_status == "revealed":
                challenge_ceo()
            # if ceos identity is not revealed to the player by hologram
            print_pause("\nNOTE: Perhaps you should come back later")
            print_pause("You head back to the inner halls")
            inner_corporate()
    # if player enters central hall during night time
    elif "hall" in inner_corporate_choice and time_zone == "night":
        # if security is alerted
        if phone == "activated":
            prison()
        # if security is not alerted
        print_pause("The central hall is empty and lack any security patrols")
        print_pause("This place is perfect to create any distractions")
        print_pause("\nWhat would you do ?")
        hall_choice = input("1. Ring the central hall phone"
                            "\n2. Go back\n").lower()
        # if player chooses to create a distraction
        if "phone" in hall_choice:
            print_pause("You rang the central hall phone")
            print_pause("The sound of the phone echoes throught out the corporate")
            print_pause("The ceo and the gaurds are alerted !!")
            print_pause("\nNOTE: It is advised to avoid the "
                        "central hall untill next day")
            # trigger to indicate gaurds are alerted
            phone = "activated"
            print_pause("You leave the central hall")
            inner_corporate()
        # if player chooses to not to create a distraction
        elif "back" in hall_choice:
            print_pause("May be it is best to consider all options")
            print_pause("You head back to the inner corporate")
            inner_corporate()
        # condition to deal with unrecognized input
        else:
            print_pause("Choose the correct words, ")
            print_pause("come back after you make up your mind")
            inner_corporate()

    # if player chooses to enter the cabinet
    elif "cabinet" in inner_corporate_choice:
        # if cabinet is already brunt by player as a distraction
        if cabinet_status == "burnt":
            # if gaurds are alerted
            if phone == "activated":
                prison()
            # if gaurds are not alerted
            print_pause("The cabinet has been burnt to crisp")
            print_pause("There is nothing to salvage")
            print_pause("You head back to inner halls of corporate")
            inner_corporate()
        if time_zone == "night":
            # if gaurds are alerted
            if phone == "activated":
                prison()
            # if gaurds are not alerted
            print_pause("\nThis is another choice to create a distraction")
            print_pause("What would you do ?")
            cabinet_choice = input("1. Burn the cabinet"
                                   "\n2. Head back to inner corporate\n").lower()
            # if player chooses to burn cabinet as a distraction
            if "burn" in cabinet_choice:
                print_pause("\nYou take a lantern in the corner of the"
                            " cabinet,")
                print_pause("and started fire in multiple places to "
                            "confuse the soldiers")
                print_pause("\nNOTE: It is advisible to avoid cabinet for "
                            "the rest of the day")
                # trigger to indicate cabinet is burnt
                cabinet_status = "burnt"
                # trigger to indicate gaurds are alerted
                phone = "activated"
                print_pause("\nyou head back to the inner halls")
                inner_corporate()
            # if player chooses not to burn cabinet as a distraction
            elif "corporate" in cabinet_choice:
                print_pause("\nIt is wise to consider other options")
                print_pause("You head back to inner halls of the corporate")
                inner_corporate()
            # condition to deal with unrecognized input
            else:
                print_pause("\nEnter the correct words next time")
                print_pause("You were sent back to inner halls of the corporate")
                inner_corporate()
        # if cabinet access is given to the player by the king
        if corporate_access == "granted":
            print_pause("\nYou have entered the Great cabinet of the scranton")
            print_pause("The cabinet has more than 1000 books "
                        "collected for over 30 years")
            print_pause("You may find important information here:")
            print_pause("what would you like to study ?")
            cabinet_study = input("\n1. Ancient Beast"
                                  "\n2. Scranton"
                                  "\n3. Corporate"
                                  "\n4. DM\n").lower()
            # if player wants to study about the Beast
            if "beast" in cabinet_study:
                print_pause("\nThe beast is old and witty")
                print_pause("It is said to possess the strength greater than "
                            "any creature known")
                print_pause("The beast has the ability to disguise itself "
                            "as human being")
                print_pause("It can also manipulate other humans according "
                            "to its will")
                print_pause("The beast's skin is thick enough to deflect any"
                            " weapon's attacks")
            # if player wants to study about the scranton
            elif "scranton" in cabinet_study:
                print_pause("\nScranton is the place where the tv show office is set in")
                print_pause("They shot several scenes at actual locations")
                print_pause("The 'Electricity Song' was a hit.")
                print_pause("The tourism obviously boomes after the show")
            # if player wants to study about the corporate
            elif "corporate" in cabinet_study:
                print_pause("\nThe corporate is where the paper business happens")
                print_pause("It has been built as to overwatch"
                            " any enemy companies activities")
                print_pause("The corporate has withstood many seizes and "
                            "weather conditions")
                print_pause("Over the time, only few minor renovations are "
                            "made it.")
            # if player wants to study about the kingdom
            elif "DM" in cabinet_study:
                print_pause("\nDunder Mifflin is a paper company")
                print_pause("The main competetion is Staples")
                print_pause("Robert Dunder was the founder and first CEO")
                print_pause("The DM eventually expanded and divided "
                            "among many ceos for effective business")
            # condition to deal with unrecognized input
            else:
                print_pause("\nThere are no records of the word you mentioned")
                print_pause("You were sent back to inner halls of the corporate")
                inner_corporate()
            # after each study player is sent back to the 'inn'
            print_pause("\nYou are tired from all the reading")
            print_pause("You have no choice but to rest till morning")
            print_pause("You head back to the Schrute Farms to rent a room")
            room()
        # if corporate access is not given to the player
        elif corporate_access != "granted":
            print_pause("\nThe Cabinet is not accessable to everyone !")
            print_pause("You need permit from the CEO himself")
            print_pause("You were sent back to the inner halls of the corporate")
            inner_corporate()

    # if player chooses to enter the jan office
    elif "jan office" in inner_corporate_choice:
        # if player enters the jan office during night time
        if time_zone == "night":
            print_pause("\nThe jan office is dark without any light")
            print_pause("One can hide / sneak in the jan office at night "
                        "without getting detected")
            print_pause("There is nothing interesting here")
            print_pause("\nWhat would you do ?")
            jan_office_choice = input("1. Go Back to corporate"
                                  "\n2. Enter Secret Passage\n").lower()
            # if player wants to enter corporate
            if "corporate" in jan_office_choice:
                print_pause("\nYou sneaks into the inner halls of corporate")
                inner_corporate()
            # if player wants to enter secret passage
            elif "secret" in jan_office_choice:
                print_pause("\nYou enter the Secret Passage")
                secret_passage()
            # condition to deal with unrecognized input
            else:
                print_pause("\nEnter the correct choice")
                print_pause("You were sent to the inner halls anyway")
                inner_corporate()
        # if corporate/jans office access was not granted to the player
        if corporate_access != "granted":
            print_pause("\nThe Jan Office area is restricted to strangers")
            print_pause("You need permit from the ceo himself")
            print_pause("You were sent back to the inner halls of the corporate")
            inner_corporate()
        # if corporate/jans office access is granted to the player
        elif corporate_access == "granted" and time_zone == "day":
            print_pause("\n Jan's Office looks beautiful under the radiant sun")
            print_pause("You find jan roaming in her Office")
            jan()

    # if player chooses to enter the quaters
    elif "quaters" in inner_corporate_choice:
        # quaters are restricted during daytime
        if time_zone == "day":
            print_pause("The quaters are not accessable to anyone "
                        "but head members")
            print_pause("You head back to the inner halls")
            inner_corporate()
        # player can sneak into the quaters during night time
        if time_zone == "night":
            print_pause("You sneak into the quaters")
            royal_quaters()
    # if player chooses to return to the scranton
    elif "scranton" in inner_corporate_choice:
        print_pause("You head back to the scranton")
        scranton()
    # condition to deal with unrecognized input
    else:
        print_pause("\nNOTE: Enter the correct words....\n")
        inner_corporate()


# A branch sequence to the funtion 'inner_corporate'
def royal_quaters():
    global phone
    global player_items
    # player's choice
    print_pause("Where would you like to go ?")
    royal_quaters_choice = input("\n1. Ceos Quaters"
                                 "\n2. Jan Quaters"
                                 "\n3. Go back to corporate \n").lower()
    # if player chooses to sneak into ceo's quaters
    if "ceo" in royal_quaters_choice:
        # if gaurds are alerted and deistraction created
        if phone == "activated":
            print_pause("\nThe room is empty, perhaps the distraction worked"
                        " fine!!")
            print_pause("You tip-toed into the ceo's quaters")
            print_pause("You searched the room for the cellar keys")
            print_pause("The cellar keys are were found inside a cabinet")
            print_pause("\nNOTE: You have accquired the Cellar keys!")
            player_items.append("Cellar Key")
            print_pause("NOTE: It is adviced to leave the corporate for the day")
            print_pause("You head back to the inner halls of corporate")
            inner_corporate()
        print_pause("\nThe ceo is sleeping on the Royal bed")
        print_pause("\nNOTE: It is adviced to create a distraction before"
                    " going inside")
        ceos_quaters()
    # if player chooses to sneak into jan quaters
    elif "jan" in royal_quaters_choice:
        print_pause("\nJan is fast asleep")
        print_pause("Perhaps it is better to leave")
        print_pause("You head back to the inner halls")
        inner_corporate()
    # if player chooses to return to the corporate
    elif "corporate" in royal_quaters_choice:
        print_pause("\nYou head back to the inner halls of the corporate")
        inner_corporate()
    # condition to deal with unrecognized input
    else:
        print_pause("\nEnter the correct choice of words")
        royal_quaters()


# A branch sequence to the funtion 'inner_corporate'
def ceos_quaters():
    # if player already stole the cellar key from ceos quaters
    if "Cellar Key" in player_items:
        print_pause("\nNOTE: You alredy got the Cellar Key")
        print_pause("You head back to the inner halls")
        inner_corporate()
    # if player has not yet stolen the cellar key from ceos quaters
    print_pause("\nWill you take the risk ?")
    print_pause("Enter the NUMBER of your choice:")
    ceos_quaters_choice = input("1. Yes, go inside and take the risk"
                                 "\n2. No, go back and consider a "
                                 "distraction\n").lower()
    # if player decided to sneak into the ceos quaters
    if ceos_quaters_choice == "1":
        print_pause("\nYou sneak into the ceos quaters to search for "
                    "cellar key")
        print_pause("The ceo started to wake up!!!!!")
        print_pause("\nWould you still look for the cellar key?")
        search_choice = input("1. Yes"
                              "\n2. No\n").lower()
        # if player chooses to take take the risk
        if "yes" in search_choice:
            print_pause("\nThe ceo wakes up and find you sneaking in "
                        "his room")
            print_pause("The ceo does not like Trespassers")
            print_pause("You were caught and imprisoned!!!!!")
            prison()
        # if player chooses not to take take the risk
        elif "no" in search_choice:
            print_pause("\nYou avoided getting caught")
            print_pause("You head back to the inner halls of the corporate")
            print_pause("Perhaps it is best to consider a distraction, \n"
                        "before trying again !!")
            inner_corporate()
        # condition to deal with unrecognized input
        else:
            print_pause("\nNOTE: You were not sure of your choice")
            print_pause("Hence you are sent back to the inner halls to "
                        "re-evalute your choices")
            inner_corporate()
    # if player decided not to sneak into the ceos quaters
    elif ceos_quaters_choice == "2":
        print_pause("You decided to wise up and create a distraction "
                    "instead taking a risk")
        print_pause("You head back to the quaters to consider possible"
                    " distractions")
        royal_quaters()
    # condition to deal with unrecognized input
    else:
        print_pause("\nNOTE: Choose the correct NUMBER of your choice")
        ceos_quaters()


# A branch sequence to the funtion 'inner_corporate'
def jan():
    global jan_introduction
    global jan_quest_status
    global jan_count
    global name

    jan_count += 1
    # intro of the jan to be displayed only once
    if jan_count == 1:
        print_pause("You approach her with elegance to introduce yourself")
        print_pause("Jan is shy and distant")
    # if player visit the jan more than once
    elif jan_count > 1:
        print_pause("\nJan seemed excited to see you")
        print_pause("She approaches to talk to you")
    # player's decision
    print_pause("\nWhat would you do ?")
    jan_choice = input("1. Talk to her"
                            "\n2. Go back to corporate\n\n").lower()
    # if player wishes to talk to the jan
    if "talk" in jan_choice:
        print_pause("\nYou initiate a conversation with Jan")
        # if jan quest is already completed
        if jan_quest_status == "completed":
            print_pause("\nYou chat with Jan")
            print_pause("After a while you head back to the inner corporate area")
            inner_corporate()
        # if jan quest is still active and not introduced yet
        if jan_introduction != "completed":
            print_pause("\nGreetings Jan, you look beautiful")
            print_pause("jan: Greetings, What is your name?")
            name = input("Enter your name: ")
            initial_name = player.lower()
            new_name = name.lower()
            print_pause("jan: Nice to meet you " + name + " !!")
            # a message is displayed if you lie about your name
            if new_name != initial_name:
                print_pause("\nNOTE: You lied to jan regarding your"
                            " name")
            # trigger to indicate jan intro is done
            jan_introduction = "completed"
        # if jan quest is still active and introduction finished
        elif jan_introduction == "completed":
            print_pause("\njan: You are back again " + name + " !")
        print_pause("\nYou intend to offer a gift to jan")
        jan_quest()
    # if player wishes not to talk to the jan and return to corporate
    elif "corporate" in jan_choice:
        print_pause("You head back to the inner halls of the corporate")
        inner_corporate()
    # condition to deal with unrecognized input
    else:
        print_pause("\nJan seemed puzzeled by your words")
        print_pause("You should say the correct words")
        jan()


# A branch sequence to the funtion 'jan'
def jan_quest():
    global player_items
    global gift_items
    global jan_items
    global player
    global jan_quest_status
    global scranton_locations
    # if jan accepted more than 2 gifts from the player
    # she ask for a quest
    if len(jan_items) == 2 and jan_quest_status != "completed":
        # if quest is completed
        if "Royal candle" in player_items:
            print_pause("\njan: You brought back the Royal candle !!")
            print_pause("jan: Thank you " + player + " !! , This means a "
                        "lot to me")
            print_pause("jan: How could I repay you ?!")
            print_pause(player + " : It is my duty, jan. I will help you"
                        " however I could")
            player_items = remove_item(player_items, "Royal candle")
            jan_items.append("Royal candle")
            jan_quest_status = "completed"
            print_pause("jan: As a gratitude, let me tell you a secret")
            print_pause("jan: There ia a secret passage in this office"
                        " which leads to scranton")
            print_pause("jan: Only the head members"
                        " know about this passage")
            print_pause("jan: Perhaps it might help you !!\n")
            print_pause("Jan then leaves the Office in exitement")
            print_pause("\nNOTE: Jan forgot to take back "
                        "the 'private key' from you")
            print_pause("NOTE: Perhaps it might come in handy later!!???")
            print_pause("\nNOTE: The 'Royal candle' has been removed from "
                        "your possession")
            print_pause("\nNOTE: A secret passage has been revealed to you "
                        "between Office and scranton")
            # a secret passage will be added to the scranton locations
            scranton_locations.append("Secret Passage")
            print_pause("You head back to the inner halls of the corporate")
            inner_corporate()
        # if quest is not yet completed but briefed already
        elif "private key" in player_items:
            print_pause("\njan: Did you get the family "
                        "heirloom " + player + " ?")
            print_pause("jan: I hope you find it !!")
            print_pause("You head out to retrive the stolen item")
            scranton()
        # if quest is not yet completed nor briefed
        print_pause("\njan: I have a request to make of you " + player)
        print_pause("jan: There ia a family heirloom passed down for"
                    " generations")
        print_pause("jan: Apparently its been lost, more like stolen")
        print_pause("jan: I heard it has been stashed in one of the office"
                    " partitions")
        print_pause("jan: Will you bring it for me " + player + " ??")
        print_pause("jan: The heirloom is sealed in a royal box")
        print_pause("jan: You may need this private key to open it")
        player_items.append("private key")
        print_pause("\nNOTE: You have accquired 'private key'.")
        print_pause("You head back to the inner halls of the corporate")
        inner_corporate()

    # if jans quest is does not meet required conditions to get triggered
    # and player wants to give gift to the jan
    print_pause("\nWhat do you choose to offer ?")
    # if player does not have anything to offer to the jans
    # / len(gift_items) == 1 / is used because / leave / option
    # is used inside gift list
    if len(gift_items) == 1:
        print_pause("\nNOTE:You have nothing to offer to Jan")
        print_pause("NOTE: Come back later")
        print_pause("You head back to the inner halls")
        inner_corporate()
    # displays list of gift items in a serial list
    jan_choice = input(list_serial(gift_items)).lower()
    # if player wants to gift flowers and have them in his possession
    if "flowers" in jan_choice and "flowers" in gift_items:
        print_pause("jan: Beautiful flowers but nothing I haven't "
                    "seen in this Office")
        player_items = remove_item(player_items, "flowers")
        gift_items = remove_item(gift_items, "flowers")
        print_pause("\nNOTE: 'Flowers' has been removed from your possession\n")
        jan_quest()
    # if player wants to gift glowing lilies and have them in his possession
    elif "glowing" in jan_choice and "Glowing lilies" in gift_items:
        print_pause("jan: I have never seen a flower of this kind")
        print_pause("jan: Thank you!!! " + player)
        player_items = remove_item(player_items, "Glowing lilies")
        gift_items = remove_item(gift_items, "Glowing lilies")
        print_pause("\nNOTE: 'Glowing lilies' has been removed from your "
                    "possession\n")
        # if jan do not have them in her possession
        # she consider them as a gift item
        if "Glowing lilies" not in jan_items:
            jan_items.append("Glowing lilies")
            print_pause("\nNOTE: You relationship strengthened")
        jan_quest()
   
    # if player wants to gift steel armour and have them in his possession
    elif "armour" in jan_choice:
        if "Steel armour" in gift_items:
            print_pause("jan: Thank you very much " + player + " !!")
            print_pause("jan: I always wanted to try one of these")
            print_pause("jan: You have my gratitude " + player)
            player_items = remove_item(player_items, "steel armour")
            gift_items = remove_item(gift_items, "Glittering steel armour")
            print_pause("\nNOTE: 'Glittering steel armour' has been removed "
                        "from your possession\n")
            # if jan do not have them in her possession
            # she consider them as a gift item
            if "Glittering steel armour" not in jan_items:
                jan_items.append("Glittering steel armour")
                print_pause("\nNOTE: You relationship strengthened")
        else:
            print_pause("you do not have Glittering steel armour")
        jan_quest()
    # if player wants to gift beets and have them in his possession
    elif "beets" in jan_choice and "beets" in gift_items:
        print_pause("jan: I appreciate the intention but I am not "
                    "hungry")
        player_items = remove_item(player_items, "beets")
        gift_items = remove_item(gift_items, "beets")
        print_pause("\nNOTE: 'beets' has been removed from your possession\n")
        jan_quest()
  
    # if player chooses to leave the Office
    elif "leave" in jan_choice:
        print_pause("You head back to the inner halls")
        inner_corporate()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter the correct gift....")
        jan_quest()


# A branch sequence to the multiple funstions
def prison():
    global phone
    global player_items
    global coins
    global time_zone
    global scranton_locations
    global corporate_locations
    global player_status
    print_pause("\nYou were caught by the gaurds")
    print_pause("The ceo is not tolrent of trespassers")
    print_pause("You were sent to prison!!!!!!!")
    print_pause("After 4 days of imprisonment, you started to lose hope")
    print_pause("Many time sensitive items in your inventory, "
                "like beets and flowers are dimished")
    # time is reset to night
    # gaurds are reset to not alerted as player is captured
    # player status is changed to wanted
    time_zone = "night"
    phone = "deactivated"
    player_status = "wanted"
    # any time sensitive items in player's possession will be removed
    player_items = remove_item(player_items, "beets")
    player_items = remove_item(player_items, "Flowers")
    player_items = remove_item(player_items, "Glowing Flowers")
    print_pause("\nOn 4th day night, jan herslf comes to save you from the shackles "
                "of imprisonment")
    print_pause("You were rescued and sneaked into the inner corporate")
    print_pause("You are on your own from here...")
    inner_corporate()


# A branch sequence to the multiple funstions
def secret_passage():
    global time_zone
    # player's choice
    print_pause("You are in the secret passage")
    print_pause("\nPick a location to travel undetected:")
    secret_passage_choice = input("1. Jan's Office"
                                  "\n2. Scranton"
                                  "\n3. Explore\n").lower()
    # if player chooses to enter Jan's Office during daytime
    if "jans office" in secret_passage_choice and time_zone == "day":
        print_pause("\nYou head towards the jans office in the corporate")
        print_pause("\nNOTE: You might expose the secret passage in"
                    " broad-day-light")
        print_pause("\nDo you want to risk it ?")
        passage_to_jans_office_choice = input("1. Yes"
                                         "\n2. No\n").lower()
        # if player wants to risk it
        if "yes" in passage_to_jans_office_choice:
            print_pause("\nYou have entered the jans office during the day time")
            print_pause("The gaurds caught you and sent you to prison!!!!!!!")
            prison()
        # if player does not want to risk it
        else:
            print_pause("You have decided to use another route \nto avoid risk"
                        " exposing the secret path")
            secret_passage()
    # if player chooses to enter jans office during night time
    elif "jans office" in secret_passage_choice and time_zone == "night":
        print_pause("\nYou entered jans office area through secret passage")
        print_pause("As it is dark, you are able to sneak past gaurds")
        print_pause("You then enter the inner halls of corporate")
        inner_corporate()
    # if player chooses to enter scranton during night time
    elif "scranton" in secret_passage_choice:
        print_pause("You head towards the scranton")
        scranton()
    # if player chooses to explore the passage
    elif "explore" in secret_passage_choice:
        print_pause("\nYou hear peculiar sounds coming from inside "
                    "the passage")
        print_pause("You decided to investigate the passage")
        print_pause("You went furthur deep into the passage")
        print_pause("You have stumbled upon an old door")
        print_pause("The lock resembles the 'private key' the jan"
                    " gave you")
        hologram()
    # condition to deal with unrecognized input
    else:
        print_pause("\nNOTE: Enter the correct choice of words\n")
        secret_passage()


# A branch sequence to the funstion 'secret_passage'
def hologram():
    global hologram_room_count
    # player's choice
    print_pause("\nWould you open the lock ?")
    hologram_choice = input("1. open"
                         "\n2. Head back\n").lower()
    # if players chooses to open the door
    if "open" in hologram_choice:
        hologram_room_count += 1
        # intro to be displayed only once
        if hologram_room_count == 1:
            print_pause("\nYou enter the old room while being on gaurd")
            print_pause("THe room is full of Jan's old stuff "
                        "\nwhich happen to be under the jans office")
            print_pause("You witness an old figure lurking behind your back")
            print_pause("You react by swinging your arm but to no avail")
            print_pause("The arm passes right through the thing doing no "
                        "harm")
            print_pause("The thing asks you to calm down and try to reason"
                        " with you")
            print_pause("It introduces itself as an hologram of creed and an victim to"
                        " ceo's true nature\n")
            print_pause("hologram: The ceo is not who the poeple think he is.. "
                        "!!")
            print_pause("hologram: I have been branded as hologram for trying to "
                        "expose the ceos true self !!")
            print_pause("hologram: He then locks me here to die")
            print_pause("hologram: I want you to take revenge for me")
            print_pause("hologram: The ceo is the moster in disguise")
            print_pause("hologram: You cannot kill him with normal weapons....")
            print_pause("hologram: I can help you defeat him")
            print_pause("hologram: Will you do it, agent ??")
            hologram_sequence()
        # if player enters the room more than once
        if hologram_room_count > 1:
            hologram_sequence()
    # if players chooses not to open the door and head back
    elif "back" in hologram_choice:
        print_pause("\nYou decided to come back later")
        print_pause("You head back to the secret passsage intersection")
        secret_passage()
    # condition to deal with unrecognized input
    else:
        print_pause("\nNOTE: Enter the correct words\n")
        hologram()


# A branch sequence to the funstion 'hologram'
def hologram_sequence():
    global player
    global tomb_password
    global ceos_status
    # if tomb password is already revealed by the hologram
    if tomb_password == "revealed":
        print_pause("\nhologram: What do you need agent?")
        print_pause("hologram: I'm afraid I can't help you execpt with the "
                    "tomb spell")
        print_pause("hologram: Do you want me to repeat the spell to you again"
                    " agent?")
        password_again = input("\n1. Yes"
                               "\n2. No\n").lower()
        # if player wants to hear the password again
        if "yes" in password_again:
            print_pause("\nhologram: Tomb Spell - joshirk ")
            print_pause("\nNOTE: Password is case sensitive!!!!")
            print_pause("\nYou travel back to the secret passage intersection")
            secret_passage()
        # if player does not need to hear the password again
        elif "no" in password_again:
            print_pause("You travel back to the secret passage intersection")
            secret_passage()
        # condition to deal with unrecognized input
        else:
            print_pause("\nhologram: I don't understand your words agent !!")
            hologram_sequence()
    # if tomb password is not revealed by the hologram yet
    print_pause("\nhologram: Will you help me expose the ceo ?")
    hologram_sequence_choice = input("1. Yes, I will"
                                  "\n2. My be later\n").lower()
    # if player choose to expose ceo's identity
    if "yes" in hologram_sequence_choice:
        print_pause("\n" + player + " : Yes, I will help you")
        print_pause("hologram: You have my gratitude agent")
        print_pause("hologram: He can only be harmed by the legendary sword - "
                    "Light Saber")
        print_pause("hologram: The sword has been sealed slong with the ceo "
                    "Robert Dunder's corpse")
        print_pause("hologram: It is located somewhere inside the jungle")
        print_pause("\nhologram: The spell to unbind the seal "
                    "is : " + "'joshirk'\n")
        print_pause("\nNOTE: You may enter old ceo Robert Dunder's Tomb now")
        print_pause("hologram: Also you might need a SHEILD to defend "
                    "against ceo's attacks")
        print_pause("hologram: I can't help you with the sheild though !!")
        print_pause("hologram: I plead you agent, bring peace to my "
                    "agonized soul")
        print_pause(player + " : I will, you may rest in peace now.\n")
        # tomb password and ceo's identity is revealed by the hologram
        tomb_password = "revealed"
        ceos_status = "revealed"
        print_pause("You head back to the secret passage intersection")
        secret_passage()
    # if player chooses not to expose ceo's identity
    elif "later" in hologram_sequence_choice:
        print_pause("\nYou were not sure of the choice")
        print_pause("You decide to come back later")
        print_pause("You head back to the secret passage intersection")
        secret_passage()
    # condition to deal with unrecognized input
    else:
        print_pause("\nhologram: I don't understand your words agent !!")
        hologram_sequence()


# A branch sequence to the funstion 'inner_corporate'
def challenge_ceo():
    # player's choice
    print_pause("\nWould you challenge the ceo to a battle ?")
    challenge = input("1. yes, challenge the ceo"
                      "\n2. No, not yet\n").lower()
    # if player chooses to fight the ceo
    if "yes" in challenge:
        print_pause("\nYou challenge the ceo to single combat")
        print_pause("The ceo did not hesitate to accept the challenge\n")
        fight_result = fight_sequence("ceo", 50, 70, 50)
        # if player wins
        if fight_result == "player wins":
            print_pause("The ceo is on his final breath")
            print_pause("You approach him with your sword drawn")
            ceos_fate_scenario()
    # if player chooses not to fight the ceo
    elif "no" in challenge:
        print_pause("\nYou were not ready yet")
        print_pause("You decided to wait for the right time")
        print_pause("You head back to the scranton")
        scranton()
    # condition to deal with unrecognized input
    else:
        print_pause("\nNOTE: Enter the correct words\n")
        challenge_ceo()


# A branch sequence to the funstion 'challenge_ceo'
def ceos_fate_scenario():
    global beast_list
    # player's choice
    print_pause("\nEnter the NUMBER of your choice :")
    ceos_fate = input("1. Kill the ceo and finish this!"
                       "\n2. Somethings not righ...spare his life!\n")
    # if player decides to kill the ceo
    if ceos_fate == "1":
        print_pause("\nYou deliver a powerful blow to the ceo ")
        print_pause("The ceo took the final blow with out any "
                    "resistance")
        print_pause("almost as if he wanted you to slay him!?!")
        print_pause("You have slain the ceo, but something feels unsettled"
                    " to you.")
        print_pause("You were branded as ceo's killer and abolished "
                    "from the scranton!!!")
        print_pause(".")
        print_pause(".")
        print_pause(".")
        print_pause(".")
        print_pause("After 4 months of the incident")
        print_pause("You were drinking in the bar in the neighbouring"
                    " town")
        print_pause("You enquire Bartender for the info as a daily"
                    " routine")
        print_pause("According to the information,")
        print_pause("Jan was kidnapped by the beast and "
                    "never returned !!")
        print_pause("As suspected, the beast was not the ceo !!")
        print_pause("There is something behind the scenes playing the ceo")
        print_pause("\nNOTE: Play the game again for different end "
                    "scenario")
        print_pause("Time to return to the scranton ....//\n")
        print_pause("--------------- GAME ENDED ------------------")
        credits()
    # if player decides not to kill the ceo
    elif ceos_fate == "2":
        print_pause("\nYou take a leap of faith, to spare the ceo's life")
        print_pause("You gave the ceo a chance to explain his actions")
        print_pause("The ceo is in no condition to talk to you,")
        print_pause("He appears to be be possessed")
        print_pause("\nYou sense a dark presence lurking in the shadows !!")
        print_pause("It appears to be the beast, manipulating the ceo all"
                    " along")
        print_pause("The ceo is nothing but a puppet,\n a victim to beast's"
                    " vicious nature")
        print_pause("You leap towards the beast at full throttle")
        print_pause("The beast was caught off gaurd and wounded badly")
        # beast will be revealed as a random from a list of characters
        beast_trueform = random.choice(beast_list)
        print_pause("\nThe beast ACTUALLY is the " + beast_trueform + ", "
                    "\ndisguised as a human !!!\n")
        print_pause("The beast is both wounded and tired")
        print_pause("This is the perfect chance to end this...\n")
        fight_result = fight_sequence("beast", 40, 60, 40)
        if fight_result == "player wins":
            print_pause("The beast is finally slain!!!!!!!!")
            print_pause("You rescued Dunder Mifflin and Scranton from the "
                        "beast's evil plan")
            print_pause("You were rewarded with coins and you go to your home in Colorado with a triumph!\n")
            print_pause("------------------ THE END -------------------")
            credits()
    # condition to deal with unrecognized input
    else:
        print_pause("\nEnter the NUMBER of your choice to decide ceo's fate: ")
        ceos_fate_scenario()


# function to be displayed if player successfully complete the game
def credits():
    global player
    print_pause("\n\n         //  Congratulations you finished the game  //")
    print_pause("___________________ CREDITS ____________________")
    print_pause("\nThis game was developed by and\nsole property of "
                "// 'Ritika Joshi' //\n")
    print_pause("Cast and Crew:")
    print_pause("Protagonist - " + player)
    print_pause("Jan         - Herself")
    print_pause("ceo         - was manipulated by beast!")
    print_pause("Shopkeeper  - Himself")
    print_pause("Jim         - Anonymous")
    print_pause("Guard       - special appearance")
    print_pause("Kevin       - Himself")
    print_pause("Beast       - Killed")
    print_pause("\n\n")
    print_pause("Thank you for playing the game!!")
    exit()


# ------------ Game Trigger ------------
adventure_game()
