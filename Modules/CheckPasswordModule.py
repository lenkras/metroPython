def test_me(password):
    pass_length = len(password)
    only_letters = password.isalpha()
    only_num = password.isdigit()
    if pass_length < 6 or only_letters or only_num:
        return False
    if pass_length > 6 and password != only_letters and password != only_num:
        return True
