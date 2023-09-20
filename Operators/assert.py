# assert isinstance(34, int)
from string import digits, ascii_lowercase, ascii_uppercase

def password_strength_check(psw: str) -> str:
    if len(psw) < 8:
        return "Too Weak"
    def getFlagArr(kit: list[str], line: str):
        return list(char in kit for char in line)
    df = getFlagArr(digits, psw)
    dlow = getFlagArr(ascii_lowercase, psw)
    dup = getFlagArr(ascii_uppercase, psw)
    
    if any([all(df), all(dlow), all(dup)]):
        return "Weak"
    
    if any([not any(df), not any(dlow), not any(dup)]):
        return "Good"
    
    return "Very Good"

    # if any(df) and any(dlow) and any(dup):
    #     return "Very Good"

if __name__ == "__main__":
    # assert Не используем в коде проектов только в тестах
    assert password_strength_check('') == 'Too Weak'
    assert password_strength_check('1234567') == 'Too Weak'
    assert password_strength_check('dsadfdf') == 'Too Weak'
    assert password_strength_check('AAa231S') == 'Too Weak'
    assert password_strength_check('QAaa1') == 'Too Weak'

    assert password_strength_check('12523611372732163') == 'Weak'
    assert password_strength_check('123321123') == 'Weak'
    assert password_strength_check('gfdsdgfgdfgdfg') == 'Weak'
    assert password_strength_check('sfddsfdsf') == 'Weak'
    assert password_strength_check('DSSDFGSHYHHFHGFD') == 'Weak'
    assert password_strength_check('DGGGDDGSGD') == 'Weak'
    assert password_strength_check('GFDDFFDDFGFHG') == 'Weak'

    assert password_strength_check('12213dfgfdsgf') == 'Good'
    assert password_strength_check('12321323DSSDFSGF') == 'Good'
    assert password_strength_check('FDSDFDFSFSFDdsfgdgf') == 'Good'
    assert password_strength_check('dfdsfDSFFfdfd') == 'Good'
    assert password_strength_check('2323FSDF2332') == 'Good'
    assert password_strength_check('DSDDSdfsfFdSF') == 'Good'

    assert password_strength_check('123234dsghajfdsaJHHHHksald') == 'Very Good'
    assert password_strength_check('kFJJFIdsfidsfj324243') == 'Very Good'
    assert password_strength_check('121284396532974765hJ') == 'Very Good'
    assert password_strength_check('1212HHH2138HHHdjsdk') == 'Very Good'
    assert password_strength_check('kjldfgkdsfgjkhsdfD1') == 'Very Good'
    assert password_strength_check('DSAHJADSKJHDSAJHDS1j') == 'Very Good'
