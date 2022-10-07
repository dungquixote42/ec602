# when

# positional only: cos(x)
#
# default: positional or keyword.
#
# keyword only: where using position would be confusing

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
   print(pos1,pos2)
   print(pos_or_kwd)
   print(kwd1,kwd2)


f(5,6,12,kwd1='one',kwd2="two")

def f(pos_or_kwd1, pos_or_kwd2, *, kwd1, kwd2):
  pass


def f(pos0, pos1, /, either1, either2):
  pass

def cos(x,/):
  print('x is position only',x)

try:
  cos(x=1)
except:
  print('not allowed')

