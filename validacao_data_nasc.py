from datetime import datetime

def certification(data_nas):
  data_div = data_nas.split('/')
  data_int = [int(data) for data in data_div]
  if data_int[2] >= datetime.now().year: 
    return False

  if data_int[2] % 4 == 0 and (data_int[2] % 100 != 0 or data_int[2] % 400 == 0):
    if data_int[1] == 1 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True

    elif data_int[1] == 2 and (data_int[0] >= 1 and data_int[0] <= 29):
      return True

    elif data_int[1] == 3 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True
    
    elif data_int[1] == 4 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True

    elif data_int[1] == 5 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True
    
    elif data_int[1] == 6 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True

    elif data_int[1] == 7 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True 

    elif data_int[1] == 8 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True 

    elif data_int[1] == 9 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True 

    elif data_int[1] == 10 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True

    elif data_int[1] == 11 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True

    elif data_int[1] == 12 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True

    else:
      return False

  else:
    if data_int[1] == 1 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True

    elif data_int[1] == 2 and (data_int[0] >= 1 and data_int[0] <= 28):
      return True

    elif data_int[1] == 3 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True
    
    elif data_int[1] == 4 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True

    elif data_int[1] == 5 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True
    
    elif data_int[1] == 6 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True

    elif data_int[1] == 7 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True 

    elif data_int[1] == 8 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True 

    elif data_int[1] == 9 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True 

    elif data_int[1] == 10 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True

    elif data_int[1] == 11 and (data_int[0] >= 1 and data_int[0] <= 30):
      return True

    elif data_int[1] == 12 and (data_int[0] >= 1 and data_int[0] <= 31):
      return True

    else:
      return False