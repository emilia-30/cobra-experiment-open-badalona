PRIME_TYPES = {
    "BEEP": "BEEP",
    "PREDICTABLE_SENTENCE": "predictable sentence",
    "UNPREDICTABLE_SENTENCE": "unpredictable sentence",
}

# so there are 36 images
# there are 72 audio files
# and 108 trials per session

# any given trial is one image and one audio file or beep - for each session an image is shown 3 times so a unique key
# needs to be the sentence type concat with the stim image key eg. p_hammer, u_corbeau.
# p_hammer will map to p_hammer.wav and hammer.jpeg and be saved as an audio file and db trial key p_hammer


STIMS = [
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
