from Roles.character import Enemy, Warrior, Wizard, Golem

def confirm_role(name, role, confirmation):
    if confirmation == '2':
        if role == '1':
            character = Warrior(name,290, 110, 1.2)
        elif role == '2':
            character = Wizard(name,260, 130, 1.5)
        elif role == '3':
            character = Golem(name,400, 160, 2.3)
            
        enemy = Enemy('Boss',1000, 200, 3)
        
    return character, enemy