#Return the probability of A conditioned on B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 
#P(A)= Cancer *** P(B|A) = Positive and cancer *** Cancer and P(Not B|Not A) = No cancer and Negative
def f(p0,p1,p2):
#Insert your code here
    notP0 = 1-p0 #No cancer
    pBNotA = 1-p2 #Postive and No Cancer
    totalA = p0*p1+pBNotA*notP0
    return ((p0*p1)/totalA)
