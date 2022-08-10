from abc import ABCMeta, abstractmethod, ABC
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    def __init__(self, data, filename):
        self.data = data
        self.__filename = None
        self.filename = filename

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class SerializeJson(SerializationInterface):
    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        parse = filename.split('.')
        if parse[1] == 'json':
            self.__filename = filename
        else:
            raise ValueError("File must be JSON format")

    def serialize(self):
        with open(self.__filename, 'w') as file:
            json.dump(self.data, file, ensure_ascii=False)

    def deserialize(self):
        with open(self.__filename, 'r') as file:
            unpacked = json.load(file)
            print(unpacked)
test_data = {'name': 'Niska', 'phone': ['0995552611', '0662911954'], 'age': 99}

json_test = SerializeJson(test_data, 'DB.json')
json_test.serialize()
json_test.deserialize()

bin_test = SerializeBin(test_data, 'DB.bin')
bin_test.serialize()
bin_test.deserialize()