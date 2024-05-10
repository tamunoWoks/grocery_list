def main():
    #create empty dictionary
    groceries = {}
    while True:
        try:
            #Collect user input, remove whitespace and Make uppercase
            item = input().strip().upper()
            #Check if user input is or is not in grocery dict and add with count
            if item not in groceries:
                groceries[item] = 1
            else:
                groceries[item] += 1
        #Catch EOFError when user exits program and print sorted list with count
        except EOFError:
            for key in sorted(groceries):
                print(groceries[key], key)
            #Exit while loop
            break


if __name__ == "__main__":
    main()