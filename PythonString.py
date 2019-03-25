
template = '{0},{1} and {2}'
print template.format('spam','aaa','88')

template1 = '{motto},{pork} and {food}'
print template1.format(motto='spam',pork='ham',food='eggs')

template2 = '{motto},{0},{food}'
print template2.format('ham',motto='spam',food ='eggs')
X = '{motto},{0} and {food}'.format(42,motto=3.14,food=[1,2])
#print '{motto},{0} and {food}'.format(42,motto=3.14,food=[1,2])
print X.split('and')

import sys

print  'My {1[spam]} runs {0.platform}'.format(sys,{'spam':'laptop'})