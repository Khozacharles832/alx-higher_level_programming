#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        error_message = "Exception: {}\n".format(error)
        import sys
        sys.stderr.write(error_message)
        return False
