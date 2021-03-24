from datetime import datetime

id=1

class Post(object):
    def __init__(self,contingut):
        global id
        self.contingut=contingut
        self.id=id
        id+=1
        date=datetime.now()
        self.__date=date.strftime("%c")
        
    
    
    def __str__(self):
        return "Post ID: " + str(self.id) + " // Info: " + self.contingut + " // Date: " + self.__date

class Usuari(object):
    def __init__(self,nick,email,password):
        """
        >>> u=Usuari('F',3456,19867)
        >>> u.nick
        'F'
        >>> u.email
        3456
        """
        self.nick=nick
        self.__email=email
        self.__password=password

    def getEmail(self):
        """
        >>> p1=Usuari("john24","john24@gmail.com","abracadabra")
        >>> p1.getEmail()
        'john24@gmail.com'
        """
        return self.__email
        

    def getPassword(self):
        """
        >>> p1=Usuari("john24","john24@gmail.com","abracadabra")
        >>> p1.getPassword()
        'abracadabra'
        """
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

class Hashtag(object):
    def __init__(self,id):
        self.id=id


class iTICApp(object):
    def __init__(self):
        self.__usuaris={}
        self.__posts={}
        self.__hashtags={}
    
    def getUsuaris(self):
        return self.__usuaris
    
    def afegeix_usuari(self,nick,email,password):
        self.__usuaris['Usuari']= nick
        if nick in self.getUsuaris():
            print('Nick not available')
        else:
            print('Nick available')

    def getHashtag(self):
        return self.__hashtags

    def afegeix_hashtags(self,id):
        self.__hashtags['Hashtag id']= id
        print('Available', self.getHashtag())

    def getPosts(self):
        return self.__posts

    def publicar_post(self,nick,id_hashtag,contingut_post):
        if nick in self.getUsuaris():
            self.__posts['Usuari: ', 'Hashtags: ', 'Info: ']= nick, id_hashtag, contingut_post
            return True
        else:
            return False

    def users(self):
        return self.getPosts()

    def posts(self):
        for k in reversed(list(self.getPosts())):
            print(k)

    def __str__(self):
        return 'Usuari: ' +  + ' Email: ' +  + ' Encripted password: ' +  + '\n' + ' Published posts: ' +  + '\n' + ' Post id: ' +  + 'info:' +  + ' Date: ' +  + ' Nick user: ' +  + ' Available hashtags: ' +



    
if __name__=='__main__':
    i=iTICApp()
    i.afegeix_usuari("pere","pere@gmail.com","gilisticoexpia")
    i.afegeix_hashtags("adventure")
    i.publicar_post("pere","winter","into the wild")
