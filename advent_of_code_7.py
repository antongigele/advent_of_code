
def read_data(path):
    try:
        file = open(path,'r')
    except:
        print('file ', path, ' wurde nicht gefunden.')
        quit()

    data = file.readlines()
    file.close()

    return(data)

#-----------------------part1----------------------#
# zuerst alle strings "bags" und "bag" loeschen, und dann alle "contain" durch ":" ersetzen
def listcreater(data, sep = None, replace_old = None, replace_new = None):
    if sep is not None:
        sep_list = data.split(sep)
        if replace_old is not None:
            for e in range(len(sep_list)):
                sep_list[e] = sep_list[e].replace(replace_old, replace_new)
        return sep_list        
    else:
        for e in range(len(data)):
            data[e] = data[e].replace(replace_old, replace_new)          
        return data

def get_valid_bag(data, valid_bag_lst, len_list = []): # listenlängen werden in der len_list festgehalten
    next_bag_layer_lst = [] # next_bag_layer_lst wird bei jeder iteration neu gemacht und and valid_bag_lst drangehaengt

    if len(len_list) > 2 and len_list[len(len_list)-1] == len_list[len(len_list)-2]: # abbruchbedingung, die laengenliste nimmt bei jeder iteration die laenge der returnliste auf
        return valid_bag_lst # wenn die letzte und vorletzte liste gleich lang sind, dann brich ab
            # achtung: valid_bag_lst ist immer ein neuer und aktueller input
    else:
        for line in data:
            for i in range(len(valid_bag_lst)):
                if valid_bag_lst[i] in line:
                    splitted_line = line.split()
                    if not (splitted_line[0] + splitted_line[1] == valid_bag_lst[i]): # wenn die ersten zwei woerter nicht das gesuchte bag sind, man moechte nur enthaltene bags
                        next_bag_layer_lst.append(splitted_line[0]+" "+splitted_line[1])   

        new_list = list(set(next_bag_layer_lst + valid_bag_lst))
        len_list.append(len(new_list))
        return get_valid_bag(data, new_list) # meine erste listenrekursion


def count_bags_inside(data, valid_bag_lst):
    count = 0
    for l in range(len(data)):
        for entry in valid_bag_lst:
            if entry in data[l]:
                count += 1
                data[l] = "empty"
    return count

#-----------------------part2----------------------#
def get_bag_content(data, bag):
    splitted_string_bag = bag.split() # tasche in "shiny" und "gold" aufteilen
    for line in data:
        splitted_line = line.split() # zeile im datensatz wird aufgeteilt
        if splitted_line[0] == splitted_string_bag[0] and splitted_line[1] == splitted_string_bag[1]: # such die tasche am anfang jeder zeile in der liste
            split_by_colon = line.split(":")
            inside_bag = split_by_colon[1].split(",")
            for i in range(len(inside_bag)):
                if inside_bag[i][0] == " ":
                   inside_bag[i] = inside_bag[i].replace(" ", "", 1)
                if inside_bag[i][-1] == " ":
                   inside_bag[i] = inside_bag[i][:-1]

    return inside_bag # alles was in der tasche ist als eine saubere liste mit der man arbeiten kann


# formula = lambda x, n : x + x*n

# erster bag_content ist hier: [' 5 mirrored crimson', ' 5 mirrored tan', ' 5 drab green', ' 5 shiny silver']
# def content_count_1(data, bag_content, bags_content_list = []):
#     bags_content_list.append(bag_content)
    
#     # print(bag_content)
#     for entry in bag_content:
#         contents = entry.replace(" ","",1) # von leerzeichen säubern
#         contents = contents.split(" ", 1)
#         # counting_bags += int(contents[0]) # summiert über alle taschenanzahlen in der jeweiligen tasche
        
#         for line in data:
#             splitted_line = line.split(":")
#             if contents[1] in splitted_line[0] and not "no other" in splitted_line[1]:
#                 print(line)

#                 content_count_1(data, get_bag_content(data, contents[1]), bags_content_list)
#                 break
#             elif contents[1] in splitted_line[0] and "no other" in splitted_line[1]:
#                 print(line)

#                 content_count_1(data, get_bag_content(data, contents[1]), bags_content_list)
#                 break
#     return bags_content_list
        
# hier nochmal die gleiche funktion

# def content_count(data, bag_content, level_new_number = 0, heritage = 0):
#     for entry in bag_content:
#         print(entry)
#         print(level_new_number)
#         contents = entry.split(" ", 1) # erstes leerzeichen als trennzeichen
#         upper_level_number = int(contents[0])
#         upper_level_bag = contents[1]
#         # if heritage == 0:
#         #     level_new_number += upper_level_number
#         # else:
#         #     level_new_number += upper_level_number*heritage
#         heritage = level_new_number
#         # hol den tascheninhalt einer tasche aus dem bag_content
#         inner_bags = get_bag_content(data, upper_level_bag)
#         # print(inner_bags)
#         if not "no other" in inner_bags: # ist die tasche am beginn der zeile von data und die tasche nicht leer dann...
#             for inner_bag_entry in inner_bags:
#                 sub_content = inner_bag_entry.split(" ", 1) # erstes leerzeichen als trennzeichen
#                 lower_level_number = int(sub_content[0])
#                 lower_level_bag = sub_content[1]
#                 # print(upper_level_number)
#                 # print(lower_level_number)
#                 # level_new_number += upper_level_number*lower_level_number
#                 # print(level_new_number)
#             # print("content_count has been called")
#             # im ersten durchlauf bei test_7.txt level_new_number = 8
#                 level_new_number += content_count(data, get_bag_content(data, upper_level_bag), level_new_number, heritage)

#         elif "no other" in inner_bags:
#             # pass
#             print("the end")

#     return level_new_number

def try_count(data, bag_content, upper_bag_num = 0, lnn = 0):
    for entry in bag_content:
        print(lnn)
        print(entry)
        contents = entry.split(" ", 1) # erstes leerzeichen als trennzeichen
        entry_num = int(contents[0])
        entry_bag = contents[1]
        if upper_bag_num == 0:
            lnn += entry_num
            # print(lnn , "first layer")
            if not "no other" in get_bag_content(data, entry_bag):
                lnn += entry_num*try_count(data, get_bag_content(data, entry_bag), entry_num, lnn)
            else:
                print("the end")
        else:
            # print(entry_num, "deeper layer")
            if not "no other" in get_bag_content(data, entry_bag):
                print("XOXO")
                lnn += entry_num*try_count(data, get_bag_content(data, entry_bag), entry_num, lnn)
            # elif "no other" in get_bag_content(data, entry_bag):
            #     print(entry_num, "return value")
    return lnn


def main():
    data = read_data("test_7.txt") # data ist schon eine liste
    cleaned_data = listcreater(data, None, "\n", "") # mit listcreater werden alle unnötigen chars entfernt
    cleaned_data = listcreater(cleaned_data, None, "contain", ":")
    cleaned_data = listcreater(cleaned_data, None, " bags", "")
    cleaned_data = listcreater(cleaned_data, None, " bag", "")
    cleaned_data = listcreater(cleaned_data, None, ".", "")
    # print(cleaned_data)
    #------------------part1-------------------
    # valid_bag_lst = ["shiny gold"]
    # valid_bags = get_valid_bag(cleaned_data, valid_bag_lst)
    # valid_bags.remove("shiny gold") # entferne shiny gold bag aus der suchliste weil shiny gold bag nicht in sich selbst enthalten sein soll

    # print(count_bags_inside(cleaned_data, valid_bags))
    #------------------part2-------------------
    shiny_gold_bag_content = get_bag_content(cleaned_data, "shiny gold")
    content = try_count(cleaned_data, shiny_gold_bag_content)
    print(content)
    # bag_content = get_bag_content(cleaned_data,"dotted black")
    # print(bag_content)
    # print(taschen_anzahl_ast(content, len(content)-1))

if __name__ == "__main__":
    main()