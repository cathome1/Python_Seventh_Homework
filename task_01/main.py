# Создать телефонный справочник с возможностью импорта и экспорта данных в формате CSV.

def main():
    global file
    ch = int(input('Телефонный справочник\n1)Импортировать номера\n2)Эксортировать номера\n'))
    if ch == 1:
        file = input('Введите название файла для импорта(например test.csv): ')
        if file[-4:] != ".csv":
            print('\nФайл должен иметь расширение .csv\n')
            main()
        imp_ch = int(input('''\nТелефонный справочник
1) Добавить номер
2) Добавить несколько номеров вручную
3) Добавить несколько номеров из файла
'''))
        match (imp_ch) :
            case 1:
                EnterOneNum()
            case 2:
                EnterSomeNumbers()
            case 3:
                EnterFromFile()
            case _:
                exit()
        
    elif ch == 2:
        file = input('Введите название файла для экспорта : ')
        with open(file, 'a', encoding='utf-8') as exp: 
            exp_ch = int(input('''Телефонный справочник
1) Вывести информацию о телефоне на экран
2) Вывести информацию о нескольких номерах на экран
3) Вывести информацию о нескольких номерах в файл'''))

def EnterOneNum(flag = True):
     with open(file, 'a', encoding='utf-8') as imp:
        fam = input("Введите Фамилию: ")
        if len(fam) < 2:
            print("\nФамилия слишком короткая, минимум 2 символа.\n")
            return main()
        imya = input('Введите имя: ')
        if len(imya) < 2:
            print("\nИмя слишком короткое, минимум 2 символа.\n")
            return main()
        otch = input('Введите отчество (при наличии): ')
        if len(otch)>0 and len(otch)<5:
            print("\nОтчество слишком короткое, минимум 5 символов.\n")
            return main()
        num = input("Введите номер без +: ")
        if not num.isdigit():
            print("\nНомер должен состоять только из цифр\n")
        note = input("Введите заметку(не более 20 символов): ")
        if len(note) > 20:
            print("\nЗаметка должна содержать не более 20 символов\n")
            return main()
        res = [fam,imya,otch,num,note]
        imp.write(f"{';'.join(res)}\n")
        print(f"\nНомер успешно импортирован файл {file}\n")
        imp.close()
        if flag:
            return main()
def EnterSomeNumbers():
    count = input("Введите количество импортируемых номеров: ")
    if count.isdigit() and int(count)>0:
        for i in range(1, int(count) + 1):
            print(f"======= Импорт номера №{i} =======")
            EnterOneNum(0)
    else:
        print("\nВведено некорректное значение.\n")
    return main()
def EnterFromFile():
    with open(file, 'a', encoding='utf-8') as to_imp:
        f = input('Введите название файла откуда импортировать контакты: ')
        if f[-4:] != ".csv":
            print('\nФайл должен иметь расширение .csv\n')
            EnterFromFile()
            return main()
        try:
            with open(f,"r", encoding="utf-8") as from_imp:
                for i in from_imp:
                    to_imp.write(i)
            from_imp.close()
            print(f"\nКонтакты из файла {f} успешно импортированы в файл {file}\n")
        except:
            print('\nДанного файла не существует.\n')
        to_imp.close()
        return main()
main()