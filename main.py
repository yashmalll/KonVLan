class Room:
    max_members = 5
    def __init__(self, name):
       self.name = name
       self.members = []

    def is_full(self):
        return len(self.members) >= self.max_members


    def add_member(self, username):
        if username not in self.members and len(self.members) <= self.max_members:
            self.members.append(username)
            print(f'Учатсник {username} Добавлен в группу {self.name}')
            return True
        else:
            print('Участник уже в гупуппе или группа переполнена')
            return False

    def remove_member(self, username):
        if username in self.members:
            self.members.remove(username)
        else:
            print('Нет такого участника')

    def show_members(self):
        print(f'Комната: {self.name}')
        print(f'Учасники: {self.members}')
        print(f'Всего учасников: {len(self.members)}')








room = Room('Minecraft')

# Проверка повторного добавления
print(room.add_member('player1'))

# Заполняем комнату до лимита
room.add_member('player2')
room.add_member('player3')
room.add_member('player4')

# Попытка добавить шестого участника
print(room.add_member('player5'))
print(room.add_member('player5'))

print("Комната заполнена:", room.is_full())
