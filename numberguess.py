import random

def number_guessing_game():

    print("\n================================")
    print("     NUMBER GUESSING GAME")
    print("================================")

    
    secret_number = random.randint(1, 100)

    attempts = 0

    while True:

        try:
            guess = int(input("Guess a number (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too Low! Try again.")

            elif guess > secret_number:
                print("Too High! Try again.")

            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Total Attempts: {attempts}")

                # Scoring system
                if attempts == 1:
                    score = 100
                elif attempts <= 3:
                    score = 80
                elif attempts <= 5:
                    score = 60
                elif attempts <= 10:
                    score = 40
                else:
                    score = 20

                print(f"Your Score: {score}/100")

                break

        except ValueError:
            print("Invalid input! Please enter a number.")




def word_counter(filename):

    print("\n================================")
    print("         WORD COUNTER")
    print("================================")

    try:

        
        with open(filename, "r") as file:
            text = file.read()


        text = text.lower()

      
        punctuation = ".,!?;:()[]{}\"'"

        for symbol in punctuation:
            text = text.replace(symbol, "")

      
        words = text.split()

       
        total_words = len(words)

        print(f"\nTotal Words: {total_words}")

        word_frequency = {}

        for word in words:

            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

  
        print("\nWord Frequency:")

        for word, count in word_frequency.items():
            print(f"{word}: {count}")

        
        if word_frequency:
            most_frequent_word = max(
                word_frequency,
                key=word_frequency.get
            )

            highest_count = word_frequency[most_frequent_word]

            print("\nMost Frequent Word:")
            print(f"{most_frequent_word} → {highest_count} times")

    except FileNotFoundError:
        print(f"Error: '{filename}' file not found.")


def main():

    while True:

        print("\n================================")
        print("        PYTHON MINI PROJECT")
        print("================================")

        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            number_guessing_game()

        elif choice == "2":

            filename = input("Enter text file name: ")

            word_counter(filename)

        elif choice == "3":

            print("\nThank you for using the program!")
            break

        else:

            print("Invalid choice! Please select 1, 2, or 3.")

main()
