import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodInsValue = None

    def handlePrintCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view._ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione! Selezionare un periodo didattico")
            self._view.update_page()
            return

        pdInt = int(pd)
        corsiPD = self._model.getCorsiPD(pdInt)

        if len(corsiPD) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pdInt}° periodo didattico"))
            # self._view.create_alert("Attenzione! Selezionare un periodo didattico")
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Corsi del {pdInt}° periodo didattico:"))
        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view._ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione! Selezionare un periodo didattico")
            self._view.update_page()
            return

        pdInt = int(pd)
        corsi = self._model.getCorsiPDIscritti(pdInt)

        if len(corsi) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pdInt}° periodo didattico"))
            # self._view.create_alert("Attenzione! Selezionare un periodo didattico")
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Corsi del {pdInt}° periodo didattico con dettaglio iscritti:"))
        for c in corsi:
            self._view.txt_result.controls.append(ft.Text(f"{c[0]}; Numero Iscritti: {c[1]}"))
        self._view.update_page()


    def handlePrintIscrittiCodIns(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodInsValue is None: # variabile si lega alla funzione che ho sotto (l'ho già letta)
            self._view.create_alert("Attenzione! Selezionare un insegnamento")
            self._view.update_page()
            return

        # posso recuperare studenti
        studenti = self._model.getStudentiCorso(self._ddCodInsValue.codins)
        if len(studenti) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessuno studente iscritto al corso"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Studenti iscritti al corso: {self._ddCodInsValue}"))
        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(f"{s}"))
        self._view.update_page()


    def handlePrintCDSCodIns(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodInsValue is None:
            self._view.create_alert("Attenzione! Selezionare un insegnamento")
            self._view.update_page()
            return

        cds = self._model.getCDSCorso(self._ddCodInsValue.codins)

        if len(cds) == 0:
            self._view.txt_result.controls.append(ft.Text(f"Nessun CDS afferente al corso {self._ddCodInsValue}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"CDS che frequentano il corso: {self._ddCodInsValue}"))
        for s in cds:
            self._view.txt_result.controls.append(ft.Text(f"{s[0]} - Numero iscritti: {s[1]}"))
        self._view.update_page()



    def fillddCodIns(self):
        # for codice in self._model.getCodIns():
            # self._view._ddCodIns.options.append(ft.dropdown.Option(codice))
        for corso in self._model.getAllCorsi():
            self._view._ddCodIns.options.append(ft.dropdown.Option(
                key = corso.codins,
                data = corso,
                on_click = self._choiceDDCodIns
            ))

    def _choiceDDCodIns(self, e):
        self._ddCodInsValue = e.control.data
        print(self._ddCodInsValue)