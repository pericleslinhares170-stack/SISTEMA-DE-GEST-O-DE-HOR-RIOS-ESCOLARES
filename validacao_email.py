
def verificacao(email):
    
    qntd_arroba = email.count('@')
    if qntd_arroba != 1 or '.' not in email:
        return False
    
    divisao_email = email.split('@')
    if divisao_email[0].startswith('-') or divisao_email.endswith('-'):
        return False
    
    if email.count() < 2 or email.count() > 63:
        return False
    
    else:
        return True