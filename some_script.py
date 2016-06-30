from orm.models import User
from uuid import uuid4

def main():
    user = User()
    user.guid = uuid4()
    # requests.post('http://google.com/?q=omg-some-really-long-annoying-string', header={'Content-type': 'application/json'})
    pass

if __name__ == '__main__':
    main()