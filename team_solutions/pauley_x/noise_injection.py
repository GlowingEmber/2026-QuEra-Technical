import cirq
from bloqade import cirq_utils
from bloqade.cirq_utils.noise import (
    GeminiOneZoneNoiseModel,
    GeminiTwoZoneNoiseModel,
    GeminiOneZoneNoiseModelConflictGraphMoves,
)


def _apply_gemini_one_zone_noise(circuit: cirq.Circuit, scaling_factor: float = 1.0):
    noise_model = GeminiOneZoneNoiseModel(scaling_factor=scaling_factor)
    noisy_circuit = circuit.with_noise(noise_model)

    return noisy_circuit


def _apply_gemini_two_zone_noise(circuit: cirq.Circuit, scaling_factor: float = 1.0):
    noise_model = GeminiTwoZoneNoiseModel(scaling_factor=scaling_factor)
    noisy_circuit = circuit.with_noise(noise_model)

    return noisy_circuit


def _apply_custom_noise_model(
    circuit: cirq.Circuit,
    single_q_err: float,
    two_q_err: float,
    move_err: float,
):
    # noise_model

    # return noise_model.apply_to_circuit(circuit)
    return NotImplementedError()


def noise_injection_squin_to_cirq(ker):
    """
    Convert a Squin kernel to Cirq and apply heuristic noise model.
    """
    cirq_circuit = cirq_utils.emit_circuit(ker)
    noisy_circuit = _apply_gemini_one_zone_noise(cirq_circuit)

    return noisy_circuit


def analyze_noise_channels(circuit: cirq.Circuit):
    """
    Print detailed noise model information for different noise channels.

    This shows the error rates for:
    - Local gates
    - Global gates
    - CZ gates (paired and unpaired)
    - Move operations
    - Sit operations
    """
    noise_model = GeminiOneZoneNoiseModel()

    print("=== Gemini One-Zone Noise Model ===\n")

    print("Local Single-Qubit Gate Errors:")
    print(f"  Pauli Rates: {noise_model.local_pauli_rates}")
    print()

    print("Global Single-Qubit Gate Errors (parallel operations):")
    print(f"  Pauli Rates: {noise_model.global_pauli_rates}")
    print()

    print("CZ Paired Gate Errors (correlated):")
    print(f"  Pauli Rates: {noise_model.cz_paired_pauli_rates}")
    print()

    print("CZ Unpaired Gate Errors:")
    print(f"  Pauli Rates: {noise_model.cz_unpaired_pauli_rates}")
    print()

    print("Move Operation Errors (atom shuttling):")
    print(f"  Pauli Rates: {noise_model.mover_pauli_rates}")
    print()

    print("Sit Operation Errors (idle time):")
    print(f"  Pauli Rates: {noise_model.sitter_pauli_rates}")
    print()
