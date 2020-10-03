import sys
import itertools
from fractions import Fraction
#https://www.hackerrank.com/challenges/s10-mcq-3/problem

""" this is my program"""
if __name__ == '__main__':
    urn1=['R', 'R', 'R', 'R', 'B', 'B', 'B']
    urn2=['R', 'R', 'R', 'R', 'R', 'B', 'B', 'B',  'B']
    urn3=['R', 'R', 'R', 'R', 'B', 'B', 'B', 'B']

    p1=Fraction(urn1.count('R'),len(urn1))
    p2=Fraction(urn2.count('R'),len(urn2))
    p3=Fraction(urn3.count('R'),len(urn3))

    prob=(p1*p2*(1-p3)+p1*(1-p2)*p3+(1-p1)*p2*p3)
    print(prob)




    tf=[x.count('R')==2 for x in (list(itertools.product(urn1,urn2,urn3)))]
    print(Fraction(tf.count(True),len(tf)))


