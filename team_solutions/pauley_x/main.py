from bloqade import squin
from kirin.dialects.ilist import IList

@squin.kernel
def _msd_encode_state__circuit():
    q = squin.qalloc(7)
    squin.u3(0,0,0,q[6])
    for i in range(6):
        squin.sqrt_y_adj(q[i])
    squin.cz(q[1], q[2])
    squin.cz(q[3], q[4])
    squin.cz(q[5], q[6])
    squin.sqrt_y(q[6])
    squin.cz(q[0],q[3])
    squin.cz(q[2],q[5])
    squin.cz(q[4],q[6])
    for i in range(5):
        squin.broadcast.sqrt_y(q[i+2])
    squin.cz(q[0],q[1])
    squin.cz(q[2],q[3])
    squin.cz(q[4],q[5])
    squin.sqrt_y(q[1])
    squin.sqrt_y(q[2])
    squin.sqrt_y(q[4])
    squin.broadcast.measure(q)


    