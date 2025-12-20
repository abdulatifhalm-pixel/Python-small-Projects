, name2):
    # Clean and prepare names
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    combined = name1 + name2

    # Count letters in the word "love"
    score = 0
    for letter in "love":
        score += combined.count(letter)

    # Generate a percentage (0–100)
    percentage = (score * 10) % 101
    return percentage


print("❤️ Welcome to Love Calculator ❤️")

person1 = input("Enter first name: ")
person2 = input("Enter second name: ")

result = love_calculator(person1, person2)

print(f"\n💖 Love Percentage between {person1} and {person2}: {result}%")

if result >= 80:
    print("💍 Perfect match!")
elif result >= 50:
    print("😊 Good relationship!")
elif result >= 30:
    print("🙂 Can work with effort.")
else:
    print("💔 Better stay friends.")
