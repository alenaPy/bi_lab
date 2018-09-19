"""Task 1."""


list1 = []
list2 = []
list3 = []
try:
    count = 0
    with open('ratings.list', 'r', encoding='ISO-8859-1') as ratings:
        for line in ratings:
            if 'New  Distribution  Votes  Rank  Title' in line:
                break
        for line in ratings:
            if count < 250:
                title = line.strip().split('  ')[3].split('(')[0]
                rat = line.strip().split('  ')[2]
                year = line.strip().split('  ')[3].rstrip(')').split('(')[1]
                print(title, rat, year)
                count += 1
                list1.append(title)
                list2.append(rat)
                list3.append(year)
except FileNotFoundError:
        print('File not exists')


write_movies = open('top250_movies.txt', 'w', encoding='UTF-8')
for i in list1:
    write_movies.write(i + '\n')
write_movies.close()


dict_year = dict((i, list3.count(i)) for i in list3)

write_year = open("years.txt", "w")
for i in dict_year:
    a = str(i)
    write_year.write(
        a.rstrip('/I') + ' ' + '*' *
        dict_year[i] + ' ' + str(dict_year[i]) + '\n')
write_year.close()

dict_rat = dict((i, list2.count(i)) for i in list2)

write_rat = open("ratings.txt", "w")
for i in dict_rat:
    a = str(i) + ' '
    write_rat.write(a + '*' * dict_rat[i] + ' ' + str(dict_rat[i]) + '\n')
write_rat.close()
