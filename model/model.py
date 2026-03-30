from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodIns(self):
        return DAO.getCodIns()

    def getAllCorsi(self):
        return DAO.getAllCorsi()