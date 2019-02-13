with open('results_2.txt', 'r') as f:
    file_contents = f.read()

# print(file_contents)
# d = {}
# for i in range(0, len(file_contents), 2):
#     try:
#         d[file_contents[i]] = file_contents[i + 1]
#     except IndexError:
#         continue
#
# print(d)

file_contents = file_contents.split('$')

l = []
for i in file_contents:
    l.append(i.split('@'))

d = {}
for i in l:
    try:
        try:
            d[i[0]] = float(i[1])
        except ValueError:
            pass
    except IndexError:
        pass

sorted_list = sorted(d.items(), key=lambda t: t[1], reverse=True)

rank = 0
with open('results_sorted.txt', 'w') as f:
    f.write('Top ranks in ISE 3rd Semester results\nBy Gaurav K.\n\n')
    for i in sorted_list:
        rank += 1
        f.write(str(rank) + ". " + ": ".join(i[0].split('-')) + ": " + str(i[1]) + "\n")


