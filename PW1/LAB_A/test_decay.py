"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
import math
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised? Answer: I am using pytest.raises method
#   NumPY also gives a ValueError, so I add match in order to detect our own error.

def test_rejects_negative_rate():
    with pytest.raises(ValueError, match="lam must be >= 0"):
        simulate(1000, -0.4)


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance? Answer: pytest.approx() method

def test_matches_law():

    results = []

    for s in range(1000):
        results.append(simulate(1000, 0.4, seed=s)[-1])
        
    simulation_average = np.mean(results)

    assert 1000 * math.exp(-0.4 * 0.05 * 200) == pytest.approx(simulation_average, abs=1.0)