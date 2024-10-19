def safe_print_integer(value):
    """
    function that prints an integer with "{:d}".format().

    Args:
        value: The value to be printed

    return:
        True: if the value is an integer else return False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
