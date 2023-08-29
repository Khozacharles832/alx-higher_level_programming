#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        printed = fct(*args)
        return (printed)
    except Exception as error:
        error_message = "Exception: {}\n".format(error)
        import sys
        sys.stderr.write(error_message)
        return None
