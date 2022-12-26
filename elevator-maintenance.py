# turn a string into a tuple containing elevator version numbers
def make_tuple(s):
    # split input by '.' characters
    version_strings = s.split('.')

    # if version_strings has missing entries, fill with '-1'
    version_strings += ['-1'] * (3 - len(version_strings))

    # return tuple with numerical conversions of entries
    return tuple([int(x) for x in version_strings])


def solution(l):
    # use the make_tuple function as a key and use Python's inbuilt tuple sorting
    l.sort(key=make_tuple)
    return l
