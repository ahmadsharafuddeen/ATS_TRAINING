def do_stuff(num=0):
    try:
        if int(num) <= 0:
            return 'Value must be greater than 0'
        return int(num) + 5
    except ValueError as err:
        return err
    except TypeError as err:
        return err