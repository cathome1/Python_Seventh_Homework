# Создать телефонный справочник с возможностью импорта и экспорта данных в формате CSV.


def main():
    global file
    ch = int(input('Телефонный справочник\n1)Импортировать номера\n2)Эксортировать номера'))
    if ch == 1:
        file = input('Введите название файла для импорта: ')
        imp_ch = int(input('''Телефонный справочник
1) Добавить номер
2) Добавить несколько номеров вручную
3) Добавить несколько номеров из файла
'''))
        match (imp_ch) :
            case 1:
                EnterOneNum()
        
    elif ch == 2:
        file = input('Введите название файла для экспорта : ')
        with open(file, 'a', encoding='utf8') as imp: 
            exp_ch = int(input('''Телефонный справочник
1) Вывести информацию о телефоне на экран
2) Вывести информацию о нескольких номерах на экран
3) Вывести информацию о нескольких номерах в файл'''))

def EnterOneNum():
     with open(file, 'a', encoding='utf8') as imp:
        fam = input("Введите Фамилию: ")
        if len(fam) < 2:
            print("Фамилия слишком короткая, минимум 2 символа.")
            main()
            exit()
        imya = input('Введите имя: ')
        if len(imya) < 2:
            print("Имя слишком короткое, минимум 2 символа.")
            main()
            exit()
        otch = input('Введите отчество (при наличии): ')
        if len(otch)>0 and len(otch)<5:
            print("Отчество слишком короткое, минимум 5 символов.")
            main()
            exit()
        num = input("Введите номер без +: ")
        if not num.isdigit():
            print("Номер должен состоять только из цифр")
        note = input("Введите заметку(не более 20 символов): ")
        if len(note) > 20:
            print("Заметка должна содержать не более 20 символов")
            main()
            exit()
        res = [fam,imya,otch,num,note]
        imp.write(f"{';'.join(res)}\n")
        print(f"Номер успешно импортирован файл {file}")
        main()
def EnterSomeNumbers():
    count = input("Введите количество импортируемых номеров: ")
    if count.isdigit() and int(count)>0:
        for i in range(1, count + 1):
            print(f"======= Импорт номера №{i} =======")
            EnterOneNum()
    else:
        print("Введено некорректное значение.")
    main()
