from Functions import *

k_var = 10
students = {}
variants = {}
testing_table = {}
names1 = []
name_bd1 = ''
flag = False
command = input("Введите команду: ")

while command != "exit":
    if command == "open-names":
        names1, name_bd1, students, variants, testing_table = db_names(k_var, students, variants, testing_table)
        flag = True

    elif command == "create":
        names1, name_bd1, students, variants, testing_table = create_bd(k_var, names1, students, testing_table, variants)
        flag = True

    elif command == "open":
         name_bd1, students, variants, testing_table = db()
         flag = True

    elif command == "print" and flag:
        print_bd(students, variants, testing_table)

    elif command == "add" and flag:
        names1, name_bd1, students, variants, testing_table = add_str(k_var, names1, name_bd1, students, variants, testing_table)

    elif command == "print-string" and flag:
        out_str(students, variants, testing_table)

    elif command == "print-students" and flag:
        print_students(students)

    elif command == "print-variants" and flag:
        print_variants(variants)

    elif command == "add-variant" and flag:
        variants = add_variant(variants, name_bd1, k_var)

    elif command == "delete-variant" and flag:
        variants, testing_table = delete_variants(name_bd1, variants, k_var, testing_table)

    elif command == "random-variants" and flag:
        testing_table = random_var(name_bd1, variants, testing_table)

    elif command == "delete" and flag:
        variants, students, testing_table, names1 = delete_str(name_bd1, variants, students, testing_table, names1)

    elif command == "correct" and flag:
        students, variants, testing_table = correct_str(name_bd1, students, variants, testing_table)

    elif command == "back-up" and flag:
        back_up(names1, name_bd1, students, variants, testing_table)

    elif command == "return-back-up":
        names1, name_bd1, students, variants, testing_table = return_back_up()
        flag = True

    elif command == "close" and flag:
        students, variants, testing_table, names1 = close(students, variants, testing_table, names1)
        flag = False
    else:
        print("incorrect command")
    command = input("Введите команду: ")






