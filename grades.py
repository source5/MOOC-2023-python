# a program which asks for the amount of points received and then prints out the grade attained

def main():
    points = int(input('How many points [0-100]:'))
    if (points > 100) :
        print('impossible!')
    elif (90 <= points <= 100):
        print('Grade: 5')
    elif (80<= points <= 89):
        print('Grade: 4')
    elif (70 <= points <= 79):
        print('Grade: 3')
    elif (60 <= points <= 69):
        print('Grade: 2')
    elif (50 <= points <= 59):
        print('Grade: 1')
    elif (0 <= points <=49):
        print("fail")
    else:
        print('impossible!')
main()