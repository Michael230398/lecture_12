import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as numbers_file:
        data = csv.reader(numbers_file, delimiter="\t")
        for row in data:
            number_row = []
            for i in row:
                i = int(i)
                number_row.append(i)
    return number_row



def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as numbers_file:
        data = csv.reader(numbers_file, delimiter=",")
        for idx, row in enumerate(data):
            if idx == row_number:
                number_row = []
                for i in row:
                    i = int(i)
                    number_row.append(i)
    return number_row




def selection_sort(number_array, direction = "ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    n = len(number_array)
    for i in range(n-1):
        idx = i
        for num in range(i + 1, n):
            if direction == "asceding":
                if number_array[idx] > number_array[num]:
                    idx = num
            elif direction == "descending":
                if number_array[idx] < number_array[num]:
                    idx = num
        number_array[i], number_array[idx] = number_array[idx], number_array[i]
    return number_array



def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """



def main():
    # Ukol: Selection Sort
    row = read_row("numbers_one.csv")
    print(row)

    # Ukol: Selection Sort - se smerem razeni
    sorted_data = selection_sort(row)
    print(sorted_data)
    sorted_data = selection_sort(row, "descending")
    print(sorted_data)

    rows = read_rows("numbers_two.csv", row_number=2)
    print(rows)

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

