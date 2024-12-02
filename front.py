import time

def display_welcome():
    print("\n" + "=" * 70)
    print("🌟✨ WELCOME TO THE QUIZ GAME!✨🌟".center(65))
    print("=" * 70)
    
    time.sleep(1)
    
    print("\n" + "🧩  Choose Your Challenge  🧩".center(70))
    print("💫" + "=" * 66 + "💫")
    print("1. 🧠  Random Facts  🌍".center(70))
    print("2. 💻  About Programming  🖥️".center(70))
    print("💫" + "=" * 66 + "💫")
    
    print("\n" + "=" * 70 + "\n")


def choose_category():
    while True:
        try:
            choice = int(input("✨ Please enter the number of your choice (1 or 2): "))
            if choice == 1:
                print("🎉 You chose: 🧠 Random Facts! 🎉".center(70))
                random_facts_design()  
                break
            elif choice == 2:
                print("🎉 You chose: 💻 About Programming! 🎉".center(70))
                about_programming_design()  
                break
            else:
                print("❌ Invalid choice. Please choose 1 or 2. ❌".center(70))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌".center(70))


def random_facts_design():
    print("\n" + "=" * 70)
    print("🌍 RANDOM FACTS SECTION 🌍".center(70))
    print("=" * 70)
    
    time.sleep(1)

    print("\n" + "🎮  What would you like to do next? 🎮".center(70))
    print("💫" + "=" * 66 + "💫")
    print("1. Play the Quiz! 🎉".center(70))
    print("2. Go Back 🔄".center(70))
    print("💫" + "=" * 66 + "💫")
    
    print("\n" + "=" * 70 + "\n")
    
    while True:
        try:
            choice = int(input("✨ Please enter your choice (1 to Play, 2 to Go Back): "))
            if choice == 1:
                print("\n🎉 Starting the Random Facts Quiz! 🎉\n".center(70))
                break
            elif choice == 2:
                print("\n🔄 Going back to the main menu... 🔄\n".center(70))
                display_welcome()  
                choose_category() 
                break
            else:
                print("❌ Invalid choice. Please choose 1 to Play or 2 to Go Back. ❌".center(70))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌".center(70))


def about_programming_design():
    print("\n" + "=" * 70)
    print("💻 ABOUT PROGRAMMING SECTION 💻".center(70))
    print("=" * 70)
    
    time.sleep(1)

    print("\n" + "🎮  What would you like to do next? 🎮".center(70))
    print("💫" + "=" * 66 + "💫")
    print("1. Play the Quiz! 🎉".center(70))
    print("2. Go Back 🔄".center(70))
    print("💫" + "=" * 66 + "💫")
    
    print("\n" + "=" * 70 + "\n")
    
    while True:
        try:
            choice = int(input("✨ Please enter your choice (1 to Play, 2 to Go Back): "))
            if choice == 1:
                print("\n🎉 Starting the About Programming Quiz! 🎉\n".center(70))
                break
            elif choice == 2:
                print("\n🔄 Going back to the main menu... 🔄\n".center(70))
                display_welcome()  
                choose_category()  
                break
            else:
                print("❌ Invalid choice. Please choose 1 to Play or 2 to Go Back. ❌".center(70))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌".center(70))

if __name__ == "__main__":
    display_welcome()  
    choose_category()  