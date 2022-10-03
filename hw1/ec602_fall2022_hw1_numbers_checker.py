"numbers checker"
import unittest

COURSE = 'ec602'
SEMESTER = "fall2022"
hw="HW1"

DEBUG = True

VERSION, CURL_GRADING_VER = (2,3), (3, 6)



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
('6','1+2+3 = 6'),
('28','1+2+4+7+14 = 28'),
('10','1+2+5 =8'),
('8888','1+2+4+8+11+22+44+88+101+202+404+808+1111+2222+4444 = 9472'),
('888','1+2+3+4+6+8+12+24+37+74+111+148+222+296+444 = 1392'),
('123123','1+3+7+11+13+21+33+39+41+77+91+123+143+231+273+287+429+451+533+861+1001+1353+1599+3003+3157+3731+5863+9471+11193+17589+41041 = 102669'),
]

primedivsumTests=[
('19','1 = 1'),
('29','1 = 1'),
]

bigdivsumTests=[
('8147712','1+2+3+4+6+8+12+16+24+32+48+64+96+103+128+192+206+256+309+384+412+618+768+824+1236+1648+2472+3296+4944+6592+9888+10609+13184+19776+21218+26368+31827+39552+42436+63654+79104+84872+127308+169744+254616+339488+509232+678976+1018464+1357952+2036928+2715904+4073856= 13749660')
]


def divsumtest(self,thetest,testcases):
   points_per_case = self.Points[thetest]/len(testcases)
   self.Points[thetest] = 0 

   for case,answer in testcases:
          if DEBUG:
            print('divsum',case)
          with self.subTest(CASE=case):
              try:
                val = check(answer,modtest.divisorsum(int(case)), case)
              except curl_grading.TimeoutException as e:
                self.process = Popen([self.executable],**self.popen_specs)

                self.fullfail(thetest,f"Timeout {e}")
              if val:
                  self.fullfail(thetest,val)
              self.Points[thetest] += points_per_case


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



# CONVERTBASE

normalconvertbaseTests = [
  ('11011 2 10','27'),
  ('123456 8 5',"2332143")
  ]

harderconvertbaseTests = [
  ('abc 100 2','1111000110111001011'),
  ('<A;>B 20 18','11;634'),
  (';; 12 10', '143'),
  ('4291289 10 80','8NY9'),
  ('4291289 10 200','\x9bh\x89'),
  ('101 200 2','1001110001000001')
  ]

def cbasetest(self,thetest,testcases):
    points_per_case = self.Points[thetest]/len(testcases)
    self.Points[thetest] = 0 
    for case,answer in testcases:
        if DEBUG:
            print('convertbase',case)
        with self.subTest(CASE=case):
            num2convert,frombase,tobase = case.split()

            stud_ans = modtest.convertbase(num2convert,int(frombase),int(tobase))
            if stud_ans != answer:
                print(thetest,stud_ans,answer)
                self.fullfail(thetest,f"The result should be {answer}, you have {stud_ans}")
            self.Points[thetest] += points_per_case



# HEAVY

def heavytest(self,thetest,testcases):
  points_per_case = self.Points[thetest]/len(testcases)
  self.Points[thetest] = 0 

  for case,answer in testcases:
    with self.subTest(CASE=case):
        if DEBUG:
            print('heavy',case)
        yval,baseval = case.split()
        stud_ans = modtest.heavy(int(yval),int(baseval))
        if stud_ans != answer:
            print(thetest,stud_ans,answer)
            self.fullfail(thetest,f"The result should be {answer}, you have {stud_ans}")

        self.Points[thetest] += points_per_case


firstheavyTests = [
  ('1 10',True),
  ('1 4',True),
  ('1 132',True),
  ('2 402',False)
  ]
base10heavyTests=[
('4 10',False),
('7 19',False),
('145 10',False),
('91 10', True),
('31435135 10',False)
]

otherheavyTests=[
('14500 10',False),
('2 3',False),
('255 2',True),
('255 4',True),
('998 998',True),
('4 10',False),
('41 100',False),
] #{234, 100}, {124, 100}, {22357, 1000}, {1049, 1000}};



class NumbersTestCase(unittest.TestCase):
    "hw1_numbers.py"
    def fullfail(self,test,msg):
      self.Points[test] = 0
      self.fail(msg)

    @classmethod
    def setUpClass(cls):
        cls.Penalty = {'libraries':50,'authors':100,'c':50,'w':20,'s':20}
        cls.Points = {}
        cls.Points['ds_small'] = 20
        cls.Points['ds_big'] = 5
        cls.Points['ds_prime'] = 5
        cls.Points['cb_normal'] = 15
        cls.Points['cb_harder'] = 15
        cls.Points['h_first'] = 15
        cls.Points['h_base10'] = 15
        cls.Points['h_other'] = 10

        cls.MaxPoints = cls.Points.copy() 

        cls.authorlimit = 2
        cls.valid_includes = set()
        cls.refcode = {'lines':40,'words':153}
        cls.msgs=[]
        cls.realfilename = tested_programs[cls.__doc__]

        with open(cls.realfilename) as f:
            cls.file_contents=f.read()

    
    test_libraries = curl_grading.test_libraries
    test_authors = curl_grading.test_authors
    test_style = curl_grading.test_pystyle


    def test_s(self):
        "ds_small. divisorsum: simple small numbers"
        divsumtest(self,"ds_small",smalldivsumTests)

    def test_b(self):
        "ds_big. divisorsum: big number challenge"
        divsumtest(self,"ds_big",bigdivsumTests)
    
    def test_p(self):
        "ds_prime. divisorsum: prime numbers"
        divsumtest(self,"ds_prime",primedivsumTests)
    

    def test_n(self):
        "cb_normal. convertbase: bases 10 or less"
        cbasetest(self,"cb_normal",normalconvertbaseTests)

    def test_h(self):
        "cb_harder. convertbase: bases more than 10"
        cbasetest(self,"cb_harder",harderconvertbaseTests)
    




    def test_h_first(self):
        "h_first. heavy: some first tests"
        heavytest(self,"h_first",firstheavyTests)

    def test_h_base(self):
        "h_base10. heavy: some base 10 tests"
        heavytest(self,"h_base10",base10heavyTests)

    def test_h_other(self):
        "h_other. heavy: some other tests"
        heavytest(self,"h_other",otherheavyTests)
    


#COURSE = 'EC602'

programs = ['hw1_numbers.py']

tested_programs = {x:x for x in programs}


testcases={
'hw1_numbers.py':NumbersTestCase,
}

import hw1_numbers as modtest

if __name__ == '__main__':
    s= f' ({hw}  Checker Version {VERSION[0]}.{VERSION[1]})'
    g={}

    for prog in testcases:
        print(f'\n\n{hw} checker version',VERSION,"checking",prog)
        if DEBUG:
           print('debugging info')
        testcases[prog].program = prog
        report, g[prog] = curl_grading.check_program(testcases[prog],versioninfo=s,course=COURSE)
        print(report)
    print(f'\nGrade Summary for {hw}')
    print("=====================")
    for prog in testcases:
      print(prog,g[prog])
