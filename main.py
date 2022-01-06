
import re
from copy import deepcopy
import itertools

"""==================================== LIST ===================================="""


def reversed_tom(liste: list) -> list:
    """
    Return the reversed list.
    :param liste: list to be returned
    :return: returned list
    """
    liste.reverse()

    return liste


"""==================================== HTML ===================================="""


def tag(tag_name: str, **attributes: str) -> str:
    """
    Return a tag with all the parameters needed.
    :param tag_name: Name of the tag.
    :param attributes:
    :return:
    """
    attribute_list = [
        f'{name}="{value}"' for name, value in attributes.items()
    ]
    return f"<{tag_name} {' '.join(attribute_list)}>"


def removeHtmlTag(text) -> str:
    """
    This function only returns the text content inside an HTML tag.
    :param text: str. The full HTML tag.
    :return: The text content of an HTML tag.
    """
    text = str(text)

    if text == '':
        return 'empty'

    if rep := re.match('(.*?)(<.*?>)(.*?)', text):
        text = text.replace(rep.group(2), '')
    if '<' in text and '>' in text:
        return removeHtmlTag(text)

    return text


def findInHtmlTag(text, attribute) -> str:
    """
    Returns the value of the argument passed as argument of the tag passed as argument
    :param text: Whole tag.
    :param attribute: Attribute needed.
    :return: The attribute value.
    """

    if rep := re.match(f'(<.*?{attribute}=")(.*?)(".*)', str(text)):
        return rep.group(2)
    return f"{attribute} attibute not in {text}"


"""==================================== MATRICES ===================================="""


def permute(*args, **kwargs):
    """
    Allows you to exchange :
    - either two lists with the same index in the same matrix.
    - or two lists of different indexes of a matrix.
    - or the lists of same index of two different matrices.
    - or two lists of different indexes of two different matrices.
    :param args: Either one or two matrices.
    :type args: list[list[int]]
    :param kwargs: Either one or two indexes :
            - if one, it will be named "index.
            - if two, they will be named "index_1" and "index_2.
    :type kwargs: int
    :return: Either the processed matrix or the two processed matrices.
    """
    assert 1 <= len(args) <= 2
    assert 1 <= len(kwargs) <= 2
    if len(args) == 1:
        index_1 = kwargs.get("index_1", None)
        index_2 = kwargs.get("index_2", None)

        print(index_1)
        print(index_2)

        temp_matrix = deepcopy(args[0])

        args[0][index_1] = temp_matrix[index_2]
        args[0][index_2] = temp_matrix[index_1]

        return args[0]

    index = kwargs.get("index", None)
    index_1 = kwargs.get("index_1", None)
    index_2 = kwargs.get("index_2", None)

    if index:
        temp_matrix = deepcopy(args[0])

        args[0][index] = args[1][index]
        args[1][index] = temp_matrix[index]

        return args[0], args[1]

    temp_matrix = deepcopy(args[0])

    args[0][index_1] = args[1][index_2]
    args[1][index_2] = temp_matrix[index_1]

    return args[0], args[1]


def show_matrix(matrix: list) -> None:
    """
    Show a matrix with the numbers alligned.
    :param matrix: Matrix needed to be shown.
    :type matrix: list
    :return: Nothing, it just prints
    :rtype: None
    """
    flatten_matrix = list(itertools.chain.from_iterable(matrix))
    len_max_value = max([len(str(elem)) for elem in flatten_matrix])

    for line in matrix:
        print('|', end='')
        for i, value in enumerate(line):
            space_needed = len_max_value - len(str(value)) + 1
            space = " " * space_needed
            print((f"{value} " if value < 0 else f" {value}"), end = space)
        print('|', end='')
        print()


if __name__ == '__main__':
    """====== HTML EXEMPLES ======"""
    # tag function ======
    print(tag('a', href = "https://github.com/TomPlanche"))
    tagExemple = tag('img', height = '20px', width = '40px', src = "face.jpg")
    print(tagExemple)

    # findInHtmlTag function ======
    print(findInHtmlTag(tagExemple, "src"))

    # show_matrix function ======
    m1 = [
        [1, 2, 3],
        [13, 14, 15],
        [7, 8, 9]
    ]
    show_matrix(m1)
