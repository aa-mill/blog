---
title: tabular
tags:
---

# Overview of Tabular Reinforcement Learning Methods

We'll first introduce the reinforcement learning (RL) framework and Markov Decision Process formalism. The latter specifies precisely what we're trying to achieve in an RL algorithm. Once we have this, we'll focus on a subset of RL problems, called tabular problems, to examine some foundational approaches that illustrate how the RL formalism is used to solve a problem.

Broadly speaking, reinforcement learning (RL) is concerned with goal-directed learning from interaction. It considers an agent who takes actions in an environment, which in turn produces rewards and representations of the environment's state. The goal-directed component of the agent-environment interface refers to the agent's interaction with the reward process and is encapsulated in the so-called reward hypothesis, which states that

> All goals can be described as the maximization of an agent's expected return, or expected cumulative reward [1].

The reinforcement learning problem is formalized as a Markov Decision Process, which gives precise definitions of the terms we introduced loosely above.

## Markov decision process (MDP)

The following introduction to MDPs follows that of [2].

In a Markov Decision Process, an agent and its environment interact at discrete times $t = 0, 1, 2, \dots$. At time $t$, the agent perceives a representation of its state $S_t \in \mathcal{S}$ and chooses an action $A_t \in \mathcal{A}(s)$ based on that state. The state may restrict the set of available actions, as indicated by the argument of $\mathcal{A}(s)$. An agent's action is defined by a policy $\pi(A_t = a | S_t = s)$, which is a probability distribution over the set of actions available from the state $s$. At time $t + 1$, the environment returns a scalar reward $R_{t + 1} \in \mathcal{R} \subseteq \mathbb{R}$ and a representation of the next state $S_{t + 1}$, both of which may be stochastic. The result of this sequential interaction is a trajectory

$$S_0, A_0, R_1, S_1, A_1, R_2, S_2, A_2, R_3, \dots.$$

We have a finite MDP when $\mathcal{S}$, $\mathcal{A}$, and $\mathcal{R}$ are finite. The defining feature of a Markov process is that the probability distribution over $R_t$ and $S_t$ depends only on the previous state $S_t$ and the previous action $A_t$. If this is true, the state $S_t$ is said to have the Markov property, which captures the idea that the current state includes all information relevant to the present decision. As a result, the complete dynamics of an MDP are described by the function

$$p(s', r | s, a) \equiv \mathrm{Pr}(S_t = s', R_t = r | S_{t - 1} = s, A_{t - 1} = a).$$

The dynamics alone are insufficient to specify how an agent should behave in the environment. We have to be explicit about the agent's goal. Let

$$G_t \equiv \sum_{k = t + 1}^T \gamma^{k - t- 1}R_k$$

be the cumulative return that an agent receives after time $t$. Here, $\gamma$ is a discount rate that puts greater emphasis on returns that are received sooner. We adpot the unified interpretation of [2] that lets this definition of $G_t$ represent both episodic tasks, or those that can be broken into episodes that end in a terminal state $T$, and continuing tasks, which go on forever. Specifically, we represent a continuing task by choosing $T = \infty$ and $\gamma < 1$ and an episodic task by letting $T$ be a finite random variable. An important identity related to the return is $G_t = R_{t + 1} + \gamma G_{t + 1}$.

In words, the quantity that we would like an agent to optimize is the expected cumulative return (Since the rewards are random variables, so is $G_t$). A more precise statement of the optimality we seek can be made after introducing two critically important definitions.

The value function 

$$v_\pi(s) \equiv \mathbb{E}_\pi[G_t | S_t = s] = \mathbb{E}_\pi\left[\sum_{k = 0}^\infty \gamma^kR_{t + k + 1} | S_t = s\right]$$

is the expected return starting from state $s$ and following policy $\pi$ thereafter. The action value function 

$$q_\pi(s, a) \equiv \mathbb{E}_\pi[G_t | S_t = s, A_t = a] = \mathbb{E}_\pi\left[\sum_{k = 0}^\infty \gamma^kR_{t + k + 1} | S_t = s, A_t = a\right]$$

is the expected return starting from state $s$, taking action $a$, and following policy $\pi$ thereafter. In general, $\mathbb{E}_\pi[\cdot]$ denotes the expected value given that the agent follows policy $\pi$. 


We want these expected returns to be as large as possible in each state $s$, and the component an agent can change to make that happen is its policy. *So, the primary objective in an RL problem is to determine an optimal policy $\pi$.*

A policy $\pi$ is better than policy $\pi'$, denoted $\pi \ge \pi'$, if and only if $v_\pi(s) \ge v_{\pi'}(s)\ \forall s$. We define an optimal policy $\pi_*$ as a policy that is better than all others. It possible to have multiple optimal policies, but the associated optimal state-value and action-value functions, defined as

$$v_*(s) \equiv \max_\pi v_\pi(s) \quad\text{and}\quad q_*(s, a) \equiv \max_\pi q_\pi(s, a)$$

$\forall s \in \mathcal{S}$ and $a \in \mathcal{A}(s)$, respectively, are unique.

**The key statement that encapsulates the relationship between optimal policies, optimal value functions, and optimal action value functions is** 

$$v_*(s) = \max_{a \in \mathcal{A}(s)}q_*(s, a).$$

We can see this as follows. Imagine I'm in a state $s$. The action value function $q_*(s, a)$ tells me the expected return I can receive for any action $a$ available to me, i.e. in $\mathcal{A}(s)$. If I am to act optimally, I must choose the action that has the highest value of $q_*(s, a)$, for otherwise I would be limiting my expected return. Selecting an optimal action in this way is precisely the policy associated with $v_*(s)*, so the value $q_*(s, a)$ of my choice is equal to the value $v_*(s, a)$ of my current state.

At this point, we can see an obvious way of finding an optimal policy. Just choose $a \in \mathcal{A}(s)$ to maximize $q_*(s, a)$. The problem, of course, is that the values $q_*(s, a)$ aren't known. In the following sections, I will outline some fundamental approaches for determining the optimal policy. Different approaches focus on determining $v_*$, $q_*$, or $\pi_*$ directly.

### Helpful tip on identities and derivations

I want to point out some helpful tips that I've found useful for understanding many of the derivations in [2]. First, be mindful what the expectations are being taken over. Oftentimes, in going from one line to the next, the random variables that appear inside $\mathbb{E}$ change. In this case, you need to keep in mind that the sums or integrals that would appear in an explicit statement of the expected value are different. In some cases, authors are explicit about the distribution relevant to the expectation and denote it with a subscript, e.g. $\mathbb{E}_{X \sim p(x)}[X]$, but if nothing is there, it's usually safe to assume the expectation is over the joint distribution of all variables that appear in the brackets, e.g. $\mathbb{E}[f(X, Y)] = \mathbb{E}_{X,Y \sim f(x, y)}[f(X, Y)]$.

Another useful tip is to keep track of key identities that appear often. For example, an identity that's relevant for understanding Eqs. 3.17, 3.18, and 4.3 of [2], is

$$\mathbb{E}[G_{t + 1}] = \mathbb{E}[v_\pi(S_{t + 1})].$$

The proof of this is straightforward and related to the comment earlier about being mindful of the distribution used in an expectation. We have

$$\begin{align*}
\mathbb{E}[G_{t + 1}] &= \sum_gg\mathrm{Pr}(G_{t + 1} = g) \\
&= \sum_g\sum_{s'}g\mathrm{Pr}(G_{t + 1} = g \cap S_{t + 1} = s') \\
&= \sum_g\sum_{s'}g\mathrm{Pr}(G_{t + 1} = g | S_{t + 1} = s')\mathrm{Pr}(S_{t + 1} = s') \\
&= \sum_{s'}\mathbb{E}[G_{t + 1} | S_{t + 1} = s']P(S_{t + 1} = s') \\
&= \sum_{s'}v_\pi(s')P(S_{t + 1} = s') \\
&= \mathbb{E}[v_\pi(S_{t + 1})].
\end{align*}$$

## Finding an optimal policy $\pi_*$

### Direct method

### Dynamic programming (DP)

Include backup diagrams.

### Monte-Carlo

### Temporal difference (TP) learning

## References

[1] Two main approaches for solving RL problems—Hugging Face Deep RL Course. (n.d.). Retrieved January 27, 2024, from https://huggingface.co/learn/deep-rl-course/unit1/two-methods

[2] Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction (Second edition). The MIT Press.




