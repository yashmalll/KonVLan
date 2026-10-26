class Room:
    max_members = 5

    def __init__(self, name):
        self.name = name
        self.members = []

    def is_full(self):
        return len(self.members) >= self.max_members

    def add_member(self, username):
        if username in self.members:
            print(f'{username} уже находится в комнате')
            return False

        if self.is_full():
            print('Комната переполнена')
            return False

        self.members.append(username)
        print(f'Участник {username} добавлен в комнату {self.name}')
        return True

    def remove_member(self, username):
        if username in self.members:
            self.members.remove(username)
            print(f'Участник {username} удалён из комнаты {self.name}')
        else:
            print('Нет такого участника')

    def show_members(self):
        print(f'Комната: {self.name}')
        print(f'Участники: {self.members}')
        print(f'Всего участников: {len(self.members)}')


class RoomManager:
    def __init__(self):
        self.rooms = []

    def create_room(self, room_name):
        if any(room.name == room_name for room in self.rooms):
            print('Такая комната уже существует')
            return False

        self.rooms.append(Room(room_name))
        print(f'Комната {room_name} создана')
        return True

    def list_room(self):
        if not self.rooms:
            print('Комнат пока нет')
            return

        for room in self.rooms:
            print(room.name)

    def get_room(self, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room

        return None



manager = RoomManager()

manager.create_room('Minecraft')
manager.create_room('Terraria')

manager.list_room()

room = manager.get_room('Minecraft')

if room is not None:
    room.add_member('Player1')
    room.add_member('Player2')
    room.show_members()
