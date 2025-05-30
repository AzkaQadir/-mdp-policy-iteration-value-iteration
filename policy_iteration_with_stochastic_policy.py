# -*- coding: utf-8 -*-
"""policy_iteration_with_stochastic_policy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ne69fQwM9RN1IrdNJwVrIAnLxgx-HlE5
"""

import numpy as np

# Define MDP Components
states = ["top", "rolling", "bottom"]
actions = ["drive", "don't drive"]
gamma = 0.9  # Discount factor
theta = 1e-6  # Convergence threshold

# Transition probabilities and rewards
transitions = {
    "top": {
        "drive": [(0.5, "top", 2), (0.5, "rolling", 2)],
        "don't drive": [(0.5, "top", 3), (0.5, "rolling", 1)]
    },
    "rolling": {
        "drive": [(0.3, "top", 2), (0.4, "rolling", 1.5), (0.3, "bottom", 0.5)],
        "don't drive": [(1.0, "bottom", 1)]
    },
    "bottom": {
        "drive": [(0.5, "top", 2), (0.5, "bottom", 2)],
        "don't drive": [(1.0, "bottom", 1)]
    }
}

# Initialize a stochastic policy with equal probabilities
policy = {state: {action: 0.5 for action in actions} for state in states}

def evaluate_policy(policy):
    values = {state: 0 for state in states}
    while True:
        delta = 0
        new_values = values.copy()
        for state in states:
            new_values[state] = sum(
                policy[state][action] * sum(prob * (reward + gamma * values[next_state])
                                            for prob, next_state, reward in transitions[state][action])
                for action in actions
            )
            delta = max(delta, abs(new_values[state] - values[state]))
        values = new_values
        if delta < theta:
            break
    return values

def improve_policy(values):
    policy_stable = True
    new_policy = {}
    for state in states:
        action_values = {
            action: sum(prob * (reward + gamma * values[next_state])
                        for prob, next_state, reward in transitions[state][action])
            for action in actions
        }
        best_action = max(action_values, key=action_values.get)
        best_action_prob = 1.0
        new_policy[state] = {action: (best_action_prob if action == best_action else 0.0) for action in actions}
        if policy[state] != new_policy[state]:
            policy_stable = False
    return new_policy, policy_stable

def policy_iteration_stochastic():
    global policy
    iterations = 0
    while True:
        values = evaluate_policy(policy)
        policy, stable = improve_policy(values)
        iterations += 1
        if stable:
            break
    return values, policy, iterations

# Run policy iteration with stochastic policy
optimal_values_stochastic, optimal_policy_stochastic, iterations_stochastic = policy_iteration_stochastic()

# Print results
print("Optimal Values (Stochastic Policy):", optimal_values_stochastic)
print("Optimal Policy (Stochastic Policy):", optimal_policy_stochastic)
print("Iterations for Convergence (Stochastic Policy):", iterations_stochastic)