from notebook_app_main import Notebook, Note

def menuOption():
    print("""
Notebook Menu

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")
    choice = int(input("Enter an option: "))
    return choice

def search_notes(myNotebook):
    filter = input("Search for: ")
    print("... results for ...", filter)
    notes = myNotebook.search(filter)
    # need a loop to print
    for n in notes:
        print(n)

def add_note(myNotebook):
    memo = input("Enter a memo: ")
    tags = input("Enter tags: ")
    myNotebook.newNote(memo, tags)
    print("Your note has been added.")

def modify_note(myNotebook):
    id = int(input("Enter a note id: "))
    memo = input("Enter a memo: ")
    tags = input("Enter tags: ")
    if memo:
        if myNotebook.modifyMemo(id, memo):
            print("Memo is modified")
    if tags:
        if myNotebook.modifyTags(id, tags):
            print("Tags is modified")

def main():
    myNoteBook = Notebook()
    myNoteBook.newNote("test1", "tag1")
    myNoteBook.newNote("test3", "tag1")
    myNoteBook.newNote("test2", "tag2")

    while True:
        option = menuOption()
        if option == 5:
            break
        elif option == 1:
            print(myNoteBook)
        elif option == 2:
            search_notes(myNoteBook)
        elif option == 3:
            add_note(myNoteBook)
        elif option == 4:
            modify_note(myNoteBook)
        else:
            print("{} is not a valid choice".format(option))

    print("Thank you for using your notebook today.")

main()
