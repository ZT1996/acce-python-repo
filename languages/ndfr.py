class NDFR:
    """Objects representing nondeterministic finite recognizers"""

    def __init__(self, S, Q, qstart, F, T) :
        assert F.issubset(Q)
        for (q,s,r) in T:
            assert q in Q
            assert r in Q
            assert len(s) <= 1
            assert len(s) == 0 or s[0] in S
        self.S = S
        self.Q = Q
        self.qstart = qstart
        self.F = F
        self.T = T

    def __repr__( self ):
        return ( "NDFR( " + repr(self.S) + ", "
               + repr(self.Q) + ", "
               + repr(self.qstart) + ", "
               + repr(self.F) + ", "
               + repr(self.T) + " )" )

def renameStates( A,  f = 0 ) : 
    """Rename the states.
       A should be an ndfr
       f can be a dictionary that maps old states to new states.
       f can also be a list of pairs or anything else that will convert to a dictionary
       f can also be an int, in which case the states are renamed to f, f+1, f+2
       f should map each state in A.Q to a unique value
    """
    # Ensure that f is a dictionary with appropriate domain.
    if isinstance( f, int ) : f = dict( zip( A.Q, range(f, f+len(A.Q) ) ) )
    try : f = dict(f)
    except: raise AssertionError(
               "2nd arg to renameStates should be a dictionary or an integer" )
    domainOf_f = set(f.keys())
    assert A.Q.issubset( domainOf_f ), \
           "2nd arg of renameStates should map every state of A"
    # Now build the new NDFR
    newQ = { f[q] for q in A.Q }
    assert len( newQ ) == len( A.Q ), \
           "2nd arg to renameStates should map each state to a unique new state."
    newqstart = f[ A.qstart ]
    newF = { f[q] for q in A.F }
    newT = { (f[q],s,f[r]) for (q,s,r) in A.T }
    return NDFR( A.S, newQ, newqstart, newF, newT ) 

