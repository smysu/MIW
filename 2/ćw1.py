def funkcja(a_list, b_list):
    if len(a_list) < len(b_list) or len(a_list) == len(b_list):
        c_list = []
        for i in range(len(b_list)):
            if i < len(a_list):
                if i % 2 == 0:
                    c_list.append(a_list[i])
            if i % 2 == 1:
                c_list.append(b_list[i])
        return c_list
    else:
        c_list = []
        for i in range(len(a_list)):
            if i % 2 == 0:
                c_list.append(a_list[i])
            if i < len(b_list):
                if i % 2 == 1:
                    c_list.append(b_list[i])
        return c_list


print(funkcja([0, 1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15, 16, 17, 18]))
