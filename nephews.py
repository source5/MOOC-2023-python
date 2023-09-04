#Code it check matching list items using conditional statement
def main():
    nephew_donald = ['Huey','Dewey','Louie']
    newphew_mickey = ['Morty','Ferdie']
    name = input()

    if name in nephew_donald:
        print('I think you might be one of Donald Duck\'s nephews.')
    elif name in newphew_mickey:
        print('I think you might be one of Mickey Mouse\'s nephews.')
    else:
        print('You\'re not a nephew of any character I know of.')

main()