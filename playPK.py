from PK import *

msg = "welcome………… "
if __name__ == "__main__":
    print(msg)
    milo = Hero('milo')
    bo = Element('bo')
    print(bo.hp)
    milo.hit(bo)
    print(bo.hp)