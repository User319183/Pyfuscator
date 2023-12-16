import random

def generate_compliment(name):
    compliments = ["is awesome!", "rocks!", "is the best!", "is fantastic!", "is incredible!"]
    compliment = random.choice(compliments)
    return f"{name} {compliment}"

def main():
    name = input("What's your name? ")
    compliment = generate_compliment(name)
    print(compliment)

if __name__ == "__main__":
    main()