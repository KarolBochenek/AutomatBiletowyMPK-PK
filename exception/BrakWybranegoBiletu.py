class BrakWybranegoBiletu(Exception):
    """Wyjatek używany do komunikatu o braku wybranego biletu."""

    def __init__(self):
        super().__init__("Nie wybrałeś żadnego biletu")