#Only to be used with large parameters when Beta can be approximated to the Normal Distribution

import numpy as np
import scipy.stats as ss

def probability_B_beats_A_approx(alpha_a, beta_a, alpha_b, beta_b):
    mean_a = alpha_a/(alpha_a+beta_a)
    mean_b = alpha_b/(alpha_b+beta_b)
    var_a = alpha_a*beta_a/(((alpha_a+beta_a)**2)*(alpha_a+beta_a+1))
    var_b = alpha_b*beta_b/(((alpha_b+beta_b)**2)*(alpha_b+beta_b+1))
    x = mean_b-mean_a #Derived by using z-score formula and solving for x
    return 1-ss.norm.cdf(0, mean_b-mean_a, np.sqrt(var_b+var_a))
    
if __name__ == "__main__":
    print(probability_B_beats_A_approx(3847, 8812, 2203, 5003)) #0.60577266042249
