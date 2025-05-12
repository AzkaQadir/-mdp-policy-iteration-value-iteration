## 📈 Markov Decision Processes: Value and Policy Iteration
This repository contains various implementations of Value Iteration and Policy Iteration algorithms applied to a simple Markov Decision Process (MDP) with three states: Top, Rolling, and Bottom. Each file explores the effects of changing the environment, policies, or parameters like rewards and discount factors.

## 🧠 What is an MDP?
A Markov Decision Process is a mathematical framework used to model decision-making problems where outcomes are partly random and partly under the control of a decision-maker. It includes:
A set of states
- A set of actions
- Transition probabilities and rewards
- A policy defining actions taken in each state


## 📁 Files and Descriptions:
1. value_iteration.py


Basic implementation of the Value Iteration algorithm using the default MDP configuration.

States: Top, Rolling, Bottom

Actions: Drive, Don’t Drive

Goal: Find the optimal value function and policy by iteratively improving value estimates.

2. value_iteration_with_changed_discount.py:

Value Iteration with a modified discount factor (gamma = 0.75 instead of 0.9).

Demonstrates how a lower discount factor causes the agent to focus more on immediate rewards.

Observe changes in optimal policy and value convergence.

3. value_iteration_with_changed_transition_probabilities.py:

Value Iteration using altered transition probabilities to simulate a more uncertain environment.

Helps to analyze how changes in system dynamics affect the optimal decision-making policy.


4. value_iteration_with_changed_reward.py:

Value Iteration with updated rewards—specifically increased reward for not driving when in the Bottom state.

Illustrates how reward shaping influences the agent's behavior and policy structure.

5. policy_iteration_with_deterministic_policy.py:

Policy Iteration initialized with a deterministic policy where the agent never drives.

Applies both Policy Evaluation and Policy Improvement steps.

Tracks convergence to the optimal policy and value function.


6. policy_iteration_with_stochastic_policy.py:

Starts with a stochastic policy.

## 🔧 Environment:
- Language: Python 3
- No external libraries used other than numpy
- Can be run in Google Colab or locally in a Python environment

## 📊 Outputs:
- Each script prints:
- value function
- Optimal policy
Number of iterations until convergence

## 🚀 Learning Objectives:
- Understand and implement core dynamic programming methods in MDPs
- Analyze the effect of rewards, transitions, and discounting on optimal strategies
- Compare deterministic vs stochastic policy iteration

## 📝 Credits:
Created as part of a reinforcement learning study project to better understand planning algorithms in discrete environments.


## 📌 Disclaimer:
This project was developed as part of a personal learning journey in reinforcement learning.
As such, it may include experimental implementations, non-optimized code, or areas for improvement.
Feedback, suggestions, and contributions are always welcome!
