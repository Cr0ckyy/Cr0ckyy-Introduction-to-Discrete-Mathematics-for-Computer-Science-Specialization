from scipy.stats import binom

# The scipy.stats.binom.pmf function is used to calculate the probability mass function of a binomial distribution,
# which is the distribution that describes the number of successes in a fixed number of independent Bernoulli trials
# (like the beans falling through the layers of the Galton board) with the same probability of success.
# The sum function is used to sum up the probabilities for all the bins from the start bin to the end bin.

# Question 1
# What is the fraction of beans that end near the center (bins 40-60 among 0-100) for the ideal Galton board with 100 layers?
num_layers_q1 = 100
start_bin_q1 = 40
end_bin_q1 = 60
prob_q1 = sum(binom.pmf(range(start_bin_q1, end_bin_q1+1), num_layers_q1, 0.5))
print(f"Answer to Question 1: The fraction of beans that end near the center (bins 40-60 among 0-100) for the ideal Galton board with 100 layers is approximately {prob_q1*100}%.")

# Question 2
# What is the fraction of beans that end near the center (bins 400-600 among 0-1000) for the ideal Galton board with 1000 layers?
num_layers_q2 = 1000
start_bin_q2 = 400
end_bin_q2 = 600
prob_q2 = sum(binom.pmf(range(start_bin_q2, end_bin_q2+1), num_layers_q2, 0.5))
print(f"Answer to Question 2: The fraction of beans that end near the center (bins 400-600 among 0-1000) for the ideal Galton board with 1000 layers is approximately {prob_q2*100}%.")
