
def load_data():
    cred = []
    default = ("root","root","localhost")
    try:
        f = open("cred/cred.json",'r')
        data = eval(f.read())
        
        for i in data.keys():
            cred.append(data[i])
    except Exception :
        return default 
    
    return tuple(cred)

#print(load_data())

# store database name
def set(dbname):
    global  user
    user = dbname


def get():
    return user

# print the tname
def tset(Tname):
    global  tname
    tname = Tname

def tget():
    return tname

# import datetime as dt
# def current_datetime():
#     return f"{dt.datetime.now().date()}[{dt.datetime.now().time().replace(microsecond=0)}]"
   

# print(current_datetime())
