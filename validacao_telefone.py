def validacao(telefone):
    ddd_inexi = ['00','01','02','03','04','05','06','07','08','09','10','20','23','25','26','29','30','39','40','50','52','56','57','58','59','60','70','72','78','80','90']
    ddd_telefone = telefone.split(' ')
    
    if ddd_telefone[0] in ddd_inexi:
        return False
    if len(ddd_telefone[1]) != 9:
        return False
    else:
        return True