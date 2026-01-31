import cirq
from bloqade import cirq_utils
from bloqade.cirq_utils.noise import (
    GeminiOneZoneNoiseModel,
    GeminiTwoZoneNoiseModel
)
from bloqade.cirq_utils.noise.transform import transform_circuit
import numpy as np
import numpy as np

def _cirq_gemini_one_zone_noise(circuit: cirq.Circuit, scaling_factor: float = 1.0):
    "Exports Squin code to Cirq and returns a noisy circuit using GeminiOneZoneNoiseModel"
    noise_model = GeminiOneZoneNoiseModel(scaling_factor=scaling_factor)
    noisy_circuit = circuit.with_noise(noise_model)
    return noisy_circuit


def _cirq_gemini_two_zone_noise(circuit: cirq.Circuit, scaling_factor: float = 1.0):
    "Exports Squin code to Cirq and returns a noisy circuit using GeminiTwoZoneNoiseModel"
    noise_model = GeminiTwoZoneNoiseModel(scaling_factor=scaling_factor)
    noisy_circuit = circuit.with_noise(noise_model)
    return noisy_circuit


def analyze_noise_channels(ker, noise_source, noise_model = _cirq_gemini_two_zone_noise):
    """Tests importance of different noise channels"""
    
    ### Uses a Cirq backend
    if noise_source == "cirq_heuristic_model":
        clean_circuit = cirq_utils.emit_circuit(ker)
        noisy_circuit = transform_circuit(clean_circuit, noise_model)
        simulator = cirq.DensityMatrixSimulator()
        result = simulator.simulate(noisy_circuit)
        return result
    
    ### Uses a QuEra tsim backend
    if noise_source == "custom":
        clean_circuit = ker
        sampler = clean_circuit.compile_sampler()
        samples = sampler.sample(shots=100)
        return samples

    raise ValueError("Unknown parameters")

ker = None # Replace with Pranav's stuff
print(analyze_noise_channels(ker, _cirq_gemini_two_zone_noise))
