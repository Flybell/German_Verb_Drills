"""creates a list of dictionaries"""

import csv

verbs = []

# Open the CSV file
with open('German_verbs.csv', newline='') as csvfile:

    # Create a CSV reader object
    csvreader = csv.DictReader(csvfile)

    # Loop through each row in the CSV file
    for row in csvreader:

        # Process the row as a dictionary
        dict = {
            'verb': row['verb'],
            'p': row['p'],
            'pp': row['pp'],
            'English': row['English']
        }

        # Do something with the dictionary
        verbs.append(dict)
        print(verbs)
