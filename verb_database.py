"""creates a list of dictionaries"""

verbs = []

# Open the tab-delimited file
with open('German_verbs.txt', 'r') as file:

    # Loop through each line in the file
    for line in file:

        # Remove any trailing whitespace from the line
        line = line.strip()

        # Split the line into separate items based on the tab delimiter
        items = line.split('\t')

        # Process the items as needed
        item1 = items[0]
        item2 = items[1]
        item3 = items[2]
        item4 = items[3]

        # Create a dictionary from the items
        dict = {
            'verb': item1,
            'p': item2,
            'pp': item3,
            "English": item4
        }

        # Do something with the dictionary
        verbs.append(dict)
        print(verbs)
