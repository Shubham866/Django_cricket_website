import datetime
import sys
import time
import pytz
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from.models import article, Nation, Player, Match , Ball, player_match
from.forms import form_article, form_nation, form_player, form_schedule_match, Form_Ball
from django.core import serializers
# from.models import player
# from.models import Match
# from.models import Venue

# Create your views here.
x=[]
y=[]
abc=1
def index(request):
    return render(request, 'basic.html')
def match_detail(request, match_id):
    a=Match.objects.get(pk=match_id)
    one=player_match.objects.filter(Match=a ).order_by('bat_position')
    r=Ball.objects.filter(Match=a).order_by('-id')
 
    x=[]

    z=[]
    bowler1=[]
    bowler2=[]
    d=[]
    e=[]
    e.clear()
    f=[]
    g=[]
   
    
    for q in one :
        if(q.status=='Finished'):
            if(q.status=='batting'):
                q.status='Not Out'
                q.save()
        if(q.Name.nation==a.Opp_one):
            x.append(q)
        else:
            z.append(q)
    for q in x:
        if(q.status=='Out' or q.status=='batting' or q.status=='Not Out'):
            d.append(q)
        else:
            e.append(q)
    for q in z:
        if(q.status=='Out' or q.status=='batting' or q.status=='Not Out'):
            f.append(q)
        else:
            g.append(q)
    if a.Opp_one == a.Toss and a.Toss_Result == 'Bat' or a.Opp_two == a.Toss and a.Toss_Result == 'Field' :
        t=a.opp1_total_runs+1 - a.opp2_total_runs
    else:
        t=a.opp2_total_runs +1 - a.opp1_total_runs
    
       
    
    for q in x:
        if(q.over>0):
            bowler1.append(q)
    for q in z:
        if(q.over>0):
            bowler2.append(q)

    

    
    return render(request ,"match_detail.html", {'q':a , 'one_bat' :d, 'two_bat':f ,'one_yet':e , 'two_yet':g ,'bowler_one':bowler1, 'bowler_two':bowler2, 'comm':r, 't':t})

 
def get_article(request):
    if request.method == 'POST':
        f_a = form_article(request.POST)
        if f_a.is_valid():
            head = f_a.cleaned_data['heading']
            texting = f_a.cleaned_data['text']
            short = f_a.cleaned_data['text'][0:160]
            author = f_a.cleaned_data['pub_author']
            author = f_a.cleaned_data['pub_author']
            dt = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))

            ar = article(heading=head, text=texting,
                         short_text=short, pub_date=dt, pub_author=author)

            ar.save()
            return render(request, 'basic.html')
    else:
        f_a = form_article()
    return render(request, "enter_article.html", {'a': f_a})

def get_ball(request):
    if request.method == 'POST':
        f_a = Form_Ball(request.POST)
     
        if f_a.is_valid():
            b=Ball()
            b.Match=f_a.cleaned_data["Match"]
            b.Over=f_a.cleaned_data["Over"]
            b.Runner_Player=f_a.cleaned_data["Runner_Player"]
            b.Strike_Player=f_a.cleaned_data["Strike_Player"]
            b.Bowler_Player=f_a.cleaned_data["Bowler_Player"]
            b.Run_on_ball=f_a.cleaned_data["Run_on_ball"]
            b.real_comm=f_a.cleaned_data["real_comm"]
            b.Actual_Run=b.Run_on_ball.value
            

            # Comparing two objects in all five 
            strike=player_match.objects.filter(Name=b.Strike_Player , Match=b.Match)
            Runner=player_match.objects.filter(Name=b.Runner_Player , Match=b.Match)
            Bowler=player_match.objects.filter(Name=b.Bowler_Player , Match=b.Match)
        
            
            #chane
            # mtch=Match.objects.all()
            # # for q in mtch:
            # #     if(q==b.Match):


            # 4 over 4 wicket match 
            
        

                

                
                



            for q in strike:
                    q.status="batting"
                    if(q.Name.nation==q.Match.Opp_one):
                            if(q.Match.opp1_wicket==0):
                                q.bat_position=1
                            elif(q.bat_position==50):
                                q.bat_position=q.Match.opp1_wicket+2

                    else:
                            if(q.Match.opp2_wicket==0):
                                q.bat_position=1
                            elif(q.bat_position==50):
                                q.bat_position=q.Match.opp2_wicket+2
                    if(q.Balls_Faced==0 and not (b.Run_on_ball.Mode=='Wide , 1 run' or b.Run_on_ball.Mode=='Wide' or b.Run_on_ball.Mode=='Wide , 2 runs' or b.Run_on_ball.Mode=='Wide , 3 runs' or b.Run_on_ball.Mode=='Wide , 4 runs') ):
                        b.Strike_Player.batting_innings+=1
                        b.Strike_Player.No+=1

                    if(b.Run_on_ball.Mode=='Wide , 1 run' or b.Run_on_ball.Mode=='Wide' or b.Run_on_ball.Mode=='Wide , 2 runs' or b.Run_on_ball.Mode=='Wide , 3 runs' or b.Run_on_ball.Mode=='Wide , 4 runs'):
                        q.Balls_Faced+=0
                        b.Strike_Player.BF+=0

                    elif (b.Run_on_ball.Mode=='Byes 1 run' or b.Run_on_ball.Mode=='Byes 2 runs' or b.Run_on_ball.Mode=='Byes 3 runs' or b.Run_on_ball.Mode=='Byes 4 runs' or b.Run_on_ball.Mode=='Dot ball' ):
                        q.Balls_Faced+=1
                        b.Strike_Player.BF+=1
                        
                    elif(b.Run_on_ball.Mode=='OUT'):
                        q.status='Out'
                        b.Strike_Player.BF+=1
                        q.Balls_Faced+=1
                        b.Strike_Player.BF+=1
                        b.Strike_Player.No-=1
                        if(q.Runs>=200):
                            b.Strike_Player.double_hundred+=1
                        elif(q.Runs>=100):
                            b.Strike_Player.hundred+=1
                        elif(q.Runs>=50):
                            b.Strike_Player.fifty+=1
                        
                            
                    elif(b.Run_on_ball.Mode=='SIX'):
                        q.Runs+=b.Actual_Run
                        q.six+=1
                        q.Balls_Faced+=1
                        b.Strike_Player.runs+=b.Actual_Run
                        b.Strike_Player.sixes+=1
                        b.Strike_Player.BF+=1
                    elif(b.Run_on_ball.Mode=='FOUR'):
                        q.Runs+=b.Actual_Run
                        q.four+=1
                        q.Balls_Faced+=1
                        b.Strike_Player.runs+=b.Actual_Run
                        b.Strike_Player.four+=1
                        b.Strike_Player.BF+=1
                    # id not mode then we r comparing an object(id) with a string

                    elif (b.Run_on_ball.Mode=='No Ball' or b.Run_on_ball.Mode=='No Ball , 1 run' or b.Run_on_ball.Mode=='No Ball , 2 runs' or b.Run_on_ball.Mode=='No Ball , 3 runs' or b.Run_on_ball.Mode=='No Ball , 4 runs' or b.Run_on_ball.Mode=='No Ball , 6 runs'):
                        q.Balls_Faced+=1
                        b.Strike_Player.BF+=1
                        b.Strike_Player.runs+=b.Actual_Run-1

                        q.Runs+=b.Actual_Run-1
                        if(b.Run_on_ball.Mode=='No Ball , 6 runs'):
                            q.six+=1
                            b.Strike_Player.sixes+=1
                        if(b.Run_on_ball.Mode=='No Ball , 4 runs'):
                            q.four+=1
                            b.Strike_Player.four+=1
                        
                    else:
                        q.Runs+=b.Actual_Run
                        q.Balls_Faced+=1
                        b.Strike_Player.runs+=b.Actual_Run
                        b.Strike_Player.BF+=1
                    HS=q.Runs
                    if(b.Strike_Player.highest<HS):
                        b.Strike_Player.highest=HS
                    
                    # if(q.batting_innings-q.No!=0):
                    #     q.bat_avg=q.runs/(q.batting_innings-q.No)
                    q.save()


                    if(q.Balls_Faced!=0):
                        q.SR=q.Runs/q.Balls_Faced*100
                    if(b.Strike_Player.BF!=0):
                        b.Strike_Player.bat_SR=b.Strike_Player.runs/b.Strike_Player.BF*100
                    if((b.Strike_Player.batting_innings-b.Strike_Player.No)!=0):
                        b.Strike_Player.bat_avg=b.Strike_Player.runs/(b.Strike_Player.batting_innings-b.Strike_Player.No)

                    q.save()
                    b.Strike_Player.save()

            for q in Runner:
                if(q.Balls_Faced==0 ):
                        b.Strike_Player.batting_innings+=1
                        b.Strike_Player.No+=1
                if(q.bat_position==50):
                    if(q.Name.nation==q.Match.Opp_one):
                        q.bat_position=q.Match.opp1_wicket+2

                    else:
                        q.bat_position=q.Match.opp2_wicket+2

                   
                q.status="batting"
                q.save()
            for q in Bowler:
                    if(q.over==0 and not(b.Run_on_ball.Mode=='Wide , 1 run' or b.Run_on_ball.Mode=='Wide' or b.Run_on_ball.Mode=='Wide , 2 runs' or b.Run_on_ball.Mode=='Wide , 3 runs' or b.Run_on_ball.Mode=='Wide , 4 runs' or b.Run_on_ball.Mode=='No Ball' or b.Run_on_ball.Mode=='No Ball , 1 run' or b.Run_on_ball.Mode=='No Ball , 2 runs' or b.Run_on_ball.Mode=='No Ball , 3 runs' or b.Run_on_ball.Mode=='No Ball, 4 runs' or b.Run_on_ball.Mode=='No Ball, 6 runs') ):
                        b.Bowler_Player.Bowling_innings+=1
            
                    if(b.Run_on_ball.Mode=='Byes 1 run' or b.Run_on_ball.Mode=='Byes 2 runs' or b.Run_on_ball.Mode=='Byes 3 runs' or b.Run_on_ball.Mode=='Byes 4 runs' or b.Run_on_ball.Mode=='Dot ball'):
                        q.over+=1
                        b.Bowler_Player.Ball_bowled+=1
                    elif(b.Run_on_ball.Mode=='OUT'):
                        q.over+=1
                        q.wicket+=1
                        b.Bowler_Player.wickets+=1
                        b.Bowler_Player.Ball_bowled+=1
                    elif(b.Run_on_ball.Mode=='Wide, 1 run' or b.Run_on_ball.Mode=='Wide' or b.Run_on_ball.Mode=='Wide , 2 runs' or b.Run_on_ball.Mode=='Wide , 3 runs' or b.Run_on_ball.Mode=='Wide , 4 runs' or b.Run_on_ball.Mode=='No Ball' or b.Run_on_ball.Mode=='No Ball , 1 run' or b.Run_on_ball.Mode=='No Ball , 2 runs' or b.Run_on_ball.Mode=='No Ball , 3 runs' or b.Run_on_ball.Mode=='No Ball , 4 runs' or b.Run_on_ball.Mode=='No Ball , 6 runs'):
                        q.runs_conceded+=b.Actual_Run
                        b.Bowler_Player.runs_conceded+=b.Actual_Run
                    else:                    
                        q.runs_conceded+=b.Actual_Run
                        q.over+=1
                        b.Bowler_Player.runs_conceded+=b.Actual_Run
                        b.Bowler_Player.Ball_bowled+=1
                    q.over1=int(q.over/6)
                    q.over1+=(q.over%6)/10
                    
                    if(q.over!=0):
                        q.Economy=q.runs_conceded/q.over*6
                    q.save()
                    if(b.Bowler_Player.Ball_bowled!=0):
                        b.Bowler_Player.economy=b.Bowler_Player.runs_conceded/b.Bowler_Player.Ball_bowled*6
                    if(b.Bowler_Player.wickets!=0):
                        b.Bowler_Player.bowl_avg=b.Bowler_Player.runs_conceded/b.Bowler_Player.wickets
                        b.Bowler_Player.bowl_SR=b.Bowler_Player.Ball_bowled/b.Bowler_Player.wickets
                    b.Bowler_Player.save()
            
     
            # b.Bowler_Player=f_a.cleaned_data["Bowler_Player"]
            
                   
                
                   
            
           
            
            # if(b.Over==0.6):
            #     if((b.Match.Opp_one==b.Match.Toss and b.Match.Toss_Result=='Bat') or b.Match.Opp_two==b.Match.Toss and b.Match.Toss_Result=='Field'):
            #         if(b.Match.status2=='1st Innings'):
            #             b.Match.opp1_overs=1
            #         else:
            #             b.Match.opp1_overs=2

                
            # if(b.Match.opp1_overs==1.6):
            #     b.Match.opp1_overs=2
            # if(b.Match.opp2_overs==0.6):
            #     b.Match.opp2_overs=1
            # if(b.Match.opp2_overs==1.6):
            #     b.Match.opp2_overs=2
            
            #to decide the status1 and status 2 
            #status = 'Upcoming and Toss ' , 'Live' , 'Finished'
            #status1 = 'Mtch starting in time' , '1st INNIGS ' 'INNINGS BREAK' '2ND INNINBGS' 'THIS TEAM WON BY so and so margin'
            # two cases in which won the toss
            # we can place the run and extras and over and wicket of mathc statment in between as well above while vcalucltaing the players 
            if((b.Match.Opp_one==b.Match.Toss and b.Match.Toss_Result=='Bat') or b.Match.Opp_two==b.Match.Toss and b.Match.Toss_Result=='Field'):
                if(b.Match.status=='Upcoming & Toss' or b.Match.status2=='1st Innings'):
                    b.Match.status='Live'
                    b.Match.status2='1st Innings'
                    if(b.Run_on_ball.Mode=='OUT'):
                        b.Match.opp1_wicket+=1
                    b.Match.opp1_total_runs+=b.Actual_Run 
                    b.Match.opp1_overs=b.Over
                if((b.Match.opp1_overs==4 or b.Match.opp1_wicket>=4) and b.Match.opp2_overs<=0 and b.Over>0.1):
                     b.Match.status2='Innings Break'
                elif(b.Match.status2=='Innings Break' and b.Over>0.0):
                     b.Match.status2='2nd Innings'
                     b.Match.opp2_total_runs+=b.Actual_Run
                     b.Match.opp2_overs=b.Over
                     if(b.Run_on_ball.Mode=='OUT'):
                        b.Match.opp2_wicket+=1
                elif(b.Match.status2=='2nd Innings' and b.Over<=4):
                    b.Match.opp2_total_runs+=b.Actual_Run
                    b.Match.opp2_overs=b.Over
                    if(b.Run_on_ball.Mode=='OUT'):
                        b.Match.opp2_wicket+=1
                else:
                    print("Hello")
                if(b.Match.status2=='2nd Innings'):
                
                    if(b.Match.status2=='2nd Innings' and b.Match.opp2_total_runs>b.Match.opp1_total_runs):
                        b.Match.status='Finished'
                        b.Match.winning_nation=b.Match.Opp_two.Name
                        b.Match.status2=b.Match.winning_nation + " won by " + str(4-b.Match.opp2_wicket) + " wickets "
                    elif(b.Match.status2=='2nd Innings' and b.Match.opp2_total_runs<b.Match.opp1_total_runs and (b.Match.opp2_wicket==4 or b.Match.opp2_overs==4)):
                        b.Match.status='Finished'
                        b.Match.winning_nation=b.Match.Opp_one.Name
                        b.Match.status2=b.Match.winning_nation + " won by " + str(b.Match.opp1_total_runs-b.Match.opp2_total_runs) + " runs "
                    elif(b.Match.status2=='2nd Innings' and b.Match.opp1_total_runs==b.Match.opp2_total_runs and (b.Match.opp2_wicket==4 or b.Match.opp2_overs==4)):
                        b.Match.status='Finished'
                        b.Match.status2='Tied'
            else:
                if(b.Match.status=='Upcoming & Toss' or b.Match.status2=='1st Innings'):
                    b.Match.status='Live'
                    b.Match.status2='1st Innings'
                    if(b.Run_on_ball.Mode=='OUT'):
                        b.Match.opp2_wicket+=1
                    b.Match.opp2_total_runs+=b.Actual_Run 
                    b.Match.opp2_overs=b.Over
                if((b.Match.opp2_overs==4 or b.Match.opp2_wicket>=4) and b.Match.opp1_overs<=0 and b.Over>0.1):
                     b.Match.status2='Innings Break'
                elif(b.Match.status2=='Innings Break' and b.Over>0.0):
                     b.Match.status2='2nd Innings'
                     b.Match.opp1_total_runs+=b.Actual_Run
                     b.Match.opp1_overs=b.Over
                     if(b.Run_on_ball.Mode=='OUT'):
                        b.Match.opp1_wicket+=1
                elif(b.Match.status2=='2nd Innings' and b.Over<=4):
                    b.Match.opp1_total_runs+=b.Actual_Run
                    b.Match.opp1_overs=b.Over
                    if(b.Run_on_ball.Mode=='OUT'):
                        b.Match.opp1_wicket+=1
                else:
                    print("Hello")
                if(b.Match.status2=='2nd Innings'):
                
                    if(b.Match.status2=='2nd Innings' and b.Match.opp1_total_runs>b.Match.opp2_total_runs):
                        b.Match.status='Finished'
                        b.Match.winning_nation=b.Match.Opp_one.Name
                        b.Match.status2=b.Match.winning_nation + " won by " + str(4-b.Match.opp1_wicket) + " wickets "
                    elif(b.Match.status2=='2nd Innings' and b.Match.opp1_total_runs<b.Match.opp2_total_runs and (b.Match.opp1_wicket==4 or b.Match.opp1_overs==4)):
                        b.Match.status='Finished'
                        b.Match.winning_nation=b.Match.Opp_two.Name
                        b.Match.status2=b.Match.winning_nation + " won by " + str(b.Match.opp2_total_runs-b.Match.opp1_total_runs) + " runs "
                    elif(b.Match.status2=='2nd Innings' and b.Match.opp1_total_runs==b.Match.opp2_total_runs and (b.Match.opp1_wicket==4 or b.Match.opp1_overs==4)):
                        b.Match.status='Finished'
                        b.Match.status2='Tied'

                # elif(b.Match.status1=='2nd Innings' and b.Match.opp2_total_runs==b.Match.opp1_total_runs and (b.Match.opp2_wicket==4 or b.Match.opp2_overs==4)):
          
            
         #
                
            # elif(b.M)
                
            # b.Match.save()
            if(b.Run_on_ball.Mode=='Wide , 1 run' or b.Run_on_ball.Mode=='Wide' or b.Run_on_ball.Mode=='Wide , 2 runs' or b.Run_on_ball.Mode=='Wide , 3 runs' or b.Run_on_ball.Mode=='Wide , 4 runs'):
                if((b.Match.Opp_one==b.Match.Toss and b.Match.Toss_Result=='Bat') or b.Match.Opp_two==b.Match.Toss and b.Match.Toss_Result=='Field'):
                            if(b.Match.status2=='1st Innings'):
                                b.Match.opp1_extras+=b.Actual_Run
                            else:
                                b.Match.opp2_extras+=b.Actual_Run
                else:
                            if(b.Match.status2=='1st Innings'):
                                b.Match.opp2_extras+=b.Actual_Run
                            else:
                                b.Match.opp1_extras+=b.Actual_Run

                
            elif (b.Run_on_ball.Mode=='Byes 1 run' or b.Run_on_ball.Mode=='Byes 2 runs' or b.Run_on_ball.Mode=='Byes 3 runs' or b.Run_on_ball.Mode=='Byes 4 runs' or b.Run_on_ball.Mode=='Dot ball' ):
                if((b.Match.Opp_one==b.Match.Toss and b.Match.Toss_Result=='Bat') or b.Match.Opp_two==b.Match.Toss and b.Match.Toss_Result=='Field'):
                            if(b.Match.status2=='1st Innings'):
                                b.Match.opp1_extras+=b.Actual_Run
                            else:
                                b.Match.opp2_extras+=b.Actual_Run
                else:
                            if(b.Match.status2=='1st Innings'):
                                b.Match.opp2_extras+=b.Actual_Run
                            else:
                                b.Match.opp1_extras+=b.Actual_Run
            elif (b.Run_on_ball.Mode=='No Ball' or b.Run_on_ball.Mode=='No Ball , 1 run' or b.Run_on_ball.Mode=='No Ball , 2 runs' or b.Run_on_ball.Mode=='No Ball , 3 runs' or b.Run_on_ball.Mode=='No Ball , 4 runs' or b.Run_on_ball.Mode=='No Ball , 6 runs'):
                if((b.Match.Opp_one==b.Match.Toss and b.Match.Toss_Result=='Bat') or b.Match.Opp_two==b.Match.Toss and b.Match.Toss_Result=='Field'):
                            if(b.Match.status2=='1st Innings'):
                                b.Match.opp1_extras+=1
                            else:
                                b.Match.opp2_extras+=1
                else:
                            if(b.Match.status2=='1st Innings'):
                                b.Match.opp2_extras+=1
                            else:
                                b.Match.opp1_extras+=1
            else:
                print("Hello")
        # # if(b.Match.status=='Finished'):

        #     a=f_a.cleaned_data["Runner_Player"]
        #     b=f_a.cleaned_data["Strike_Player"]
        #     if(b.Run_on_ball.Mode)=='1 run'):
        #         f_a.Strike_Player=a
        #         f_a.Runner_Player=b
        #     f_a.save()
            if(b.Over==1):
                b.Over=0.6
            if(b.Over==2):
                b.Over=1.6

            b.save()
            b.Match.save()
            
    else:
        f_a = Form_Ball()
    return render(request, "enter_article4.html", {'a': f_a})


def get_nation(request):
    if request.method == 'POST':
        f_a = form_nation(request.POST)
        if f_a.is_valid():
            name = f_a.cleaned_data['Name']
            ar = Nation(Name=name)
            a = ar.id
            ar.save()
            return render(request, 'basic.html')
    else:
        f_a = form_nation()
    return render(request, "enter_article3.html", {'a': f_a})


def get_sched(request):
    if request.method == 'POST':
        f_a = form_schedule_match(request.POST)
        if f_a.is_valid():
            Tourna = f_a.cleaned_data['Tourn']
            op_one = f_a.cleaned_data['Opp_one']
            op_two = f_a.cleaned_data['Opp_two']
            status1 = f_a.cleaned_data['status']
            place1 = f_a.cleaned_data['place']
            Date1 = f_a.cleaned_data['Date_match']
            op1_one = f_a.cleaned_data['Toss']
            # time = f_a.cleaned_data['time']
            a = f_a.cleaned_data['player_one_one']
            
         
            b = f_a.cleaned_data['player_one_two']
           
            c = f_a.cleaned_data['player_one_three']
          
            d = f_a.cleaned_data['player_one_four']
           
            e = f_a.cleaned_data['player_one_five']
        
            f = f_a.cleaned_data['player_two_one']
        
            g = f_a.cleaned_data['player_two_two']
      
            h = f_a.cleaned_data['player_two_three']
          
            i = f_a.cleaned_data['player_two_four']
           
            j = f_a.cleaned_data['player_two_five']
           
            k = f_a.cleaned_data['Toss_Result']
            
            ar = Match(Tourn=Tourna, Opp_one=op_one, Opp_two=op_two, status=status1, place=place1, Date_match=Date1,  
                       Toss=op1_one,
                       player_one_one=a,
                       player_one_two=b,
                       player_one_three=c,
                       player_one_four=d,
                       player_one_five=e,
                       player_two_one=f,
                       player_two_two=g,
                       player_two_three=h,
                       player_two_four=i,
                       player_two_five=j,Toss_Result=k)
            ar.status2=op1_one.Name +" won the toss and chose to "+k+" first"

            ar.save()

            p1=player_match(Name=a , Match=ar )
            # comparing objects
            p1.Name.matches+=1
            # saving p1.name object
            p1.Name.save()
            # to reflect in database
            p1.save()
            p2=player_match(Name=b , Match=ar )
            p2.Name.matches+=1
            p2.Name.save()
            p2.save()
            p3=player_match(Name=c , Match=ar )
            p3.Name.matches+=1
            p3.Name.save()
            p3.save()
            p4=player_match(Name=d , Match=ar )
            p4.Name.matches+=1
            p4.Name.save()
            p4.save()
            p5=player_match(Name=e , Match=ar )
            p5.Name.matches+=1
            p5.Name.save()
            p5.save()# on saving the obejct values are saved into the databse
            p6=player_match(Name=f , Match=ar )
            p6.Name.matches+=1
            p6.Name.save()
            p6.save()
            p7=player_match(Name=g , Match=ar )
            p7.Name.matches+=1
            p7.Name.save()
            p7.save()
            p8=player_match(Name=h , Match=ar )
            p8.Name.matches+=1
            p8.Name.save()
            p8.save()
            p9=player_match(Name=i , Match=ar )
            p9.Name.matches+=1
            p9.Name.save()
            p9.save()
            p10=player_match(Name=j , Match=ar )
            p10.Name.matches+=1
            p10.Name.save()
            p10.save()
            
            
            return render(request, 'basic.html')
    else:
        f_a = form_schedule_match()
    return render(request, "enter_article2.html", {'a': f_a})
def intro(request):
    a=Match.objects.filter(status='Finished').order_by('-Date_match')[:2]
    c=Match.objects.filter(status='Live').order_by('-Date_match')[:1]

    b=article.objects.all().order_by('-pub_date')[:3]
    for q in b:
        dt = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
        t= dt-q.pub_date
        if(t.days > 0):
            if(t.days > 1):
                q.time= (str(t.days)+" days ago")
            else:
                    q.time =(str(t.days)+" day ago ")
        else:
            seconds = t.total_seconds()
            minutes = int(seconds/60)
            hours = int(seconds/3600)
            if(hours == 1):
                q.time=str(hours)+" hour ago"
            elif(hours > 1):
                q.time=str(hours)+" hours ago"
            elif(minutes == 1):
                q.time=str(minutes)+" minute ago"
            elif(minutes > 1):
                q.time=str(int(minutes))+" minutes ago"
            else:
                q.time=str(int(seconds))+" seconds ago"
        q.save()
        
    one=Match.objects.filter(status='Upcoming & Toss').order_by('-Date_match')[:2]

    return render(request,'intro.html',{'a':a, 'b':b,'one':one,'c':c})


def get_player(request):
    if request.method == 'POST':
        f_a = form_player(request.POST)
        if f_a.is_valid():
            head = f_a.cleaned_data['nation']
            n = f_a.cleaned_data['name']
            texting = f_a.cleaned_data['born']
            short = f_a.cleaned_data['place']
            rol = f_a.cleaned_data['Role']
            b_style = f_a.cleaned_data['Batting_style']
            bo_style = f_a.cleaned_data['Bowling_style']
            dec = f_a.cleaned_data['desc']
            b = f_a.cleaned_data['icc_bowling']
            ba = f_a.cleaned_data['icc_batting']

            a = f_a.cleaned_data['age']

            ar = Player(name=n, nation=head, age=a, born=texting, place=short, Role=rol,
                        Batting_style=b_style, Bowling_style=bo_style, desc=dec, icc_bowling=b, icc_batting=ba)
            ar.save()
            return render(request, 'basic.html')
    else:
        f_a = form_player()
    return render(request, "enter_article1.html", {'a': f_a})


def player(request):
    a = Player.objects.all().order_by('icc_batting')
    b = Player.objects.all().order_by('icc_bowling')

    return render(request, "player_index.html",  {
        'a': a,
        'b': b,
    })
def player_detail(request, player_id):
    abc=player_id
    a=Player.objects.get(pk=player_id)
    return render(request, "player1.html", {'q':a})


def nation(request):
    b = Nation.objects.all()
    return render(request, "nation_index.html", {'b': b})


def index_news(request):
    b=article.objects.all()

    return render(request, "index_match.html", {'b':b})


def get_News(request):
    a = article.objects.all().order_by('-id')
    for q in a:
        dt = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
        t= dt-q.pub_date
        if(t.days > 0):
            if(t.days > 1):
                q.time= (str(t.days)+" days ago")
            else:
                    q.time =(str(t.days)+" day ago ")
        else:
            seconds = t.total_seconds()
            minutes = int(seconds/60)
            hours = int(seconds/3600)
            if(hours == 1):
                q.time=str(hours)+" hour ago"
            elif(hours > 1):
                q.time=str(hours)+" hours ago"
            elif(minutes == 1):
                q.time=str(minutes)+" minute ago"
            elif(minutes > 1):
                q.time=str(int(minutes))+" minutes ago"
            else:
                q.time=str(int(seconds))+" seconds ago"
        q.save()
    a = article.objects.all().order_by('-id')
    return JsonResponse({"news": list(a.values())})
def get_player_detail(request):
    a = Player.objects.get(id=abc)
    print(abc)
   
    return JsonResponse({"news": list(a)})
def search_news(request):
    text=request.POST["message"]
    a=article.objects.filter(heading__contains=text).order_by('-time')
    return render(request, "index_match1.html",{'a':a} )
def match(request):
    a=Match.objects.filter(status='Upcoming & Toss').order_by('-Date_match')
    b=Match.objects.filter(status='Live').order_by('-Date_match')
    c=Match.objects.filter(status='Finished').order_by('-Date_match')
    return render(request, "match.html", {'a':a,'b':b,'c':c})
def info(request, match_id):
    a=Match.objects.get(pk=match_id)
    one=player_match.objects.filter(Match=a )
    x=[]
    z=[]
    for q in one :
        if(q.Name.nation==a.Opp_one):
            x.append(q)
        else:
            z.append(q)
    
    return render(request, "hey.html", {'q':a , 'one':x, 'two':z})



def detail(request, article_id):
    q = article.objects.get(pk=article_id)
    return render(request, "new.html", {'q': q})


# # def players(request):
#     e=Player.objects.all()
#     for a in e:
#         a.update()
#         a.save()
#     q=Player.objects.all().order_by('-id')[:2]
#     return render(request , "index_players.html" , {'q':q})
# def match_index(request):
#     q=Match.objects.all().order_by('-Date_match')
#     return render(request , "index_match.html", {'q':q})

#     return render(request , "yello1.html ", {'a':a})
# def news(request):
#     a=article.objects.all().order_by('-id')
#     return render(request , 'yello.html', {'a':a})
# def player_detail(request , player_id):
#     q=Player.objects.get(pk=player_id)
#     return render (request , "player_profile.html" , {'q':q})
# def match_scorecard_index(request):
#     for i in range (sys.maxint):
#         score=Match.objects.all()
#         time.sleep(120)
#         return()
