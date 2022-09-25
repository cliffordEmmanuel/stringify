def get_raw_objects():
    # standard input only for now
    # this method gets the input from the stdin and
    # returns everything into a big string

    raw = input("Enter the objects: ")

    return raw


def get_seperator():
    separator = input("Enter your preferred delimeter(',','|',';','n'): ")
    return separator


def stringify(raw: str, separator: str = ",") -> str:
    """Converts a raw list of objects into their string versions.

    Args:
        raw (str): assumes that the input is a big string of the objects combined.
        separator (str, optional): the character to be used as a delimeter. Defaults to ','.

    Returns:
        str: a 'stringified' version of the delimited objects.
    """

    # TODO: a way to detect the separator used
    # assume the standard separators(spaces, comma, semicolon, pipe, new line)
    # and use that to split this big string into a list
    # but that depends on the source of the input
    def detect_separator(raw: str):
        default_separators = [" ", ",", "|"]
        pass

    if separator == "n":
        separator = "\n"

    # for now assume they are separated by the space character
    splitted = raw.split()
    # the str.split function always returns a list of string versions.

    stringified = separator.join(splitted)

    return stringified


# for test
"""
130503 132989 229778 220800 247181 229777 248570 231070 234120 233068 228579 136038
"""


def main():
    # get raw objects from standard input
    raw = get_raw_objects()
    # get delimeter choice
    separator = get_seperator()
    # stringify
    stringified = stringify(raw, separator)
    # output to standard output
    print(stringified)


if __name__ == "__main__":
    main()
