from src.Langues.Constantes import Constantes
from src.PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueAnglaise:

    def dire_bonjour(self, periode_journee):
        match periode_journee:
            case PeriodeDeLaJournee.MATIN:
                return Constantes.Anglais.GOOD_MORNING
            case PeriodeDeLaJournee.APRES_MIDI:
                return Constantes.Anglais.GOOD_AFTERNOON
            case PeriodeDeLaJournee.SOIR:
                return Constantes.Anglais.GOOD_EVENING
            case PeriodeDeLaJournee.NUIT:
                return Constantes.Anglais.GOOD_NIGHT

        return Constantes.Anglais.HELLO

    def bien_dit(self):
        return Constantes.Anglais.WELL_DONE

    def au_revoir(self, periode_journee):
        if (periode_journee == PeriodeDeLaJournee.SOIR or periode_journee == PeriodeDeLaJournee.NUIT):
            return Constantes.Anglais.HAVE_GOOD_NIGHT
        else:
            return Constantes.Anglais.HAVE_GOOD_DAY
