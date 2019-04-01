from orm import model
from sqlalchemy.orm import sessionmaker
from hashlib import md5

session = sessionmaker()()

def insertuser(user,account,password):
    secret = md5()
    password = password.encode("utf8")
    secret.update(password)
    password = secret.hexdigest()
    u = model.User(username = user,account=account,pwd = password)
    result = session.query(model.User.id).filter(model.User.username == user).first()
    if result == None:
        session.add(u)
        session.commit()
        session.close()
        return True
    else:
        result = str(result[0])
        if result:
            return False
        else:
            session.add(u)
            session.commit()
            session.close()
            return True

def checkuser(account,password):
    secret = md5()
    password = password.encode("utf8")
    secret.update(password)
    password = secret.hexdigest()
    result = session.query(model.User.username).filter(model.User.account == account).filter(model.User.pwd == password).first()
    result = result[0]
    if result:
        return result
    else:
        return -1

def insertservice(project,describe,building,unit,roomnum,username,tel):
    building = int(building)
    unit = int(unit)
    roomnum = int(roomnum)
    print(project,type(project))
    u = model.Service(project =project,describe = describe,building = building,unit = unit,roomnum = roomnum,username = username,tel = tel)
    session.add(u)
    session.commit()
    session.close()
    return 0

def viewservice(username):
    result = session.query(model.Service).filter(model.Service.username == username).all()
    return result

def delservice(id):
    session.query(model.Service).filter(model.Service.id ==id).delete()
    session.commit()