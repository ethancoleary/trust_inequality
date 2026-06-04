from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 's2_tg1'
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
    ret = models.IntegerField(choices=[
        [0, '0'],
        [5, '5'],
        [10, '10'],
        [15, '15'],
        [20, '20'],
        [25, '25'],
        [30, '30']
    ])
    blur_log = models.LongStringField(blank=True)
    blur_count = models.IntegerField(initial=0, blank=True)
    blur_warned = models.IntegerField(initial=0, blank=True)

    CQ1 = models.IntegerField(blank=True)  # transfer possibilities
    CQ2 = models.IntegerField(blank=True)  # second mover
    CQ3 = models.IntegerField(blank=True)  # K

    belief = models.IntegerField(choices=[
        [0, '0'],
        [5, '5'],
        [10, '10'],
        [15, '15'],
        [20, '20'],
        [25, '25'],
        [30, '30']
    ])


# PAGES
class Info(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player: Player):
        player.role1 = random.randint(1, 2)
        if player.role1 == 1:
            role1 = 'first'
            m_role1 = 'second'
        else:
            role1 = 'second'
            m_role1 = 'first'

        return {
            'role1': role1,
            'm_role1': m_role1,
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



class FM(Page):
    form_model = 'player'
    form_fields = ['transfer', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):


        if player.participant.group_assignment == 1:
            initial_bonus = 80
            transfer_bonus_l = 70
            transfer_bonus_u = 100
        else:
            initial_bonus = 40
            transfer_bonus_l = 30
            transfer_bonus_u = 60
        if player.participant.match == 1:
            match_bonus = 80
            m_transfer_bonus_u = 110
            m_transfer_bonus_l = 80
        else:
            match_bonus = 40
            m_transfer_bonus_u = 70
            m_transfer_bonus_l = 40

        return {
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus_l': transfer_bonus_l,
            'transfer_bonus_u': transfer_bonus_u,
            'm_transfer_bonus_l': m_transfer_bonus_l,
            'm_transfer_bonus_u': m_transfer_bonus_u,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

class Belief(Page):
    form_model = 'player'
    form_fields = ['belief', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        if player.participant.group_assignment == 1:
            own_group = "A"
            initial_bonus = 80
            transfer_bonus_l = 70
            transfer_bonus_u = 100
        else:
            own_group = "B"
            initial_bonus = 40
            transfer_bonus_l = 30
            transfer_bonus_u = 60
        if player.participant.match == 1:
            match_group = "A"
            match_bonus = 80
            m_transfer_bonus_u = 110
            m_transfer_bonus_l = 80
        else:
            match_group = "B"
            match_bonus = 40
            m_transfer_bonus_u = 70
            m_transfer_bonus_l = 40

        return {
            'own_group': own_group,
            'match_group': match_group,
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus_l': transfer_bonus_l,
            'transfer_bonus_u': transfer_bonus_u,
            'm_transfer_bonus_l': m_transfer_bonus_l,
            'm_transfer_bonus_u': m_transfer_bonus_u,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


class SM(Page):
    form_model = 'player'
    form_fields = ['ret', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        if player.role1 == 1:
            role1 = 'first'
            m_role1 = 'second'
        else:
            role1 = 'second'
            m_role1 = 'first'

        if player.participant.group_assignment == 1:
            initial_bonus = 80
            transfer_bonus_l = 80
            transfer_bonus_u = 110
        else:
            initial_bonus = 40
            transfer_bonus_l = 40
            transfer_bonus_u = 70
        if player.participant.match == 1:
            match_bonus = 80
            m_transfer_bonus_l = 70
            m_transfer_bonus_u = 100
        else:
            match_bonus = 40
            m_transfer_bonus_l = 30
            m_transfer_bonus_u = 60

        return {
            'role1': role1,
            'm_role1': m_role1,
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus_l': transfer_bonus_l,
            'transfer_bonus_u': transfer_bonus_u,
            'm_transfer_bonus_l': m_transfer_bonus_l,
            'm_transfer_bonus_u': m_transfer_bonus_u,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return "s2_dg2"






page_sequence = [
    Info,
    Comp,
    FM,
    Belief,
    SM
]
