import pgmpy.models
import pgmpy.inference
import networkx as nx
import pylab as plt

model = pgmpy.models.BayesianModel([('Burgalary', 'Alarm'), 
                                    ('Earthquake', 'Alarm'),
                                    ('Alarm', 'Marycalls'),
                                    ('Alarm', 'Jackcalls')])

cpd_burgalary = pgmpy.factors.discrete.TabularCPD('Burgalary', 2, [[0.001], [0.999]])
cpd_earthquake = pgmpy.factors.discrete.TabularCPD('Earthquake', 2, [[0.002], [0.998]])
# Probability that Monty selects a door (0, 1, 2), when we know which door the guest has selected and we know were the price is
cpd_alarm = pgmpy.factors.discrete.TabularCPD('Alarm', 2, [[0.95, 0.94, 0.29, 0.001], 
                                                           [0.05, 0.06, 0.71, 0.999]], 
                                              evidence=['Burgalary', 'Earthquake'], 
                                              evidence_card=[2, 2])

cpd_Jack = pgmpy.factors.discrete.TabularCPD('Jackcalls', 2, [[0.90, 0.05], 
                                                           [0.10, 0.95]], 
                                              evidence=['Alarm'], 
                                              evidence_card=[2])

cpd_Mary = pgmpy.factors.discrete.TabularCPD('Marycalls', 2, [[0.70, 0.01], 
                                                           [0.30, 0.99]], 
                                              evidence=['Alarm'], 
                                              evidence_card=[2])
# Add CPDs to the network structure
model.add_cpds(cpd_burgalary, cpd_earthquake, cpd_alarm,cpd_Jack,cpd_Mary)
# Check if the model is valid, throw an exception otherwise
model.check_model()
# Print probability distributions
print('Probability distribution, P(Burgalary)')
print(cpd_burgalary)
print()
print('Probability distribution, P(Earthquake)')
print(cpd_earthquake)
print()
print('Joint probability distribution, P(Alarm | Burglary,Earthquake)')
print(cpd_alarm)
print()

print(cpd_Jack)
print()
print(cpd_Mary)
print()

plt.close()
