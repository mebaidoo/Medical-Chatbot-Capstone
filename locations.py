import pandas as pd

hosp = [{'name': 'S.D.A Hospital', 'area': 'Takoradi-Liberation Road', 'map_location': 'https://goo.gl/maps/GdjRdK9NZAMnFKsu9'},
          {'name': 'Takoradi Hospital', 'area': 'Takoradi-Beach Road', 'map_location': 'https://goo.gl/maps/61nyzdziyopQ3pUHA'},
          {'name': 'Effia Nkwanta Hospital', 'area': 'Sekondi-Takoradi Road', 'map_location': 'https://goo.gl/maps/ybD16FZmVjUuicY59'},
          {'name': 'Kwesimintsim Hospital', 'area': 'Kwesimintsim', 'map_location': 'https://goo.gl/maps/fLrQujJPdvAs3gC37'},
          {'name': 'Grace Spring Mission Hospital', 'area': 'Effia', 'map_location': 'https://goo.gl/maps/EFCWUF8QEh25em1b8'},
          {'name': 'Takoradi Family Health Specialist Hospital', 'area': 'Anaji Hills', 'map_location': 'https://goo.gl/maps/iJMwim4Hjjrg9yXZ8'},
          {'name': 'Jemima Crentsil Hospital', 'area': 'Takoradi-Akufo-Addo Road', 'map_location': 'https://goo.gl/maps/wZ4psDry7s2LyJrbA'},
          {'name': 'G.P.H.A Clinic', 'area': 'Takoradi-J. De Graft-Johnson Ave', 'map_location': 'https://goo.gl/maps/yhVQpEDs1TJ67V5F9'},
          {'name': 'End Point Homeopathic Clinic', 'area': 'Anaji-Queen of Peace inside', 'map_location': 'https://goo.gl/maps/azBX9RwSCPtnLwY87'},
          {'name': 'Bethel Methodist Medical Hospital', 'area': 'Takoradi-Pakos Ave', 'map_location': 'https://goo.gl/maps/uchfKzf8tpE7NmreA'}
          ]
          
pharm = [{'name': 'Kendicks Pharmacy', 'area': 'Takoradi-Market Circle', 'map_location': 'https://goo.gl/maps/QnYTcyA5DDhwsfFB7'},
        {'name': 'Day By Day Pharmacy', 'area': 'Takoradi-Kitson Ave', 'map_location': 'https://goo.gl/maps/efJATHoFERBJhLot6'},
        {'name': 'Medrugs Pharmacy', 'area': 'Takoradi-Liberation Road', 'map_location': 'https://goo.gl/maps/dZGunVo2RJLxmZcr7'},
        {'name': 'Abuakwa Pharmacy', 'area': 'Takoradi-Market Circle', 'map_location': 'https://goo.gl/maps/95HHL7abYtTmzB7r7'},
        {'name': 'A.A.A. Mens Pharmacy', 'area': 'Takoradi-Market Circle', 'map_location': 'https://goo.gl/maps/whwKAMus8gMrWYgR7'},
        {'name': 'Akan Chemist', 'area': 'Takoradi-Pakos Ave', 'map_location': 'https://goo.gl/maps/fmGrLxZBaBA3wja2A'},
        {'name': 'Eff-Ess Pharmacy', 'area': 'Takoradi-Liberation Rd', 'map_location': 'https://goo.gl/maps/c7hfVnAbMsSHXiWv8'}]

lab = [{'name': 'Mediwest Laboratory', 'area': 'Sawmill', 'map_location': 'https://goo.gl/maps/gWUDJYf3EH3TeiZn7'},
        {'name': 'Solar Medical Laboratory', 'area': 'New Takoradi', 'map_location': 'https://goo.gl/maps/WRppCWCoaj6uX4ra9'},
        {'name': 'Oasis Medical Laboratory', 'area': 'Fijai', 'map_location': 'https://goo.gl/maps/ouqNthQFFTM42nZF8'},
        {'name': 'Blue Waves Diagnostic Laboratory', 'area': 'Anaji', 'map_location': 'https://goo.gl/maps/27vXp5rT4ktVajUg9'},
        {'name': 'Diascan Laboratory', 'area': 'Assakae Road', 'map_location': 'https://goo.gl/maps/mhkyFT9t1XRDuyGw5'}]

hospitals = pd.DataFrame(hosp)
pharmacies = pd.DataFrame(pharm)
labs = pd.DataFrame(lab)

map = hospitals.map_location[hospitals['name'] == 'Takoradi Hospital']
print(map[1])