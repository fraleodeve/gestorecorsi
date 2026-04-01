from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


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

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select * from corso c where c.pd = %s"""
        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(Corso(
                **row
                # codins=row["codins"],
                # crediti=row["crediti"], # superfluo se nome colonne = nome attributi
                # nome=row["nome"],
                # pd=row["pd"],
            ))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getCorsiPDIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # provo prima su dBeaver, faccio il join e creo count
        query = """ select c.codins, c.crediti, c.nome, c.pd, count(*) as n
                    from corso c, iscrizione i 
                    where c.codins = i.codins and c.pd = 1
                    group by c.codins, c.crediti, c.nome, c.pd"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append((Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd= row["pd"],
            ), row["n"]))
        cursor.close()
        cnx.close()

        return res

    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # provo prima su dBeaver, faccio il join e creo count
        query = """ select s.*
                    from studente s, iscrizione i 
                    where s.matricola = i.matricola and i.codins = %s """
        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))
        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getCDSCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # provo prima su dBeaver, non considero campi CD in cui è vuoto
        query = """ select s.CDS, count(*) as n
                    from studente s, iscrizione i 
                    where s.matricola = i.matricola and i.codins = %s and s.CDS != ""
                    group by s.cds """
        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))
        cursor.close()
        cnx.close()

        return res