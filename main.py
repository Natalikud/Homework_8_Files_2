file_name1 = '1.txt'
file_name2 = '2.txt'
file_name3 = '3.txt'
file_name4 = 'result_file.txt'

with open(file_name1,encoding='utf-8') as file:
    file1 = file.read()
with open(file_name2,encoding='utf-8') as file:
    file2 = file.read()
with open(file_name3,encoding='utf-8') as file:
    file3 = file.read()
#список параметров
file_list = [file_name1,file_name2,file_name3]
#список значений параметров
file_list_result = []
file_list_result.append(''.join(file1))
file_list_result.append(''.join(file2))
file_list_result.append(''.join(file3))
# print(file_list_result)
#словарь параметров и их значений
file_dict = dict(zip(file_list,file_list_result))
# print(file_dict)
###############################
#словарь с количеством строк
count_dict = {}
def len_file_lines(file_name:str):
    with open(file_name, encoding='utf-8') as file:
            count = len(file.readlines())
            count_dict[file_name] = count

len_file_lines(file_name1)
len_file_lines(file_name2)
len_file_lines(file_name3)
# print(count_dict)

#######################################
#отсортированный словарь с количеством строк
sorted_dict = {}
def sort():
    sorted_values = sorted(count_dict.values())
    for i in sorted_values:
        for k in count_dict.keys():
            if count_dict[k] == i:
                sorted_dict[k] = count_dict[k]
                break
    # print(sorted_dict)
sort()
# print(sorted_dict)


##############################
with open(file_name4,mode='a',encoding='utf-8') as file:
    for k, v in sorted_dict.items():
        for key, value in file_dict.items():
            if k == key:
                file.write(f'{k}\n{v}\n{value}\n')


