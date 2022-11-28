""" heavy checker"""
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

VERSION, CURL_GRADING_VER = (2,1), (3, 1)

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




# HEAVY

def heavytest(self,thetest,testcases):
  points_per_case = self.Points[thetest]/len(testcases)
  self.Points[thetest] = 0 

  for case,answer in testcases:
    with self.subTest(CASE=case):
        try:
            T=run([self.executable,*case.split()],timeout=2)
        except TimeoutExpired as e:
            self.fullfail(thetest,f"Timeout {e}")

        stud_ans =T.returncode
        if stud_ans != int(answer):
            print(thetest,stud_ans,answer)
            self.fullfail(thetest,f"The result should be {answer}, you have {stud_ans}")

        self.Points[thetest] += points_per_case


firstheavyTests = [
  ('1 10','1'),
  ('1 4','1'),
  ('1 132','1'),
  ('2 402','0')
  ]
base10heavyTests=[
('4 10','0'),
('7 19','0'),
('145 10','0'),
('91 10', '1'),
('31435135 10','0')
]

otherheavyTests=[
('14500 10','0'),
('2 3','0'),
('255, 2','1'),
('255 4','1'),
('998 998','1'),
('4, 10','0'),
('41 100','0'),
] #{234, 100}, {124, 100}, {22357, 1000}, {1049, 1000}};



class heavyTestCase(unittest.TestCase):
    "heavy.cpp"
    def fullfail(self,test,msg):
      self.Points[test] = 0
      self.fail(msg)

    @classmethod
    def setUpClass(cls):
        cls.Penalty = {'authors':100,'libraries':100,'brackets':50}
        cls.Points = {"first":50,'base10':20,'other':20,"style":10}
        cls.MaxPoints = cls.Points.copy()
        cls.refcode = {'lines':26,'words':95}
        cls.realfilename = tested_programs[cls.__doc__]
        cls.valid_includes = set(['vector','string'])
        cls.msgs = []
        cls.authorlimit = 2

        rc,errors = curl_grading.compile(cls,"st3_heavy")
        if rc:
            raise unittest.SkipTest("Compile failed.\n"+str(errors))


    test_libraries = curl_grading.test_libraries
    test_authors = curl_grading.test_authors
    test_style = curl_grading.test_style
    test_brackets = curl_grading.bracket_check

    def test_h(self):
        "first. some first tests"
        heavytest(self,"first",firstheavyTests)

    def test_b(self):
        "base10. some base 10 tests"
        heavytest(self,"base10",base10heavyTests)

    def test_o(self):
        "other. some other tests"
        heavytest(self,"other",otherheavyTests)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(cls.executable)
        curl_grading.stylegrade(cls)


COURSE = 'EC602'

programs = ["heavy.cpp"]

tested_programs = {x:x for x in programs}


testcases={
'heavy.cpp':heavyTestCase}


if __name__ == '__main__':
    s= ' (HW8 Checker Version {0}.{1})'.format(*VERSION)
    g={}
    for prog in testcases:
        print('\n\nHW8 checker version',VERSION,"checking",prog)
        testcases[prog].program = prog
        report, g[prog] = curl_grading.check_program(testcases[prog],versioninfo=s,course=COURSE)
        print(report)
    print('\nGrade Summary for HW8')
    print("=====================")
    for prog in testcases:
      print(prog,f"{g[prog]:5.1f}")