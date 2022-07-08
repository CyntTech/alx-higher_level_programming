#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def find_search(uc):
        return uc if uc != search else replace
    return list(map(find_search, my_list))
