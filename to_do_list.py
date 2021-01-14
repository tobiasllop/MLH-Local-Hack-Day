#Store the notes from the list
To_do_list = []
def main():
    Command = input(str("Instructions: \nWelcome to the to do list app \n- If you want to see your list, type 'See my list' \n- If you want to add notes to your list, type 'add' \n- If You want to stop this app type 'Stop' \nInsert the command here: "))
    #Upper the string
    Command = Command.upper()

    #Ask the user if he/she wants to insert another command, after he/she have inserted another command before
    def ask():
        ask = input(str("Do you want to insert another command? Answer with yes or no: "))
        ask = ask.upper()
        if ask == "YES":
            return main()
        elif ask == "NO":
            return None
        else:
            print("Incorrect command\n")
            return main()

    #Show the list        
    if Command == "SEE MY LIST":
        print("\nYour list: ")
        for x in To_do_list:
            print(f"- {x}")
        print("\n")
        return ask()

    #Add notes to the list
    elif Command == "ADD":
        notes = input(str("Add a note to your list: "))
        To_do_list.append(notes)
        return ask()

    #Stop the program
    elif Command == "STOP":
        return None

    #Incorrect command
    else:
        print("You should return the correct commands\n")
        return ask()
    

main()