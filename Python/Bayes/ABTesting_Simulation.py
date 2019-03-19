import numpy as np
import scipy.stats as ss

def probability_B_beats_A_simulation(alpha_a, beta_a, alpha_b, beta_b, n_sim = 10000):
    a_sims = ss.beta.rvs(alpha_a, beta_a, size = n_sim)
    b_sims = ss.beta.rvs(alpha_b, beta_b, size = n_sim)
    return np.mean(b_sims > a_sims)
