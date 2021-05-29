# any given trial is one image and one audio file or beep - for each session an image is shown 3 times so a unique key
# is the prime type and the stim image key eg. p_hammer, (predictable hammer) u_corbeau (unpredictable corbeau).
# p_hammer will look up p_hammer.wav and hammer.jpeg and the trial will be saved as an audio file and db trial entry with key p_hammer


PRACTICE_STIMS = [
    {
        "stim": 'agrafeuse',
        "prime": 'predictable'
    },
    {
        "stim": 'balai',
        "prime": 'unpredictable'
    }
    #   ...
]

STIM_KEYS = [
    'agrafeuse',
    'aiguille',
    'balai',
    'cadenas',
    'ciseaux',
    'compas',
    'couteau',
    'echelle',
    'hache',
    'marteau',
    'metre',
    'pelle',
    'perceuse',
    'pinceau',
    'rateau',
    'regle',
    'rouleau',
    'tondeuse',
    'ane',
    'antilope',
    'autruche',
    'cameleon',
    'corbeau',
    'elephant',
    'escargot',
    'guepe',
    'herisson',
    'hibou',
    'lezard',
    'moustique',
    'pingouin',
    'renard',
    'sanglier',
    'sauterelle',
    'vache',
    'zebre'
]
