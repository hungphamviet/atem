""" This function checks if all elements in the given lst is monotonically increasingly, returns None if it is.
 Otherwise returns the first element that violates the rule
  For example, [1, 2, 3, 5, 7, 7, 8, 10] will return None
               [1, 3, 4, 7, 5, 8, 10, 9] will return 7

    If reverse is True, it will check if lst is monotonically decreasingly instead
"""


def find_bad_element_from_monotonically_increasing_list(lst, reverse=False):
    prev = lst.pop(0)   # Pop out the first element from the lst and store it to prev
    for e in lst:       # At this point lst does not have the first element
        if (not reverse and e < prev) or (reverse and e > prev):  # Even if e is string, python can handle the comparison correctly
            return prev
        prev = e
    return None


def str2bool(s):
    return s.lower() in ("true", "yes", "t", "1", "is")


def is_str_none(s):
    return s in ("None", "none")


def status_str2bool(status):
    return status.strip().lower() in ('active', 'activated', 're-activated', 'on', 'enable', 'displayed')


def extract_digits_from_str(s):
    import re
    return re.findall(r'\d+', s)


def ordinal_str_to_indexes(s):
    ordinal_nums = extract_digits_from_str(s)
    return [int(num)-1 for num in ordinal_nums]


def ordinal_str_to_single_index(s):
    return ordinal_str_to_indexes(s)[0]


def table_to_str(table):
    result = ''
    if table.headings:
        result = '|'
    for heading in table.headings:
        result += heading + '|'
    result += '\n'
    for row in table.rows:
        if row.cells:
            result += '|'
        for cell in row.cells:
            result += cell + '|'
        result += '\n'
    return result


def table_to_dictionary(table):
    if table is None:
        raise NameError('Key/value table is required')
    result = {}
    for row in table:
        result[row[0]] = row[1]
    return result
