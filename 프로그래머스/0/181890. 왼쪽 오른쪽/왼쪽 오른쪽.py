def solution(str_list):
    if "l" in str_list and "r" in str_list:
        l_idx = str_list.index("l")
        r_idx = str_list.index("r")
        return str_list[:l_idx] if l_idx < r_idx else str_list[r_idx + 1:]
    elif "l" in str_list:
        l_idx = str_list.index("l")
        return str_list[:l_idx]
    elif "r" in str_list:
        r_idx = str_list.index("r")
        return str_list[r_idx + 1:]
    else:
        return []