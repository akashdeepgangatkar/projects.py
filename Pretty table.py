from prettytable import PrettyTable

mytable = PrettyTable(['student name', 'class', 'percentage'])

mytable.add_rows([['yogesh', 'x', '90.2'],
                  ['prajwal', 'y', '80.2'],
                  ['anish', 'z', '70.2'],
                  ['neeraj', 'a', '60.2']])

print(mytable)