---
title: Active vs. Passive Transformations
date: 2025-02-25 18:24:48
tags: Quantum mechanics
---

## Introduction

I always pause on statements like $O \to D(g)OD(g)^{\dagger}$ because I get stuck trying to reason about what transformation is actually going on. It'd be nice to look at the placement of the $\dagger$ and have a clear sense of this, so my goal here is to separate two different sets of ideas:

- Active vs. passive transformations, and
- Transformations vs. a change of basis.

The distinctions can but subtle, and many texts don't explicitly specify the convention they're using. It's also my opinion that these notions are less symmetric than many sources make them out to be.

## Active transformations

Let $Q$ be some quantum mechanical operator, and let $U$ be some unitary transformation. In an active transformation, we transform the *states* but not the *operators*, i.e.

$$
\begin{align}
\| \psi \rangle &\to U\| \psi \rangle, \\\\
\langle \psi \| &\to \langle \psi \|U^{\dagger}, \\\\
Q &\to Q.
\end{align}
$$

That is, **we're actually changing the system**. As a result, the expectation value of $Q$ changes as $\langle  \psi \| Q \| \psi  \rangle\to \langle  \psi \| U^{\dagger}QU \| \psi  \rangle$. Nothing says that these two expectation values have to be equal. After all, the state is different, so it makes sense that we could measure different values for the observable corresponding to $Q$.

Note that I didn't need to say anything about matrix elements or vector components to define an active transformation. However, if we do want to talk about these things, we can start by asking what the matrix elements of $Q$ look like. 

**The matrix elements always depend on our choice of basis**, so if we choose our basis vectors to be the transformed vectors (i.e. the images of $U$), then the matrix elements of $Q$ become

$$
\begin{pmatrix}
\langle  e\_{1} \| Q \| e\_{1}  \rangle & \langle  e\_{1} \| Q \| e\_{2}  \rangle & \cdots \\\\
\langle  e\_{2} \| Q \| e\_{1}  \rangle & \langle  e\_{2} \| Q \| e\_{2}  \rangle & \\\\
\vdots &  & \ddots
\end{pmatrix}\begin{pmatrix}
\langle  e\_{1} \| \psi  \rangle \\\\
\langle  e\_{2} \| \psi  \rangle \\\\
\vdots
\end{pmatrix}\to \begin{pmatrix}
\langle  e\_{1} \| U^{\dagger}QU \| e\_{1}  \rangle & \langle  e\_{1} \| U^{\dagger}QU \| e\_{2}  \rangle & \cdots \\\\
\langle  e\_{2} \| U^{\dagger}QU \| e\_{1}  \rangle & \langle  e\_{2} \| U^{\dagger}QU \| e\_{2}  \rangle & \\\\
\vdots &  & \ddots
\end{pmatrix}\begin{pmatrix}
\langle  e\_{1}\| \psi  \rangle \\\\
\langle  e\_{2}\| \psi  \rangle \\\\
\vdots
\end{pmatrix}.
$$

## Passive transformations

In a passive transformation, we transform the *operators* but not the *states*. We can obtain the same change in expectation values as before, namely $\langle  \psi \| Q \| \psi  \rangle\to \langle  \psi \| U^{\dagger}QU \| \psi  \rangle$, if we let

$$
\begin{align}
\| \psi \rangle &\to \| \psi \rangle , \\\\
\langle \psi \| &\to \langle \psi \|, \\\\
Q &\to U^{\dagger}QU.
\end{align}
$$

In other words, we let the operator transform such that the expectation value of the *original* operator for the *transformed* state is the same as that of the *transformed* operator on the *original* state. What I've said so far is summarized succinctly in this [comment](https://physics.stackexchange.com/questions/611187/symmetry-transformations-of-states-and-operators#:~:text=This%20does%20not,at%2014%3A51).

## Transformations

The key idea I want to emphasize is that, for both conventions, what I've so far described is a transformation of the system that *changes the physics*. That is, in general, it will be that $\langle  \psi \| Q \| \psi  \rangle \neq \langle  \psi \| U^{\dagger}QU \| \psi  \rangle$.

## Change of basis

On the other hand, with a change of basis, transforming either the states or the operator must come with a *compensatory change in the other* so that the [physics do not change](https://physics.stackexchange.com/questions/650140/is-application-of-a-unitary-operator-equivalent-to-a-phase-change-of-a-wave-func/650355#650355:~:text=When%20does%20changing%20basis%20change%20the%20physics%3F). In particular, if we actively transform the states via $\| \psi \rangle\to \| \psi' \rangle = U\| \psi \rangle$, then the operator $Q$ must also transform, namely as $Q\to Q' = UQU^{\dagger}$, such that

$$
\langle  \psi' \| Q' \| \psi'  \rangle = \langle  \psi \| U^{\dagger}(UQU^{\dagger})U \| \psi  \rangle = \langle  \psi \| Q \| \psi  \rangle.
$$

The difference between a transformation and a change of basis thus alleviates the confusion when encountering an excerpt such as "the states transform as $\| \psi \rangle\to D(g)\| \psi \rangle$, so the operators transform as $O \to D(g)OD(g)^{\dagger}$." Here, since the states and operators transform oppositely, the transformation is indicating a change of basis. Had the transformation been specified exclusively for the states (or exclusively for the operators), it'd indicate a transformation that changes the physics of the system.

The last thing I'll add is a short rule for the placement of the $\dagger$. In a change of basis, the operator that acts on the states is the *leftmost* operator in the operator transformation. In a transformation, it's the *rightmost* operator.