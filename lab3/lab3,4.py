def translate(word):
    ug = {
        "happy": "баяртай",
        "sad": "гашуун",
        "yes": "тийм",
        "no": "үгүй",
        "love": "хайр",
        "friend": "найз",
        "family": "гэр бүл",
        "peace": "энх тайван",
        "thank you": "баярлалаа",
        "goodbye": "баяртай",
        "help": "туслах",
    }
    
    ugm = {m: e for e, m in ug.items()}  
    if word in ug:
        return ug[word]
    elif word in ugm:
        return ugm[word]
    else:
        return "Уучлаарай, үгийн санд байхгүй байна"

t = input("Үг оруул нь уу: ")
tr = translate(t)

print(tr)
