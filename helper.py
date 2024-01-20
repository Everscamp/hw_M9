import re


contacts = {}
phone_pattern = r'\d+'
name_pattern = r'[a-zA-Z_]+'
operator_pattern = r'(show all)|(good bye)|[a-zA-Z_]+\s?'
phone_operator_pattern = r'(add)|(change)'

# remove spaces at the beginning and at the end of the string and lower case the string
def operator_handler(operator):
    parced_operator = re.search(operator_pattern, operator)
    return parced_operator.group().lower().strip()

# defines name and telephone number
def operand_maker(operator):
    operands = []
    trimmedContact = re.sub(phone_operator_pattern, '', operator)
    
    phoneName = re.search(name_pattern, trimmedContact)
    phoneNum = re.search(phone_pattern, trimmedContact)
    
    if not phoneName:
        raise Exception('No name? Enter the contact in the format: "Name" "Phone Number"')
    else:
        operands.append(phoneName.group().capitalize())
    
    if not phoneNum:
        raise Exception('No number? Enter the contact in the format: "Name" "Phone Number"')
    else:
        operands.append(phoneNum.group())

    return operands

#simple welcome function
def hello(operator):
    return 'How can I help you?'

# adds a phone number to the contacts list
def add(operator):
    phoneName = operand_maker(operator)[0]
    phoneNum = operand_maker(operator)[1]
        
    contacts.update({phoneName: phoneNum})

    return f'Contact {phoneName} has been added!'

# update the contact number, but I think to add a possibility to add new contact on user's demand
def change(operator):
    phoneName = operand_maker(operator)[0]
    phoneNum = operand_maker(operator)[1]

    if phoneName not in contacts:
        raise Exception(f'No contacts with name {phoneName}')
    else:
        contacts.update({phoneName: phoneNum})
        return f'Contact {phoneName} has been updated!'

# displays the phone number of the requested contact
def phone(operator):
    phoneName = re.search(name_pattern, operator.replace("phone", ""))

    if not phoneName:
        raise Exception('No name? Enter the contact in the format: "Name" "Phone Number"')
    
    capitalized_name = phoneName.group().capitalize()
    
    if contacts.get(capitalized_name) == None:   
        return f'No contacts with name {phoneName.group().capitalize()}'
    else:
        return f'{capitalized_name} number: {contacts.get(capitalized_name)}'

# shows contact list
def show_all(operator):
    return f'{contacts}'

# simple farewell function
def goodbye(operator):
    return 'Good bye!'

# shows commad list
def commands(operator):
    return 'The list of commands: \n \
        Type "phone [name of the contact]" to see its phone num.\n \
        Type "add [name] [phone number]" to add new contact.\n \
        Type "change [name] [new phone number]" to add new contact.\n \
        Type "show all" to see all contacts \n \
        Type "end" to exit'


OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'goodbye': goodbye,
    'commands': commands
}

def get_handler(operator):
    operator = operator_handler(operator)
    if operator not in OPERATIONS:
        raise AttributeError
    else:
        return OPERATIONS[operator]

if __name__ == '__main__':
    print('Go to the main file!')
