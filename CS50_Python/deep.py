# Takes in the users answer
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().title()

# Checks if the users answer is correct or not
 match ans:
     case "42" | "Forty Two" | "Forty-Two":
         print("Yes")
     case _:
         print("no")


