from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodIns(self):
        return DAO.getCodIns()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDIscritti(self, pd):
        result = DAO.getCorsiPDIscritti(pd)
        result.sort(key=lambda x: x[1], reverse=True) # per ordinare in base al numero
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda x: x.cognome)
        return studenti

    def getCDSCorso(self, codins):
        cds = DAO.getCDSCorso(codins)
        cds.sort(key=lambda x: x[1], reverse=True)
        return cds