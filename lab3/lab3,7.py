# def ner(ner1, ovog):
#     return f"{ovog} овогтой {ner1}"
# ner1 = "Зоригтбаатар"
# ovog = "Пүрэв-Очир"
# print(ner(ner1, ovog))


# def ner(nere, ovog):
#     return f"{ovog[0]}.{nere}"
# nere = "Зоригтбаатар"
# ovog = "Пүрэв-Очир"
# print(ner(nere, ovog))


def re(udur):
    return f"20{udur[2:4]}-{udur[5]}-{udur[6:8]}"
reg = "УО05292119"
udr = re(reg)
print(udr)
