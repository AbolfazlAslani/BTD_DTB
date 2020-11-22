def decimal_to_binary(d):
    kharej_ghesmat = 1
    baghi_mande = []
    answer = ""
    while kharej_ghesmat != 0 :
        kharej_ghesmat = d // 2
        baghi_mande.append(d % 2)
        d = kharej_ghesmat
    for i in baghi_mande:
        answer = str(i) + answer
    return answer
