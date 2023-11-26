# Replay should be raw replay binary data
def parse(replay):
  
  # Placeholder data until the replay parser is written.
  data = {
    'hash'    : '1073e6378bf02fb1fae3ed1c60db6054',
    'name'    : 'ba 6v6 rmk',
    'map'     : 'Broken Alliances 7.0f.w3x',
    'size'    : 3438133,
    'length'  : 4009,
    'host'    : 'Anders#1366',
    'players' : [
      {
        'name': 'Anders#1366',
        'color': 'Red',
        'leftAt': 3978,
        'stayPercent': 99.23,
        'isWinner': True,
        'isSolo': True,
        'team': 1,
        'rating': 2810,
        'rank': 'Grand Master',
        'bases': [
          'Tishlak',
          'Vak Voh',
          'Dark Spire'
        ],
        'hero': 'Kel\'Thurax',
        'units': [
          'Tishlak:Assassin',
          'Tishlak:Headhunter',
          'Shamania:Fel Orc Warlock'
        ],
        'perks': [
          'Taxer',
          'Forger',
          'Teleporter',
          'Pillager'
        ],
        'dragons': [
          'Blue',
          'Red'
        ]
      },
      {
        'name': 'HappyFeet#19992',
        'color': 'Brown',
        'leftAt': 3968,
        'stayPercent': 98.21,
        'isWinner': False,
        'isSolo': True,
        'team': 2,
        'rating': 1990,
        'rank': 'Diamond IV',
        'bases': [
          'Gapbreak',
          'Icelock',
          'Balkar'
        ],
        'hero': 'Kel\'Thurax',
        'units': [
          'Icelock:Wendigo',
          'Icelock:Wendigo',
          'Icelock:Priest',
          'Icelock:Ranger',
        ],
        'perks': [
          'Warrior',
          'Looter',
          'Slavemaster',
          'Teleporter'
        ],
        'dragons': [
          'Yellow'
        ]
      }
    ]
  }

  return data
