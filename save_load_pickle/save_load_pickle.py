import pickle
import random
import os
import fileinput

path = os.path.join(os.path.dirname(__file__), 'saved_pickles')

class save_load():

    def __init__(self, data=None):
        self.data_to_save = data
        self.pickle_id = random.randint(0, 10000) * random.randint(-10, 300)

    def save_pickle(self):
        if self.data_to_save is not None:
            with open(os.path.join(path, f"{self.pickle_id}.pkl"), 'wb') as new_file:
                pickle.dump(self.data_to_save, new_file) #ver os outros params dessa função
                print("Params salvos no pickle")
                self.__save_id()

    def load_pickle(self, id=None):
        if id is not None:
            self.pickle_id = id
        file_to_load = os.path.join(path, f"{self.pickle_id}.pkl")

        with open(file_to_load, 'rb') as to_load:
            try:
                calc = pickle.load(to_load)
            except:
                raise Exception("Não foi possivel carregar o pickle")
        os.remove(file_to_load)

        with fileinput.FileInput(f"saved_id.txt", inplace=True, backup='.bak') as ids_file:
            for line in ids_file:
                line.replace(self.pickle_id, '')
        return calc

    def __save_id(self):
        with open(f"saved_id.txt", "a") as id_file:
            id_file.write(str(self.pickle_id)+'\n')

    def list_id(self):
        with open(f"saved_id.txt", "r") as id_file:
            return id_file.readlines()

    def load_all_pickles(self):
        id_list = []
        data_list = []

        for ids in self.list_id():
            id_list.append(ids.strip())
        for x in id_list:
            if not x.__eq__(''):
                data_list.append(self.load_pickle(x))
        return data_list


if __name__ == '__main__':
    pass
    # s_l = save_load()#("qualquer_bosta", True, False))
    # s_l.save_pickle()
    # for x in s_l.list_id():
    #     print(x)
    # test = s_l.load_pickle('937787')
    # # print(test)
    # print(s_l.load_all_pickles())