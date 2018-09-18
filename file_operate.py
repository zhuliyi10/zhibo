import codecs

file = codecs.open('badminton.csv', 'r', 'utf-8')

file.readline()
first=file.readline()
first_list=first.split(',')
if len(first_list)>0:
    if first_list[0].isdigit():
        id=first_list[0]
file.close()
# old=file.readlines()
# file = codecs.open('badminton.csv', 'w', 'utf-8')
# file.write("hello world \r\n")
# for n in range(1,len(old)):
#     line=old[n]
#     file.write(line)
# file.close()
