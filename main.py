def dori_baza(dori_nomi):
    dori_nomi = dori_nomi.lower() 
    
    if dori_nomi == "paratsetamol":
        return "Bosh og'rig'i va isitmani tushirish uchun ishlatiladi."
    elif dori_nomi == "ibuprofen":
        return "Yallig'lanishga qarshi va og'riq qoldiruvchi vosita."
    elif dori_nomi == "amoksitsillin":
        return "Bakterial infeksiyalar uchun antibiotik."
    elif dori_nomi == "tsiprofloksatsin":
        return "Bakterial infeksiyalar, ayniqsa siydik yo'llari infeksiyalari uchun ishlatiladi."
    elif dori_nomi == "loratadin":
        return "Allergiya va burun oqishini kamaytiruvchi antihistamin."
    elif dori_nomi == "omeprazol":
        return "Qorinda kislotalilikni kamaytiruvchi dori."
    elif dori_nomi == "metformin":
        return "Qandli diabet bilan kasallangan bemorlarda qand darajasini tushirish uchun ishlatiladi."
    elif dori_nomi == "aspirin":
        return "Qon ivishini oldini olish va og'riqni kamaytirish uchun ishlatiladi."
    elif dori_nomi == "azitromitsin":
        return "Turli bakterial infeksiyalar uchun antibiotik."
    elif dori_nomi == "lizinopril":
        return "Qon bosimini tushirish uchun ishlatiladi."
    elif dori_nomi == "atorvastatin":
        return "Qonda xolesterin miqdorini kamaytiruvchi dori."
    elif dori_nomi == "klopidogrel":
        return "Qon ivishini oldini olish uchun ishlatiladi."
    elif dori_nomi == "furosemid":
        return "Suyuqlik to'planishini kamaytiruvchi diuretik."
    elif dori_nomi == "prednizolon":
        return "Yallig'lanishga qarshi steroid dori."
    elif dori_nomi == "setirizin":
        return "Allergiya alomatlarini kamaytiruvchi antihistamin."
    elif dori_nomi == "doksitsiklin":
        return "Bakterial infeksiyalar uchun antibiotik."
    elif dori_nomi == "salbutamol":
        return "Astma va nafas olish qiyinchiliklarini yengillashtiruvchi bronxodilatator."
    elif dori_nomi == "lozartan":
        return "Qon bosimini tushirish uchun ishlatiladi."
    elif dori_nomi == "gabapentin":
        return "Asab og'riqlarini kamaytirish va epilepsiyani nazorat qilish uchun ishlatiladi."
    elif dori_nomi == "levotiroksin":
        return "Gipotireoz (qalqonsimon bez yetishmovchiligi)ni davolash uchun ishlatiladi."
    else:
        return "Bunday dori bazada mavjud emas."
    # Ma'lumotlar ChatGPT dan olindi
    
dori = input("Dorini nomini kiriting: ")
dori_malumoti = dori_baza(dori)
print(dori_malumoti)
