from bloqade import squin, stim
from kirin.dialects.ilist import IList
from noise_injection import analyze_noise_channels
import numpy as np


def MSD_encoding(theta, phi, basis="z"):

    @squin.kernel
    def parameterized_MSD_encoding():
        q = squin.qalloc(7)  # allocate qubits
        squin.u3(theta, phi, 0, q[6])
        for i in range(6):
            squin.sqrt_y_adj(q[i])
        # [squin.broadcast.sqrt_y_adj(q[i]) for i in range(5)]
        squin.cz(q[1], q[2])
        squin.cz(q[3], q[4])
        squin.cz(q[5], q[6])
        squin.sqrt_y(q[6])
        squin.cz(q[0], q[3])
        squin.cz(q[2], q[5])
        squin.cz(q[4], q[6])
        for i in range(5):
            squin.sqrt_y(q[i + 2])
        # [squin.broadcast.sqrt_y(q[i+2]) for i in range(5)]
        squin.cz(q[0], q[1])
        squin.cz(q[2], q[3])
        squin.cz(q[4], q[5])
        squin.sqrt_y(q[1])
        squin.sqrt_y(q[2])
        squin.sqrt_y(q[4])
        squin.broadcast.measure(q)

    return parameterized_MSD_encoding


def MSD_encoding_X(theta, phi, basis="z"):

    @squin.kernel
    def parameterized_MSD_encoding():
        q = squin.qalloc(7)  # allocate qubits
        squin.u3(theta, phi, 0, q[6])
        for i in range(6):
            squin.sqrt_y_adj(q[i])
        # [squin.broadcast.sqrt_y_adj(q[i]) for i in range(5)]
        squin.cz(q[1], q[2])
        squin.cz(q[3], q[4])
        squin.cz(q[5], q[6])
        squin.sqrt_y(q[6])
        squin.cz(q[0], q[3])
        squin.cz(q[2], q[5])
        squin.cz(q[4], q[6])
        for i in range(5):
            squin.sqrt_y(q[i + 2])
        # [squin.broadcast.sqrt_y(q[i+2]) for i in range(5)]
        squin.cz(q[0], q[1])
        squin.cz(q[2], q[3])
        squin.cz(q[4], q[5])
        squin.sqrt_y(q[1])
        squin.sqrt_y(q[2])
        squin.sqrt_y(q[4])
        squin.broadcast.h(q)
        squin.broadcast.measure(q)

    return parameterized_MSD_encoding


# MSD_enc = MSD_encoding_X(np.pi, 0)
# stim_circ = bloqade.stim.Circuit(MSD_enc)
# sampler = stim_circ.compile_sampler()
# samples = sampler.sample(shots=100)
# result = 1 - 2 * samples.astype(int)
# import numpy as np

# print(f"ExpVal:{np.mean(np.array([i[0]*i[1]*i[5] for i in result]))}")

ker = MSD_encoding_X(np.pi, 0)
print(analyze_noise_channels(ker, "cirq_heuristic_model"))
