from database.DB_connect import DBConnect
from model.corso import Corso


# per inserire database
# trascino file all'interno di DBeaver -> selezionare localhost -> attivare connessione
# -> eseguire file (terzo tasto a sinistra) -> refresh sul database


class DAO():

    @staticmethod
    def getCodIns():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT codins from corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"]) # non serve creare DTO

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * from corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd= row["pd"],
            ))

        cursor.close()
        cnx.close()

        return res