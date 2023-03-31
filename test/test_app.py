from lab7 import check_type, check_name, check_name_len, check_sid_len


def test_check_type():
    assert check_type() == False
    assert check_type('test') == True

    try:
        check_type(123)
    except TypeError:
        assert True
    else:
        assert False

    myname = "john"
    myID = 123456789
    assert check_type(myname, myID) == True

    myID2 = "123456789"
    assert check_type(myname, myID2) == True

    myID3 = "123456789a"
    assert check_type(myname, myID3) == False

    myID4 = "a_john"
    assert check_type(myname, myID4) == False

    assert check_name("abc") == True
    assert check_name("\xaa\xaa") == True
    assert check_name("\xaa \xaa") == True
    assert check_name("\xaa \xfa ") == False

    assert check_name_len("abc") == True
    assert check_name_len("abc abc") == True
    assert check_name_len("\xaa\xaa") == True
    assert check_name_len("\xaa \xaa") == True
    assert check_name_len("abc abc abc abc abc a") == False
    assert check_name_len("\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa") == True
    assert check_name_len("\xaa\xaa\xaa\xaa\xaa \xaa\xaa\xaa\xaa\xaa") == False

    assert check_sid_len("1155") == False
    assert check_sid_len("1155111111") == True
    assert check_sid_len("115511111 ") == False
    assert check_sid_len(115511111) == False
    assert check_sid_len(1155111111) == True
    assert check_sid_len("1155 11111") == False
