def story_game():

    noun = input("Enter a noun:")
    city = input("Enter a city:")
    number = int(input("Enter a number:"))
    time = input("Enter a period of time:")
    first_adjective = input("Enter a adjective:")
    second_adjective = input("Enter a second adjective:")
    name = input("Enter a persons name:")
    cloth =input("Enter a type of clothing:")
    color= input("Enter a color:")
    
    print ("_________________________________________________________________")
    print ("\nIt is a little known fact that",noun,"have been watching",city,"for",number,time,".")
    print ("\nOnly the" ,first_adjective, "people believed that it was just a matter of time before",noun,"invaded the", second_adjective, "city of", city, ".\n")
    print (name,",who was a", first_adjective, "person tried to warn the people, telling them their best defense was to hang",cloth, "from the trees and", color, "shoes on every door knob.")
    print ("\nUnfortunately no one believed", name, "and when",noun, "attacked", city, ",only the", first_adjective, "people survived.")
    print ("_________________________________________________________________")
    
    print ("\nWould you like to play the game again?")
    ans = input("Enter your decision(Y or N):")
    if ans in ("Y","y"):
        story_game();
    else:
        print ("Thank you.")
story_game();
