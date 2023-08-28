def raise_exception():

    try:
        raise TypeError()
    except TypeError as e:
        print("Exception raised", e)
