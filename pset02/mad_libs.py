
import random

templates = [
    {
        "text": "A :adjective ghost is behind you! ",
        "author": "annascaroline"
    },
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert ",
        "author": "annascaroline"
    },
    {
        "text": "Look! There is a :adjective :verb a :noun in :place",
        "author": "annascaroline"
    },
    {
        "text": "A :adjective witch did a :verb with a :object",
        "author": "annascaroline"
    },
    {
        "text": "You are alone in a :place beware of :adjective :creature",
        "author": "annascaroline"
    },
    {"text": "A :adjective :creature stole my :object during the :noun",
        "author": "annascaroline"},
    {"text": "I found a :adjective :object hiding inside my :place",
        "author": "annascaroline"},
    {"text": "The :creature challenged me to a :adjective :noun",
        "author": "annascaroline"},
    {"text": "Never trust a :adjective :creature carrying a :object",
        "author": "annascaroline"},
    {"text": "At midnight, the :creature began to :verb inside the :place",
        "author": "annascaroline"}

]

yes_answers = {"yes", "sí", "oui", "yup", "bet", "yeah"}

while True:
    current_template = random.choice(templates)
    text = (current_template["text"])
    author = (current_template["author"])

    for word in current_template["text"].split():
        if word.startswith(":"):
            while True:
                answer = input(f"Please enter {word[1:]}: ")
                if 0 < len(answer) <= 30:
                    text = text.replace(word, answer)
                    break
                else:
                    print("Invalid input, please try again.")
    print(text)
    print()
    print(f"Story by: {author}")
    print()
    print()
    guess = input("Would you like to play again? ").lower().strip()
    if guess in yes_answers:
        continue
    else:
        print("Thanks for playing!")
        break
