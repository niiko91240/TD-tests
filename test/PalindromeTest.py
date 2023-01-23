import unittest
import parameterized.parameterized

from src.Langues.Constantes import Constantes
from src.Langues.LangueAnglaise import LangueAnglaise
from src.Langues.LangueFrancaise import LangueFrancaise
from utilities.LangueSpy import LangueSpy
from utilities.OhceBuilder import OhceBuilder


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        # QUAND on saisit une chaîne
        ohce = OhceBuilder.default()
        resultat = ohce.palindrome(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], resultat)

    @parameterized.parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE],
        [LangueFrancaise(), Constantes.Francais.BIEN_DIT],
    ],
        lambda _, __, args:
        "test ETANT DONNE un utilisateur parlant la langue %s \n"
        "QUAND on saisit un palindrome \n"
        "ALORS %s est renvoyé ensuite"
        % (str(type(args.args[0]).__name__), args.args[1])
    )
    def test_palindrome(self, langue, bien_dit):
        palindrome = "radar"

        ohce = OhceBuilder().ayant_pour_langue(langue).build()
        resultat = ohce.palindrome(palindrome)

        self.assertIn(palindrome, resultat)

        # ET 'Bien dit' est renvoyé ensuite
        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn(bien_dit, resultat_apres_palindrome)

    def test_non_palindrome(self):
        spy_langue = LangueSpy()
        ohce = OhceBuilder()\
            .ayant_pour_langue(spy_langue)\
            .build()

        ohce.palindrome("toto")

        self.assertEqual(0, spy_langue.nombre_appels_a_bien_dit)


if __name__ == '__main__':
    unittest.main()