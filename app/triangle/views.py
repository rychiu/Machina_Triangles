from otree.api import Currency as c, currency_range
from otree.api import safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Info_tri(Page):
    # If treatment is tri, display info_tri html
    def is_displayed(self):
        return self.player.treat == 'tri'


#This class sends information to the Questions_tri.html page
class Question_tri(Page):
    form_model = models.Player
    form_fields = ['submitted_answer']

    #Creates text for answer options
    def submitted_answer_choices(self):
        qd = self.player.current_question()
        #Numbers for Option A
        a_p1 = int(100*float(qd['A_p1']))
        a_p3 = int(100*float(qd['A_p3']))
        a_p2 = int(100 - a_p1 - a_p3)

        #Numbers for Option B
        b_p1 = int(100*float(qd['B_p1']))
        b_p3 = int(100*float(qd['B_p3']))
        b_p2 = int(100 - a_p1 - a_p3)

        #Returns dynamic text options for A and B
        return [
           "A: "+str(a_p1)+"%"+" chance of $"+qd['payoff1']+", "+str(a_p2)+"%"+" chance of $"+qd['payoff2']+", or "+str(a_p3)+"%"+" chance of $"+qd['payoff3'],
           "B: "+str(b_p1)+"%"+" chance of $"+qd['payoff1']+", "+str(b_p2)+"%"+" chance of $"+qd['payoff2']+", or "+str(b_p3)+"%"+" chance of $"+qd['payoff3'],
        ]

    #Creates data series that is passed to imbeded highchart triangle
    #Data takes form [[a1,a2],[b1,b2]]
    def vars_for_template(self):
        #Array for single set of points
        pointA = []
        pointB = []
        #Array to hold 2 sets of points
        pointsA = []
        pointsB = []
        qd = self.player.current_question()

        #Adding points for set A
        pointA.append(float(qd['A_p1']))
        pointA.append(float(qd['A_p3']))

        #Adding points for set B
        pointB.append(float(qd['B_p1']))
        pointB.append(float(qd['B_p3']))

        #Adding A and B to points
        pointsA.append(pointA)
        pointsB.append(pointB)

        #This line is needed for the data to be passed to highcharts
        #Without it the data is in the wrong form and will crash program
        pointsA = safe_json(pointsA)
        pointsB = safe_json(pointsB)
        payofflab1 = "$" + qd['payoff1']
        payofflab3 = "$" + qd['payoff3']

        #Returns [[a1,a2],[b1,b2]] as a series
        return{
            'seriesA' : pointsA,
            'seriesB' : pointsB,
            'poffA' : payofflab1,
            'poffC' : payofflab3,
        }
    # If treatment is tri, display q_tri html
    def is_displayed(self):
        return self.player.treat == 'tri'



class Info_pie(Page):
    # If treatment is pie, display info_pie html
    def is_displayed(self):
        return self.player.treat == 'pie'

#This class sends information to the Questions_pie.html page
class Question_pie(Page):
    form_model = models.Player
    form_fields = ['submitted_answer']

    #Creates text for answer options
    def submitted_answer_choices(self):
        qd = self.player.current_question()
        #Numbers for Option A
        a_p1 = int(100*float(qd['A_p1']))
        a_p3 = int(100*float(qd['A_p3']))
        a_p2 = int(100 - a_p1 - a_p3)

        #Numbers for Option B
        b_p1 = int(100*float(qd['B_p1']))
        b_p3 = int(100*float(qd['B_p3']))
        b_p2 = int(100 - a_p1 - a_p3)

        #Returns dynamic text options for A and B
        return [
           "A: "+str(a_p1)+"%"+" chance of $"+qd['payoff1']+", "+str(a_p2)+"%"+" chance of $"+qd['payoff2']+", or "+str(a_p3)+"%"+" chance of $"+qd['payoff3'],
           "B: "+str(b_p1)+"%"+" chance of $"+qd['payoff1']+", "+str(b_p2)+"%"+" chance of $"+qd['payoff2']+", or "+str(b_p3)+"%"+" chance of $"+qd['payoff3'],
        ]

    #Creates data series that is passed to imbeded highchart piechart
    def vars_for_template(self):
        qd = self.player.current_question()

        return{
            'ap1' : int(100*float(qd['A_p1'])),
            'ap2' : int(100*(float(1-float(qd['A_p1'])-float(qd['A_p3'])))),
            'ap3' : int(100*float(qd['A_p3'])),

            'd1' : str(qd['payoff1']),
            'd2' : str(qd['payoff2']),
            'd3' : str(qd['payoff3']),

            'bp1' : int(100*float(qd['B_p1'])),
            'bp2' : int(100*(float(1-float(qd['B_p1'])-float(qd['B_p3'])))),
            'bp3' : int(100*float(qd['B_p3'])),
        }
    #Displays q_pie html if treatment is pie
    def is_displayed(self):
        return self.player.treat == 'pie'


class Info_base(Page):
    # If treatment is base, display info_base html
    def is_displayed(self):
        return self.player.treat == 'base'

#This class sends information to the Questions_base.html page
class Question_base(Page):
    form_model = models.Player
    form_fields = ['submitted_answer']

    #Creates text for answer options
    def submitted_answer_choices(self):
        qd = self.player.current_question()
        #Numbers for Option A
        a_p1 = int(100*float(qd['A_p1']))
        a_p3 = int(100*float(qd['A_p3']))
        a_p2 = int(100 - a_p1 - a_p3)

        #Numbers for Option B
        b_p1 = int(100*float(qd['B_p1']))
        b_p3 = int(100*float(qd['B_p3']))
        b_p2 = int(100 - a_p1 - a_p3)

        #Returns dynamic text options for A and B
        return [
           "A: "+str(a_p1)+"%"+" chance of $"+qd['payoff1']+", "+str(a_p2)+"%"+" chance of $"+qd['payoff2']+", or "+str(a_p3)+"%"+" chance of $"+qd['payoff3'],
           "B: "+str(b_p1)+"%"+" chance of $"+qd['payoff1']+", "+str(b_p2)+"%"+" chance of $"+qd['payoff2']+", or "+str(b_p3)+"%"+" chance of $"+qd['payoff3'],
        ]

    #Creates data series that is passed to imbeded highchart piechart
    def vars_for_template(self):
        qd = self.player.current_question()

        return{

        }
    #Displays q_pie html if treatment is base
    def is_displayed(self):
        return self.player.treat == 'base'


#This class sends information to Results.html
class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,

        }

#Order in which pages are displayed
page_sequence = [
    Info_base,
    Info_tri,
    Info_pie,
    Question_base,
    Question_tri,
    Question_pie,
    Results
]
