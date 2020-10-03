import sys
import itertools
from fractions import Fraction

if __name__ == '__main__':
    urn1=4*['R']+3*['B']
    urn2=5*['R']+4*['B']
    urn3=4*['R']+4*['B']


    p1=Fraction(urn1.count('R'),len(urn1))
    p2=Fraction(urn2.count('R'),len(urn2))
    p3=Fraction(urn3.count('R'),len(urn3))

    prob=(p1*p2*(1-p3)+p1*(1-p2)*p3+(1-p1)*p2*p3)
    print(prob)

    #Inefficient implmentation by using product
    tf=[x.count('R')==2 for x in (list(itertools.product(urn1,urn2,urn3)))]
    print(Fraction(tf.count(True),len(tf)))


