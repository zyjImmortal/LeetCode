from abc import ABCMeta, abstractmethod


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Animal(metaclass=ABCMeta):
    """
    定义一个抽象接口，一个抽象方法
    """

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow~~~")


class Cat(Animal):
    def do_say(self):
        print('MIAO MIAO')


class ForestFactory:
    @classmethod
    def make_sound(cls, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    # single = Singleton()
    # single1 = Singleton()
    # print(id(single))
    # print(id(single1))
    ForestFactory.make_sound('Dog')
