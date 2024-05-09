def main():
    #create empty dictionary
    groceries = {}
    while True:
        #Collect user input, remove whitespace and Make uppercase
        item = input().strip().upper()
        #Check if user input is or is not in grocery dict and add with count
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1

