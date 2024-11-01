# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from itertools import combinations

def all_variants(text):
    lis = []
    for i in range(1, len(text)+1):
        lis = []
        b = combinations(text, i)
        lis.extend(b)
        for j in lis:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    if i == 'ac':
        continue
    print(i)

