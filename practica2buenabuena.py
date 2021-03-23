class Usuari(object):
    def __init__(self,nick,email,password):
        self.nick=nick
        self.__email=email
        self.__password=password

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def setNick(self,u):
        self.nick=n

    def setPassword(self,p):
        self.__password=p

    def setEmail(self,e):
        self.__email=e

    def __str__(self):
        return 'Usuari: ' + self.nick + ' Email: ' + self.getEmail() + ' Encripted password: ' + self.getPassword()

    def __eq__(self,other):
        return self.nick==other.nick

class Post(object):
    def __init__(self,date,id,contingut):
        self.__date=date
        self.id=id
        self.contingut=contingut

    def getDate(self):
        return self.__date

class Hashtag(object):
    def __init__(self,id):
        self.id=id


class iTICApp(object):
    def __init__(self):
        self.c=[]
    
    
if __name__=='__main__':
    p1=Usuari("john24","john24@gmail.com","abracadabra")
    p2=Usuari("johh24","john244@gmail.com","patadecabra")
    print(p1)
    print (p2)
    p3=Usuari("john24","john2444@gmail.com","supercalifra")
    print (p3.nick)
    p1==p3

