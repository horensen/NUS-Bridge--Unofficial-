from random import randint

words = {
    'Animated': [1, 1, 'Sanguine', 'strength'], #OK
    'Adventurous': [2, 1, 'Choleric', 'strength'], #OK
    'Analytical': [3, 1, 'Melancholic', 'strength'], #OK
    'Adaptable': [4, 1, 'Phlegmatic', 'strength'], #OK
    'Playful': [5, 2, 'Sanguine', 'strength'], #OK
    'Persuasive': [6, 2, 'Choleric', 'strength'], #OK
    'Persistent': [7, 2, 'Melancholic', 'strength'], #OK
    'Peaceful': [8, 2, 'Phlegmatic', 'strength'], #OK
    'Sociable': [9, 3, 'Sanguine', 'strength'], #OK
    'Strong-willed': [10, 3, 'Choleric', 'strength'], #OK
    'Self-sacrificing': [11, 3, 'Melancholic', 'strength'], #OK
    'Submissive': [12, 3, 'Phlegmatic', 'strength'], #OK
    'Convincing': [13, 4, 'Sanguine', 'strength'], #OK
    'Competitive': [14, 4, 'Choleric', 'strength'], #OK
    'Considerate': [15, 4, 'Melancholic', 'strength'], #OK
    'Controlled': [16, 4, 'Phlegmatic', 'strength'], #OK
    'Refreshing': [17, 5, 'Sanguine', 'strength'], #OK
    'Resourceful': [18, 5, 'Choleric', 'strength'], #OK
    'Respectful': [19, 5, 'Melancholic', 'strength'], #OK
    'Reserved': [20, 5, 'Phlegmatic', 'strength'], #OK
    'Spirited': [21, 6, 'Sanguine', 'strength'], # OK
    'Self-reliant': [22, 6, 'Choleric', 'strength'], #OK
    'Sensitive': [23, 6, 'Melancholic', 'strength'], #OK
    'Satisfied': [24, 6, 'Phlegmatic', 'strength'], #OK
    'Promoter': [25, 7, 'Sanguine', 'strength'], #OK
    'Positive': [26, 7, 'Choleric', 'strength'], #OK
    'Planner': [27, 7, 'Melancholic', 'strength'], #OK
    'Patient': [28, 7, 'Phlegmatic', 'strength'], #OK
    'Optimistic': [29, 8, 'Sanguine', 'strength'], #OK
    'Outspoken': [30, 8, 'Choleric', 'strength'], #OK
    'Orderly': [31, 8, 'Melancholic', 'strength'], #OK
    'Obliging': [32, 8, 'Phlegmatic', 'strength'], #OK
    'Spontaneous': [33, 9, 'Sanguine', 'strength'], #OK
    'Sure': [34, 9, 'Choleric', 'strength'], #OK
    'Scheduled': [35, 9, 'Melancholic', 'strength'], #OK
    'Shy': [36, 9, 'Phlegmatic', 'strength'], #OK
    'Funny': [37, 10, 'Sanguine', 'strength'], #OK
    'Forceful': [38, 10, 'Choleric', 'strength'], #OK
    'Faithful': [39, 10, 'Melancholic', 'strength'], #OK
    'Friendly': [40, 10, 'Phlegmatic', 'strength'], #OK
    'Delightful': [41, 11, 'Sanguine', 'strength'], #OK
    'Daring': [42, 11, 'Choleric', 'strength'], #OK
    'Detailed': [43, 11, 'Melancholic', 'strength'], #OK
    'Diplomatic': [44, 11, 'Phlegmatic', 'strength'], #OK
    'Cheerful': [45, 12, 'Sanguine', 'strength'], #OK
    'Confident': [46, 12, 'Choleric', 'strength'], #OK
    'Cultured': [47, 12, 'Melancholic', 'strength'], #OK
    'Consistent': [48, 12, 'Phlegmatic', 'strength'], #OK
    'Inspiring': [49, 13, 'Sanguine', 'strength'], #OK
    'Independent': [50, 13, 'Choleric', 'strength'], #OK
    'Idealist': [51, 13, 'Melancholic', 'strength'], #OK
    'Inoffensive': [52, 13, 'Phlegmatic', 'strength'], #OK
    'Demonstrative': [53, 14, 'Sanguine', 'strength'], #OK
    'Decisive': [54, 14, 'Choleric', 'strength'], #OK
    'Deep': [55, 14, 'Melancholic', 'strength'], #OK
    'Dry humour': [56, 14, 'Phlegmatic', 'strength'], #OK
    'Mixes easily': [57, 15, 'Sanguine', 'strength'], #OK
    'Mover': [58, 15, 'Choleric', 'strength'], #OK
    'Musical': [59, 15, 'Melancholic', 'strength'], #OK
    'Mediator': [60, 15, 'Phlegmatic', 'strength'], #OK
    'Talker': [61, 16, 'Sanguine', 'strength'], #OK
    'Tenacious': [62, 16, 'Choleric', 'strength'], #OK
    'Thoughtful': [63, 16, 'Melancholic', 'strength'], #OK
    'Tolerant': [64, 16, 'Phlegmatic', 'strength'], #OK
    'Lively': [65, 17, 'Sanguine', 'strength'], #OK
    'Leader': [66, 17, 'Choleric', 'strength'], #OK
    'Loyal': [67, 17, 'Melancholic', 'strength'], #OK
    'Listener': [68, 17, 'Phlegmatic', 'strength'], #OK
    'Cute': [69, 18, 'Sanguine', 'strength'], #OK
    'Chief': [70, 18, 'Choleric', 'strength'], #OK
    'Chart-maker': [71, 18, 'Melancholic', 'strength'], #OK
    'Contented': [72, 18, 'Phlegmatic', 'strength'], #OK
    'Popular': [73, 19, 'Sanguine', 'strength'], #OK
    'Productive': [74, 19, 'Choleric', 'strength'], #OK
    'Perfectionist': [75, 19, 'Melancholic', 'strength'], #OK
    'Pleaser': [76, 19, 'Phlegmatic', 'strength'], #OK
    'Bouncy': [77, 20, 'Sanguine', 'strength'], #OK
    'Bold': [78, 20, 'Choleric', 'strength'], #OK
    'Behaved': [79, 20, 'Melancholic', 'strength'], #OK
    'Balanced': [80, 20, 'Phlegmatic', 'strength'], #OK
    'Brassy': [81, 21, 'Sanguine', 'weakness'], #OK
    'Bossy': [82, 21, 'Choleric', 'weakness'], #OK
    'Bashful': [83, 21, 'Melancholic', 'weakness'], #OK
    'Blank': [84, 21, 'Phlegmatic', 'weakness'], #OK
    'Undisciplined': [85, 22, 'Sanguine', 'weakness'], #OK
    'Unsympathetic': [86, 22, 'Choleric', 'weakness'], #OK
    'Unforgiving': [87, 22, 'Melancholic', 'weakness'], #OK
    'Unenthusiastic': [88, 22, 'Phlegmatic', 'weakness'], #OK
    'Repetitious': [89, 23, 'Sanguine', 'weakness'], #OK
    'Resistant': [90, 23, 'Choleric', 'weakness'], #OK
    'Resentful': [91, 23, 'Melancholic', 'weakness'], #OK
    'Reticent': [92, 23, 'Phlegmatic', 'weakness'], #OK
    'Forgetful': [93, 24, 'Sanguine', 'weakness'], #OK
    'Frank': [94, 24, 'Choleric', 'weakness'], #OK
    'Fussy': [95, 24, 'Melancholic', 'weakness'], #OK
    'Fearful': [96, 24, 'Phlegmatic', 'weakness'], #OK
    'Interrupts': [97, 25, 'Sanguine', 'weakness'], #OK
    'Impatient': [98, 25, 'Choleric', 'weakness'], #OK
    'Insecure': [99, 25, 'Melancholic', 'weakness'], #OK
    'Indecisive': [100, 25, 'Phlegmatic', 'weakness'], #OK
    'Unpredictable': [101, 26, 'Sanguine', 'weakness'], #OK
    'Unaffectionate': [102, 26, 'Choleric', 'weakness'], #OK
    'Unpopular': [103, 26, 'Melancholic', 'weakness'], #OK
    'Uninvolved': [104, 26, 'Phlegmatic', 'weakness'], #OK
    'Haphazard': [105, 27, 'Sanguine', 'weakness'], #OK
    'Headstrong': [106, 27, 'Choleric', 'weakness'], #OK
    'Hard to please': [107, 27, 'Melancholic', 'weakness'], #OK
    'Hesitant': [108, 27, 'Phlegmatic', 'weakness'], #OK
    'Permissive': [109, 28, 'Sanguine', 'weakness'], #OK
    'Proud': [110, 28, 'Choleric', 'weakness'], #OK
    'Pessimistic': [111, 28, 'Melancholic', 'weakness'], #OK
    'Plain': [112, 28, 'Phlegmatic', 'weakness'], #OK
    'Angered easily': [113, 29, 'Sanguine', 'weakness'], #OK
    'Argumentative': [114, 29, 'Choleric', 'weakness'], #OK
    'Alienated': [115, 29, 'Melancholic', 'weakness'], #OK
    'Aimless': [116, 29, 'Phlegmatic', 'weakness'], #OK
    'Naive': [117, 30, 'Sanguine', 'weakness'], #OK
    'Nervy': [118, 30, 'Choleric', 'weakness'], #OK
    'Negative attitude': [119, 30, 'Melancholic', 'weakness'], #OK
    'Nonchalant': [120, 30, 'Phlegmatic', 'weakness'], #OK
    'Wants credit': [121, 31, 'Sanguine', 'weakness'], #OK
    'Workaholic': [122, 31, 'Choleric', 'weakness'], #OK
    'Withdrawn': [123, 31, 'Melancholic', 'weakness'], #OK
    'Worrier': [124, 31, 'Phlegmatic', 'weakness'], #OK
    'Talkative': [125, 32, 'Sanguine', 'weakness'], #OK
    'Tactless': [126, 32, 'Choleric', 'weakness'], #OK
    'Too sensitive': [127, 32, 'Melancholic', 'weakness'], #OK
    'Timid': [128, 32, 'Phlegmatic', 'weakness'], #OK
    'Disorganised': [129, 33, 'Sanguine', 'weakness'], #OK
    'Domineering': [130, 33, 'Choleric', 'weakness'], #OK
    'Depressed': [131, 33, 'Melancholic', 'weakness'], #OK
    'Doubtful': [132, 33, 'Phlegmatic', 'weakness'], #OK
    'Inconsistent': [133, 34, 'Sanguine', 'weakness'], #OK
    'Intolerant': [134, 34, 'Choleric', 'weakness'], #OK
    'Introvert': [135, 34, 'Melancholic', 'weakness'], #OK
    'Indifferent': [136, 34, 'Phlegmatic', 'weakness'], #OK
    'Messy': [137, 35, 'Sanguine', 'weakness'], #OK
    'Manipulative': [138, 35, 'Choleric', 'weakness'], #OK
    'Moody': [139, 35, 'Melancholic', 'weakness'], #OK
    'Mumbles': [140, 35, 'Phlegmatic', 'weakness'], #OK
    'Show-off': [141, 36, 'Sanguine', 'weakness'], #OK
    'Stubborn': [142, 36, 'Choleric', 'weakness'], #OK
    'Skeptical': [143, 36, 'Melancholic', 'weakness'], #OK
    'Slow': [144, 36, 'Phlegmatic', 'weakness'], #OK
    'Loud': [145, 37, 'Sanguine', 'weakness'], #OK
    'Lord over others': [146, 37, 'Choleric', 'weakness'], #OK
    'Loner': [147, 37, 'Melancholic', 'weakness'], #OK
    'Lazy': [148, 37, 'Phlegmatic', 'weakness'], #OK
    'Scatterbrained': [149, 38, 'Sanguine', 'weakness'], #OK
    'Short-tempered': [150, 38, 'Choleric', 'weakness'], #OK
    'Suspicious': [151, 38, 'Melancholic', 'weakness'], #OK
    'Sluggish': [152, 38, 'Phlegmatic', 'weakness'], #OK
    'Restless': [153, 39, 'Sanguine', 'weakness'], #OK
    'Rash': [154, 39, 'Choleric', 'weakness'], #OK
    'Revengeful': [155, 39, 'Melancholic', 'weakness'], #OK
    'Reluctant': [156, 39, 'Phlegmatic', 'weakness'], #OK
    'Changeable': [157, 40, 'Sanguine', 'weakness'], #OK
    'Crafty': [158, 40, 'Choleric', 'weakness'], #OK
    'Critical': [159, 40, 'Melancholic', 'weakness'], #OK
    'Compromising': [160, 40, 'Phlegmatic', 'weakness'] #OK
}

temperaments = {
    'Sanguine': [
        {
            'emotions': [
                'have an appealing personality',
                'are a storyteller',
                'are the life of the party',
                'have a good sense of humour',
                'have memory for colour',
                'physically hold on to listener',
                'are emotional and demonstrative',
                'are enthusiastic and expressive',
                'are cheerful and bubbly',
                'are curious',
                'are good on stage',
                'are wide-eyed and innocent',
                'live in the present',
                'have a changeable disposition',
                'are sincere at heart',
                'are always a child'
            ]
        },
        {
            'at work': [
                'volunteer for jobs',
                'can think up new activities',
                'look great on the surface',
                'are creative and colourful',
                'have energy and enthusiasm',
                'can start in a flashy way',
                'can inspire others to join',
                'can charm others to work'
            ]
        },
        {
            'as a friend': [
                'make friends easily',
                'love people',
                'can thrive on compliments',
                'are exciting',
                'envied by others',
                'don\'t hold grudges',
                'apologise quickly',
                'prevent dull moments',
                'like spontaneous activities'
            ]
        },
        {
            'best in': [
                'dealing with people enthusiastically',
                'expressing thoughts with excitement',
                'up-front positions of attention'
            ]
        },
        {
            'needs to be': [
                'organised'
            ]
        },
        {
            'flaws': [
                'may talk too much',
                'are self-centered',
                'have uncultivated memories',
                'are disorganised'
            ]
        },
        {
            'positives carried to extremes': [
                'constantly talking',
                'monopolising',
                'interrupting and straying too far from the truth'
            ]
        },
        {
            'improvements': [
                'talk half as much as before',
                'watch for signs of boredom',
                'condense your comments',
                'stop exaggerating',
                'be sensitive to other people\'s interest',
                'learn to listen',
                'put others\' need first',
                'pay attention to names',
                'write things down'
            ]
        },
        {
            'how to get along with this': [
                'recognise your difficulty in accomplishing tasks',
                'realise that may have a tendancy to talk without thinking first',
                'realise that you like variety and flexibility',
                'need help to keep yourself from accepting more than what you can do',
                'you would appreciate praises for everything you accomplish',
                'know that you are a circumstantial person',
                'realise that you mean well'
            ]
        }
    ],
    'Melancholic': [
        {
            'emotions': [
                'are deep and thoughtful',
                'are analytical',
                'are serious and purposeful',
                'are genius prone',
                'are talented and creative',
                'are artistic or musical',
                'are philosophical and poetic',
                'are appreciative of beauty',
                'are sensitive of others',
                'are self-sacrificing',
                'are conscientious',
                'are idealistic'
            ]
        },
        {
            'at work': [
                'are schedule oriented',
                'are perfectionist; high standards',
                'are detail conscious',
                'are persistent and thorough',
                'are orderly and organised',
                'are neat and tidy',
                'are economical',
                'can see the problems',
                'can find creative solutions',
                'finish what is started',
                'like charts, graphics, figures and lists'
            ]
        },
        {
            'as a friend': [
                'make friends cautiously',
                'are content to stay in background',
                'avoid causing attention',
                'are faithful and devoted',
                'will listen to complains',
                'can solve others\' problems',
                'have deep concern for other people',
                'can be moved to tears with compassion',
                'usually seek an ideal mate'
            ]
        },
        {
            'best in': [
                'attending to details and deep thinking',
                'keeping records, charts and graphs',
                'analysing problems too difficult for others'
            ]
        },
        {
            'needs to be': [
                'cheered up'
            ]
        },
        {
            'flaws': [
                'are easily depressed',
                'may procastinate',
                'may put unrealistic demands on others'
            ]
        },
        {
            'positives carried to extremes': [
                'brooding',
                'depressed'
            ]
        },
        {
            'improvements': [
                'realise no one likes gloomy people',
                'not to be hurt easily',
                'look for the positives',
                'not to spend too much time planning',
                'relax your standards'
            ]
        },
        {
            'how to get along with this': [
                'know thay you are very sensitive and may get hurt easily',
                'realise that you are programmed with a pessimistic attitude',
                'allow you space to deal with probable depression',
                'know that you appreciate sincere compliments',
                'acceot accept that you like it quiet sometimes',
                'try to keep you in a reasonable schedule',
                'realise that neatness is a necessity for you'
            ]
        }
    ],
    'Choleric': [
        {
            'emotions': [
                'are a born leader',
                'are dynamic and active',
                'have compulsive need for change',
                'must correct wrongs',
                'are strong-willed and decisive',
                'are unemotional',
                'are not easily discouraged',
                'areindependent and self-sufficient',
                'exude confidence',
                'can run anything'
            ]
        },
        {
            'at work': [
                'are goal oriented',
                'can see the whole picture',
                'can organise well',
                'seek practical solutions',
                'can move quickly to action',
                'can delegate work',
                'insist on production',
                'can make the goal',
                'stimulate activity',
                'thrive on opposition'
            ]
        },
        {
            'as a friend': [
                'have little need for friends',
                'will work for group activitiy',
                'will lead and organise',
                'are usually right',
                'excel in emergencies'
            ]
        },
        {
            'best in': [
                'jobs that require quick decisions',
                'spots that need instant action and accomplishment',
                'areas that demand strong control and authority'
            ]
        },
        {
            'needs to be': [
                'toned down'
            ]
        },
        {
            'flaws': [
                'are a compulsive worker',
                'must be in control',
                'may not know how to handle people',
                'are right but unpopular'
            ]
        },
        {
            'positives carried to extremes': [
                'bossy',
                'controlling',
                'manipulative'
            ]
        },
        {
            'improvements': [
                'learn to relax',
                'take pressure off others',
                'plan leisure activities',
                'respond to other leadership',
                'don\'t look down on \'the dummies\'',
                'stop manipulating',
                'practice patience',
                'keep advice until asked',
                'tone down your approach',
                'stop arguing and causing trouble',
                'let someone else be right',
                'learn to apologise',
                'admit you have some faults'
            ]
        },
        {
            'how to get along with this': [
                'recognise that you are a born leader',
                'insist on two-way communication with you',
                'know that you don\'t mean to hurt',
                'try to divide areas of responsibility with you',
                'realise that you are not compassionate'
            ]
        }
    ],
    'Phlegmatic': [
        {
            'emotions': [
                'have a low-key personality',
                'are easygoing and relaxed',
                'are calm and cool',
                'are patient',
                'have a consistent life',
                'are quiet but witty',
                'are sympathetic and kind',
                'keep emotions hidden',
                'are happily reconciled to life',
                'are an all-purpose person'
            ]
        },
        {
            'at work': [
                'are competent and steady',
                'are peaceful and agreeable',
                'have administrative ability',
                'can mediate problems',
                'avoid conflicts',
                'are good under pressure',
                'find the easy way'
            ]
        },
        {
            'as a friend': [
                'are easy to get along with',
                'are pleasant and enjoyable',
                'are inoffensive',
                'are a good listener',
                'have a dry sense of humour',
                'enjoy watching people',
                'have many friends',
                'have compassion and concern'
            ]
        },
        {
            'best in': [
                'position of mediation and unity',
                'storms that need a calming hand',
                'routines that might seem dull to others'
            ]
        },
        {
            'needs to be': [
                'motivated'
            ]
        },
        {
            'flaws': [
                'are not exciting',
                'resist change',
                'seem lazy',
                'appear wishy-washy'
            ]
        },
        {
            'positives carried to extremes': [
                'not caring about doing anything',
                'indifferent',
                'indecisive'
            ]
        },
        {
            'improvements': [
                'try to get enthused',
                'learn to communicate your feelings',
                'try something new',
                'learn to accept responsibility for your life',
                'don\'t put off until tomorrow what you can do today',
                'motivate yourself',
                'practice making decision'
            ]
        },
        {
            'how to get along with this': [
                'realise that you need direct motivation',
                'know that you need to help to set goals',
                'not expect enthusiasm from you',
                'realise that putting things off is your form of quiet control',
                'understand that you need to be encouraged to make decisions',
                'not heap all the blame on you',
                'understand that you need to be encouraged to accept responsibilities'
            ]
        }
    ]
}

def get_word_id(word):
    return words[word][0]

def get_question_set_id(word):
    return words[word][1]

def get_temperament(word):
    return words[word][2]

def get_strength_or_weakness(word):
    return words[word][3]

def get_random_emotion(temperament):
    descriptions = temperaments[temperament][0]['emotions']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_at_work(temperament):
    descriptions = temperaments[temperament][1]['at work']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_as_a_friend(temperament):
    descriptions = temperaments[temperament][2]['as a friend']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_best_in(temperament):
    descriptions = temperaments[temperament][3]['best in']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_needs_to_be(temperament):
    descriptions = temperaments[temperament][4]['needs to be']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_flaw(temperament):
    descriptions = temperaments[temperament][5]['flaws']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_extreme(temperament):
    descriptions = temperaments[temperament][6]['positives carried to extremes']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_improvement(temperament):
    descriptions = temperaments[temperament][7]['improvements']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]

def get_random_how_to_get_along_with(temperament):
    descriptions = temperaments[temperament][8]['how to get along with this']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]