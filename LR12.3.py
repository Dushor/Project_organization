class Staff:
    def __init__(self):
        pass

    def register(self):
        pass

    def unregister(self):
        pass

    def notifyAll(self):
        pass


class ProgForum(Staff):
    def __init__(self):
        self._listOfUsers = []
        self.postname = None

    def register(self, userObj):
        if userObj not in self._listOfUsers:
            self._listOfUsers.append(userObj)

    def unregister(self, userObj):
        self._listOfUsers.remove(userObj)

    def notifyAll(self):
        for objects in self._listOfUsers:
            objects.notify(self.postname)

    def Write_the_code(self, postname):
        self.postname = postname
        self.notifyAll()


class Client:
    def __init__(self):
        pass

    def notify(self):
        pass


class User1(Client):
    def notify(self, postname):
        print('User1 has not been notified of new codes {0}'.format(postname))


class User2(Client):
    def notify(self, postname):
        print('User2 has not been notified of new codes {0}'.format(postname))


class SoftSites(Client):
    def __init__(self):
        self._sisterWebsites = ['Soft1', 'Soft2', 'Soft3']

    def notify(self, postname):
        for site in self._sisterWebsites:
            print('A notification has been sent to the client : {0}'.format(site))


if __name__ == '__main__':
    progForum = ProgForum()
    user1 = User1()
    user2 = User2()
    sites = SoftSites()
    progForum.register(user1)
    progForum.register(user2)
    progForum.register(sites)
    progForum.Write_the_code('Observer Pattern in Python')
    progForum.unregister(user2)
    progForum.Write_the_code('MVC Pattern in Python')
