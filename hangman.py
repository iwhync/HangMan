import random
from time import sleep
import winsound

def hangman():
    
    print("Welcome to Brutal Hangman By Richard. Good Luck.")


    
    game = True
    while game == True:
        incorrect = 7
        guess = []
        fail = []
        words = ('abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon',
         'banjo', 'bayou', 'beekeeper', 'bikini',
         'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing',
          'buzzwords',
         'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex',
          'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack',
           'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled',
          'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph',
           'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory',
            'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey',
             'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki',
              'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury',
               'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub',
                'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm',
                 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue',
                  'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw',
                   'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength',
                    'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless',
                     'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth',
                      'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo',
                       'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey',
                        'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 
                        'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging',
                         'zilch', 'zipper', 'zodiac', 'zombie', 'abecedarian', 'abracadabra', 'accoutrements', 'adagio',
                          'aficionado', 'agita', 'agog', 'akimbo', 'alfresco', 'aloof', 'ambrosial', 'amok', 'ampersand',
                           'anemone', 'anthropomorphic', 'antimacassar', 'aplomb', 'apogee', 'apoplectic', 'appaloosa',
                            'apparatus', 'archipelago', 'atingle', 'avuncular', 'azure', 'babushka', 'bailiwick', 'bafflegab',
                             'balderdash', 'ballistic', 'bamboozle', 'bandwagon', 'barnstorming', 'beanpole', 'bedlam',
                              'befuddled', 'bellwether', 'berserk', 'bibliopole', 'bigmouth', 'bippy', 'blabbermouth',
                               'blatherskite', 'blindside', 'blob', 'blockhead', 'blowback', 'blowhard', 'blubbering',
                                'bluestockings', 'boing', 'boffo', '(boffola)', 'bombastic', 'bonanza', 'bonkers',
                                 'boondocks', 'boondoggle', 'borborygmus', 'bozo', 'braggadocio', 'brainstorm',
                                  'brannigan', 'breakneck', 'brouhaha', 'buckaroo', 'bucolic', 'buffoon', 'bugaboo',
                                   'bugbear', 'bulbous', 'bumbledom', 'bumfuzzle', 'bumptious', 'bumpkin', 'bungalow',
                                    'bunkum', 'bupkis', 'burnsides', 'busybody', 'cacophony', 'cahoots', 'calamity',
                                     'calliope', 'candelabra', 'canoodle', 'cantankerous', 'catamaran', 'catastrophe',
                                      'catawampus', 'caterwaul', 'chatterbox', 'chichi', 'chimerical', 'chimichanga',
                                       'chitchat', 'clandestine', 'claptrap', 'clishmaclaver', 'clodhopper', 'cockamamie',
                                        'cockatoo', 'codswallop', 'collywobbles', 'colossus', 'comeuppance', 'concoction',
                                         'conniption', 'contraband', 'conundrum', 'convivial', 'copacetic', 'corkscrew',
                                          'cornucopia', 'cowabunga', 'coxcomb', 'crackerjack', 'crescendo', 'crestfallen',
                                           'cryptozoology', 'cuckoo', 'curlicue', 'curmudgeon', 'demitasse', 'denouement',
                                            'derecho', 'desperado', 'diaphanous', 'diddlysquat', 'digeridoo', 'dilemma',
                                             'dillydally', 'dimwit', 'diphthong', 'dirigible', 'discombobulated', 'dodecahedron',
                                             'doldrums', 'donkeyman', 'donnybrook', 'doodad', 'doohickey', 'doppelganger',
                                              'dumbfounded', 'dumbwaiter', 'dunderhead', 'earwig', 'eavesdrop', 'ebullient',
                                               'effervescence', 'egads', 'eggcorn', 'egghead', 'elixir', 'ephemeral', 'epiphany',
                                                'ersatz', 'eucatastrophe', 'extraterrestrial', 'finagle', 'fandango', 'festooned',
                                                 'fez', 'fiasco', 'fiddlefooted', 'fiddlesticks', 'finicky', 'firebrand',
                                                  'fishwife', 'fisticuffs', 'flabbergasted', 'flapdoodle', 'flibbertigibbet',
                                                   'flimflam', 'flippant', 'floccinaucinihilipilification', 'flophouse', 'flotsam',
                                                    'flummery', 'flummoxed', 'flyaway', 'flyspeck', 'folderol', 'foofaraw',
                                                     'foolhardy', 'foolscap', 'footloose', 'fopdoodle', 'fortuitous', 'fracas', 'frangipani',
                                                      'freewheeling', 'fricassee', 'frippery', 'frogman', 'froufrou', 'fuddyduddy', 'fussbudget',
                                                       'futz', 'gadfly', 'gadzooks', 'gallimaufry', 'gambit', 'gangplank', 'gangway', 'gargoyle', 'gasbag',
                                                        'gazebo', 'gazpacho', 'gewgaw', 'genteel', 'ghostwriter', 'gibberish', 'gimcrack', 'gizmo', 'glabella', 'glitch',
                                                         'globetrotter', 'gobbledygook', 'gobsmacked', 'goosebump', 'gooseflesh', 'gorgonzola', 'gossamer', 'grandiloquent',
                                                          'greenhorn', 'guffaw', 'gumshoe', 'guru', 'gussied', 'guttersnipe', 'haberdashery', 'haboob', 'hairpin', 'halcyon',
                                                           'halfwit', 'hangdog', 'haphazard', 'harebrained', 'harumph', 'harumscarum', 'headlong', 'heartstrings', 'heebiejeebie',
                                                            'heirloom', 'helterskelter', 'hemidemisemiquaver', 'heyday', 'higgledypiggledy', 'highfalutin', 'hijinks', 'hillbilly',
                                                             'hippocampus', 'hippogriff', 'hobbledehoy', 'hobnobbed', 'hocuspocus', 'hodgepodge', 'hogwash', 'hokum', 'hoodoo',
                                                              'hoodwink', 'hooey', 'hooligan', 'hoopla', 'hootenanny', 'hornswoggle', 'horsefeathers', 'hotbed', 'hotfoot',
                                                               'hothead', 'hubbub', 'hullabaloo', 'humbug', 'humdinger', 'humdrum', 'hunkydory', 'hurlyburly', 'hushpuppy', 'huzzah',
                                                                'hyperbole', 'idiom', 'idiosyncrasies', 'igloo', 'ignoramus', 'impromptu', 'incognito', 'incorrigible', 'incredulous',
                                                                'indomitable', 'indubitably', 'infinitesimal', 'interloper', 'interrobang', 'ironclad', 'izzard', 'jabberwocky',
                                                                 'jacuzzi', 'jalopy', 'jamboree', 'jargogle', 'jawbreaker', 'jetsam', 'jibberjabber', 'jink', 'jitney', 'jubilee',
                                                                  'juggernaut', 'jujubes', 'jumbo', 'junket', 'juxtaposition', 'kaleidoscope', 'kaput', 'kerfuffle', 'kerplunk',
                                                                   'kibosh', 'killjoy', 'kismet', 'knickerbocker', 'knickknack', 'kowtow', 'kumquat', 'kvetch', 'lackadaisical',
                                                                    'lagoon', 'lambasted', 'lampoon', 'landlubber', 'laughingstock', 'lexicographer', 'limburger', 'lingo', 'loco',
                                                                     'loggerhead', 'logjam', 'logophile', 'logorrhea', 'lollapalooza', 'lollygag', 'loofah', 'loony', 'loophole',
                                                                      'lugubrious', 'lummox', 'machinations', 'madcap', 'maelstrom', 'magnificent', 'majordomo', 'malapropism',
                                                                       'malarkey', 'manifesto', 'mastermind', 'mayhem', 'mealymouthed', 'mellifluous', 'menagerie', 'miasma',
                                                                        'miffed', 'milquetoast', 'misanthrope', 'mishmash', 'moocher', 'mojo', 'mollycoddle', 'mondegreen', 'moniker',
                                                                         'monkeyshines', 'monsoon', 'mnemonic', 'moonstruck', 'mucketymuck', 'mudpuppy', 'mudslinger', 'muffuletta',
                                                                          'mufti', 'mulligatawny', 'mumbojumbo', 'murmuration', 'muumuu', 'nabob', 'nambypamby', 'nimrod', 'nincompoop',
                                                                          'nitwit', 'nomenclature', 'nonplussed', 'noodge', 'nudnik', 'numbskull', 'onomatopoeia', 'oomph', 'orotund',
                                                                           'outfox', 'outlandish', 'oxymoron', 'pachyderm', 'pagoda', 'palindrome', 'palomino', 'panache', 'pandemonium',
                                                                            'pantaloons', 'papyrus', 'parabola', 'parallelogram', 'parapet', 'paraphernalia', 'peccadillo', 'pedagogue',
                                                                             'peewee', 'pellmell', 'persimmon', 'persnickety', 'pettifogger', 'phalanx', 'phantasmagorical', 'phantonym',
                                                                              'phylactery', 'piffle', 'pizzazz', 'plethora', 'pogo', 'pogonip', 'pollex', 'pollywog', 'poltroon',
                                                                               'pomposity', 'poppycock', 'portmanteau', 'potpourri', 'pseudonym', 'pugnacious', 'pulchritudinous',
                                                                                'pusillanimous', 'pussyfoot', 'quibble', 'quicksilver', 'quicksticks', 'quiddle', 'quinzee', 'quirky',
                                                                                 'quixotic', 'quizzity', 'rabblerouser', 'raconteur', 'rainmaker', 'ragamuffin', 'ragtag', 'ramshackle',
                                                                                  'ransack', 'rapscallion', 'razzledazzle', 'razzmatazz', 'rejigger', 'rendezvous', 'resplendent',
                                                                                   'rickrack', 'ricochet', 'riffraff', 'rigmarole', 'riposte', 'roundabout', 'roustabout', 'rubberneck',
                                                                                    'ruckus', 'ruffian', 'rugrat', 'rumpus', 'sabayon', 'sashay', 'sassafras', 'scallywag', 'scatterbrain',
                                                                                     'schadenfreude', 'schlep', 'schluffy', 'schmooze', 'schmutz', 'scintillating', 'scrofulous',
                                                                                      'scrumdiddlyumptious', 'scuttlebutt', 'serendipity', 'sesquipedalian', 'shabang', 'shenanigans',
                                                                                       'skedaddle', 'skirmish', 'skullduggery', 'slapdash', 'slapstick', 'slipshod', 'smithereens',
                                                                                        'smorgasbord', 'snollygoster', 'sobriquet', 'sojourn', 'spellbind', 'splendiferous', 'squeegee',
                                                                                         'squooshy', 'staccato', 'stupefaction', 'succotash', 'supercilious', 'superfluous', 'surreptitious',
                                                                                          'Svengali', 'swashbuckler', 'switcheroo', 'swizzlestick', 'synchronicity', 'syzygy', 'talisman',
                                                                                           'taradiddle', 'tchotchke', 'teepee', 'telekinesis', 'thingamabob', 'thingamajig', 'thunderstruck',
                                                                                            'tidbit', 'tintinnabulation', 'toadstool', 'toady', 'tomfoolery', 'tommyrot', 'toothsome',
                                                                                             'topsyturvy', 'trapezoid', 'tubthumper', 'tumultuous', 'typhoon', 'ululation', 'umlaut',
                                                                                              'umpteen', 'usurp', 'uvula', 'vagabond', 'vamoose', 'verboten', 'verisimilitude', 'vermicious',
                                                                                               'vertigo', 'verve', 'virtuoso', 'vivacious', 'vuvuzela', 'wackadoodle', 'wallflower',
                                                                                                'wanderlust', 'whatchamacallit', 'whatsis', 'whimsical', 'whippersnapper', 'whirligig',
                                                                                                 'whirlybird', 'whizbang', 'whodunit', 'whoop', 'widget', 'wigwam', 'willynilly', 'windbag',
                                                                                                  'wipeout', 'wiseacre', 'wisecrack', 'wisenheimer', 'wishywashy', 'woebegone', 'wonky',
                                                                                                   'woozy', 'wordplay', 'wordsmith', 'wunderkind', 'wuthering', 'xylophone', 'yahoo', 'yokel',
                                                                                                   'yoyo', 'zaftig', 'zeitgeist', 'zenzizenzizenzic', 'zephyr', 'zeppelin', 'ziggurat',
                                                                                                    'zigzag', 'zonked', 'zoom', 'zydeco')

        b = random.randint(0,800)
        word = words[b]
        word = word.lower()
        x = len(word)
        print(f"Word is {x} letters long.")
        y = len(word) - 1
        blanks = "-"*x
        print(blanks)
        print("\n")
        sortset = ""

        worde = sorted(word)
        wordset = set(worde)

        while incorrect > 0:


            if incorrect == 7:

                print(" _________ ")

            if incorrect == 6:

                print("|")
                print("|")
                print("|")
                print("|_________ ")

            if incorrect == 5:


                print("__")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|_________ ")

            if incorrect == 4:


                print("________  ")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|_________ ")    

            if incorrect == 3:


                print("________  ")
                print("|       | ")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|_________ ")

            if incorrect == 2:


                print("________  ")
                print("|       | ")
                print("|       o ")
                print("|")
                print("|")
                print("|")
                print("|_________ ")  

            if incorrect == 1:


                print("________  ")
                print("|       | ")
                print("|       o ")
                print("|      /|\ ")
                print("|")
                print("|")
                print("|_________ ")      

            p = input("Guess a letter: ")
            p = p.lower()

            while len(p) > 1:

                p = input("No cheating!! Guess **ONE** letter!: ")

            while p in guess:

                p = input("Already tried letter. Try again: ")
                p = p.lower()

            while p in fail:

                p = input("Already tried letter. Try again: ")
                p = p.lower()
        
            print("\n"*100)

            if p in word:
                winsound.Beep(700, 100)

                guess.append(p)
                sorte = sorted(guess)
                sortset = set(sorte)

                for i in range(x):
                    if word[i] in guess: 
                        blanks = blanks[:i] + word[i] + blanks[i+1:]

            print("\n")
            print(blanks)

            if p not in word:
                    
                winsound.Beep(400, 200)

                incorrect = incorrect - 1
                print(f"{p} Not in word.\n")
                print("Tries left",incorrect)
                fail.append(p)
                print("Letters guessed incorrectly: ",fail)
                print("\n")


            if incorrect == 0:


                print("________  ")
                print("|       | ")
                print("|       o ")
                print("|      /|\ ")
                print("|      / \ ")
                print("|          ")
                print("|_________ ")
                print("\n")
                print(f"Word was: {word}")
                print("You LOSE.")
                winsound.Beep(400, 300)
                winsound.Beep(300, 400)
                winsound.Beep(200, 800)
                
                try:
                    x = input("Play Again? y or n: ")
                    x = x.lower()
                    x = x[0]
                    if x == "y":
                        game = True
                    else:
                        game = False
                except:
                    game = False

            if sortset == wordset:
                print("\n")
                print("WINNER!!!")

                winsound.Beep(400, 600)
                winsound.Beep(500, 600)
                winsound.Beep(600, 50)
                winsound.Beep(700, 50)
                winsound.Beep(800, 300)
                winsound.Beep(600, 400)

                try:
                    x = input("Play Again? y or n: ")
                    x = x.lower()
                    x = x[0]
                    if x == "y":
                        break
                        game = True
                    else:
                        game = False
                        break
                except:
                    game = False


hangman()
