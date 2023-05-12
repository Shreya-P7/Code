# Define the rules for information management
rules = {
    1: {'condition': lambda x: x > 1000, 'output': 'You need a database management system'},
    2: {'condition': lambda x: x > 100, 'output': 'You need a spreadsheet program'},
    3: {'condition': lambda x: x > 0, 'output': 'You need a text editor'},
    4: {'condition': lambda x: x == 0, 'output': 'You do not need any software'},
    5: {'condition': lambda x: x < 0, 'output': 'You cant process negative records!!'},
}


def get_user_input():
    while True:
        try:
            num_of_records = int(input('How many employee records do you need to manage? '))
            break
        except ValueError:
            print('Please enter a valid integer!!')
    return num_of_records


def determine_software(num_of_records):
    for rule in rules:
        if rules[rule]['condition'](num_of_records):
            return rules[rule]['output']


def get_user_feedback(software):
    feedback = input('\nThe recommended software is \n' + software + '. \n\tDo you agree? (y/n) ')
    if feedback.lower() == 'y':
        return True
    elif feedback.lower() == 'n':
        return False
    else:
        print('Invalid input! Please enter y or n.')
        return get_user_feedback(software)


def suggest_alternative_software(software):
    if software == 'You need a database management system':
        return '\nYou can consider using a document-oriented database like MongoDB.'
    elif software == 'You need a spreadsheet program':
        return '\nYou can consider using a data visualization tool like Tableau.'
    elif software == 'You need a text editor':
        return '\nYou can consider using an integrated development environment (IDE) like Visual Studio Code.'
    else:
        return '\nNo alternative software to suggest.'

flag=1

print("Welcome to an Expert System for Information Management(Employees). Here you can provide the nu")
while(flag==1):
        
    num_of_records = get_user_input()
    software = determine_software(num_of_records)

    feedback = get_user_feedback(software)
    if not feedback:
        alternative_software = suggest_alternative_software(software)
        print('\nBased on your feedback, you can consider the following alternative software: \n' + alternative_software)
    else:
        print('\nBased on your input, you need the following software: ' + software)
    
    flag=int(input("\n\nDo you want to more recommendations(1/0)? "))