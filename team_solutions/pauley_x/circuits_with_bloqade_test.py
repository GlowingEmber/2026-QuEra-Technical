from typing import Any

import numpy as np
import bloqade.types
from kirin.ir import Method
from bloqade.types import Qubit, MeasurementResult

# Some types we will use, useful for type hints
from kirin.dialects.ilist import IList

from bloqade import squin

Register = IList[Qubit, Any]

@squin.kernel
def hello_world(theta: float) -> IList[MeasurementResult, Any]:
    """
    Prepare a Bell state and measure in a basis that might have a Bell violation
    """
    qubits = squin.qalloc(2)
    squin.h(qubits[0])
    squin.cx(qubits[0], qubits[1])
    squin.rx(theta, qubits[0])
    bits = squin.broadcast.measure(qubits)
    return bits


# [kernel].print() prints the raw SSA, which is the intermediate representation of the kernel
# as used internally by Kirin.
# hello_world.print()
