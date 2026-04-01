from otree.api import *
import random
import os

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 's2_intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    AVG_PILOT = 7


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    group_assignment = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B']
        ]
    )
    match_same = models.IntegerField()
    match = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B']
        ]
    )
    blur_log = models.LongStringField(blank=True)
    blur_count = models.IntegerField(initial=0, blank=True)
    blur_warned = models.IntegerField(initial=0, blank=True)

    CQ1 = models.IntegerField(blank=True)  # own endowment
    CQ2 = models.IntegerField(blank=True)  # match endowment
    CQ3 = models.IntegerField(blank=True)  # random allocation T/F
    CQ4 = models.IntegerField(blank=True)  # number of situations
    CQ5 = models.IntegerField(blank=True)  # payment rule

    TG_first = models.IntegerField()


class Intro(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']


    @staticmethod
    def before_next_page(player, timeout_happened):

        if player.participant.merit == 0:
            player.group_assignment = random.randint(1,2)
            player.participant.group_assignment = player.group_assignment
        else:
            if player.participant.s1score >= C.AVG_PILOT:
                player.group_assignment = 1
            else:
                player.group_assignment = 2

            player.participant.group_assignment = player.group_assignment

        player.match_same = random.randint(0, 1)
        player.participant.match_same = player.match_same

        if player.participant.match_same == 1:
            player.match = 1 if player.group_assignment == 1 else 2
        else:
            player.match = 1 if player.group_assignment == 2 else 1

        player.participant.match = player.match

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

# PAGES
class Info(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']


    @staticmethod
    def vars_for_template(player: Player):

        g = "A" if player.group_assignment == 1 else "B"
        endowment = 80 if player.group_assignment == 1 else 40
        m = "A" if player.match == 1 else "B"
        m_endowment = 80 if player.match == 1 else 40
        return {
            'average': C.AVG_PILOT,
            'g': g, 'm': m,
            'endowment': endowment,
            'm_endowment': m_endowment,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

class Comp(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def is_displayed(player):
        return 1  #player.participant.s_treatment==1

    @staticmethod
    def vars_for_template(player):
        g = "A" if player.group_assignment == 1 else "B"
        endowment = 80 if player.group_assignment == 1 else 40
        m = "A" if player.match == 1 else "B"
        m_endowment = 80 if player.match == 1 else 40
        return {
            'g': g, 'm': m,
            'endowment': endowment,
            'm_endowment': m_endowment,
            'correct_CQ1': 4 if player.group_assignment == 1 else 2,
            'correct_CQ2': 4 if player.match == 1 else 2,
            'correct_CQ3': 1 if player.participant.merit == 0 else 2,
            'hidden_fields': ['blur_count', 'blur_log', 'blur_warned'],
        }

    @staticmethod
    def live_method(player, data):
        if data['type'] == 'save_cq':
            field = 'C' + data['question']  # 'Q1' -> 'CQ1'
            setattr(player, field, data['answer'])
            return {player.id_in_group: {'type': 'ack'}}

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        player.TG_first = random.randint(0,1)
        player.participant.TG_first = player.TG_first
        if player.TG_first == 0:
            return "s2_dg1"
        else:
            return "s2_tg1"


page_sequence = [
                Intro,
                 Info,
                Comp
                 ]
