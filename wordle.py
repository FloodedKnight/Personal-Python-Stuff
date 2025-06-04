import random

# Words list are chatgptd

words_1 = (
    "Abide", "Adept", "Adore", "Agent", "Alibi",
    "Alive", "Alpha", "Amend", "Angel", "Angle",
    "Ankle", "Anvil", "Apple", "Apron", "Arena",
    "Arrow", "Ashen", "Asset", "Audio", "Avenge",
    "Avoid", "Award", "Bacon", "Badge", "Bagel",
    "Baker", "Balmy", "Banjo", "Barge", "Basin",
    "Batch", "Beach", "Beast", "Beech", "Bento",
    "Berry", "Bingo", "Bison", "Black", "Blast",
    "Blaze", "Bless", "Bliss", "Block", "Blond",
    "Bloom", "Blush", "Bongo", "Bonus", "Booth",
    "Braid", "Brain", "Bravo", "Bread", "Briar",
    "Bride", "Brief", "Brisk", "Bulge", "Bunny",
    "Burge", "Burst", "Cabin", "Cable", "Cacao",
    "Cameo", "Candy", "Canoe", "Carve", "Cedar",
    "Cello", "Chalk", "Champ", "Chant", "Charm",
    "Chase", "Cheek", "Chess", "Cider", "Cigar",
    "Citro", "Claim", "Clash", "Climb", "Clove",
    "Cloud", "Coach", "Cobra", "Comet", "Comic",
    "Craft", "Crane", "Crate", "Creek", "Crews",
    "Crisp", "Crown", "Cupid", "Curvy", "Cycle",
    "Dance", "Dandy", "Dealt", "Debit", "Debut",
    "Delta", "Dense", "Depth", "Derby", "Diary",
    "Dicey", "Dingo", "Dizzy", "Dozen", "Draft",
    "Drama", "Dream", "Drift", "Drink", "Drive",
    "Drone", "Drool", "Druid", "Dumpy", "Dwarf",
    "Eager", "Eagle", "Early", "Earth", "Elbow",
    "Elect", "Elude", "Ember", "Empty", "Enact",
    "Ended", "Enrol", "Entry", "Error", "Etude",
    "Event", "Evict", "Evil", "Excel", "Exile",
    "Exist", "Exude", "Fable", "Faint", "Fairy",
    "False", "Fame", "Fancy", "Fares", "Fatal",
    "Favor", "Fazed", "Feast", "Fever", "Fiber",
    "Field", "Fifth", "Fight", "Final", "Finch",
    "Fixed", "Flair", "Flame", "Flask", "Fleet",
    "Flint", "Flirt", "Float", "Flock", "Flood",
    "Floor", "Flora", "Flour", "Fluid", "Fluke",
    "Flush", "Flyer", "Foamy", "Force", "Forge",
    "Forum", "Fours", "Frame", "Fresh", "Fried",
    "Front", "Frost", "Frown", "Fruit", "Funny",
    "Fuzzy", "Gains", "Gamer", "Gamma", "Gangs",
    "Gavel", "Gears", "Gecko", "Gents", "Ghost",
    "Giant", "Gifts", "Given", "Giver", "Glade",
    "Glass", "Gleam", "Glory", "Gloss", "Glyph",
    "Gnarl", "Gnome", "Going", "Gooey", "Goose",
    "Gorse", "Gotta", "Grabs", "Grace", "Grain",
    "Grand", "Grant", "Graph", "Grass", "Gravy",
    "Great", "Green", "Grind", "Groom", "Grope",
    "Group", "Grove", "Grown", "Gumbo", "Gusto",
    "Gypsy", "Habit", "Happy", "Hardy", "Harsh",
    "Haste", "Hatch", "Haven", "Hazel", "Heals",
    "Heart", "Heave", "Heavy", "Heirs", "Helix",
    "Hello", "Helps", "Hence", "Henry", "Hertz",
    "Hiker", "Hitch", "Hoist", "Holds", "Honor",
    "Hooks", "Hopes", "Horny", "Horse", "Hotel",
    "House", "Hunts", "Hurry", "Hydra", "Hyena",
    "Ideal", "Image", "Inert", "Inked", "Inlay",
    "Inlet", "Inner", "Input", "Irish", "Irony",
    "Ivory", "Jacks", "Jaded", "Jelly", "Jewel",
    "Joker", "Judge", "Juicy", "Jumbo", "Jumps",
    "Junky", "Junky", "Karst", "Karma", "Kicks",
    "Kicks", "Kills", "Kinds", "Kinky", "Knack",
    "Kneel", "Knife", "Knock", "Knoll", "Known",
    "Lands", "Lanky", "Laser", "Lasso", "Later",
    "Lazzy", "Learn", "Legal", "Lemma", "Lemma",
    "Lemon", "Lemon", "Level", "Light", "Liked",
    "Likes", "Lilly", "Lilly", "Limbo", "Limit",
    "Linen", "Lined", "Lines", "Lingy", "Links",
    "Lives", "Lives", "Lodge", "Logic", "Loner",
    "Loner", "Longs", "Looks", "Loose", "Lorry",
    "Lousy", "Lucky", "Lumps", "Lunar", "Lurks",
    "Lying", "Lyric", "Macho", "Mains", "Maker",
    "Males", "Manly", "Mango", "Maple", "March",
    "Mares", "Marks", "Marsh", "Match", "Matte",
    "Maven", "Meant", "Medal", "Meets", "Mends",
    "Merry", "Messy", "Metal", "Meter", "Metre",
    "Micky", "Miles", "Milky", "Minds", "Mirth",
)

words_2 = (
    "Acorn", "Ample", "Arrow", "Avail", "Azure",
    "Badge", "Bliss", "Bloom", "Brave", "Candy",
    "Charm", "Clear", "Cloud", "Coast", "Coral",
    "Crisp", "Daisy", "Dance", "Dazzle", "Dewey",
    "Eager", "Earth", "Evoke", "Fable", "Fancy",
    "Favor", "Feast", "Fever", "Flick", "Giddy",
    "Glory", "Grain", "Gusto", "Hazel", "Honor",
    "Hushy", "Ideal", "Ivory", "Jolly", "Jumbo",
    "Kindl", "Kitty", "Lavvy", "Lucky", "Lunar",
    "Lushy", "Merry", "Misty", "Nifty", "Noble",
    "Nymph", "Oasis", "Ocean", "Olive", "Petal",
    "Pixel", "Plush", "Poise", "Prime", "Proud",
    "Quain", "Quest", "Quick", "Radia", "Rainy",
    "Rebel", "Regal", "Rhyme", "Riple", "Rosie",
    "Sandy", "Sassy", "Serena", "Silky", "Sizzl",
    "Solar", "Spira", "Splen", "Starr", "Sunna",
    "Tende", "Thril", "Trank", "Treas", "Tropi",
    "Unity", "Urban", "Velvy", "Vinta", "Vivid",
    "Whims", "Wilde", "Windy", "Zestyy",
)

words_3 = ("Forge", "Frost", "Grace", "Grain", "Grove",
    "Heart", "Honor", "Humor", "Icing", "Ivory",
    "Jewel", "Joint", "Judge", "Knife", "Knock",
    "Lemon", "Lodge", "Logic", "Mocha", "Mural",
    "Noble", "Novel", "Nymph", "Oasis", "Olive",
    "Opera", "Paint", "Peace", "Petal", "Plaza",
    "Queen", "Quilt", "Quiet", "Radar", "Radio",
    "Raven", "Rifle", "Roast", "Royal", "Sable",
    "Satin", "Shade", "Shape", "Silky", "Snail",
    "Spark", "Spice", "Spire", "Spray", "Stall",
    "Stead", "Storm", "Style", "Sugar", "Sunset",
    "Table", "Taffy", "Tango", "Tease", "Tiger",
    "Trace", "Trail", "Train", "Tribe", "Twist",
    "Unity", "Urban", "Usher", "Valve", "Venus",
    "Vista", "Vivid", "Voice", "Wagon", "Whirl",
    "Widow", "Witch", "Woman", "Woven", "Xerox",
    "Yacht", "Yield", "Yogic", "Young", "Zebra",
)

TheWord = random.choice(words_1+words_2+words_3).upper()

attempts = 0
valid_letters = "abcdefghijklmnopqrstuvwxyz".upper()

while True:
    flag = False
    PlayersGuess = input("Guess the 5-letter word: ").upper()

    for char in PlayersGuess:
        if (char in valid_letters) == False:
            print("You're using invalid letters! Try again.")
            flag = True
            break
    if PlayersGuess == TheWord:
        print("Congrats! You guessed the word " + TheWord.title() + " correctly!")
        break

    elif attempts >= 4.9:
        print("You ran out of tries D: The word was " + TheWord.title() + "...")    
        break
    elif len(PlayersGuess) != 5:
        print("You can only guess 5 letter words!")

    elif flag == False:
        attempts += 1
        print("")
        for i in range(5):

            if PlayersGuess[i] == TheWord[i]:
                print("🟩 ", end="")

            elif PlayersGuess[i] in [char for char in TheWord]:
                print("🟨 ", end="")

            elif PlayersGuess[i] != TheWord[i]:
                print("🟥 ", end="")

        
        print(PlayersGuess)
