
def verificacao(email):
    
    qntd_arroba = email.count('@')
    if qntd_arroba != 1 or '.' not in email:
        return False
    
    divisao_email = email.split('@')
    if divisao_email[0].startswith('-') or divisao_email[1].endswith('-'):
        return False
    
    tam_email = len(email)
    if tam_email < 2 or tam_email > 63:
        return False
    
    else:
        return True