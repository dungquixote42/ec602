""" convertbase checker"""
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
# 2.2 disable code analysis

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

# CONVERTBASE

normalconvertbaseTests = [
  ('11011 2 10',b'27'),
  ('123456 8 5',b"2332143")
  ]

harderconvertbaseTests = [
  ('abc 100 2',b'1111000110111001011'),
  ('<A;>B 20 18',b'11;634'),
  (';; 12 10', b'143'),
  ('4291289 10 80',b'8NY9'),
  ('4291289 10 200',b'\x9bh\x89'),
  ('101 200 2',b'1001110001000001')
  ]

def cbasetest(self,thetest,testcases):
    points_per_case = self.Points[thetest]/len(testcases)
    self.Points[thetest] = 0 
    for case,answer in testcases:
        with self.subTest(CASE=case):
            try:
                T=run([self.executable,*case.split()],stdout=PIPE,timeout=2)
            except TimeoutExpired as e:
                self.fullfail(thetest,f"Timeout {e}")

            stud_ans = T.stdout.strip()
            if stud_ans != answer:
                print(thetest,stud_ans,answer)
                self.fullfail(thetest,f"The result should be {answer}, you have {stud_ans}")
            self.Points[thetest] += points_per_case


class convertbaseTestCase(unittest.TestCase):
    "hw6_convertbase.cpp"
    def fullfail(self,test,msg):
      self.Points[test] = 0
      self.fail(msg)

    @classmethod
    def setUpClass(cls):
        cls.Penalty = {'authors':100,'libraries':100,'brackets':30}
        cls.Points = {"normal":60,'harder':40}
        cls.MaxPoints = cls.Points.copy()
        cls.refcode = {'lines':26,'words':103}
        cls.realfilename = tested_programs[cls.__doc__]
        cls.valid_includes = set(['iostream','string'])
        cls.msgs = []
        cls.authorlimit = 2
        cls.check_code = False

        rc,errors = curl_grading.compile(cls,"st3_convbase")
        if rc:
            raise unittest.SkipTest("Compile failed.\n"+str(errors))


    test_libraries = curl_grading.test_libraries
    test_authors = curl_grading.test_authors
    test_brackets = curl_grading.bracket_check

    def test_n(self):
        "normal. bases 10 or less"
        cbasetest(self,"normal",normalconvertbaseTests)

    def test_h(self):
        "harder. bases 10 or more"
        cbasetest(self,"harder",harderconvertbaseTests)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(cls.executable)
        #curl_grading.stylegrade(cls)



COURSE = 'EC602'

programs = ['hw6_convertbase.cpp']

tested_programs = {x:x for x in programs}


testcases={'hw6_convertbase.cpp':convertbaseTestCase}


if __name__ == '__main__':
    s= ' (HW6 Checker Version {0}.{1})'.format(*VERSION)
    g={}
    for prog in testcases:
        print('\n\nHW6 checker version',VERSION,"checking",prog)
        testcases[prog].program = prog
        report, g[prog] = curl_grading.check_program(testcases[prog],versioninfo=s,course=COURSE)
        print(report)
    print('\nGrade Summary for HW6')
    print("=====================")
    for prog in testcases:
      print(prog,f"{g[prog]:5.1f}")