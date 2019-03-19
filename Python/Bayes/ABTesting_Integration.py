#Bayesian AB testing formulas
#Derived here http://www.evanmiller.org/bayesian-ab-testing.html#binary_ab_derivation

import numpy as np
import scipy.special as sp

def probability_B_beats_A_v1(alpha_a, beta_a, alpha_b, beta_b):
    total = 0.0
    for i in range(0, alpha_b):
        total = total + np.exp(sp.betaln(alpha_a+i, beta_a+beta_b)
                               - np.log(beta_b+i)
                               - sp.betaln(1+i, beta_b)
                               - sp.betaln(alpha_a, beta_a))
    return total
    
def probability_B_beats_A_v2(alpha_a, beta_a, alpha_b, beta_b):
    total = 0.0
    for i in range(0, alpha_a):
        total = total + (np.exp(sp.betaln(alpha_b+i, beta_a+beta_b)
                               - np.log(beta_a+i)
                               - sp.betaln(1+i, beta_a)
                               - sp.betaln(alpha_b, beta_b)))
    return 1 - total

def probability_B_beats_A_v3(alpha_a, beta_a, alpha_b, beta_b):
    total = 0.0
    for i in range(0, beta_a):
        total = total + np.exp(sp.betaln(beta_b+i, alpha_a+alpha_b)
                               - np.log(alpha_a+i)
                               - sp.betaln(1+i, alpha_a)
                               - sp.betaln(alpha_b, beta_b))
    return total
    
def probability_B_beats_A_v4(alpha_a, beta_a, alpha_b, beta_b):
    total = 0.0
    for i in range(0, beta_b):
        total = total + np.exp(sp.betaln(beta_a+i, alpha_a+alpha_b)
                               - np.log(alpha_b+i)
                               - sp.betaln(1+i, alpha_b)
                               - sp.betaln(alpha_a, beta_a))
    return 1 - total

#According to http://varianceexplained.org/r/bayesian_ab_baseball/ I should be getting close to 0.608 (0.003 off because of
#precision differences with r/python)
if __name__ == "__main__":
    print(probability_B_beats_A_v1(3847, 8812, 2203, 5003)) #0.6053639618240768
    print(probability_B_beats_A_v2(3847, 8812, 2203, 5003)) #0.6053639618240768
    print(probability_B_beats_A_v3(3847, 8812, 2203, 5003)) #0.6053639618240768
    print(probability_B_beats_A_v4(3847, 8812, 2203, 5003)) #0.6053639618240768
