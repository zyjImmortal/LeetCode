from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass

class AlbumSection(Section):

    def describe(self):
        print('Album section')

