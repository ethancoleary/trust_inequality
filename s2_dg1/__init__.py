from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 's2_dg1'
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

    @staticmethod
    def live_method(player, data):
        if data['type'] == 'save_cq':
            field = 'C' + data['question']  # 'Q1' -> 'CQ1'
            setattr(player, field, data['answer'])
            return {player.id_in_group: {'type': 'ack'}}



class Situation1_1(Page):
    form_model = 'player'
    form_fields = ['transfer', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        player.participant.group_assignment=1
        player.participant.match = 1

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

        return {
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus': transfer_bonus,
            'm_transfer_bonus': m_transfer_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


    @staticmethod
    def is_displayed(player):
        return 1 #player.role1 == 1

class Situation1_2(Page):
    form_model = 'player'
    form_fields = [ 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        player.participant.group_assignment=1
        player.participant.match = 1

        if player.participant.group_assignment == 1:
            initial_bonus = 80
            transfer_bonus = 110
        else:
            initial_bonus = 40
            transfer_bonus = 70
        if player.participant.match == 1:
            match_bonus = 80
            m_transfer_bonus = 70
        else:
            match_bonus = 40
            m_transfer_bonus = 30

        return {
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus': transfer_bonus,
            'm_transfer_bonus': m_transfer_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


    @staticmethod
    def is_displayed(player):
        return 1 #player.role1 == 1

class Situation2_1(Page):
    form_model = 'player'
    form_fields = ['transfer', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        player.participant.group_assignment=1
        player.participant.match = 1

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

        return {
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus': transfer_bonus,
            'm_transfer_bonus': m_transfer_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


    @staticmethod
    def is_displayed(player):
        return 1 #player.role1 == 1

class Situation2_2(Page):
    form_model = 'player'
    form_fields = [ 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        player.participant.group_assignment=1
        player.participant.match = 1

        if player.participant.group_assignment == 1:
            initial_bonus = 80
            transfer_bonus = 110
        else:
            initial_bonus = 40
            transfer_bonus = 70
        if player.participant.match == 1:
            match_bonus = 80
            m_transfer_bonus = 70
        else:
            match_bonus = 40
            m_transfer_bonus = 30

        return {
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus': transfer_bonus,
            'm_transfer_bonus': m_transfer_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


    @staticmethod
    def is_displayed(player):
        return 1 #player.role1 == 1

class Belief(Page):
    form_model = 'player'
    form_fields = ['belief', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        player.participant.s_treatment = 1
        player.participant.group_assignment=1
        player.participant.match = 1

        if player.participant.group_assignment == 1:
            initial_bonus = 80
            transfer_bonus = 110
        else:
            initial_bonus = 40
            transfer_bonus = 70
        if player.participant.match == 1:
            match_bonus = 80
            m_transfer_bonus = 70
        else:
            match_bonus = 40
            m_transfer_bonus = 30

        return {
            's_treatment': player.participant.s_treatment,
            'initial_bonus': initial_bonus,
            'match_bonus': match_bonus,
            'transfer_bonus': transfer_bonus,
            'm_transfer_bonus': m_transfer_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


    @staticmethod
    def is_displayed(player):
        return 1 #player.role1 == 1


page_sequence = [
    Info,
    Comp,
    Situation1_1,
    Situation1_2,
    Situation2_1,
    Situation2_2,
    Belief
]
