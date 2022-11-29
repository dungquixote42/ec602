""" divsum checker"""
import unittest
from subprocess import PIPE, Popen, run, TimeoutExpired
import time
import os

# 1.1 add infinite loop protection
# 1.3 require updated cargrdlib
# 1.4 better compile messages
# 1.5 use newer cargrdlib
# 1.6 fix heavy tests

# 2.0 sum21, use curl_grading
# 2.1 adjust fail mechanism
# 2.2 disable cpplint usage

VERSION, CURL_GRADING_VER = (2,2), (3, 7)

def update_curl_grading():
    print('updating curl_grading')
    from requests import get
    r = get('https://curl.bu.edu/static/content/curl_grading.py')
    with open('curl_grading.py','w') as f:
        f.write(r.text)

def get_curl_grading():
    from os import listdir
    files = listdir();
    if "curl_grading.py" not in files:
        update_curl_grading()

    import curl_grading as e


    if e.VERSION < CURL_GRADING_VER:
        update_curl_grading()
        from importlib import reload
        e = reload(e)

    return e

curl_grading = get_curl_grading()




# DIVISORSUM

smalldivsumTests=[
('6','6: 1+2+3 = 6'),
('28','28: 1+2+4+7+14 = 28'),
('10','10: 1+2+5 =8'),
('8888','8888: 1+2+4+8+11+22+44+88+101+202+404+808+1111+2222+4444 = 9472'),
('888','888: 1+2+3+4+6+8+12+24+37+74+111+148+222+296+444 = 1392'),
('123123','123123: 1+3+7+11+13+21+33+39+41+77+91+123+143+231+273+287+429+451+533+861+1001+1353+1599+3003+3157+3731+5863+9471+11193+17589+41041 = 102669'),
]

primedivsumTests=[
('19','19: 1 = 1'),
('29','29: 1 = 1'),
]

bigdivsumTests=[
('814773960','814773960: 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+17+18+19+20+21+22+24+26+28+30+33+34+35+36+38+39+40+42+44+45+49+51+52+55+56+57+60+63+65+66+68+70+72+76+77+78+84+85+88+90+91+95+98+99+102+104+105+110+114+117+119+120+126+130+132+133+136+140+143+147+152+153+154+156+165+168+170+171+180+182+187+190+195+196+198+204+209+210+220+221+228+231+234+238+245+247+252+255+260+264+266+273+280+285+286+294+306+308+312+315+323+330+340+342+357+360+364+374+380+385+390+392+396+399+408+418+420+429+440+441+442+455+456+462+468+476+490+494+495+504+510+520+532+539+546+561+570+572+585+588+595+612+616+627+630+637+646+660+663+665+680+684+693+714+715+728+735+741+748+760+765+770+780+792+798+819+833+836+840+855+858+882+884+910+924+931+935+936+952+969+980+988+990+1001+1020+1045+1064+1071+1078+1092+1105+1122+1140+1144+1155+1170+1176+1190+1197+1224+1235+1254+1260+1274+1287+1292+1309+1320+1326+1330+1365+1368+1386+1428+1430+1463+1470+1482+1496+1530+1540+1547+1560+1596+1615+1617+1638+1666+1672+1683+1710+1716+1729+1764+1768+1785+1820+1848+1862+1870+1881+1911+1938+1960+1976+1980+1989+1995+2002+2040+2090+2142+2145+2156+2184+2205+2210+2223+2244+2261+2280+2310+2340+2380+2394+2431+2470+2499+2508+2520+2548+2574+2584+2618+2652+2660+2695+2717+2730+2772+2793+2805+2856+2860+2907+2926+2940+2964+3003+3060+3080+3094+3135+3185+3192+3230+3234+3276+3315+3332+3366+3420+3432+3458+3465+3528+3553+3570+3640+3705+3724+3740+3762+3822+3876+3927+3960+3978+3990+4004+4095+4165+4180+4199+4284+4290+4312+4389+4410+4420+4446+4488+4522+4620+4641+4655+4680+4760+4788+4845+4851+4862+4940+4998+5005+5016+5096+5148+5187+5236+5304+5320+5355+5390+5434+5460+5544+5586+5610+5720+5733+5814+5852+5880+5928+5985+6006+6120+6188+6270+6370+6435+6460+6468+6545+6552+6630+6664+6732+6783+6840+6916+6930+7007+7106+7140+7293+7315+7410+7448+7480+7497+7524+7644+7735+7752+7854+7956+7980+8008+8085+8151+8190+8330+8360+8379+8398+8415+8568+8580+8645+8778+8820+8840+8892+9009+9044+9163+9240+9282+9310+9405+9555+9576+9690+9702+9724+9880+9945+9996+10010+10241+10296+10374+10472+10659+10710+10780+10829+10868+10920+11115+11172+11220+11305+11466+11628+11704+11781+11970+12012+12103+12155+12376+12495+12540+12597+12740+12870+12920+12936+13090+13167+13260+13464+13566+13585+13832+13860+13923+13965+14014+14212+14280+14535+14586+14630+14820+14994+15015+15048+15288+15470+15561+15708+15827+15912+15960+16170+16302+16380+16660+16758+16796+16830+17017+17160+17290+17556+17640+17765+17784+18018+18088+18326+18564+18620+18810+19019+19110+19380+19404+19448+19635+19890+19992+20020+20349+20482+20748+20995+21021+21318+21420+21560+21658+21736+21879+21945+22230+22344+22440+22610+22932+23205+23256+23562+23940+24024+24206+24255+24310+24453+24871+24990+25080+25194+25480+25740+25935+26180+26334+26520+27132+27170+27489+27720+27846+27930+28028+28424+28665+29070+29172+29260+29393+29640+29988+30030+30723+30940+31122+31416+31654+31977+32340+32487+32604+32760+33320+33516+33592+33660+33915+34034+34580+35035+35112+35530+36036+36309+36465+36652+37128+37240+37485+37620+37791+38038+38220+38760+38808+39270+39780+40040+40698+40755+40964+41496+41895+41990+42042+42636+42840+43316+43758+43890+44460+45045+45220+45815+45864+46189+46410+47124+47481+47880+48412+48510+48620+48906+49742+49980+50388+51051+51205+51480+51870+52360+52668+53295+54145+54264+54340+54978+55692+55860+56056+57057+57330+58140+58344+58520+58786+58905+59976+60060+60515+61446+61880+62244+62985+63063+63308+63954+64680+64974+65208+65835+67032+67320+67830+68068+69160+69615+70070+71060+72072+72618+72930+73304+74613+74970+75240+75582+76076+76440+77805+78540+79135+79560+81396+81510+81928+82467+83790+83980+84084+85085+85272+86632+87516+87780+88179+88920+90090+90440+91630+92169+92378+92820+94248+94962+95095+96824+97020+97240+97461+97812+99484+99960+100776+101745+102102+102410+103740+105105+105336+106590+108290+108680+108927+109395+109956+111384+111720+114114+114660+116280+117572+117810+119119+120120+121030+122265+122892+124355+124488+125970+126126+126616+127908+129948+131670+133133+135660+136136+137445+138567+139230+140140+142120+142443+145236+145860+146965+149226+149940+151164+152152+153153+153615+155610+157080+158270+159885+162435+162792+163020+164934+167580+167960+168168+170170+171171+174097+175032+175560+176358+180180+181545+183260+184338+184756+185640+188955+189924+190190+194040+194922+195624+198968+203490+204204+204820+205751+207480+210210+213180+216580+217854+218790+219912+223839+228228+229320+230945+235144+235620+237405+238238+242060+244530+245784+248710+251940+252252+255255+255816+259896+263340+264537+266266+271320+274890+277134+278460+280280+284886+285285+290472+291720+293930+298452+299880+302328+306306+307230+311220+315315+316540+319770+323323+324870+326040+329868+335160+340340+342342+348194+352716+357357+360360+363090+366520+368676+369512+373065+377910+379848+380380+389844+399399+406980+408408+409640+411502+412335+415701+420420+426360+433160+435708+437580+440895+447678+456456+460845+461890+471240+474810+476476+484120+487305+489060+497420+503880+504504+510510+522291+526680+529074+532532+544635+549780+554268+556920+569772+570570+587860+595595+596904+612612+614460+617253+622440+630630+633080+639540+646646+649740+659736+665665+680680+684684+692835+696388+705432+712215+714714+726180+737352+746130+755820+760760+765765+779688+798798+813960+823004+824670+831402+840840+855855+870485+871416+875160+881790+895356+921690+923780+949620+952952+969969+974610+978120+994840+1021020+1028755+1044582+1058148+1065064+1072071+1089270+1099560+1108536+1119195+1139544+1141140+1175720+1191190+1198197+1225224+1228920+1234506+1261260+1279080+1293292+1299480+1322685+1331330+1369368+1385670+1392776+1424430+1429428+1452360+1492260+1511640+1531530+1566873+1597596+1616615+1646008+1649340+1662804+1711710+1740970+1763580+1786785+1790712+1843380+1847560+1851759+1899240+1939938+1949220+1996995+2042040+2057510+2078505+2089164+2116296+2144142+2178540+2238390+2263261+2282280+2382380+2396394+2469012+2522520+2586584+2611455+2645370+2662660+2771340+2848860+2858856+2909907+2984520+3063060+3086265+3133746+3195192+3233230+3298680+3325608+3423420+3481940+3527160+3573570+3686760+3703518+3879876+3898440+3993990+4115020+4157010+4178328+4288284+4357080+4476780+4526522+4764760+4792788+4849845+4938024+5222910+5290740+5325320+5360355+5542680+5697720+5819814+5990985+6126120+6172530+6267492+6466460+6789783+6846840+6963880+7147140+7407036+7759752+7834365+7987980+8230040+8314020+8576568+8953560+9053044+9258795+9585576+9699690+10445820+10581480+10720710+11316305+11639628+11981970+12345060+12534984+12932920+13579566+14294280+14549535+14814072+15668730+15975960+16628040+18106088+18517590+19399380+20369349+20891640+21441420+22632610+23279256+23963940+24690120+27159132+29099070+31337460+33948915+37035180+38798760+40738698+42882840+45265220+47927880+54318264+58198140+62674920+67897830+74070360+81477396+90530440+101846745+116396280+135795660+162954792+203693490+271591320+407386980 = 3218637240'),
]

@curl_grading.timeout(8)
def ask_divisorsum(process,case):
    process.stdin.write(case+'\n')
    process.stdin.flush()
    return process.stdout.readline().strip()

def trunc(fullanswer,N):
    "show the first N and last N of an answer"
    return fullanswer[:N]+"....."+fullanswer[-N:]

def check(answer,youranswer,case):
    res = ""
    youranswer_nospace = youranswer.replace(" ","")
    answer_nospace =  answer.replace(" ", "")
    if '\b' in youranswer_nospace:
        res += r"Do not use the escape sequence \b in your output."
        res += "\n"
    if youranswer_nospace != answer_nospace:
        if len(answer)>100:
            answer= trunc(answer,30)
            youranswer= trunc(youranswer,30)
        res += "problem with case {}\n correct: {}\n   yours: {}\n".format(case,repr(answer),repr(youranswer))

    return res

def divsumtest(self,thetest,testcases):
   points_per_case = self.Points[thetest]/len(testcases)
   self.Points[thetest] = 0 

   for case,answer in testcases:
          with self.subTest(CASE=case):
              try:
                val = check(answer, ask_divisorsum(self.process,case), case)
              except curl_grading.TimeoutException as e:
                self.process = Popen([self.executable],**self.popen_specs)

                self.fullfail(thetest,f"Timeout {e}")
              if val:
                  self.fullfail(thetest,val)
              self.Points[thetest] += points_per_case


class DivisorsumTestCase(unittest.TestCase):
    "hw5_divsum.cpp"
    def fullfail(self,test,msg):
      self.Points[test] = 0
      self.fail(msg)

    @classmethod
    def setUpClass(cls):
        cls.Penalty = {'authors':100,'libraries':100,'brackets':30}
        cls.Points = {"small":40,'big':40,"prime":20}
        cls.MaxPoints = cls.Points
        cls.testorder=['authors','libraries','brackets','small',"prime",'big']
        cls.refcode = {'lines':23,'words':72}
        cls.realfilename = tested_programs[cls.__doc__]
        cls.valid_includes = set(['iostream','cstdint'])
        cls.msgs = []
        cls.authorlimit = 2
        cls.check_code = False

        rc,errors = curl_grading.compile(cls,"st3_divsum")
        if rc:
            raise unittest.SkipTest("Compile failed.\n"+str(errors))

        cls.popen_specs={'stdout':PIPE,'stdin':PIPE,'universal_newlines':True}
        cls.process = Popen([cls.executable],**cls.popen_specs)

        time.sleep(0.02)
        return_code = cls.process.poll()
        if return_code:
            cls.fail('Your program exited with return code {}.'.format(return_code))


    test_libraries = curl_grading.test_libraries
    test_authors = curl_grading.test_authors
    test_brackets = curl_grading.bracket_check


    def test_s(self):
        "small. simple small numbers"
        divsumtest(self,"small",smalldivsumTests)

    def test_b(self):
        "big. big number challenge"
        divsumtest(self,"big",bigdivsumTests)
    
    def test_p(self):
        "prime. prime numbers"
        divsumtest(self,"prime",primedivsumTests)
    
    
    @classmethod
    def tearDownClass(cls):
        cls.process.communicate('0\n',timeout=1)
        os.remove(cls.executable)
        #curl_grading.stylegrade(cls)


COURSE = 'EC602'

programs = ['hw5_divsum.cpp']

tested_programs = {x:x for x in programs}



testcases={'hw5_divsum.cpp':DivisorsumTestCase}

if __name__ == '__main__':
    s= ' (HW5 Checker Version {0}.{1})'.format(*VERSION)
    g={}
    for prog in testcases:
        print('\n\nHW5 checker version',VERSION,"checking",prog)
        testcases[prog].program = prog
        report, g[prog] = curl_grading.check_program(testcases[prog],versioninfo=s,course=COURSE)
        print(report)
    print('\nGrade Summary for HW5')
    print("=====================")
    for prog in testcases:
      print(prog,f"{g[prog]:5.1f}")