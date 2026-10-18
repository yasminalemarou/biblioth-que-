class BiblioError(Exception):
    pass

class LivreIntrouvableError(BiblioError):
    def __init__(self, livre_id: int):
        super().__init__(f"Livre avec l'ID {livre_id} introuvable")
        self.livre_id = livre_id

class StockInsuffisantError(BiblioError):
    def __init__(self, titre: str, dispo: int):
        super().__init__(f"Stock insuffisant pour '{titre}'. Disponible : {dispo}")

class EmpruntInvalideError(BiblioError):
    pass

class ValidationError(BiblioError):
    pass