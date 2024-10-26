class CdDisk:
    def __init__(self, id, name, number, cd_disk_id):
        self.id = id
        self.name = name
        self.number = number
        self.cd_disk_id = cd_disk_id

class LibraryCd:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Для реализации связи многие ко многим
class CDDickLibrary:
    def __init__(self, library_id, cd_disk_id,):
        self.cd_disk_id = cd_disk_id
        self.library_id = library_id

# Библиотеки
Libraries = [
    LibraryCd(1, 'Первая'),
    LibraryCd(2, 'Вторая'),
    LibraryCd(3, 'Третья'),
]


# cd-диски
Cd_disks = [
    CdDisk(1, 'ROM', 25000, 1),
    CdDisk(2, 'R - READ ', 35000, 2),
    CdDisk(3, 'RW - Rewritable', 45000, 3),
]

# связи дисков и библиотек
CD_dick_Libraries = [
    CDDickLibrary(1,1),
    CDDickLibrary(2,2),
    CDDickLibrary(1,3),
]

def main():
    #Основная функция
    #задание А1: Один-к-одному

    one_to_many = [(i.name, i.number, k.name) for k in Libraries for i in Cd_disks if i.cd_disk_id == k.id]
    print("задание A1")
    print(sorted(one_to_many))

    #Задание А2: суммарное количество дисков в каждой библиотеке
    suma = {}
    for i in Cd_disks:
        if i.cd_disk_id not in suma:
            suma[i.cd_disk_id] = 0
        suma[i.cd_disk_id] += i.number
    result_a2 = list(((k.name, suma.get(k.id, 0)) for k in Libraries))

    print("задание A2")
    print(result_a2)

    #Задание A3: Список cd-дисков с библиотеками
    many_to_many_temp = [(k.name, j.cd_disk_id, j.cd_disk_id)
                    for k in Libraries
                    for j in CD_dick_Libraries
                    if k.id == j.cd_disk_id]
    many_to_many = {}
    for Library_cd_name, cd_disk_id, library_id in many_to_many_temp:
        CdDisk_name = next(k.name for k in Cd_disks if k.id == cd_disk_id)
        if Library_cd_name not in many_to_many:
            many_to_many[Library_cd_name] = []
        many_to_many[Library_cd_name].append(CdDisk_name)

    print("Задание A3")
    print(many_to_many)

if __name__ == "__main__":
    main()

