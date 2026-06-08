from otree.api import *
import random
import re


doc = """
Your app description
"""

def bold_amounts(text):
    return re.sub(r'(&#8368;)(\d+)', r'\1<b>\2</b>', text)

class C(BaseConstants):
    NAME_IN_URL = 's3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    belief_perf = models.IntegerField(min=0, max=10)
    fairness = models.IntegerField(choices=[
        [1, 'Very unfair'],
        [2, 'Rather unfair'],
        [3, 'Neither unfair nor fair'],
        [4, 'Rather fair'],
        [5, 'Very fair']
    ])
    fairness_belief = models.IntegerField(choices=[
        [1, 'Very unfair'],
        [2, 'Rather unfair'],
        [3, 'Neither unfair nor fair'],
        [4, 'Rather fair'],
        [5, 'Very fair']
    ])
    risk1 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk2 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk3 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk4 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk5 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk6 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk7 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk8 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk9 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk10 = models.IntegerField(choices=[
        [1, 'A'],
        [2, 'B']
    ])
    risk_choice = models.IntegerField()
    risk_bonus = models.IntegerField(blank=True)
    age = models.IntegerField(min=18, max=100)
    gender = models.IntegerField(choices=[
        [1, 'Female'],
        [2, 'Male'],
        [3, 'Other'],
        [4, 'Prefer not to say']
    ])
    income = models.IntegerField(choices=[
        [1, 'Below £20 000'],
        [2, '£20 000-£29 999'],
        [3, '£30 000-£39 999'],
        [4, '£40 000-£49 999'],
        [5, '£50 000-£59 999'],
        [6, '£60 000-£69 999'],
        [7, '£70 000-£79 999'],
        [8, '£80 000-£89 999'],
        [9, '£90 000-£99 999'],
        [10, '£100 000 or more'],
    ])
    education = models.IntegerField(choices=[
        [1, 'GCSEs/O Levels or equivalent'],
        [2, 'A Levels or equivalent'],
        [3, 'Higher National Certificate/Diploma or Apprenticeship'],
        [4, 'Bachelor degree or equivalent'],
        [5, 'Master degree or equivalent'],
        [6, 'Doctorate']
    ])
    ethnicity = models.IntegerField(choices=[
        [1, 'Asian or Asian British'],
        [2, 'Black, Black British, Caribbean or African'],
        [3, 'Mixed or multiple ethnic groups'],
        [4, 'White'],
        [5, 'Other']
    ])
    native = models.IntegerField(choices=[
        [1, 'Yes'],
        [2, 'No']
    ]
    )
    political = models.IntegerField(choices=[
        [1, 'Left'],
        [2, 'Centre left'],
        [3, 'Centre'],
        [4, 'Centre right'],
        [5, 'Right']
    ])
    inequality = models.IntegerField()
    recall = models.IntegerField()
    situation = models.IntegerField(min=1, max=4)
    gentrust = models.IntegerField()
    advantage = models.IntegerField()
    helpful = models.IntegerField()

    blur_log = models.LongStringField(blank=True)
    blur_count = models.IntegerField(initial=0, blank=True)
    blur_warned = models.IntegerField(initial=0, blank=True)

    game_bonus = models.IntegerField()
    role_bonus = models.IntegerField()
    tg_bonus = models.IntegerField()
    random_draw = models.IntegerField()
    Risk = models.IntegerField(blank=True)


# PAGES
class Intro(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

class Beliefs(Page):
    form_model = 'player'
    form_fields = ['belief_perf', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player: Player):
        if player.participant.group_assignment == 1:
            own_group = "A"

        else:
            own_group = "B"

        if player.participant.match == 1:
            match_group = "A"

        else:
            match_group = "B"

        return {
            'own_group': own_group,
            'match_group': match_group,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

class Fairness(Page):
    form_model = 'player'
    form_fields = ['fairness', 'fairness_belief', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        if player.participant.group_assignment == 1:
            initial_bonus = 80
        else:
            initial_bonus = 40
        if player.participant.match == 1:
            match_bonus = 80
        else:
            match_bonus = 40

        return {
            'match_bonus': match_bonus,
            'initial_bonus': initial_bonus,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }



class Risk(Page):
    form_model = 'player'
    form_fields = ['risk1', 'risk2', 'risk3', 'risk4', 'risk5', 'risk6', 'risk7', 'risk8', 'risk9', 'risk10', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player: Player):
        rows = [
            {'i': 1, 'a': '1/10 of &#8473;40, 9/10 of &#8473;36', 'b': '1/10 of &#8473;77, 9/10 of &#8473;2'},
            {'i': 2, 'a': '2/10 of &#8473;40, 8/10 of &#8473;36', 'b': '2/10 of &#8473;77, 8/10 of &#8473;2'},
            {'i': 3, 'a': '3/10 of &#8473;40, 7/10 of &#8473;36', 'b': '3/10 of &#8473;77, 7/10 of &#8473;2'},
            {'i': 4, 'a': '4/10 of &#8473;40, 6/10 of &#8473;36', 'b': '4/10 of &#8473;77, 6/10 of &#8473;2'},
            {'i': 5, 'a': '5/10 of &#8473;40, 5/10 of &#8473;36', 'b': '5/10 of &#8473;77, 5/10 of &#8473;2'},
            {'i': 6, 'a': '6/10 of &#8473;40, 4/10 of &#8473;36', 'b': '6/10 of &#8473;77, 4/10 of &#8473;2'},
            {'i': 7, 'a': '7/10 of &#8473;40, 3/10 of &#8473;36', 'b': '7/10 of &#8473;77, 3/10 of &#8473;2'},
            {'i': 8, 'a': '8/10 of &#8473;40, 2/10 of &#8473;36', 'b': '8/10 of &#8473;77, 2/10 of &#8473;2'},
            {'i': 9, 'a': '9/10 of &#8473;40, 1/10 of &#8473;36', 'b': '9/10 of &#8473;77, 1/10 of &#8473;2'},
            {'i': 10, 'a': '10/10 of &#8473;40, 0/10 of &#8473;36', 'b': '10/10 of &#8473;77, 0/10 of &#8473;2'},
        ]
        risk_rows = [
            {'i': r['i'], 'a': bold_amounts(r['a']), 'b': bold_amounts(r['b'])}
            for r in rows
        ]
        return {
            'risk_rows': risk_rows,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.risk_choice = random.randint(1,10)
        random_draw = random.randint(1,10)
        player.random_draw = random_draw

        if player.risk_choice == 1:
            if player.risk1 == 1:
                player.risk_bonus = 40 if random_draw < 2 else 36
            else:
                player.risk_bonus = 77 if random_draw < 2 else 2
        elif player.risk_choice == 2:
            if player.risk2 == 1:
                player.risk_bonus = 40 if random_draw < 3 else 36
            else:
                player.risk_bonus = 77 if random_draw < 3 else 2
        elif player.risk_choice == 3:
            if player.risk3 == 1:
                player.risk_bonus = 40 if random_draw < 4 else 36
            else:
                player.risk_bonus = 77 if random_draw < 4 else 2
        elif player.risk_choice == 4:
            if player.risk4 == 1:
                player.risk_bonus = 40 if random_draw < 5 else 36
            else:
                player.risk_bonus = 77 if random_draw < 5 else 2
        elif player.risk_choice == 5:
            if player.risk5 == 1:
                player.risk_bonus = 40 if random_draw < 6 else 36
            else:
                player.risk_bonus = 77 if random_draw < 6 else 2
        elif player.risk_choice == 6:
            if player.risk6 == 1:
                player.risk_bonus = 40 if random_draw < 7 else 36
            else:
                player.risk_bonus = 77 if random_draw < 7 else 2
        elif player.risk_choice == 7:
            if player.risk7 == 1:
                player.risk_bonus = 40 if random_draw < 8 else 36
            else:
                player.risk_bonus = 77 if random_draw < 8 else 2
        elif player.risk_choice == 8:
            if player.risk8 == 1:
                player.risk_bonus = 40 if random_draw < 9 else 36
            else:
                player.risk_bonus = 77 if random_draw < 9 else 2
        elif player.risk_choice == 9:
            if player.risk9 == 1:
                player.risk_bonus = 40 if random_draw < 10 else 36
            else:
                player.risk_bonus = 77 if random_draw < 10 else 2
        elif player.risk_choice == 10:
            if player.risk10 == 1:
                player.risk_bonus = 40
            else:
                player.risk_bonus = 77


class Demo1(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income', 'education', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

class Demo2(Page):
    form_model = 'player'
    form_fields = ['ethnicity', 'native', 'political', 'inequality', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }


class Demo3(Page):
    form_model = 'player'
    form_fields = ['gentrust', 'advantage', 'helpful', 'Risk', 'blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def error_message(player, values):
        if values['Risk'] is None:
            return 'Please answer all questions before continuing.'
        if not (0 <= values['Risk'] <= 10):
            return 'Risk must be between 0 and 10.'

    @staticmethod
    def vars_for_template(player):
        return {
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.game_bonus = random.randint(1, 2)
        player.role_bonus = random.randint(1, 2)
        tg_first = getattr(player.participant, 'TG_first', 1)
        if tg_first == 1:
            player.tg_bonus = 1 if player.game_bonus == 1 else 0
        else:
            player.tg_bonus = 0 if player.game_bonus == 1 else 1


class Results(Page):
    form_model = 'player'
    form_fields = ['blur_count', 'blur_log', 'blur_warned']

    @staticmethod
    def vars_for_template(player):

        if player.role_bonus == 1:
            role = "first mover."
        else:
            role = "second mover."

        if player.participant.group_assignment == 1:
            bonus = 70 if player.participant.dg == 1 else 80
        else:
            bonus = 30 if player.participant.dg == 1 else 40

        risk_choice = player.risk_choice
        risk_answer = getattr(player, f'risk{risk_choice}')
        if risk_answer == 1:
            option = "A"
        else:
            option = "B"
        risk1 = risk_choice
        risk1_payment = 40 if risk_answer == 1 else 77
        risk2_payment = 36 if risk_answer == 1 else 2
        risk2 = 10-risk_choice

        return {
            'risk_choice': risk_choice,
            'risk1_payment': risk1_payment,
            'risk2_payment': risk2_payment,
            'risk1': risk1,
            'risk2': risk2,
            'option': option,
            'bonus': bonus,
            'role': role,
            'hidden_fields': ['blur_log', 'blur_count', 'blur_warned'],
        }

class Redirect(Page):
    form_model = 'player'

    @staticmethod
    def js_vars(player: Player):
        return dict(
            completionlinkfull=player.session.config.get('completionlinkfull')
        )

page_sequence = [
    Intro,
    Beliefs,
    Fairness,
    Risk,
    Demo1,
    Demo2,
    Demo3,
    Results,
    Redirect
]
