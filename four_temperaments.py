from random import randint

words = {
    'Animated': [1, 1, 'Sanguine', 'strength'],
    'Adventurous': [2, 1, 'Choleric', 'strength'],
    'Analytical': [3, 1, 'Melancholy', 'strength'],
    'Adaptable': [4, 1, 'Phlegmatic', 'strength'],
    'Playful': [5, 2, 'Sanguine', 'strength'],
    'Persuasive': [6, 2, 'Choleric', 'strength'],
    'Persistent': [7, 2, 'Melancholy', 'strength'],
    'Peaceful': [8, 2, 'Phlegmatic', 'strength'],
    'Sociable': [9, 3, 'Sanguine', 'strength'],
    'Strong-willed': [10, 3, 'Choleric', 'strength'],
    'Self-sacrificing': [11, 3, 'Melancholy', 'strength'],
    'Submissive': [12, 3, 'Phlegmatic', 'strength'],
    'Convincing': [13, 4, 'Sanguine', 'strength'],
    'Competitive': [14, 4, 'Choleric', 'strength'],
    'Considerate': [15, 4, 'Melancholy', 'strength'],
    'Controlled': [16, 4, 'Phlegmatic', 'strength'],
    'Refreshing': [17, 5, 'Sanguine', 'strength'],
    'Resourceful': [18, 5, 'Choleric', 'strength'],
    'Respectful': [19, 5, 'Melancholy', 'strength'],
    'Reserved': [20, 5, 'Phlegmatic', 'strength'],
    'Spirited': [21, 6, 'Sanguine', 'strength'],
    'Self-reliant': [22, 6, 'Choleric', 'strength'],
    'Sensitive': [23, 6, 'Melancholy', 'strength'],
    'Satisfied': [24, 6, 'Phlegmatic', 'strength'],
    'Promoter': [25, 7, 'Sanguine', 'strength'],
    'Positive': [26, 7, 'Choleric', 'strength'],
    'Planner': [27, 7, 'Melancholy', 'strength'],
    'Patient': [28, 7, 'Phlegmatic', 'strength'],
    'Optimistic': [29, 8, 'Sanguine', 'strength'],
    'Outspoken': [30, 8, 'Choleric', 'strength'],
    'Orderly': [31, 8, 'Melancholy', 'strength'],
    'Obliging': [32, 8, 'Phlegmatic', 'strength'],
    'Spontaneous': [33, 9, 'Sanguine', 'strength'],
    'Sure': [34, 9, 'Choleric', 'strength'],
    'Scheduled': [35, 9, 'Melancholy', 'strength'],
    'Shy': [36, 9, 'Phlegmatic', 'strength'],
    'Funny': [37, 10, 'Sanguine', 'strength'],
    'Forceful': [38, 10, 'Choleric', 'strength'],
    'Faithful': [39, 10, 'Melancholy', 'strength'],
    'Friendly': [40, 10, 'Phlegmatic', 'strength'],
    'Delightful': [41, 11, 'Sanguine', 'strength'],
    'Daring': [42, 11, 'Choleric', 'strength'],
    'Detailed': [43, 11, 'Melancholy', 'strength'],
    'Diplomatic': [44, 11, 'Phlegmatic', 'strength'],
    'Cheerful': [45, 12, 'Sanguine', 'strength'],
    'Confident': [46, 12, 'Choleric', 'strength'],
    'Cultured': [47, 12, 'Melancholy', 'strength'],
    'Consistent': [48, 12, 'Phlegmatic', 'strength'],
    'Inspiring': [49, 13, 'Sanguine', 'strength'],
    'Independent': [50, 13, 'Choleric', 'strength'],
    'Idealist': [51, 13, 'Melancholy', 'strength'],
    'Inoffensive': [52, 13, 'Phlegmatic', 'strength'],
    'Demonstrative': [53, 14, 'Sanguine', 'strength'],
    'Decisive': [54, 14, 'Choleric', 'strength'],
    'Deep': [55, 14, 'Melancholy', 'strength'],
    'Dry humour': [56, 14, 'Phlegmatic', 'strength'],
    'Mixes easily': [57, 15, 'Sanguine', 'strength'],
    'Mover': [58, 15, 'Choleric', 'strength'],
    'Musical': [59, 15, 'Melancholy', 'strength'],
    'Mediator': [60, 15, 'Phlegmatic', 'strength'],
    'Talker': [61, 16, 'Sanguine', 'strength'],
    'Tenacious': [62, 16, 'Choleric', 'strength'],
    'Thoughtful': [63, 16, 'Melancholy', 'strength'],
    'Tolerant': [64, 16, 'Phlegmatic', 'strength'],
    'Lively': [65, 17, 'Sanguine', 'strength'],
    'Leader': [66, 17, 'Choleric', 'strength'],
    'Loyal': [67, 17, 'Melancholy', 'strength'],
    'Listener': [68, 17, 'Phlegmatic', 'strength'],
    'Cute': [69, 18, 'Sanguine', 'strength'],
    'Chief': [70, 18, 'Choleric', 'strength'],
    'Chart-maker': [71, 18, 'Melancholy', 'strength'],
    'Contented': [72, 18, 'Phlegmatic', 'strength'],
    'Popular': [73, 19, 'Sanguine', 'strength'],
    'Productive': [74, 19, 'Choleric', 'strength'],
    'Perfectionist': [75, 19, 'Melancholy', 'strength'],
    'Pleaser': [76, 19, 'Phlegmatic', 'strength'],
    'Bouncy': [77, 20, 'Sanguine', 'strength'],
    'Bold': [78, 20, 'Choleric', 'strength'],
    'Behaved': [79, 20, 'Melancholy', 'strength'],
    'Balanced': [80, 20, 'Phlegmatic', 'strength'],
    'Brassy': [81, 21, 'Sanguine', 'weakness'],
    'Bossy': [82, 21, 'Choleric', 'weakness'],
    'Bashful': [83, 21, 'Melancholy', 'weakness'],
    'Blank': [84, 21, 'Phlegmatic', 'weakness'],
    'Undisciplined': [85, 22, 'Sanguine', 'weakness'],
    'Unsympathetic': [86, 22, 'Choleric', 'weakness'],
    'Unforgiving': [87, 22, 'Melancholy', 'weakness'],
    'Unenthusiastic': [88, 22, 'Phlegmatic', 'weakness'],
    'Repetitious': [89, 23, 'Sanguine', 'weakness'],
    'Resistant': [90, 23, 'Choleric', 'weakness'],
    'Resentful': [91, 23, 'Melancholy', 'weakness'],
    'Reticent': [92, 23, 'Phlegmatic', 'weakness'],
    'Forgetful': [93, 24, 'Sanguine', 'weakness'],
    'Frank': [94, 24, 'Choleric', 'weakness'],
    'Fussy': [95, 24, 'Melancholy', 'weakness'],
    'Fearful': [96, 24, 'Phlegmatic', 'weakness'],
    'Interrupts': [97, 25, 'Sanguine', 'weakness'],
    'Impatient': [98, 25, 'Choleric', 'weakness'],
    'Insecure': [99, 25, 'Melancholy', 'weakness'],
    'Indecisive': [100, 25, 'Phlegmatic', 'weakness'],
    'Unpredictable': [101, 26, 'Sanguine', 'weakness'],
    'Unaffectionate': [102, 26, 'Choleric', 'weakness'],
    'Unpopular': [103, 26, 'Melancholy', 'weakness'],
    'Uninvolved': [104, 26, 'Phlegmatic', 'weakness'],
    'Haphazard': [105, 27, 'Sanguine', 'weakness'],
    'Headstrong': [106, 27, 'Choleric', 'weakness'],
    'Hard to please': [107, 27, 'Melancholy', 'weakness'],
    'Hesitant': [108, 27, 'Phlegmatic', 'weakness'],
    'Permissive': [109, 28, 'Sanguine', 'weakness'],
    'Proud': [110, 28, 'Choleric', 'weakness'],
    'Pessimistic': [111, 28, 'Melancholy', 'weakness'],
    'Plain': [112, 28, 'Phlegmatic', 'weakness'],
    'Angered easily': [113, 29, 'Sanguine', 'weakness'],
    'Argumentative': [114, 29, 'Choleric', 'weakness'],
    'Alienated': [115, 29, 'Melancholy', 'weakness'],
    'Aimless': [116, 29, 'Phlegmatic', 'weakness'],
    'Naive': [117, 30, 'Sanguine', 'weakness'],
    'Nervy': [118, 30, 'Choleric', 'weakness'],
    'Negative attitude': [119, 30, 'Melancholy', 'weakness'],
    'Nonchalant': [120, 30, 'Phlegmatic', 'weakness'],
    'Wants credit': [121, 31, 'Sanguine', 'weakness'],
    'Workaholic': [122, 31, 'Choleric', 'weakness'],
    'Withdrawn': [123, 31, 'Melancholy', 'weakness'],
    'Worrier': [124, 31, 'Phlegmatic', 'weakness'],
    'Talkative': [125, 32, 'Sanguine', 'weakness'],
    'Tactless': [126, 32, 'Choleric', 'weakness'],
    'Too sensitive': [127, 32, 'Melancholy', 'weakness'],
    'Timid': [128, 32, 'Phlegmatic', 'weakness'],
    'Disorganised': [129, 33, 'Sanguine', 'weakness'],
    'Domineering': [130, 33, 'Choleric', 'weakness'],
    'Depressed': [131, 33, 'Melancholy', 'weakness'],
    'Doubtful': [132, 33, 'Phlegmatic', 'weakness'],
    'Inconsistent': [133, 34, 'Sanguine', 'weakness'],
    'Intolerant': [134, 34, 'Choleric', 'weakness'],
    'Introvert': [135, 34, 'Melancholy', 'weakness'],
    'Indifferent': [136, 34, 'Phlegmatic', 'weakness'],
    'Messy': [137, 35, 'Sanguine', 'weakness'],
    'Manipulative': [138, 35, 'Choleric', 'weakness'],
    'Moody': [139, 35, 'Melancholy', 'weakness'],
    'Mumbles': [140, 35, 'Phlegmatic', 'weakness'],
    'Show-off': [141, 36, 'Sanguine', 'weakness'],
    'Stubborn': [142, 36, 'Choleric', 'weakness'],
    'Skeptical': [143, 36, 'Melancholy', 'weakness'],
    'Slow': [144, 36, 'Phlegmatic', 'weakness'],
    'Loud': [145, 37, 'Sanguine', 'weakness'],
    'Lord over others': [146, 37, 'Choleric', 'weakness'],
    'Loner': [147, 37, 'Melancholy', 'weakness'],
    'Lazy': [148, 37, 'Phlegmatic', 'weakness'],
    'Scatterbrained': [149, 38, 'Sanguine', 'weakness'],
    'Short-tempered': [150, 38, 'Choleric', 'weakness'],
    'Suspicious': [151, 38, 'Melancholy', 'weakness'],
    'Sluggish': [152, 38, 'Phlegmatic', 'weakness'],
    'Restless': [153, 39, 'Sanguine', 'weakness'],
    'Rash': [154, 39, 'Choleric', 'weakness'],
    'Revengeful': [155, 39, 'Melancholy', 'weakness'],
    'Reluctant': [156, 39, 'Phlegmatic', 'weakness'],
    'Changeable': [157, 40, 'Sanguine', 'weakness'],
    'Crafty': [158, 40, 'Choleric', 'weakness'],
    'Critical': [159, 40, 'Melancholy', 'weakness'],
    'Compromising': [160, 40, 'Phlegmatic', 'weakness']
}

temperaments = {
    'Sanguine': [
        {
            'emotions': [
                'appealing personality',
                'storyteller',
                'life of the party',
                'good sense of humour',
                'memory for colour',
                'physically holds on to listener',
                'emotional and demonstrative',
                'enthusiastic and expressive',
                'cheerful and bubbly',
                'curious',
                'good on stage',
                'wide-eyed and innocent',
                'lives in the present',
                'changeable disposition',
                'sincere at heart',
                'always a child'
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
                'talk too much',
                'self-centered',
                'uncultivated memories',
                'disorganised'
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
            'to get along with this': [
                'recognise their difficulty in accomplishing tasks',
                'realise they may talk without thinking first',
                'realise they like variety and flexibility',
                'help them to keep from accepting more than they can do',
                'priase them for everything they accomplish',
                'remember they are circumstantial people',
                'realise that they mean well'
            ]
        }
    ],
    'Melancholy': [
        {
            'emotions': [
                'deep and thoughtful',
                'analytical',
                'serious and purposeful',
                'genius prone',
                'talented and creative',
                'artistic or musical',
                'philosophical and poetic',
                'appreciative of beauty',
                'sensitive of others',
                'self-sacrificing',
                'conscientious',
                'idealistic'
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
                'easily depressed',
                'procastinate',
                'put unrealistic demands on others'
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
                'don\'t be hurt easily',
                'look for the positives',
                'blow away the black clouds',
                'don\'t spend too much time planning',
                'relax your standards'
            ]
        },
        {
            'to get along with this': [
                'know thay they are very sensitive and get hurt easily',
                'realise they are programmed with pessimistic attitude',
                'learn to deal with depression',
                'compliment them sincerely',
                'accept that they like it quiet sometimes',
                'try to keep a reasonable schedule',
                'realise that neatness is a necessity',
                'help them not to become slaves to the family'
            ]
        }
    ],
    'Choleric': [
        {
            'emotions': [
                'born leader',
                'dynamic and active',
                'compulsive need for change',
                'must correct wrongs',
                'strong willed and decisive',
                'unemotional',
                'not easily discouraged',
                'independent and self-sufficient',
                'exudes confidence',
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
                'compulsive worker',
                'must be in control',
                'don\'t know how to handle people',
                'right but unpopular'
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
            'to get along with this': [
                'recognise they are born leaders',
                'insist on two-way communication',
                'know they don\'t mean to hurt',
                'try to divide areas of responsibility',
                'realise they are not compassionate'
            ]
        }
    ],
    'Phlegmatic': [
        {
            'emotions': [
                'low-key personality',
                'easygoing and relaxed',
                'calm and cool',
                'patient',
                'consistent life',
                'quiet but witty',
                'sympathetic and kind',
                'keeps emotions hidden',
                'happily reconciled to life',
                'all-purpose person'
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
                'doesn\'t care about doing anything',
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
            'how to get along with': [
                'realise they need direct motivation',
                'help them set goals and make rewards',
                'don\'t expect enthusiasm',
                'realise that putting things off is their form of quiet control',
                'force them to make decisions',
                'don\'t heap all the blame on them',
                'encourage them to accept responsibilities'
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
    descriptions = temperaments[temperament][8]['how to get along with']
    description_id = randint(0, len(descriptions)-1)
    return descriptions[description_id]