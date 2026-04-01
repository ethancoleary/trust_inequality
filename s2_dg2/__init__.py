from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 's2_dg2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    role1 = models.IntegerField(
        choices=[
            [1, 'First'],
            [2, 'Second']
        ]
    )
    transfer = models.IntegerField(
    )
    blur_log = models.LongStringField(blank=True)
    blur_count = models.IntegerField(initial=0, blank=True)
    blur_warned = models.IntegerField(initial=0, blank=True)

    CQ1 = models.IntegerField(blank=True)  # transfer possibilities
    CQ2 = models.IntegerField(blank=True)  # second mover
    CQ3 = models.IntegerField(blank=True)  # K

    belief = models.IntegerField(min=0, max=50)


# PAGES
class Intro(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player: Player):

        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }
class Info(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player: Player):

        return {

            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }
class Comp(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

    @staticmethod
    def live_method(player, data):
        if data['type'] == 'save_cq':
            field = 'C' + data['question']  # 'Q1' -> 'CQ1'
            setattr(player, field, data['answer'])
            return {player.id_in_group: {'type': 'ack'}}



class Decision(Page):
    form_model = 'player'
    form_fields = ['transfer', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        if player.participant.group_assignment == 1:
            initial_bonus = 80
            transfer_bonus = 70
        else:
            initial_bonus = 40
            transfer_bonus = 30
        if player.participant.match == 1:
            match_bonus = 80
            m_transfer_bonus = 110
        else:
            match_bonus = 40
            m_transfer_bonus = 70

        g = player.participant.group_assignment  # 1=A(80), 2=B(40)
        m = player.participant.match  # 1=A(80), 2=B(40)

        b_no_transfer = 80 if g == 1 else 40
        b_transfer = 70 if g == 1 else 30
        m_no_transfer = 80 if m == 1 else 40
        m_transfer = 110 if m == 1 else 70

        return {
            'b_no_transfer': b_no_transfer,
            'b_transfer': b_transfer,
            'm_no_transfer': m_no_transfer,
            'm_transfer': m_transfer,
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus': transfer_bonus,
            'm_transfer_bonus': m_transfer_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.dg = player.transfer

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return "s3"




page_sequence = [
    Intro,
    Info,
    Comp,
    Decision
]
