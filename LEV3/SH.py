import csv

print("Welcome to the Sports Heros project")
print('We are going to do some analysis on Wimbledon and French Open Men\'s singles champions')
print('Please see the file analysis.dat for the results')


def print_line(report_line):
  filename = 'analysis.dat'
  
  with open(filename, mode ='a') as file:
    file.write(report_line)

def print_table(table):
  # Pass in a list of dictionaries and print it. 
  
  filename = 'analysis.dat'

  with open(filename, mode ='a') as file:
    all_keys = list(table[0].keys())

    keys_line = ''
    for key in all_keys:
      keys_line = keys_line + key + (20 - len(key))*' '
      
    file.write(keys_line + '\n')

    for data in table:
      # Each data is a dictionary, we print the values.
      values_line = ''
      for values in data.values():
        values_line = values_line + str(values) + (20-len(str(values)))*' '

      file.write(values_line + '\n')



def initialize():
  filename = 'analysis.dat'

  with open(filename, mode ='w') as file:
    file.write('Analysis Results \n')


def print_set(winner_set):
  # Pass in a set and print its members one on each line. 
  filename = 'analysis.dat'

  with open(filename, mode ='a') as file:
    for winner in winner_set:
       file.write(winner + ' , ')
    file.write('\n\n')



def readcsvdata(tournament_name):
  filename = tournament_name + '.csv'
  # Open the file
  # Read the data into a list of dictionaries
  with open(filename, mode ='r') as file:
    csvFile = csv.DictReader(file)
    tournament_data = list(csvFile)

  return tournament_data

  
  


def analyze(tname, tdata):
  # Create a list of winners
  winners_list = []
  
  for winner in tdata:
    winners_list.append(winner['Champion'])

  # Find out the unique winners (Since one player may have won the tournament more than once)
  # Easiest method -- Convert to a set
  winners_set = set(winners_list)

  print_line('Reporting for ' + tname + '\n' )
  print_line('Total Winners : ' + str(len(winners_list)) + '\n')
  print_line('Unique Winners : ' + str(len(winners_set)) + '\n')

  winners_info_list = []  
  for player in winners_set:
    # Look through the list to find all items where the Champion is the particular player
    # (SAME problem statement as we had in the laptop store)
    # Use list comprehension to do this. 
    player_info = {}
    selected = [chosen for chosen in tdata if chosen['Champion'] == player]
    # Update the dictionary
    player_info['Name'] = player
    player_info['Country'] = selected[0]['Country']
    player_info['Times Won'] = len(selected)
    player_info['Years Won'] = []
    for kk in selected:
      player_info['Years Won'].append(kk['Year'])

    winners_info_list.append(player_info)

  print_table(winners_info_list)


  # Create a subset
  # winners_set contains all the names that have won the tournament. 
  #
  # mto_winners will have those players who have won More than once.

  # The set of players who have won more than once
  mto_winners_set = set()

  for player in winners_set:
    mto_winners_set.add(player)

  for player in winners_set:
    selected = [chosen for chosen in winners_info_list if chosen['Name'] == player]
    if selected[0]['Times Won'] == 1:
      mto_winners_set.remove(player)

  
  return winners_set, mto_winners_set




def comparative_analysis(winner_set1, winner_set2):

  winners_eitheror = winner_set1 | winner_set2
  winners_both = winner_set1 & winner_set2
  winners_only1 = winner_set1 - winner_set2
  winners_only2 = winner_set2 - winner_set1
  winners_onlyone_notboth = winner_set1 ^ winner_set2

  print_line('Winners (Either/Or): ' + str(len(winners_eitheror)) + '\n')
  print_line('These are: \n')
  print_set(winners_eitheror)
  
  print_line('Winners (Both): ' + str(len(winners_both)) + '\n')
  print_line('These are: \n')
  print_set(winners_both)
  
  print_line('Winners (Only 1, not both): ' + str(len(winners_onlyone_notboth)) + '\n')

  print_line('These are: \n')
  print_set(winners_onlyone_notboth)

  
  print_line('Winners (Only Wimbledon, not French Open): ' + str(len(winners_only1)) + '\n')
  print_line('These are: \n')
  print_set(winners_only1)

  
  print_line('Winners (Only French Open, not Wimbledon): ' + str(len(winners_only2)) + '\n')
  print_line('These are: \n')
  print_set(winners_only2)
  

      
initialize()


wimbledon_data = readcsvdata('Wimbledon')
frenchopen_data = readcsvdata('FrenchOpen')

wimbledon_winners, wimbledon_mto_winners = analyze('Wimbledon', wimbledon_data)
frenchopen_winners, frenchopen_mto_winners = analyze('French Open', frenchopen_data)

comparative_analysis(wimbledon_winners, frenchopen_winners)
