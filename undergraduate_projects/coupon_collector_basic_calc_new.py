# Coupon collector basic calculators
import numpy as np
n = int(input ('Number of unique items: '))
if n<=0:
    n = int(input ('Input a valid positive number of unique items: '))
#E(X)
#Numeric
def numeric_expect(n):
    k = np.arange(1, n+1)
    harmonic_n = np.sum(1.0 / k)
    num_expect = n*harmonic_n
    return num_expect
#Approximate
def approx_expect(n):
    gamma = 0.577216
    exp_log = np.log(n) + gamma
    apx_exp = n*exp_log + (0.5)
    return apx_exp

#Var(X)
#Numeric
def numeric_variance(n):
    k = np.arange(1, n+1)
    harmonic_n = np.sum(1.0 / k)
    harmonic_n_sqaured = np.sum(1.0 / (k**2))
    num_var = (n**2)*(harmonic_n_sqaured)-(n*harmonic_n) 
    return num_var

#Approximate
def approx_variance(n):
    gamma = 0.577216
    var_log = np.log(n) + gamma
    m = (np.pi**2)/6
    apx_var = m*(n**2)-n*var_log - (0.5)
    return apx_var

if n >= 100:
    decide = int(input ("Large n entered, approximation recommended.\nWhich method? ('0' for numeric, '1' for approximation, '2' for both)\n"))
    if decide == 1:    
        a_exp = approx_expect(n)
        a_var = approx_variance(n)
        print (f"\nApproximate expected value: {np.round(a_exp)}")
        print (f"\nApproximate variance of: {np.round(a_var, 2)}\n")
    elif decide == 0:
        n_exp = numeric_expect(n)
        n_var = numeric_variance(n)
        print (f"\nNumeric expected value: {np.round(n_exp)}")
        print (f"\nNumeric variance: {np.round(n_var, 2)}\n")
    elif decide == 2:
        n_exp = numeric_expect(n)
        n_var = numeric_variance(n)
        a_exp = approx_expect(n)
        a_var = approx_variance(n)
        print (f"\nNumeric expected value: {np.round(n_exp)}")
        print (f"\nNumeric variance: {np.round(n_var, 2)}")
        print (f"\nApproximate expected value: {np.round(a_exp)}")
        print (f"\nApproximate variance of: {np.round(a_var, 2)}\n")

if n < 100:
    decide = int(input ("Small n entered, numeric recommended.\nWhich method? ('0' for numeric, '1' for approximation, '2' for both)\n"))
    if decide == 1:    
        a_exp = approx_expect(n)
        a_var = approx_variance(n)
        print (f"\nApproximate expected value: {np.round(a_exp)}")
        print (f"\nApproximate variance of: {np.round(a_var, 2)}\n")
    elif decide == 0:
        n_exp = numeric_expect(n)
        n_var = numeric_variance(n)
        print (f"\nNumeric expected value: {np.round(n_exp)}")
        print (f"\nNumeric variance: {np.round(n_var, 2)}\n")
    elif decide == 2:
        n_exp = numeric_expect(n)
        n_var = numeric_variance(n)
        a_exp = approx_expect(n)
        a_var = approx_variance(n)
        print (f"\nNumeric expected value: {np.round(n_exp)}")
        print (f"\nNumeric variance: {np.round(n_var, 2)}")
        print (f"\nApproximate expected value: {np.round(a_exp)}")
        print (f"\nApproximate variance of: {np.round(a_var, 2)}\n")

    