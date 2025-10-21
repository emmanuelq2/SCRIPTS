
import random
number = random.randint(1, 100)
print(number)

# This code snippet generates a random number between 1 and 100 and checks
solution = input("Enter a number between 1 and 100: ")
solution = int(solution)  # Convert the input to an integer for comparison

# number = str(number)  # Convert the number to a string for digit check      
if solution >= 1 and solution <= 100 and str(solution).isdigit():
    print(f"{solution} is a valid digit.")
    if solution == number:
        print(f"You found it! {solution} is equal to {number}.")
    
    elif solution > number:
        print(f"{solution} is greater than the right number.")
        solution_2 = input("Enter a number lower than your first choice: ")
        solution_2 = int(solution_2)
        if solution_2 == number:
            print(f"You found it! {solution_2} is equal to {number}.")
        elif solution_2 > number:
            print(f"{solution_2} is greater than the right number.")
            solution_3 = input("Enter a number lower than your second choice: ")
            solution_3 = int(solution_3)
            if solution_3 == number:
                print(f"You found it! {solution_3} is equal to {number}.")
            elif solution_3 > number:
                print(f"{solution_3} is greater than the right number.")
                solution_4 = input("Enter a number lower than your third choice: ")
                solution_4 = int(solution_4)
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_4)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

            elif solution_3 < number:
                print(f"{solution_3} is lower than the right number.")
                solution_4 = input("Enter a number greater than your third choice: ")
                solution_4 = int(solution_4) 
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_4)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

        elif solution_2 < number:
            print(f"{solution_2} is lower than the right number.")
            solution_3 = input("Enter a number greater than your second choice: ")
            solution_3 = int(solution_3) 
            if solution_3 == number:
                print(f"You found it! {solution_3} is equal to {number}.")
            elif solution_3 > number:
                print(f"{solution_3} is greater than the right number.")
                solution_4 = input("Enter a number lower than your third choice: ")
                solution_4 = int(solution_4)
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

            elif solution_3 < number:
                print(f"{solution_3} is lower than the right number.")
                solution_4 = input("Enter a number greater than your third choice: ")
                solution_4 = int(solution_4) 
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

    elif solution < number:
        print(f"{solution} is less than the right number.")
        solution_2 = input("Enter a number greater than your first choice: ")
        solution_2 = int(solution_2)
        if solution_2 == number:
            print(f"You found it! {solution_2} is equal to {number}.")       
        elif solution_2 > number:
            print(f"{solution_2} is greater than the right number.")
            solution_3 = input("Enter a number lower than your second choice: ")
            solution_3 = int(solution_2)
            if solution_3 == number:
                print(f"You found it! {solution_3} is equal to {number}.")
            elif solution_3 > number:
                print(f"{solution_3} is greater than the right number.")
                solution_4 = input("Enter a number lower than your third choice: ")
                solution_4 = int(solution_4)
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")


            elif solution_3 < number:
                print(f"{solution_3} is lower than the right number.")
                solution_4 = input("Enter a number greater than your third choice: ")
                solution_4 = int(solution_4) 
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

        elif solution_2 < number:
            print(f"{solution} is lower than the right number.")
            solution_3 = input("Enter a number greater than your second choice: ")
            solution_3 = int(solution_2) 
            if solution == number:
                print(f"You found it! {solution} is equal to {number}.")
            elif solution_3 > number:
                print(f"{solution_3} is greater than the right number.")
                solution_4 = input("Enter a number lower than your third choice: ")
                solution_4 = int(solution_4)
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

            elif solution_3 < number:
                print(f"{solution_3} is lower than the right number.")
                solution_4 = input("Enter a number greater than your third choice: ")
                solution_4 = int(solution_4) 
                if solution_4 == number:
                    print(f"You found it! {solution_4} is equal to {number}.")
                elif solution_4 > number:
                    print(f"{solution_4} is greater than the right number.")
                    solution_5 = input("Enter a number lower than your fourth choice: ")
                    solution_5 = int(solution_5)
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")
                elif solution_4 < number:
                    print(f"{solution_4} is lower than the right number.")
                    solution_5 = input("Enter a number greater than your fourth choice: ")
                    solution_5 = int(solution_5) 
                    if solution_5 == number:
                        print(f"You found it! {solution_5} is equal to {number}.")
                    else:
                        print(f" You did not find the correct number: {number}.")

elif not solution.isdigit():
    print(f"{solution} is not a digit or valid.")
    solution = input("Please enter a number between 1 and 100: ")
    solution = int(solution)

elif not str(solution).isdigit():
    print(f"{solution} is not a digit or valid.")
    solution = input("Please enter a number between 1 and 100: ")
    solution = int(solution)
elif solution < 1 or solution > 100:
    print(f"{solution} is not between 1 and 100.")
    solution = input("Please enter a number between 1 and 100: ")
    solution = int(solution)

