from tabulate import tabulate

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
["Moon",1737,73.5],["Mars",3390,641.85]]

print(tabulate(table))

headers =['col1', 'col2', 'col3']
print(tabulate(table, headers, tablefmt="rounded_grid"))


info = {"name":"noha", "track":"gis", "age":31 }
# values = list(info.values())
# table = [values]
# # tablulate list of lists
# print(tabulate(table))  # tabulate --> accept list of lists

table = [info]  # list of dicts
# tablulate list of lists
print(tabulate(table))