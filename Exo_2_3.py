def anagrammes(chaine1:str, chaine2:str) -> bool:
    l1 = len(chaine1)
    l2 = len(chaine2)
    res = False

    if l1 == l2:
        ch1tri = sorted(chaine1)
        ch2tri = sorted(chaine2)
        if ch1tri == ch2tri:
            res = True
    return res

#Tests
assert anagrammes('chien', 'niche') == True
assert anagrammes('énergie noire', 'reine ignorée')
assert not anagrammes('louve', 'poule')