from django import forms
from .models import article , Nation , Player , Match , Ball


class form_article(forms.ModelForm):
    class Meta:
        model = article
        fields = ['heading',
                  'text',
                  'pub_author',
             ]
class form_nation(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ['Name',
             ]
class form_player(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name',
                    'nation', 'age',
                    'born',
                    'place', 'Role'  , 'Batting_style', 'Bowling_style', 'desc'
                    , 'icc_bowling', 'icc_batting',
             ]
class form_schedule_match(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['Tourn',
                    'Opp_one', 'Opp_two',
                    'status',
                    'place', 'Date_match'  ,
                    'Toss', 'player_one_one', 'player_one_two'
                    , 'player_one_three', 'player_one_four', 'player_one_five', 
                    'player_two_one','player_two_two','player_two_three', 
                    'player_two_four',  'player_two_five','Toss_Result',
             ]
class Form_Ball(forms.ModelForm):
    class Meta:
        model = Ball
        fields = [ 'Match','Over', 'Strike_Player','Runner_Player', 'Bowler_Player','Run_on_ball','real_comm'
             ]
