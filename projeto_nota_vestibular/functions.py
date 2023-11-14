def mediaHumanas(nota_ch, nota_ex, nota_cn, nota_cl, nota_red):
    var_media = ((nota_ch * 4) + (nota_ex * 1) + (nota_cn * 1) + (nota_cl * 2) + (nota_red * 2)) / (4 + 1 + 1 + 2 + 2)
    return var_media

def mediaExatas(nota_ch, nota_ex, nota_cn, nota_cl, nota_red):
    var_media = ((nota_ch * 1) + (nota_ex * 4) + (nota_cn * 1) + (nota_cl * 2) + (nota_red * 2)) / (1 + 4 + 1 + 2 + 2)
    return var_media

def mediaNatureza(nota_ch, nota_ex, nota_cn, nota_cl, nota_red):
    var_media = ((nota_ch * 1) + (nota_ex * 1) + (nota_cn * 4) + (nota_cl * 2) + (nota_red * 2)) / (1 + 1 + 4 + 2 + 2)
    return var_media

def mediaLinguistica(nota_ch, nota_ex, nota_cn, nota_cl, nota_red):
    var_media = ((nota_ch * 2) + (nota_ex * 1) + (nota_cn * 1) + (nota_cl * 4) + (nota_red * 2)) / (2 + 1 + 1 + 4 + 2)
    return var_media
