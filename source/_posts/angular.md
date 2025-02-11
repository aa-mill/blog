---
title: Angular Momentum and Rotations in Quantum Mechanics
date: 2025-02-10 18:31:27
tags: Quantum Mechanics
toc: true
---

## Summary

I'm writing this post for two reasons:

1. Quantum mechanics is cool and extremely fun to learn/write about.
2. If you're planning on understanding or doing research on equivariant neural networks, you're going to encounter the Clebsch-Gordon tensor product, which is a way to combine objects known as spherical tensors. In my experience, it helps *immensely* to conceptualize this mechanism in terms of the addition of angular momentum eigenstates. I want to first outline the context from quantum mechanics necessary to do this, and I'll make the connection in another post.

The background here closely follows the following texts:

- Sakurai, J.J., Napolitano, J., 2021. Modern quantum mechanics, 3rd ed. ed. Cambridge University Press, Cambridge. (referred to here as Sakurai)
- Griffiths, D.J., Schroeter, D.F., 2018. Introduction to quantum mechanics, Third edition. ed. Cambridge University Press, Cambridge ; New York, NY. (referred to here as Griffiths)

## Classical motivation

The basic properties of rotations in quantum mechanics stem from the commutation relations obeyed by the angular momentum operators. Before unpacking this, we can get a sense of when and how rotations fail to commute by considering rotations in classical physics^[1]. I'll say the connection between rotations and angular momentum shortly.

Imagine a vector $\boldsymbol{V}$ in three dimensions with components $V\_{x}$, $V\_{y}$, and $V\_{z}$ in an orthogonal coordinate system:

$$
\boldsymbol{V} = \begin{pmatrix}
V\_{x} \\\\
V\_{y} \\\\
V\_{z}
\end{pmatrix}.
$$

Suppose we rotate this vector. We can describe the rotation with an orthogonal matrix $R\in \mathbb{R}^{3\times 3}$ that specifies how its components change under the rotation. For example, the matrix describing a rotation by angle $\phi$ around the $z$-axis is

$$
R\_{z}(\phi) = \begin{pmatrix}
\cos\phi & -\sin\phi & 0 \\\\
\sin \phi & \cos \phi & 0 \\\\
0 & 0 & 1
\end{pmatrix}.
$$

(The general form of $R$ for arbitrary rotations is given by [Rodrigues' rotation formula](https://en.wikipedia.org/wiki/Rodrigues%27\_rotation\_formula), which can be derived by considering how the components of $\boldsymbol{V}$ parallel and perpendicular to the axis of rotation change.)

It's worth pointing out early on that there's a difference between "active" and "passive" rotations of a physical system (e.g. observe how I said "Suppose we rotate this vector" vs. "Suppose we rotate our coordinate system"). I didn't fully appreciate this at first, but knowing the difference is extremely helpful later on when trying to understand the definition of a spherical tensor. I'll hopefully write a post about this later, but for now I'll just link [these](https://en.wikipedia.org/wiki/Active\_and\_passive\_transformation) [resources](https://physics.stackexchange.com/questions/51994/active-versus-passive-transformations).

Sakurai uses the active rotation convention that a positive $\phi$ in the $R\_{z}(\phi)$ matrix corresponds to a counterclockwise rotation of the physical system (not the coordinate axes) in the $xy$-plane, as viewed from the positive $z$-axis.

Anyway, writing the analogous matrices for $R\_{x}(\phi)$ and $R\_{y}(\phi)$ and considering $\phi = \varepsilon \ll 1$, we can obtain

$$
R\_{x}(\varepsilon)R\_{y}(\varepsilon) - R\_{y}(\varepsilon)R\_{x}(\varepsilon) = R\_{z}(\varepsilon^{2}) - 1 \tag{3.7 Sakurai}
$$

to second order in $\varepsilon$. This is the classical commutation relation between the matrices for rotations about the $x$- and $y$-axes, and it gives a quantitive description of how these rotations *fail* to commute (Note that if we considered only first order in $\varepsilon$, the rotations *would* commute). We expect that an analogous relationship will exist in the quantum case.

## Defining rotations in quantum mechanics

We just saw that a rotation matrix $R$ acts on the three components of a classical column vector in 3D space. In quantum mechanics, we work with [[Quantum Mechanics|kets]] whose dimensionality varies based on the space in question. For example, when considering only the spin degree of freedom for a spin $\frac{1}{2}$ particle, the ket space is two-dimensional, and operators take the form of $2\times 2$ matrices.

So, to speak generally about a rotation identified with $R$, we associate an abstract rotation operator $\mathscr{D}(R)$, which takes different matrix representations depending on the ket space.

We construct $\mathscr{D}(R)$ by analogy to the infinitesimal operators used to describe translation and time evolution (I don't understand the origin of the infinitesimal forms yet, so I'm taking Sakurai's word here. Nonetheless, given the forms, the construction-by-analogy is clear enough). The general form of the infinitesimal operators is

$$
U\_{\varepsilon} = 1 - iG\varepsilon,
$$

where

|                | $G$ (Hermitian)                                 | $\varepsilon$ |
| -------------- | ----------------------------------------------- | ------------- |
| Translations   | $p\_{x}/\hbar$                                   | $dx'$         |
| Time evolution | $H/\hbar$                                       | $dt$          |
| Rotation       | $\boldsymbol{J}\cdot\hat{\boldsymbol{n}}/\hbar$ | $d\phi$       |

The last line of the table introduces the angular momentum operator $\boldsymbol{J}$, which is *defined* so that 

$$
\mathscr{D}(\hat{\boldsymbol{n}}, d\phi) = 1 -i\left( \frac{\boldsymbol{J}\cdot\hat{\boldsymbol{n}}}{\hbar}d\phi \right)
$$

is the infinitesimal rotation operator. In other words, $\boldsymbol{J}$ is defined to make the pattern in the last row of the table hold. Sometimes, for example in Griffiths, $\boldsymbol{J}$ is defined as $\boldsymbol{x}\times \boldsymbol{p}$. The method shown here is more general because it also applies to spin, which has no classical analogue.

A finite rotation operator can be obtained from the infinitesimal operators as

$$
\mathscr{D}(\hat{\boldsymbol{n}}, \phi) = \lim\_{ N \to \infty } \left[ 1 - i\left( \frac{\boldsymbol{J}\cdot \hat{\boldsymbol{n}}}{\hbar} \right)\left( \frac{\phi}{N} \right) \right]^{N} = \exp\left( \frac{-i\boldsymbol{J}\cdot \hat{\boldsymbol{n}}\phi}{\hbar} \right), \tag{3.16 Sakurai}
$$

where we've used the identity

$$
\lim\_{ n \to \infty } \left( 1 + \frac{x}{n} \right)^{n} = e^{x}.
$$

Note that $\mathscr{D}\_{z}(\phi)$, $\mathscr{D}(\hat{\boldsymbol{n}}, \phi)$, $\mathscr{D}(\alpha, \beta, \gamma)$, and $\mathscr{D}(R)$ are all notations for the rotation operator; they're just different shorthands for the different ways of specifying a rotation, which will hopefully become clear.

To complete the definition of $\mathscr{D}(R)$, we postulate that these operators inherit the [[Group Theory|group]] properties of $R$, i.e. we postulate that the mapping $\mathscr{D}$ is a [group homomorphism](https://en.wikipedia.org/wiki/Group\_homomorphism).

In summary, to define $\mathscr{D}(R)$, we

1. Obtain its form the infinitesimal rotation operator
2. Postulate that the finite rotation operators form a group

From this definition, we can determine the angular momentum commutation relations, on which all the properties of rotations in quantum mechanics are based.

## Fundamental angular momentum commutation relations

We can substitute the Taylor expansion of $\mathscr{D}\_{z}(\varepsilon)$ into the classical commutation relation in Eq. 3.7 to obtain $[J\_{x}, J\_{y}] = i\hbar J\_{z}$. Repeating this pattern for the other coordinate directions gives

$$
[J\_{i}, J\_{j}] = i\hbar\varepsilon\_{ijk}J\_{k}, \tag{3.20 Sakurai}
$$

the fundamental commutation relations of angular momentum. One can use these to show that

$$
\langle J\_{k} \rangle \to \sum\_{l}R\_{kl}\langle J\_{l} \rangle, 
$$

i.e. the expectation values of the angular momentum components transform as the components of a classical vector under a rotation.

So far, we have only conceptualized $\boldsymbol{J}$ as the angular momentum operator for a single particle. However, it turns out that Eq. 3.20 also holds when $\boldsymbol{J}$ is the total spin operator in a tensor product space, for example $\boldsymbol{J} = \boldsymbol{J}\_{1}\otimes 1 + 1\otimes\boldsymbol{J}\_{2}$, where $\boldsymbol{J}\_{1}$ and $\boldsymbol{J}\_{2}$ are the angular momentum operators acting on two particles labeled 1 and 2, respectively. This holds because operators in different subspaces of a tensor product space commute.

## Ways of representing rotations

### 1. $\mathrm{SO}(3)$ language

The set of $3\times 3$ orthogonal matrices $R$ with $\det R = 1$, along with the standard matrix multiplication operation, satisfies the group axioms and is called $\mathrm{SO}(3)$.

### 2. $\mathrm{SU}(2)$ language

In the [[Spin 1h Systems#Pauli two-component formalism|Pauli two-component formalism]], we have

$$
\exp\left( \frac{-i\boldsymbol{S}\cdot\hat{\boldsymbol{n}}\phi}{\hbar} \right) \doteq \exp\left( \frac{-i\boldsymbol{\sigma}\cdot\hat{\boldsymbol{n}}\phi}{2} \right),
$$

The $\doteq$ notation, which means "is represented by," emphasizes the fact that the *operator* on the left acts on a *ket*, while its *matrix representation* on the right acts on a *spinor*. Explicitly, the matrix representation is

$$
e^{-i\boldsymbol{\sigma}\cdot\hat{\boldsymbol{n}}\phi/2} = 
\begin{pmatrix}
\cos\left( \frac{\phi}{2} \right)-in\_{z}\sin\left( \frac{\phi}{2} \right) & (-in\_{x} - n\_{y})\sin\left( \frac{\phi}{2} \right) \\\\
(-in\_{x} + n\_{y})\sin\left( \frac{\phi}{2} \right) & \cos\left( \frac{\phi}{2} \right) + in\_{z}\sin\left( \frac{\phi}{2} \right)
\end{pmatrix}, \tag{3.63 Sakurai}
$$

which has the form

$$
U(a, b) = \begin{pmatrix}
a & b \\\\
-b^{\*} & a^{\*}
\end{pmatrix},
$$

with $|a|^{2} + |b|^{2} = 1$, of a general unitary matrix. The set of unitary unimodular matrices (unitary matrices $U$ with $\det(U) = 1$), along with the standard matrix multiplication operation, forms the group $\mathrm{SU}(2)$.

### Matrix representations

The matrix elements of the rotation operator (Eq. 3.16), given by

$$
\mathscr{D}\_{m'm}^{(j)}(R) = \braket{ j\ m' | \exp\left( \frac{-i\boldsymbol{J}\cdot\hat{\boldsymbol{n}}\phi}{\hbar} \right) | j\ m } \tag{3.194 Sakurai}  
$$

or

$$
\mathscr{D}\_{m'm}^{(j)}(\alpha, \beta, \gamma) = \braket{ j\ m' | \exp\left( \frac{-iJ\_{z}\alpha}{\hbar} \right)\exp\left( \frac{-iJ\_{y}\beta}{\hbar} \right)\exp\left( \frac{-iJ\_{z}\gamma}{\hbar} \right) | j\ m },
$$


are called Wigner functions. The former equation is relevant if $R$ is specified by $\hat{\boldsymbol{n}}$ and $\phi$. The latter is relevant if $R$ is expressed with Euler angles, in which case we can further write

$$
\mathscr{D}\_{m'm}^{(j)}(\alpha, \beta, \gamma) = e^{-i(m'\alpha + m\gamma)}d\_{m'm}^{(j)}(\beta),
$$

where

$$
d\_{m'm}^{(j)}(\beta) \equiv \braket{ {j\ m'} | \exp\left( \frac{-iJ\_{y}\beta}{\hbar} \right) | j\ m }.
$$

Note that since $\boldsymbol{J}^{2}$ and $J\_{k}$ commute, so do $\boldsymbol{J}^{2}$ and $\mathscr{D}(R)$, and hence $\mathscr{D}(R)\ket{j\ m}$ is an eigenket of $\boldsymbol{J}^{2}$ with the same eigenvalue. It follows that $\braket{ j'\ m' | \mathscr{D}(R) | j\ m} = 0$ unless $j' = j$, which is why $\mathscr{D}\_{m'm}^{(j)}(R)$ is defined for a single $j$.

The $(2j + 1)\times(2j + 1)$ matrix formed from these elements is the $(2j + 1)$-dimensional irreducible representation of the rotation operator. These matrices form a group:

1. Identity: $\phi = 0$.
2. Inverse: $\phi \to -\phi$. Note that $\mathscr{D}(R)$ is unitary, so $\mathscr{D}\_{m'm}(R^{-1}) = \mathscr{D}\_{mm'}^{*}(R)$.
3. Closure: Consider
	$$
	\begin{align}
	\mathscr{D}(R\_{1})\mathscr{D}(R\_{2}) &= \mathscr{D}(R\_{1}R\_{2}), \\\\
	\sum\_{m'}\mathscr{D}(R\_{1})\ket{j\ m'}\bra{j\ m'} \mathscr{D}(R\_{2}) &= \mathscr{D}(R\_{1}R\_{2}), \\\\
	\sum\_{m'}\bra {j\ m''}\mathscr{D}(R\_{1})\ket{j\ m'}\bra{j\ m'}\mathscr{D}(R\_{2})\ket{j\ m} &= \braket{ j\ m'' | \mathscr{D}(R\_{1}R\_{2}) | j\ m }, \\\\
	\sum\_{m'}\mathscr{D}\_{m''m'}^{(j)}(R\_{1})\mathscr{D}\_{m'm}^{(j)}(R\_{2}) &= \mathscr{D}\_{m''m}^{(j)}(R\_{1}R\_{2}).
	\end{align}
	$$
	
	The first line follows from the postulate that the rotation operators are a group. Next, we insert the identity operator (We could have also summed over $j$ here, but since the matrix elements of $\mathscr{D}(R)$ vanish for states with different $j$, the sum would go away in the next step). Finally, we insert each side of the equation between $\bra{j\ m''}$ and $\ket{j\ m}$.
4. Associativity: Follows from rules of matrix multiplication.

## Eigenvalues and eigenstates

Important operators:

- $\boldsymbol{J}^{2} \equiv J\_{x}J\_{x} + J\_{y}J\_{y} + J\_{z}J\_{z}$
- $J\_{\pm} \equiv J\_{x} \pm iJ\_{y}$ (non-Hermitian)
- $J\_{\pm}J\_{\mp} = \boldsymbol{J}^{2} - J\_{z}^{2} \pm \hbar J\_{z}$
	- Note $J\_{+}^{\dagger} = J\_{-}$, so, e.g., $J\_{+}^{\dagger}J\_{+} = \boldsymbol{J}^{2}-J\_{z}^{2}+\hbar J\_{z}$.

Important commutation relations

- $[\boldsymbol{J}^{2}, J\_{k}] = 0$
- $[J\_{+}, J\_{-}] = 2\hbar J\_{z}$
- $[J\_{z}, J\_{\pm}] = \pm \hbar J\_{pm}$
- $[\boldsymbol{J}^{2}, J\_{\pm}] = 0$

Using only the fundamental angular momentum commutation relations, one can show that (see Sakurai §3.5 or Griffiths §4.3)

- We can choose one of $J\_{x}$, $J\_{y}$, and $J\_{z}$ to be simultaneously diagonalized with $\boldsymbol{J}^{2}$.
- The $J\_{+}$ ($J\_{-}$) operator raises (lowers) the eigenvalue of an eigenstate of $J\_{z}$ by one unit of $\hbar$ but leaves the eigenvalues of $\boldsymbol{J}^{2}$ unchanged.
- The eigenvalue relationships for $\boldsymbol{J}^{2}$ and $J\_{z}$ are
	$$
	\boldsymbol{J}^{2}\ket{j\ m}  = j(j + 1)\hbar^{2}\ket{j\ m}\quad\text{and}\quad J\_{z}\ket{j\ m} = m\hbar \ket{j\ m}, 
	$$
	
	where $j = 0, \frac{1}{2}, 1, \frac{3}{2}, \dots$ and $m = -j, -j + 1, \dots, j - 1, j$.

Using the fact that $J\_{\pm}\ket{j\ m} = c\_{jm}^{\pm}\ket{j\ m \pm 1}$, for some constant $c\_{jm}^{+}$, we can also obtain

$$
J\_{\pm}\ket{j\ m} = \hbar\sqrt{ (j \mp m)(j \pm m + 1) }\ket{j\ m\pm 1}.
$$

## Orbital angular momentum

In classical physics, orbital angular momentum is given by $\boldsymbol{L} = \boldsymbol{x}\times \boldsymbol{p}$. However, we defined $\boldsymbol{J}$ to be the generator of an infinitesimal rotation. We can therefore ask whether the cross product definition of $\boldsymbol{L}$ is consistent with this.

First, recall the infinitesimal translation operator

$$
\mathscr{J}(d\boldsymbol{x}') = 1 - \frac{i\boldsymbol{p}\cdot d\boldsymbol{x}'}{\hbar},
$$

which acts on a ket as follows: $\mathscr{J}(d\boldsymbol{x}')\ket{\boldsymbol{x}'} = \ket{\boldsymbol{x}' + d\boldsymbol{x}'}$. This is useful because we can write

$$
\mathscr{D}\_{z}(d\phi) = 1 - \frac{iL\_{z}d\phi}{\hbar} = 1 - \frac{i(xp\_{y} - yp\_{x})d\phi}{\hbar} = 1 - \frac{i\boldsymbol{p}\cdot d\boldsymbol{x}'}{\hbar},
$$

with $d\boldsymbol{x}' = (-y'd\phi\quad x'd\phi\quad 0)^T$. In other words, we know how $\mathscr{J}(d\boldsymbol{x}')$ acts on kets, so we can use this reformulation to see how $\mathscr{D}\_{z}(d\phi)$ acts on kets when $\boldsymbol{L}$ is defined in terms of $\boldsymbol{x}$ and $\boldsymbol{p}$. For an arbitrary position eigenket, we have 

$$
\mathscr{D}\_{z}(d\phi)\ket{x', y', z'} = \ket{x' - y'd\phi, y' + x'd\phi, z'}.
$$

This is how we would expect the components of the position vector to transform under an infinitesimal rotation $R\_{z}(d\phi)$, so the classical definition of $\boldsymbol{L}$ indeed generates a rotation in the sense of our earlier definition.

The arguments of the wave function for a general ket $\ket{\psi}$ change **oppositely** to how the eigenvalues do, namely 

$$
\braket{x', y', z' | \mathscr{D}\_{z}(d\phi) | \psi} = \braket{ x' + y'd\phi, y' - x'd\phi, z' | \psi }.
$$

(Intuitively, if we rotate the *system* by $\phi$, this is equivalent to rotating the *argument* of the wave function by $-\phi$.) In spherical coordinates, we have

$$
\braket{ r, \theta, \phi | \mathscr{D}\_{z}(d\phi) | \psi } = \braket{ r, \theta, \phi - d\phi | \psi } = \braket{ r, \theta, \phi | \psi } - d\phi\frac{\partial}{\partial \phi}\braket{ r, \theta, \phi | \psi }.
$$

Here, we obtained the final equality by recognizing that $\bra{x' + y'd\phi, y'-x'd\phi, z'}$ is equivalent to $\bra{r, \theta, \phi - d\phi}$ and Taylor expanding the wave function in spherical coordinates. An alternative means is to Taylor expand the wave function in Cartesian coordinates and then transform the derivatives. In any case, the result is that

$$
\braket{ \boldsymbol{x}' | L\_{z} | \psi } = -i\hbar \frac{\partial}{\partial \phi}\braket{ \boldsymbol{x}' | \psi }.
$$

Repeating this process to determine the action of $L\_{x}$ and $L\_{y}$ (and thereby $L\_{\pm}$) in the position basis, one can then show that $\braket{ \boldsymbol{x}' | \boldsymbol{L}^{2} | \psi}$ represents the action of the angular part of the Laplacian in spherical coordinates. Importantly, these relations can be used to derive the differential equations satisfied by the spherical harmonics.

## Angular momentum addition

When we consider multiple degrees of freedom in a quantum system, e.g. the orbital and spin angular momenta of a single particle or the spin angular momenta of two particles, we can treat the base kets as belonging to a [tensor product](https://en.wikipedia.org/wiki/Tensor\_product) space (Note the [difference](https://physics.stackexchange.com/questions/756962/tensor-product-vs-direct-product-in-qm) between a tensor product space and a direct product space). In the case of two spin $\frac{1}{2}$ particles, for example,

$$
\Ket{\frac{1}{2}\ \frac{1}{2}; \frac{1}{2}\ \frac{-1}{2}} = \Ket{\frac{1}{2}\ \frac{1}{2}}\otimes\Ket{\frac{1}{2}\ \frac{-1}{2}},
$$

where we've used the naming convention $\ket{j\_{1}\ j\_{2}; m\_{1}\ m\_{2}} = \ket{j\_{1}\ m\_{1}}\otimes\ket{j\_{2}\ m\_{2}}$.

Formally, consider two angular momentum operators $\boldsymbol{J}\_{1}$ and $\boldsymbol{J}\_{2}$ that operate in different subspaces of the tensor product space. The total angular momentum operator is defined as

$$
\boldsymbol{J} = \boldsymbol{J}\_{1}\otimes 1 + 1\otimes \boldsymbol{J}\_{2}.
$$

The product notation here reflects the fact that $\boldsymbol{J}\_{1}$ and $\boldsymbol{J}\_{2}$ only affect their respective subspaces. A consequence of this is that $\boldsymbol{J}$ satisfies the fundamental angular momentum commutation relations.

The key observation surrounding angular momentum addition is that there are two choices for the base kets:

|                                      | Eigenkets of...                                                               |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| $$\ket{j\_{1}\ j\_{2}; m\_{1}\ m\_{2}}$$ | $$\boldsymbol{J}\_{1}^{2}, \boldsymbol{J}\_{2}^{2}, J\_{1z}, J\_{2z}$$            |
| $$\ket{j\_{1}\ j\_{2}; j\ m}$$         | $$\boldsymbol{J}\_{1}^{2}, \boldsymbol{J}\_{2}^{2}, \boldsymbol{J}^{2}, J\_{z}$$ |

These particular combinations arise because we want a maximal set of compatible observables, but $[\boldsymbol{J}^{2}, J\_{1z}] \neq 0$ and $[\boldsymbol{J}^{2}, J\_{2z}] \neq 0$.

### Aside on basis transformations

The eigenkets $\ket{j\_{1}\ j\_{2};m\_{1}\ m\_{2}}$ and $\ket{j\_{1}\ j\_{2};j\ m}$ are related by a change of basis. Even though the mathematics consists of standard manipulations from linear algebra, I think it's easy to get caught up in the notation when seeing this for the first time in the quantum mechanics context. So, here are the basic ideas using vectors with simple labels.

Recall that a unitary operator $U$ that transforms an orthonormal basis $\{ \ket{a\_{i}} \}$ to a new orthonormal basis $\{ \ket{b\_{i}} \}$, in the sense that $\ket{b\_{i}} = U\ket{a\_{i}}$, is

$$
U = \sum\_{i}\ket{b\_{i}} \bra{a\_{i}}. \tag{Change of basis operator}
$$

The matrix representation of $U$, called the transformation matrix, is given by $\braket{ a\_{i} | U | a\_{j} } = \braket{ a\_{i} | b\_{j} }$.

While the base *kets* transform via $U$, the expansion *coefficients* (the components of a column matrix) transform via $U^{\dagger}$:

$$
\begin{align}
\braket{ b\_{j} | \psi } &= \sum\_{i}\braket{ b\_{j} | a\_{i} } \braket{ a\_{i} | \psi } \\\\
&= \sum\_{i}\braket{ a\_{j} | U^{\dagger} | a\_{i} } \braket{ a\_{i} | \psi }. 
\end{align} \tag{Coefficient transform}
$$

We also have

$$
\ket{b\_{j}} = \sum\_{i}\ket{a\_{i}} \braket{ a\_{i} | b\_{j} } = \sum\_{i}\ket{a\_{i}}\braket{ a\_{i} | U | a\_{j}}. \tag{Base ket expansion}
$$

The point I want to make is that the operator $U$ and its matrix representation appear in slightly different forms depending on the relationship being expressed (I've labeled the above equations to underscore this). In summary

- We can form the *ket* $\ket{b\_{j}}$ by applying the *operator* $U$ to $\ket{a\_{j}}$.
- We can obtain the *components* of a general ket using the *matrix representation* of $U^{\dagger}$.
- We can expand $\ket{b\_{j}}$ as a linear combination of $\{ \ket{a\_{i}} \}$, where the components of the *matrix representation* of $U$ are the *coefficients* in the expansion.

I realize this is a bit pedantic, but it can save confusion when the term "transformation matrix" is used loosely.

### Back to angular momentum addition

**The eigenkets $\ket{j\_{1}\ j\_{2};m\_{1}\ m\_{2}}$ and $\ket{j\_{1}\ j\_{2};j\ m}$ are two choices for the ket space of fixed $j\_{1}$ and $j\_{2}$.** It's worth pausing on this statement. In general, the tensor product notation $\ket{j\_{1}\ m\_{1}}\otimes\ket{j\_{2}\ m\_{2}}$ could be taken to mean all combinations of $j\_{1}$ and $j\_{2}$, but often these are understood to be fixed (For instance, if one is considering the combined spin angular momenta of two particles, the spins of the particles are fixed). In this case, then, what we are really talking about is a subspace of the tensor product space $\ket{j\_{1}\ m\_{1}}\otimes\ket{j\_{2}\ m\_{2}}$. The identity operator in this subspace is

$$
\sum\_{m\_{1}}\sum\_{m\_{2}}\ket{j\_{1}\ j\_{2};m\_{1}\ m\_{2}} \bra{j\_{1}\ j\_{2};m\_{1}\ m\_{2}} = 1.
$$

Using this to form the base ket expansion I showed in the above aside, we can write

$$
\ket{j\_{1}\ j\_{2};j\ m} = \sum\_{m\_{1}}\sum\_{m\_{2}}\ket{j\_{1}\ j\_{2};m\_{1}\ m\_{2}} \braket{ j\_{1}\ j\_{2};m\_{1}\ m\_{2} | j\_{1}\ j\_{2};j\ m }, 
$$

where $\braket{ j\_{1}\ j\_{2};m\_{1}\ m\_{2} | j\_{1}\ j\_{2};j\ m }$ are the important **Clebsch-Gordon** coefficients. One can show the key properties that

- $\braket{ j\_{1}\ j\_{2};m\_{1}\ m\_{2} | j\_{1}\ j\_{2};j\ m } = 0$ unless $m\_{1} + m\_{2} = m$
- $|j\_{1} - j\_{2}| \le j \le j\_{1} + j\_{2}$

Since $\braket{ j\_{1}\ j\_{2};m\_{1}\ m\_{2} | j\_{1}\ j\_{2};j\ m }$ are the elements of a unitary change of basis operator, the Clebsch-Gordon coefficients form a unitary matrix. We take the matrix elements to be real.

The connection between group theory and the choice of bets kets is that the tensor product $\mathscr{D}^{(j\_{1})}\otimes \mathscr{D}^{(j\_{2})}$ is reducible:

$$
\mathscr{D}^{(j\_{1})}\otimes \mathscr{D}^{(j\_{2})} = \mathscr{D}^{(j\_{1} + j\_{2})} \oplus \mathscr{D}^{(j\_{1}+j\_{2}-1)}\oplus \cdots\oplus \mathscr{D}^{(|j\_{1}-j\_{2}|)}.
$$

In the $\ket{j\_{1}\ j\_{2};m\_{1}\ m\_{2}}$ basis, the elements of the total rotation matrix $\mathscr{D}(R) = \mathscr{D}^{(j\_{1})}(R)\otimes \mathscr{D}^{(j\_{2})}(R)$ are given by

$$
\mathscr{D}\_{m\_{1}'m\_{1}}^{(j\_{1})}(R)\mathscr{D}\_{m\_{2}'m\_{2}}^{(j\_{2})}(R) = \sum\_{j}\sum\_{m}\sum\_{m'}\braket{ j\_{1}\ j\_{2};m\_{1}'\ m\_{2}' | j\_{1}\ j\_{2};j\ m' }\mathscr{D}\_{m'm}^{(j)}(R)\braket{ j\_{1}\ j\_{2};m\_{1}\ m\_{2} | j\_{1}\ j\_{2};j\ m },
$$

which is called the Clebsch-Gordon series. We can obtain this by expanding $\braket{ j\_{1}\ j\_{2};m\_{1}'\ m\_{2}' | \mathscr{D}(R) | j\_{1}\ j\_{2};m\_{1}\ m\_{2} }$ two different ways. To get the left side, we use the fact that 

$$
\braket{ \psi\_{A}\otimes \psi\_{B} | A\otimes B | \phi\_{A}\otimes\phi\_{B} } = \braket{ \psi\_{A} | A | \phi\_{A} } \cdot \braket{ \psi\_{B} | B | \phi\_{B} } 
$$

for a tensor product space $\mathcal{H} = \mathcal{H}\_{A}\otimes\mathcal{H}\_{B}$. To get the right, we simply insert two resolutions of the identity operator in the $\ket{j\_{1}\ j\_{2};j\ m}$ basis. 

In the $\ket{j\_{1}\ j\_{2};j\ m}$ basis, the total rotation matrix $\mathscr{D}(R)$ is block diagonal, with the block for a given $j$ simply given by $\mathscr{D}\_{m'm}^{(j)}(R)$. Each subspace of definite $j$ is irreducible.

With these preliminaries about rotations and angular momentum in place, we're in a position to introduce spherical tensors and establish physical intuition for how they're combined via the Clebsch-Gordon tensor product.