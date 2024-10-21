####################################
# Exercise 1: Propositional logic
####################################
print("####################################")
print("EXERCISE 1: Propositional logic")
print("####################################")
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies,Equivalent
from sympy.logic.inference import satisfiable

L, S, W, A, R, F = symbols('L S W A R F')
knowledge_base = And(
    Implies(L,S), #If the mission landed on the Lunar surface, then it collected soil samples
    Equivalent(W,S), #The mission found evidence of water if and only if it collected soil samples
    Implies(A, Not(R)), #If the mission detected an anomalous signal, then it did not successfully return to Earth
    Equivalent(F, And(L,R)), #The mission was considered a full success if and only if it landed on the lunar surface and succesfully returned to Earth
    Or(A,R), #Either the mission detected an anomalous signal or it successfully returned to Earth
    Not(And(A,R)), #But not both (A and R)
    Not(W) #The mission did not find evidence of water
)
print("Base de conocimeintos: ", knowledge_base)
solution = satisfiable(knowledge_base)
print("Satisfiable: ", solution)

####################################
# Exercise 2: First order logic
####################################
print("####################################")
print("EXERCISE 2: First order logic")
print("####################################")
from z3 import *

# Define books, authors, genres, and availability
Books = DeclareSort('Books')
Authors = DeclareSort('Authors')
Genres = DeclareSort('Genres')

# Declare constants for books
pride_and_prejudice = Const('Pride_and_Prejudice', Books)
moby_dick = Const('Moby_Dick', Books)
to_kill_a_mockingbird = Const('To_Kill_a_Mockingbird', Books)

# Declare constants for authors
jane_austen = Const('Jane_Austen', Authors)
herman_melville = Const('Herman_Melville', Authors)
harper_lee = Const('Harper_Lee', Authors)

# Declare constants for genres
romance = Const('Romance', Genres)
adventure = Const('Adventure', Genres)
classic = Const('Classic', Genres)

# Declare predicates
is_book = Function('is_book', Books, BoolSort())
is_author = Function('is_author', Authors, BoolSort())
has_genre = Function('has_genre', Books, Genres, BoolSort())
written_by = Function('written_by', Books, Authors, BoolSort())
is_available = Function('is_available', Books, BoolSort())
is_fiction = Function('is_fiction', Books, BoolSort())

# Create a solver instance
s = Solver()

# Add constraints based on the problem description

# All books must have at least one author and one genre
s.add(is_book(pride_and_prejudice), is_book(moby_dick), is_book(to_kill_a_mockingbird))

a = Const('a', Authors)
s.add(written_by(pride_and_prejudice, jane_austen))
s.add(written_by(moby_dick, herman_melville))
s.add(written_by(to_kill_a_mockingbird, harper_lee))
s.add(ForAll([a], Implies(written_by(pride_and_prejudice, a), a == jane_austen)))
s.add(ForAll([a], Implies(written_by(moby_dick, a), a == herman_melville)))
s.add(ForAll([a], Implies(written_by(to_kill_a_mockingbird, a), a == harper_lee)))

# Each book must have one genre
s.add(has_genre(pride_and_prejudice, romance))
s.add(has_genre(moby_dick, adventure))
s.add(has_genre(to_kill_a_mockingbird, classic))

# Availability of the books (To Kill a Mockingbird is available, others are not specified)
s.add(is_available(to_kill_a_mockingbird)) # BA: Asumo que está disponible
s.add(Not(is_available(pride_and_prejudice)))  # BA: Asumo que no está disponible
s.add(Not(is_available(moby_dick)))  # BA: Asumo que no está disponible

# Fiction or Non-fiction
s.add(is_fiction(pride_and_prejudice))
s.add(is_fiction(moby_dick))
s.add(is_fiction(to_kill_a_mockingbird))

# Check if the conditions are satisfiable
if s.check() == sat:
    model = s.model()
    print("The conditions are satisfiable.")
    print(f"Is Pride and Prejudice a book?: {model.evaluate(is_book(pride_and_prejudice))}")
    print(f"Did Jane Austen write Moby Dick?: {model.evaluate(written_by(moby_dick,jane_austen,))}")
    print(f"Is To Kill a Mockinbird available?: {model.evaluate(is_available(to_kill_a_mockingbird))}")
    b = Const('b', Books)
    print(f"Is there a romance book in the catalog?: {model.evaluate(Exists(b, And(is_book(b), has_genre(b, romance))))}")
    print(f"Are all books in the catalog fiction?: {model.evaluate(ForAll(b, Implies(is_book(b), is_fiction(b))))}")
else:
    print("The conditions are not satisfiable.")

####################################
# Exercise 3: Fuzzy Logic
####################################
print("####################################")
print("EXERCISE 3: Fuzzy logic")
print("####################################")
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
budget = ctrl.Antecedent(np.arange(0, 11, 1), 'budget')
physical_activity = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_activity')
cultural_interest = ctrl.Antecedent(np.arange(0, 11, 1), 'cultural_interest')
temperature = ctrl.Antecedent(np.arange(0, 11, 1), 'temperature')
trip_duration = ctrl.Antecedent(np.arange(0, 11, 1), 'trip_duration')

# Output variable
activity = ctrl.Consequent(np.arange(0, 11, 1), 'activity')

# Membership functions for inputs
budget['low'] = fuzz.trimf(budget.universe, [0, 0, 5])
budget['medium'] = fuzz.trimf(budget.universe, [3, 5, 7])
budget['high'] = fuzz.trimf(budget.universe, [5, 10, 10])
physical_activity['low'] = fuzz.trimf(physical_activity.universe, [0, 0, 5])
physical_activity['medium'] = fuzz.trimf(physical_activity.universe, [3, 5, 7])
physical_activity['high'] = fuzz.trimf(physical_activity.universe, [5, 10, 10])
cultural_interest['low'] = fuzz.trimf(cultural_interest.universe, [0, 0, 5])
cultural_interest['medium'] = fuzz.trimf(cultural_interest.universe, [3, 5, 7])
cultural_interest['high'] = fuzz.trimf(cultural_interest.universe, [5, 10, 10])
temperature['cool'] = fuzz.trimf(temperature.universe, [0, 0, 4])
temperature['warm'] = fuzz.trimf(temperature.universe, [3, 5, 7])
temperature['hot'] = fuzz.trimf(temperature.universe, [6, 10, 10])
trip_duration['short'] = fuzz.trimf(trip_duration.universe, [0, 0, 4])
trip_duration['medium'] = fuzz.trimf(trip_duration.universe, [3, 5, 7])
trip_duration['long'] = fuzz.trimf(trip_duration.universe, [6, 10, 10])

# Membership functions for outputs
activity['beach'] = fuzz.trimf(activity.universe, [0, 0, 2])
activity['mountain'] = fuzz.trimf(activity.universe, [1, 3, 5])
activity['cultural_city'] = fuzz.trimf(activity.universe, [4, 6, 8])
activity['theme_park'] = fuzz.trimf(activity.universe, [7, 10, 10])

# Define fuzzy rules
rule1 = ctrl.Rule(
    budget['high'] & physical_activity['low'] & cultural_interest['high'] & temperature['warm'] & trip_duration[
        'medium'], activity['cultural_city'])
rule2 = ctrl.Rule(budget['low'] & physical_activity['high'] & temperature['cool'] & trip_duration['short'],
                  activity['mountain'])
rule3 = ctrl.Rule(budget['medium'] & physical_activity['medium'] & cultural_interest['medium'] & temperature['hot'],
                  activity['theme_park'])
rule4 = ctrl.Rule(budget['high'] & physical_activity['high'] & temperature['cool'] & trip_duration['long'],
                  activity['mountain'])
rule5 = ctrl.Rule(budget['low'] & physical_activity['low'] & temperature['warm'], activity['beach'])
rule6 = ctrl.Rule(
    budget['medium'] & physical_activity['medium'] & cultural_interest['medium'] & temperature['cool'] & trip_duration[
        'medium'], activity['mountain'])
rule7 = ctrl.Rule(budget['high'] & cultural_interest['medium'] & temperature['hot'] & trip_duration['long'],
                  activity['cultural_city'])
rule8 = ctrl.Rule(budget['medium'] & physical_activity['low'] & temperature['hot'] & trip_duration['short'],
                  activity['beach'])
rule9 = ctrl.Rule(budget['high'] & physical_activity['low'] & cultural_interest['low'] & temperature['warm'],
                  activity['theme_park'])
rule10 = ctrl.Rule(budget['low'] & physical_activity['low'] & cultural_interest['medium'] & temperature['cool'],
                   activity['mountain'])


activity_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
activity_sim = ctrl.ControlSystemSimulation(activity_ctrl)

def recommend_activity(budget_val, physical_activity_val, cultural_interest_val, temperature_val, trip_duration_val):
    activity_sim.input['budget'] = budget_val
    activity_sim.input['physical_activity'] = physical_activity_val
    activity_sim.input['cultural_interest'] = cultural_interest_val
    activity_sim.input['temperature'] = temperature_val
    activity_sim.input['trip_duration'] = trip_duration_val

    activity_sim.compute()

    output = activity_sim.output['activity']

    if output <= 2:
        return "Beach"
    elif output <= 5:
        return "Mountain"
    elif output <= 8:
        return "Cultural City"
    else:
        return "Theme Park"

recommendation = recommend_activity(4, 2, 9, 6, 5)
print(f"Recommended activity: {recommendation}")