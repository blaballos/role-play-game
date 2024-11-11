def show_role():
    role = input('1. Warrior\n2. Wizard\n3. Golem\nSelect a role for view its features: ')
    
    if role == '1':
        print('\nCharacteristics of the Warrior:')
        print('Health: 290 ❤\nDamage: 110 🗡\nAttack speed: 1.2s 🕰')
    elif role == '2':
        print('\nCharacteristics of the Wizard:')
        print('Health: 260 ❤\nDamage: 130 🗡\nAttack speed: 1.5s 🕰')
    elif role == '3':
        print('\nCharacteristics of the Golem:')
        print('Health: 400 ❤\nDamage: 160 🗡\nAttack speed: 2.3s 🕰')
        
    confirm = input('\n1. Back\nConfirm\nSelect an option: ')
    return role, confirm