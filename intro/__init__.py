from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField()
    s_treatment = models.IntegerField(
        choices=[
            [1, 'Random'],
            [2, 'Merit']
        ]
    )
    blur_log = models.LongStringField(blank=True)
    blur_count = models.IntegerField(initial=0, blank=True)
    blur_warned = models.IntegerField(initial=0, blank=True)


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def error_message(player, values):
        if values.get('consent') != 1:
            return "Please consent to participation or withdraw from the experiment by closing your browser."

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }



class Overview(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.s_treatment = random.randint(1,2)
        player.participant.s_treatment = player.s_treatment


page_sequence = [
                Consent,
                 Overview
                 ]
