import csv

# Open the CSV file
with open('German_verbs.csv', newline='') as csvfile:

    # Create a CSV reader object
    csvreader = csv.DictReader(csvfile)

    # Loop through each row in the CSV file
    for row in csvreader:

        # Process the row as a dictionary
        verbs = {
            'verb': row['verb'],
            'p': row['p'],
            'pp': row['pp'],
            'English': row['English']
        }

