# This program will take user inputs and store values and calculate Current and Power using lists and for loops while also producing
# Author: Skye Jacobson


resistance = [12,17,28,40,57,82]
current = []
numOfElements = 6

def currentFn():
    for i in range(numOfElements):  # Defining the amount of times a user can input current
        while True:
            try:
                currentInput = int(input(f'Please enter a non-zero and non-negative number for current ({len(current) + 1}/{numOfElements}): '))
                if currentInput <= 0:
                    print('Invalid input. Please enter a positive number or not 0.') # Validating user data 
                    continue
                current.append(currentInput) # Initializing inputted data into empty list
                break
            except ValueError:
                print('Please enter a valid number/integer.') # Allowing a smooth catch for any other user input than integers

def calcPower(current, resistance):
    power = []
    for a, b in zip(current, resistance):
        power.append((a**2) * b)  # Calculating power data against input and already established current
    return power
        
def main():
    currentFn()
    power = calcPower(current, resistance)

    # Everything below is formatting table output for a clean output.

    titles = ['Resistance', 'Current', 'Power']
    print('{:<15} {:<10} {:<10}'.format('Resistance', 'Current', 'Power'))
    print('-' * 35)
   
    for Resistance, Current, Power in zip(resistance, current, power):
        print('{:<15} {:<10} {:<10}'.format(Resistance, Current, Power))

    print('-' * 35)
    print('Totals')
    print('{:<15} {:<10} {:<10}'.format(sum(resistance), sum(current), sum(power)))
    
    
main()   # Running the main function/program