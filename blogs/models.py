from django.db import models
# Create your models here.
# automically create a primary key
import datetime
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
import pytz
from django.contrib.postgres.fields import ArrayField


class article(models.Model):
    heading = models.CharField(max_length=100)
    text = models.TextField(default='')
    short_text = models.CharField(blank=True, max_length=200)
    pub_date = models.DateTimeField(default='')
    pub_author = models.CharField(max_length=40, default='')
    image = models.ImageField(upload_to='media')
    time=models.TextField(default="", null=True)

    def __str__(self):
        return self.heading


class Nation(models.Model):
    Name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='media', default='')

    def __str__(self):
        return self.Name




class Player(models.Model):
    name = models.CharField(max_length=100)
    nation = models.ForeignKey("blogs.Nation",  on_delete=models.CASCADE)
    born = models.DateField()

    age = models.IntegerField()

    place = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    Batting_style = models.CharField(max_length=100)
    Bowling_style = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='media' , default='')
    matches = models.IntegerField(default=0)
    batting_innings = models.IntegerField(default=0)
    Bowling_innings = models.IntegerField(default=0)
    No = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    highest = models.IntegerField(default=0)
    bat_avg = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    BF = models.IntegerField(default=0)
    bat_SR = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    hundred = models.IntegerField(default=0)
    fifty = models.IntegerField(default=0)
    double_hundred = models.IntegerField(default=0)
    four = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    Ball_bowled = models.IntegerField(default=0)
    runs_conceded = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    BBI = models.CharField(max_length=10, default='-')
    BBM = models.CharField(max_length=40, default='-')
    bowl_avg = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    bowl_SR = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    economy = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    five_wicket = models.IntegerField(default=0)
    ten_wicket = models.IntegerField(default=0)
    
    icc_bowling = models.IntegerField(default=0)
    icc_batting = models.IntegerField(default=0)

    def __str__(self):
        return self.name


#     # def _init_(self):
#         for q in self.Last_batting:
#             if(q=='NB'):
#                 self.matches=self.matches+1
#             elif(q[q.length-1]=='*'):
#                 self.matches=self.matches+1
#                 self.batting_innings=self.batting_innings+1
# #                 self.No=self.No+1
  # def save(self, *args, **kwargs):
    #     self.short_text=self.text[0:50]
    #     super(article, self).save(*args, **kwargs)
     # def age(self):
    #    dt=datetime.date.now(tz=pytz.timezone('Asia/Calcutta'))
    #    a=dt-self.born
    #    return a.years
class Run(models.Model):
    Mode=models.CharField(max_length=30)
    value=models.IntegerField(default=0)
    comm=models.CharField(max_length=100, default='')
    def __str__(self) :
        return self.Mode
class Ball(models.Model):
    Match=models.ForeignKey("blogs.Match", on_delete=models.CASCADE, null=True)
    Over=models.DecimalField(max_digits=2, decimal_places=1 , default=0)
    Strike_Player=models.ForeignKey("blogs.Player",related_name='one',on_delete=models.CASCADE )
    Runner_Player=models.ForeignKey("blogs.Player",related_name='two', on_delete=models.CASCADE )
    Run_on_ball=models.ForeignKey("blogs.Run",related_name='two', on_delete=models.CASCADE )
    Actual_Run=models.IntegerField(default=0)
    Bowler_Player=models.ForeignKey("blogs.Player",related_name='three', on_delete=models.CASCADE )
    real_comm=models.CharField(max_length=100, default='')

class Match(models.Model):
    # id=models.CharField(max_length=30, default="")
   
    Tourn=models.CharField(max_length=50)
    Opp_one = models.ForeignKey(
        "blogs.nation", related_name='requests_created1', on_delete=models.CASCADE)
    Opp_two = models.ForeignKey(
        "blogs.nation", related_name='requests_created', on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    status2=models.CharField(max_length=100 , default='')

    Toss=models.ForeignKey("blogs.Nation", on_delete=models.CASCADE, null=True)
    place = models.CharField(max_length=100)
    Toss_Result=models.CharField(max_length=100, default='')
    Date_match = models.DateField()
    
    player_one_one = models.ForeignKey(
        "blogs.player", related_name='requests_created1', on_delete=models.CASCADE, blank=True, null=True)
    player_one_two = models.ForeignKey(
        "blogs.player", related_name='requests_created2', on_delete=models.CASCADE, blank=True, null=True)
    player_one_three = models.ForeignKey(
        "blogs.player", related_name='requests_created3', on_delete=models.CASCADE, blank=True, null=True)
    player_one_four = models.ForeignKey(
        "blogs.player", related_name='requests_created4', on_delete=models.CASCADE, blank=True,null=True)
    player_one_five = models.ForeignKey(
        "blogs.player", related_name='requests_created7', on_delete=models.CASCADE, blank=True, default='' ,null=True)
    player_two_five = models.ForeignKey(
        "blogs.player", related_name='requests_created8', on_delete=models.CASCADE, blank=True, null=True)
    player_two_one = models.ForeignKey(
        "blogs.player", related_name='requests_created5', on_delete=models.CASCADE, blank=True,null=True)
    player_two_two = models.ForeignKey(
        "blogs.player", related_name='requests_created6', on_delete=models.CASCADE, blank=True, null=True)
    player_two_three = models.ForeignKey(
        "blogs.player", related_name='requests_created10', on_delete=models.CASCADE, blank=True, null=True)
    player_two_four = models.ForeignKey(
        "blogs.player", related_name='requests_created9', on_delete=models.CASCADE, blank=True, null=True)
    
    
    
    opp1_extras = models.IntegerField(blank=True, default=0)
    opp2_extras = models.IntegerField(blank=True, default=0)
    opp1_overs = models.DecimalField(max_digits=2, decimal_places=1 , default=0)
    opp2_overs = models.DecimalField(max_digits=2, decimal_places=1 , default=0)
    opp1_wicket = models.IntegerField(blank=True, default=0)
    opp2_wicket = models.IntegerField(blank=True, default=0)
    opp1_total_runs=models.IntegerField(blank=True, default=0)
    opp2_total_runs=models.IntegerField(blank=True, default=0)
    winning_nation=models.CharField(max_length=100, blank=True)

    # def opp1_total_runs(self):
    #     return self.player_one_one_runs +self.player_one_three_runs +self.player_one_four_runs+self.opp1_extras+self.player_one_two_runs
    # def opp2_total_runs(self):
    #     return  self.player_two_one_runs +self.player_two_three_runs +self.player_two_four_runs+self.opp1_extras+self.player_two_two_runs
    
    # def winning_nation(self):
    #     if( self.opp1_total_runs() > self.opp2_total_runs()):
    #         return self.Opp_one
    #     elif(self.opp1_total_runs() < self.opp2_total_runs()):
    #         return self.Opp_two
    #     else:
    #         return "tied"

    # def eco_one(self):
    #         return (self.player_one_one_runs_conc)*6/((self.player_one_one_overs % 10)*10+(int(self.player_one_one_overs)*6))

    # def eco_two(self):
    #         return (self.player_one_two_runs_conc)*6/((self.player_one_two_overs % 10)*10+(int(self.player_one_two_overs)*6))

    # def eco_three(self):
    #         return (self.player_one_three_runs_conc)*6/((self.player_one_three_overs % 10)*10+(int(self.player_one_three_overs)*6))

    # def eco_four(self):
    #         return (self.player_one_four_runs_conc)*6/((self.player_one_four_overs % 10)*10+(int(self.player_one_four_overs)*6))

    # def eco_five(self):
    #         return (self.player_two_one_runs_conc)*6/((self.player_two_one_overs % 10)*10+(int(self.player_two_one_overs)*6))

    # # def eco_six(self):
    # #         return (self.player_two_two_runs_conc)*6/((self.player_two_two_overs % 10)*10+(int(self.player_two_two_overs)*6))

    # # def eco_seven(self):
    # #         return (self.player_two_three_runs_conc)*6/((self.player_two_three_overs % 10)*10+(int(self.player_two_three_overs)*6))

    # # def eco_one(self):
    # #         return (self.player_two_four_runs_conc)*6/((self.player_two_four_overs % 10)*10+(int(self.player_two_four_overs)*6))
    #    def SR_one(self):
    #         return self.player_one_one_runs/self.player_one_one_BF

    # def SR_two(self):
    #         return self.player_one_two_runs/self.player_one_two_BF

    # def SR_three(self):
    #         return self.player_one_three_runs/self.player_one_three_BF

    # def SR_four(self):
    #         return self.player_one_four_runs/self.player_one_four_BF

    # def SR_five(self):
    #         return self.player_two_one_runs/self.player_two_one_BF

    # def SR_six(self):
    #         return self.player_two_two_runs/self.player_two_two_BF

    # def SR_seven(self):
    #         return self.player_two_three_runs/self.player_two_three_BF

    # def SR_eight(self):
    #         return self.player_two_four_runs/self.player_two_four_BF
class player_match(models.Model):
    bat_position=models.IntegerField(default=50)
    Match=models.ForeignKey("blogs.Match",on_delete=models.CASCADE )
    Name=models.ForeignKey("blogs.Player", on_delete=models.CASCADE)
    Runs=models.IntegerField(default=0)
    status=models.CharField( max_length=100, default='Yet to bat')
    Balls_Faced=models.IntegerField(default=0)
    four=models.IntegerField(default=0)
    six=models.IntegerField(default=0)
    runs_conceded=models.IntegerField(default=0)
    wicket=models.IntegerField(default=0)
    over=models.DecimalField(default=0, max_digits=3, decimal_places=1)
    over1=models.DecimalField(default=0, max_digits=3, decimal_places=1)
    
    Economy=models.DecimalField(default=0, max_digits=4, decimal_places=1)
    SR=models.DecimalField(default=0, max_digits=10, decimal_places=2)
    