# HC-1R: A Falsifiable Formal Model of a Physical Hyperconnectome

**Document status:** research synthesis and proposed formalism  
**Evidence review date:** 2026-08-19  
**System-level classification:** **EXTRAPOLATED**  
**Scope boundary:** a theoretically possible physical and dynamical architecture. This document does not claim that HC-1R exists, that it is buildable with current technology, or that any listed observable demonstrates phenomenal consciousness.

### Provenance and claim labels

- **[CURRENT SOURCE]** reports what a linked peer-reviewed paper or authoritative review supports as checked for this 2026-08-19 synthesis. It does not promote that evidence beyond the source's species, scale, modality, or method.
- **[HC-1R PROPOSAL]** marks a definition, equation, architectural choice, metric set, baseline, or experiment proposed in this document. It is not a source-reported existing system.
- **[SYNTHESIS INFERENCE]** marks an inference connecting several source-supported components to HC-1R. These inferences remain open to falsification.
- **[REVIEW CLASSIFICATION]** applies DEMONSTRATED, EXTRAPOLATED, SPECULATIVE, or REJECTED using the project research method.

In each candidate-mechanism record, **Evidence scope** is [CURRENT SOURCE]; **Mechanism**, **Measurable observables**, and **Falsifier** are [HC-1R PROPOSAL]; **Limitation and counterevidence** combines [CURRENT SOURCE] and conservative [SYNTHESIS INFERENCE]; and **Classification** is [REVIEW CLASSIFICATION].

## Executive conclusion

A technically defensible “hyperconnectome brain” is **not** a brain with the largest possible number of physical links. Raw edge density is a poor objective: long-range wiring and signaling are costly, global coupling can collapse differentiation into pathological synchrony, centralized hubs are attractive failure targets, and tightly interdependent layers can turn local faults into correlated cascades.

**[HC-1R PROPOSAL]** For HC-1R, **hyperconnectome** should instead mean:

> A spatially embedded, resource-bounded, temporal multiplex network whose physical channels support a large repertoire of selectively activated, causally effective routes; whose dynamics include empirically necessary higher-order interactions; and whose integration, segregation, controllability, observability, and robustness jointly Pareto-dominate cost-matched pairwise and static baselines.

The word “physical” imposes a strong grounding rule. Every structural edge must correspond to a realizable channel with finite capacity, latency, energy, geometry, and failure domain. Every claimed hyperedge must correspond to a reproducible non-additive physical interaction, such as convergent state-dependent computation, and must survive comparison with pairwise nonlinear models, latent-common-input models, and interventional tests. A clique reconstructed from pairwise edges is not by itself a physical hyperedge.

**[SYNTHESIS INFERENCE]** The resulting architecture is plausible as a mathematical class. Its component ideas are unevenly supported: dynamic and multiplex organization, task-dependent integration and segregation, oscillatory coordination in specific circuits, structural constraints on perturbation, and topology-dependent vulnerability are demonstrated in biological systems. Their joint use as HC-1R is extrapolated. Irreducible higher-order causation and macro-scale causal emergence are promising but not established as general organizing principles. Maximizing density, synchrony, criticality, or a single graph metric is rejected.

## 1. Definitions and qualification rules

### 1.1 Keep structural, functional, and effective connectivity separate

The original connectome proposal defines a connectome as a structural description of nervous-system elements and their anatomical connections ([Sporns, Tononi & Kötter, 2005](https://doi.org/10.1371/journal.pcbi.0010042)). Standard network-neuroscience usage distinguishes:

- **Structural connectivity:** physical channels between elements.
- **Functional connectivity:** statistical dependence between measured activities.
- **Effective connectivity:** directed influence under an explicit causal or dynamical model.

Functional correlation or coherence cannot be silently promoted into a physical channel or causal influence. Reviews of connectivity inference emphasize that correlation and coherence constrain possible causal models but do not uniquely identify one ([Reid et al., 2019](https://www.nature.com/articles/s41593-019-0510-4); [Friston, 2011](https://doi.org/10.1089/brain.2011.0008)).

### 1.2 Proposed operational definition

Let a candidate system be compared with preregistered baselines having the same nodes, task set, observation bandwidth, material budget, energy budget, and allowable perturbations. It qualifies as an **HC-1R physical hyperconnectome** only if all of the following hold:

1. **Physical grounding:** each structural channel has measured or bounded weight, direction, delay, capacity, spatial length, energy cost, and shared-failure domain.
2. **Temporal multiplexity:** different interaction types or timescales form distinct layers, and time-respecting paths predict behavior or perturbation response better than the static aggregate.
3. **Selective routing:** only a sparse, context-dependent subset of possible routes is strongly active at one time; universal simultaneous coupling is not required.
4. **Higher-order necessity:** at least some interactions among three or more units are irreducible to a cost-matched pairwise nonlinear model with latent common causes.
5. **Dynamical repertoire:** the system reproducibly visits multiple differentiated states and can move among them without either freezing or entering uncontrolled global synchrony.
6. **Practical control and observation:** useful state transitions are reachable with bounded energy and can be estimated from available sensors; algebraic controllability alone is insufficient.
7. **Perturbational integration and differentiation:** a local probe produces a distributed but differentiated response in the intended operating regime.
8. **Economy and resilience:** capability gains survive explicit wiring, energy, delay, thermal, lesion, and correlated-fault accounting.
9. **Comparative advantage:** the system lies on a better empirical Pareto frontier than static, pairwise, density-matched, and hub-centralized alternatives for defined workloads.

Failure of items 1, 4, or 9 removes the “physical hyperconnectome” claim. The system may remain a useful temporal network, but the stronger label is not earned.

### 1.3 What “hyper” does and does not mean

“Hyper” has two disciplined meanings here:

- **Combinatorial:** a large set of possible time-respecting routes can be assembled from a relatively sparse structural substrate.
- **Higher-order:** some joint interactions require hyperedges or higher-order information terms rather than only dyadic edges.

It does **not** mean maximum density, maximum average degree, maximum global efficiency, permanent global integration, maximum synchrony, unlimited state count, or proof of greater intelligence or consciousness.

## 2. Formal architecture

**[HC-1R PROPOSAL]** All definitions and equations in this section are proposed formal commitments for HC-1R. Linked sources establish component mathematics or biological observations, not this combined architecture.

### 2.1 Physical multiplex substrate

Let:

- $V = \{1,\ldots,N\}$ be physical neural or neuromorphic populations;
- $\mathcal L$ be a finite set of channel layers, such as fast excitatory/inhibitory signaling, slower modulatory control, and distinct oscillatory or communication bands;
- $S^\ell_{ij}\in\{0,1\}$ denote the existence of a physical directed channel $j\rightarrow i$ in layer $\ell$;
- $w^\ell_{ij}$ be its signed coupling strength;
- $\tau^\ell_{ij}>0$ be its propagation and processing delay;
- $q^\ell_{ij}$ be its capacity;
- $c^\ell_{ij}$ be its signaling cost; and
- $d^\ell_{ij}$ identify its physical failure domain, such as shared power, clock, router, vascular supply, or support path.

The immutable or slowly changing physical support is $S$. A time-varying gate $g^\ell_{ij}(t)\in[0,1]$ determines how strongly that channel participates at time $t$:

$$
A^\ell_{ij}(t) = S^\ell_{ij} w^\ell_{ij} g^\ell_{ij}(t).
$$

The multiplex can be written as a supra-adjacency matrix with diagonal blocks $A^\ell(t)$ and inter-layer coupling blocks $\Omega^{\ell m}(t)$. Aggregating the layers into one matrix is permitted only as a lossy summary; reachability must respect the ordering and timing of edge activations. The mathematical motivation comes from temporal and multilayer network theory ([Holme & Saramäki, 2012](https://doi.org/10.1016/j.physrep.2012.03.001); [De Domenico et al., 2013](https://doi.org/10.1103/PhysRevX.3.041022); [Mucha et al., 2010](https://doi.org/10.1126/science.1184819)).

### 2.2 Directed hyperedges

Let $\mathcal E_H(t)$ be a set of directed hyperedges $e=(T_e,H_e)$, where the tail $T_e$ is a set of two or more jointly required sources and $H_e$ is one or more targets. Each hyperedge has strength $\kappa_e(t)$, delay $\tau_e$, resource cost $c_e$, and failure domain $d_e$.

A hyperedge is admitted only if the joint term $\Psi_e$ cannot be replaced, within uncertainty, by:

1. pairwise linear interactions;
2. pairwise nonlinear interactions;
3. a hidden common input;
4. a measurement or preprocessing artifact; or
5. an overfit interaction that fails held-out and interventional tests.

This is stricter than turning every graph clique into a simplex. Hypergraph and simplicial formalisms are well developed ([Battiston et al., 2020](https://doi.org/10.1016/j.physrep.2020.05.004)), but a higher-order representation does not establish literal higher-order causation.

### 2.3 Delayed nonlinear state dynamics

Let $x_i(t)\in\mathbb R^{p_i}$ be the state of node $i$, $r_i(t)$ its available local resource, $u(t)$ an external or endogenous control signal, and $\xi_i(t)$ noise. A general HC-1R dynamics is:

$$
\dot{x}_i(t) =
f_i(x_i(t), r_i(t), \theta_i)
+ \sum_{\ell \in \mathcal L}\sum_j A^\ell_{ij}(t)
\psi_\ell(x_j(t-\tau^\ell_{ij}), x_i(t))
+ \sum_{e:i\in H_e} \kappa_e(t)
\Psi_e(\{x_k(t-\tau_e):k\in T_e\})
+ B_i u(t) + \xi_i(t).
$$

This equation does not prescribe one neural model. The local term $f_i$ could be a neural mass, conductance-based population, spiking ensemble, or synthetic dynamical unit. The key commitments are finite delays, bounded resources, signed and gated coupling, explicit higher-order terms, and perturbable dynamics.

### 2.4 Oscillatory gating as one routing mechanism

When nodes have meaningful phase variables $\phi^\ell_i(t)$, one candidate gate is:

$$
g^\ell_{ij}(t) =
\sigma\left(
a^\ell_{ij}
+ b^\ell_{ij}\cos[
\phi^\ell_j(t-\tau^\ell_{ij})-\phi^\ell_i(t)-\delta^\ell_{ij}]
+ m^\ell_{ij}(t)
\right),
$$

where $\sigma$ bounds the gate, $\delta$ is a preferred phase offset, and $m$ is a contextual or modulatory term. This formalizes phase-sensitive routing without assuming that coherence is the only route or that zero-lag synchrony is desirable. Communication-through-coherence has strong circuit-specific evidence and an influential synthesis ([Fries, 2015](https://doi.org/10.1016/j.neuron.2015.09.034)), while large-scale and model evidence supports transient frequency-specific organization ([Vidaurre et al., 2018](https://www.nature.com/articles/s41467-018-05316-z); [Palmigiano et al., 2017](https://www.nature.com/articles/nn.4569)). Causal interpretation still requires intervention.

### 2.5 Resource and homeostatic constraints

The physical system must include resource dynamics rather than attaching cost after optimization:

$$
\dot{r}_i(t) =
h_i(r_i,t)
- P_i(x_i,t)
- \sum_{\ell,j} c^\ell_{ij}|A^\ell_{ij}(t)|
- \sum_{e:i\in e} c_e|\kappa_e(t)|,
\qquad
r_i^{min} \le r_i(t) \le r_i^{max}.
$$

Slow plasticity may change $w$, gating policies, or hyperedge strength, but updates must be projected onto a feasible set $\mathcal C$ that preserves energy, thermal, delay, and stability constraints:

$$
\dot{W} = \Pi_{\mathcal C}[P(W,x,m,r)].
$$

This is not decorative biological mimicry. Signaling consumes substantial energy, and economical brain organization trades topological value against wiring and metabolic expense ([Attwell & Laughlin, 2001](https://doi.org/10.1097/00004647-200110000-00001); [Bullmore & Sporns, 2012](https://www.nature.com/articles/nrn3214)). A candidate that requires most nodes or long-range channels to be continuously active fails the physical definition.

### 2.6 Controllability and observability

Around a trajectory $x^\ast(t)$, linearize the delayed nonlinear dynamics over a finite horizon:

$$
\dot{\delta x}(t) = J(t)\delta x(t) + B(t)u(t).
$$

For the corresponding state-transition operator $\Phi(t,t_0)$, the finite-horizon controllability Gramian is:

$$
W_c(T) =
\int_0^T
\Phi(T,\tau)B(\tau)B(\tau)^\top\Phi(T,\tau)^\top d\tau.
$$

Useful quantities include minimum transition energy, the smallest non-negligible eigenvalue of $W_c$, robustness across model uncertainty, and the fraction of a task-relevant target set reachable under actuator and safety constraints. The observability Gramian must likewise show that target states can be distinguished with the available measurements. Exact Kalman rank in a noise-free linear model is not enough.

Network-control theory provides a useful vocabulary and some stimulation-linked results ([Gu et al., 2015](https://www.nature.com/articles/ncomms9414); [Stiso et al., 2019](https://doi.org/10.1016/j.celrep.2019.08.008); [Tang & Bassett, 2018](https://doi.org/10.1103/RevModPhys.90.031003)). However, common structural controllability measures can track weighted degree and appear in biologically irrelevant null networks ([Tu et al., 2018](https://doi.org/10.1016/j.neuroimage.2018.04.010)). HC-1R therefore requires prospective perturbation prediction, not topology-only scores.

### 2.7 Causal emergence as an optional, not defining, property

Given an intervention-defined transition matrix $P(X_{t+\Delta}\mid do(X_t))$, define effective information as the mutual information between a maximally distributed intervention over present states and resulting future states:

$$
EI_X(\Delta) =
I(do(X_t); X_{t+\Delta}).
$$

For a preregistered coarse-graining $M=g(X)$:

$$
CE_g(\Delta) = EI_M(\Delta) - EI_X(\Delta).
$$

Positive CE means that, under the specified intervention distribution and coarse-graining, the macro-model is more informative because reduced degeneracy or indeterminism outweighs its smaller state space. This is formally possible in model systems ([Hoel, Albantakis & Tononi, 2013](https://doi.org/10.1073/pnas.1314922110)). It is not observer-independent proof of ontological emergence, and philosophical and methodological critiques dispute how causal or emergent the measure is ([Dewhurst, 2021](https://doi.org/10.1002/tht3.489)). HC-1R does not need positive CE to qualify. If tested, the intervention distribution, scale, partition, estimator, and model class must be explicit.

## 3. Objective: a constrained Pareto frontier, not a connectivity maximum

**[HC-1R PROPOSAL]**

HC-1R should be assessed by a vector of outcomes rather than one “hyperconnectivity score”:

$$
\mathbf H =
(
U_{task},
R_{route},
R_{state},
S_{HOI},
C_{control},
O_{observe},
P_{perturb},
R_{robust}
;
-C_{wire},
-C_{energy},
-C_{delay},
-C_{sync},
-C_{hub},
-C_{corrfail}
).
$$

Here:

- $U_{task}$ is held-out task utility;
- $R_{route}$ is reproducible time-respecting route repertoire;
- $R_{state}$ is reproducible dynamical-state repertoire;
- $S_{HOI}$ is higher-order explanatory or causal gain beyond pairwise baselines;
- $C_{control}$ is practical reachability at bounded energy;
- $O_{observe}$ is state-estimation quality;
- $P_{perturb}$ is integrated and differentiated perturbation response;
- $R_{robust}$ is retained function under noise, lesions, and common-cause faults;
- the negative terms are explicit costs or hazards.

HC-1R qualifies only if it Pareto-dominates at least one simpler baseline and is not dominated by another. A weighted scalar can support a specific design decision, but no universal set of weights is scientifically justified.

### Core observables

- **Temporal routing:** time-respecting reachability, earliest-arrival latency, temporal communicability, edge and community flexibility, routing sparsity, switching overhead.
- **Integration and segregation:** modularity Q(t), within-module degree, participation coefficient, inter-module efficiency, task-conditioned transfer.
- **Metastability:** dwell-time distributions, recurrence, transition entropy, phase-slip statistics, and the temporal variance of the Kuramoto order parameter as only one proxy.
- **Oscillatory routing:** directed phase-lag measures, phase-slope index, conditional transfer entropy or mutual information, spike-field coupling, cross-frequency coupling, and phase-specific perturbation effects.
- **Higher order:** cross-validated likelihood gain over pairwise models, synergy and redundancy under a declared information decomposition, O-information, and intervention-sensitive hyperedge coefficients.
- **Control and observation:** empirical transition energy, target-set reachability, Gramian spectra with regularization, model-predicted versus observed perturbation trajectories, sensor reconstruction error.
- **Perturbational complexity:** spatial spread, response diversity, compressibility, causal depth, return time, and differentiation conditional on equal perturbation energy.
- **Robustness:** area under task-performance-versus-lesion curves, worst-case k-node and k-edge loss, edge-disjoint route diversity, hub-load Gini coefficient, common-cause fault loss, and recovery time.
- **Physical economy:** total wire length and volume, active communication energy, idle energy, peak power, thermal margin, capacity utilization, and delay distribution.

## 4. Candidate mechanisms and adversarial classifications

Each mechanism below is classified for its proposed HC-1R role, not merely for whether related mathematics or biological observations exist.

### M1. Temporal multiplex routing

**Problem.** A static aggregate graph treats every link as simultaneously available and loses the ordering, type, and timescale of communication.

**Mechanism.** Separate physical interaction classes into layers and use context-dependent gates to create time-respecting routes. Inter-layer coupling allows a slow modulatory layer to bias faster signaling layers without replacing them.

**Evidence scope.** Multilayer community analysis of human motor-learning fMRI found dynamic reconfiguration and linked flexibility to later learning ([Bassett et al., 2011](https://doi.org/10.1073/pnas.1018985108)). Frequency-layer multiplex analysis can reveal hubs hidden by aggregation and has improved group discrimination in imaging data ([De Domenico et al., 2016](https://pubmed.ncbi.nlm.nih.gov/27471443/)). Temporal and multilayer formalisms are mathematically mature.

**Limitation and counterevidence.** fMRI-derived layers are statistical estimates, not literal causal channels. Apparent resting-state dynamics can reflect sampling variability, motion, arousal, or sleep ([Laumann et al., 2017](https://pubmed.ncbi.nlm.nih.gov/27591147/)); sliding-window estimates are sensitive to windowing and noise ([Hutchison et al., 2013](https://doi.org/10.1016/j.neuroimage.2013.05.079); [Lindquist et al., 2014](https://doi.org/10.1016/j.neuroimage.2014.06.052)).

**Measurable observables.** Temporal reachability, route latency, layer-specific capacity, inter-layer mutual information, community flexibility, switching energy, and held-out task prediction.

**Falsifier.** A static aggregate with the same physical cost predicts behavior and perturbation trajectories as well as or better than the multiplex; or disabling the proposed gate while preserving mean activity has no selective causal effect.

**Classification:** **EXTRAPOLATED**.

### M2. Dynamic integration, segregation, and metastability

**Problem.** Pure modular segregation cannot combine specialized results, while permanent global integration erases functional differentiation and encourages correlated activity.

**Mechanism.** Operate in a bounded regime that alternates between locally specialized and selectively integrated configurations. Metastability means reproducible transient coordination without permanent capture by one attractor, not simply high variance.

**Evidence scope.** Human fMRI shows transitions between segregated and integrated states, with integrated states associated with faster and more accurate working-memory performance ([Shine et al., 2016](https://doi.org/10.1016/j.neuron.2016.09.018)). Coordination-dynamics and whole-brain modeling motivate metastability as a balance of autonomy and coordination ([Tognoli & Kelso, 2014](https://doi.org/10.1016/j.neuron.2013.12.022); [Deco et al., 2017](https://www.nature.com/articles/s41598-017-03073-5)).

**Limitation and counterevidence.** “Metastability” has multiple non-equivalent definitions and is often operationalized by a single heuristic such as standard deviation of global phase coherence. A large value may reflect noise, excessive alternation, or model tuning rather than useful flexibility. Recent review work explicitly warns against conceptual slippage ([O'Byrne & Jerbi, 2024](https://www.nature.com/articles/s41583-024-00883-1)).

**Measurable observables.** Q(t), participation coefficients, transfer across modules, dwell-time and recurrence distributions, transition entropy, Kuramoto R(t), phase slips, largest Lyapunov exponent, and task performance conditional on state.

**Falsifier.** There is no bounded regime in which differentiated state repertoire and task utility exceed both the frozen-segregated and globally synchronized controls; or putative states fail test-retest and perturbational replication.

**Classification:** **EXTRAPOLATED**.

### M3. Oscillatory and cross-frequency routing

**Problem.** Fixed anatomical links need a rapid mechanism to select which sender influences which receiver without physical rewiring.

**Mechanism.** Phase alignment, resonance, inhibition, and nested slow-fast oscillations gate transient transfer along selected physical paths. Different frequency layers can support different directional or temporal roles.

**Evidence scope.** Attention-related, directionally lagged fronto-visual gamma coupling and selective synchronization of task-relevant inputs have been observed in macaques ([Gregoriou et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19478185/); [Bosman et al., 2012](https://pubmed.ncbi.nlm.nih.gov/22958827/)). Frequency-specific phase-coupling networks appear as short-lived states in MEG ([Vidaurre et al., 2018](https://www.nature.com/articles/s41467-018-05316-z)). Reviews synthesize coherence, resonance, inhibition, and nested oscillations as candidate communication mechanisms ([Hahn et al., 2019](https://www.nature.com/articles/s41583-018-0094-0)).

**Limitation and counterevidence.** Coherence may arise from common input or be a consequence rather than a cause of transfer. Volume conduction, spike leakage, stimulus dependence, weak and intermittent gamma, frequency mismatch, and conduction delay complicate interpretation ([Buzsáki & Schomburg, 2015](https://pubmed.ncbi.nlm.nih.gov/25706474/); [Ray & Maunsell, 2015](https://pubmed.ncbi.nlm.nih.gov/25555444/)). Communication-through-coherence is not a universal routing law.

**Measurable observables.** Conditional directed information transfer, phase-dependent gain, preferred phase offsets after delay correction, cross-frequency coupling, route-specific perturbation effects, and task-linked switching latency.

**Falsifier.** Phase-targeted perturbation, with amplitude and arousal controlled, does not selectively change transfer or behavior; or a non-oscillatory gain model explains the same interventions with lower complexity.

**Classification:** **EXTRAPOLATED**.

### M4. Irreducible higher-order interactions

**Problem.** Pairwise graphs cannot represent a target response that depends jointly and non-additively on a group of sources.

**Mechanism.** Admit sparse, directed hyperedges only when a joint transfer function or synergistic information term is necessary. Hyperedges should be context-dependent and costed, not combinatorially added wherever a clique exists.

**Evidence scope.** Higher-order information measures reveal brain subsystems not visible to bivariate functional connectivity ([Varley et al., 2023](https://www.nature.com/articles/s42003-023-04843-w)); a synergy-redundancy gradient has been linked to cortical hierarchy and higher cognition ([Luppi et al., 2022](https://www.nature.com/articles/s41593-022-01070-0)). Higher-order fMRI features can improve task decoding, individual identification, and behavior association ([Santoro et al., 2024](https://www.nature.com/articles/s41467-024-54472-y)). Region-specific neural data show that pairwise models may be adequate in some sensory areas but not in prefrontal data ([Chelaru et al., 2021](https://pubmed.ncbi.nlm.nih.gov/34665999/)).

**Limitation and counterevidence.** Statistical synergy is not automatically a physical many-way channel. Higher-order estimates are data-hungry, estimator-dependent, vulnerable to common inputs, and easy to overfit. Pairwise models explain much observed population structure in some circuits, so universal hyperedges are contradicted.

**Measurable observables.** Held-out likelihood and intervention prediction versus pairwise nonlinear and latent-variable baselines; stable hyperedge coefficients; synergy, redundancy, and O-information with estimator sensitivity; lesion effects of jointly removing hyperedge members.

**Falsifier.** Pairwise or latent-common-cause models match all held-out and interventional effects at lower cost; inferred hyperedges change radically with estimator or parcellation; or the hypergraph adds no task or robustness benefit.

**Classification:** **EXTRAPOLATED**.

### M5. Distributed practical controllability and observability

**Problem.** A large state repertoire is useless if target states cannot be reached safely or distinguished from one another.

**Mechanism.** Use multiple distributed control and sensing sites, state-dependent finite-horizon models, and explicit transition-energy limits. Rotate routing load rather than depending on a single permanent controller hub.

**Evidence scope.** Structural network models connect topology to theoretical control roles ([Gu et al., 2015](https://www.nature.com/articles/ncomms9414)). In epilepsy patients, white-matter-constrained models predicted part of the state transition induced by direct electrical stimulation better than null architectures ([Stiso et al., 2019](https://doi.org/10.1016/j.celrep.2019.08.008)). Controllability measures have also predicted some rTMS working-memory benefit ([Beynel et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32690618/)).

**Limitation and counterevidence.** Linear time-invariant, noise-free, and undirected models omit major neural dynamics. A reanalysis found no statistically supported one-region controllability and showed common metrics can resemble weighted degree and random-network results ([Tu et al., 2018](https://doi.org/10.1016/j.neuroimage.2018.04.010)). Mathematical reachability may require prohibitive energy.

**Measurable observables.** Empirical minimum transition energy, target-set success under actuator bounds, perturbation-trajectory prediction, robust Gramian spectra, sensor reconstruction error, and performance after control-site lesions.

**Falsifier.** Topology-derived scores fail to predict prospective perturbations better than degree and spatial nulls; target states require infeasible energy; or a nominal controller becomes unsafe under realistic delay and parameter uncertainty.

**Classification:** **EXTRAPOLATED**.

### M6. Perturbational integration and differentiation

**Problem.** Passive correlations cannot show how a system responds causally or distinguish useful integration from homogeneous broadcast.

**Mechanism.** Apply standardized local perturbations and measure whether responses propagate through multiple routes while remaining spatiotemporally differentiated. Use a battery of transparent response metrics rather than one consciousness-labeled score.

**Evidence scope.** TMS-EEG during wakefulness produces distributed sequential responses that become local and rapidly extinguished in non-REM sleep ([Massimini et al., 2005](https://doi.org/10.1126/science.1117256)). The perturbational complexity index combines integration and differentiation and discriminates several human consciousness conditions ([Casali et al., 2013](https://doi.org/10.1126/scitranslmed.3006294)).

**Limitation and counterevidence.** PCI is validated against human neurophysiological states, not synthetic cognition, architecture quality, or phenomenal consciousness. Results depend on perturbation site, state, sensor bandwidth, thresholding, and compression method.

**Measurable observables.** Response spread, diversity, causal depth, compressibility, recurrence, response entropy, return time, and task-state restoration, all normalized for perturbation energy.

**Falsifier.** Equal-energy probes produce only local extinction, homogeneous global response, or unstable runaway activity; or perturbation metrics do not predict independently defined system capability.

**Classification:** **EXTRAPOLATED** for HC-1R; the biological assay itself is **DEMONSTRATED**.

### M7. Macro-scale causal emergence

**Problem.** A physically detailed micro-description may be too noisy or degenerate to expose the scale at which interventions have the most reliable consequences.

**Mechanism.** Search over preregistered spatial and temporal coarse-grainings and retain a macro-model only when it has positive effective-information gain under an explicit intervention distribution and predicts held-out interventions better than the micro-model.

**Evidence scope.** Effective-information theory demonstrates in simple modeled systems that a macro transition model can exceed its fixed micro-model by reducing indeterminism or degeneracy ([Hoel et al., 2013](https://doi.org/10.1073/pnas.1314922110)). Information-decomposition work offers related formal criteria and preliminary neural applications ([Rosas et al., 2020](https://pubmed.ncbi.nlm.nih.gov/33347467/); [Mediano et al., 2022](https://doi.org/10.1098/rsta.2021.0246)).

**Limitation and counterevidence.** Results depend on state definition, partition, scale, intervention distribution, causal formalism, and estimator. Observational ECoG or fMRI generally does not implement the uniform interventions assumed by effective information. Some critiques interpret the result as epistemic compression rather than new causal power.

**Measurable observables.** EI at each scale and lag, CE under multiple justified intervention distributions, out-of-sample interventional likelihood, stability of the selected coarse-graining, and sample complexity.

**Falsifier.** Positive CE disappears after held-out testing, complexity correction, alternate plausible partitions, or real interventions; or the micro-model predicts as well at acceptable cost.

**Classification:** **SPECULATIVE** as an HC-1R organizing mechanism.

### M8. Distributed redundancy, degeneracy, and rotating connector roles

**Problem.** Efficient long-range communication often concentrates traffic in connector hubs, creating energetic bottlenecks and disproportionate lesion sensitivity.

**Mechanism.** Preserve modular specialization while providing multiple partially independent cross-module routes. Rotate connector roles over time, diversify physical failure domains, and prefer functional degeneracy—different structures capable of the same required function—over exact duplication.

**Evidence scope.** Human brain networks contain expensive rich-club and connector infrastructure, and flexible hubs change connectivity with task context ([Cole et al., 2013](https://www.nature.com/articles/nn.3470); [Bullmore & Sporns, 2012](https://www.nature.com/articles/nrn3214)). Focal damage to connector locations disproportionately disrupts global modular organization ([Gratton et al., 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3575518/)). Across neurological disorders, topology and centrality shape vulnerability and compensation ([Fornito, Zalesky & Breakspear, 2015](https://www.nature.com/articles/nrn3901); [Aerts et al., 2016](https://doi.org/10.1093/brain/aww194)).

**Limitation and counterevidence.** Redundant paths add wire, idle capacity, and coordination overhead. Dynamic connector rotation can still share power, timing, cooling, or support infrastructure, producing correlated rather than independent resilience. Biological rich clubs may be globally resilient despite local vulnerability.

**Measurable observables.** Edge- and node-disjoint paths, load and control centrality Gini coefficients, physical failure-domain diversity, worst-case lesion loss, common-cause fault loss, recovery time, and redundancy cost.

**Falsifier.** A few nodes or shared support domains still cause catastrophic loss; rotating connectors do not improve cost-matched lesion curves; or redundancy costs exceed the retained utility.

**Classification:** **EXTRAPOLATED**.

### M9. Homeostatic gain, inhibition, and stability control

**Problem.** Dense recurrent excitation, adaptive routing, and plasticity can cause runaway activity, quiescence, oscillatory instability, or seizure-like capture.

**Mechanism.** Couple fast signed excitation and inhibition with slower homeostatic gain, resource feedback, and safety envelopes. Keep global coupling and plasticity inside a robustly stable operating region rather than assuming self-organization will find one.

**Evidence scope.** Homeostatic plasticity is a major biological mechanism preventing sustained deviations in excitability ([Turrigiano & Nelson, 2004](https://www.nature.com/articles/nrn1327)). Abnormal synchronization is implicated across epilepsy, Parkinson disease, schizophrenia, autism, and Alzheimer disease, but in different forms ([Uhlhaas & Singer, 2006](https://doi.org/10.1016/j.neuron.2006.09.020)). Reducing excessive beta phase-amplitude coupling accompanies therapeutic deep-brain stimulation effects in Parkinson disease ([de Hemptinne et al., 2015](https://pubmed.ncbi.nlm.nih.gov/25867121/)).

**Limitation and counterevidence.** “Too much synchrony” is not a universal disease law: seizures can begin with desynchronization and develop synchrony later ([Jiruska et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23184516/)). Strong negative feedback can suppress useful amplification and memory. One scalar synchrony threshold is therefore inadequate.

**Measurable observables.** State-dependent Jacobian spectra, Lyapunov exponents, excitation-inhibition proxies, burst statistics, band-specific synchrony, phase-amplitude coupling, recovery from input steps, and retained task sensitivity.

**Falsifier.** Bounded perturbations or admissible learning reliably lead to runaway, quiescent, or long-lived pathological states; or stabilization removes the task advantage of the architecture.

**Classification:** **EXTRAPOLATED** for HC-1R; the need for stability regulation is **DEMONSTRATED** in adaptive neural systems.

### M10. Mandatory operation at a critical point

**Problem claimed by the proposal.** A large repertoire and high sensitivity are sometimes attributed to operation exactly at the edge of a phase transition.

**Candidate mechanism.** Tune the global system to a critical branching, synchronization, or order-disorder point.

**Evidence scope.** Connectome-constrained models can reproduce resting-state features near a modeled critical point ([Haimovici et al., 2013](https://doi.org/10.1103/PhysRevLett.110.178101)), and criticality can provide computational advantages in some models.

**Limitation and counterevidence.** Experimental results remain contradictory, critical signatures depend on the transition and scale being tested, and non-critical systems can produce power laws and other apparent signatures ([Wilting & Priesemann, 2019](https://doi.org/10.1016/j.conb.2019.08.002); [Destexhe & Touboul, 2021](https://doi.org/10.1523/ENEURO.0551-20.2021)). Exact criticality can also magnify noise and perturbations, conflicting with robust control.

**Measurable observables.** A declared order parameter, susceptibility, correlation length, finite-size scaling, branching ratio, critical slowing, task utility, and perturbation amplification across a parameter sweep.

**Falsifier.** Putative signatures appear in matched non-critical models; no finite-size scaling identifies a transition; or capability and robustness do not peak in the claimed critical corridor.

**Classification:** **REJECTED** as a mandatory HC-1R principle. A task-dependent near-critical regime remains a separately testable **SPECULATIVE** option.

### M11. Maximum physical connectivity or permanent global integration

**Problem claimed by the proposal.** More edges and shorter graph paths are assumed to increase information exchange and intelligence.

**Candidate mechanism.** Increase degree, density, long-range wiring, or global coupling as far as physically possible.

**Evidence scope.** No reviewed evidence establishes a monotonic cognition benefit from raw density. Instead, biological networks balance costly long-range integration with modularity and local specialization ([Bullmore & Sporns, 2012](https://www.nature.com/articles/nrn3214)). Signaling and postsynaptic activity consume substantial energy ([Attwell & Laughlin, 2001](https://doi.org/10.1097/00004647-200110000-00001)).

**Limitation and counterevidence.** Dense coupling raises wiring volume, power, interference, synchronization, heat, calibration burden, and correlated failure. A fully connected graph can have excellent path length and poor selective computation.

**Measurable observables.** Utility and perturbation complexity versus density at matched node count; total and active cost; selectivity; synchrony occupancy; thermal margin; lesion curves; and mutual information after conditioning on shared input.

**Falsifier.** The premise itself is falsified if adding edges beyond an optimum fails to improve held-out utility per cost or degrades differentiation, robustness, or control. This is the expected result.

**Classification:** **REJECTED**.

### M12. A single permanent superhub or single global clock

**Problem claimed by the proposal.** Centralization is assumed to simplify global access and routing.

**Candidate mechanism.** Route most inter-module communication, timing, or control through one high-centrality structure.

**Evidence scope.** Hubs and rich clubs support integration, but that evidence does not privilege one universal hub. Lesion and disease studies show disproportionate vulnerability of connector and hub infrastructure ([Crossley et al., 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107735/); [Aerts et al., 2016](https://doi.org/10.1093/brain/aww194)).

**Limitation and counterevidence.** Centralization creates a capacity bottleneck, single failure target, common timing failure, and load-driven energy concentration. Replicated hubs sharing one support domain only disguise the single point.

**Measurable observables.** Maximum betweenness and control load, failure-domain concentration, latency under load, targeted-lesion loss, and recovery after hub isolation.

**Falsifier.** Removal or saturation of one node or support domain causes a discontinuous capability collapse that a cost-matched distributed design avoids.

**Classification:** **REJECTED** as the default architecture.

## 5. Failure-mode and stress-test register

**[HC-1R PROPOSAL informed by CURRENT SOURCE failure evidence]**

### 5.1 Pathological synchrony and loss of differentiation

**Failure.** Coupling or gain drives the system into prolonged global coherence, stereotyped bursting, seizure-like propagation, or one dominant attractor.

**Stress test.** Sweep global and layer-specific coupling, delays, input amplitude, noise, and inhibitory gain. Apply local impulses and persistent disturbances from multiple states.

**Reject condition.** The fraction of time in a preregistered pathological regime exceeds the safety bound; differentiated task representations collapse; or recovery requires an unavailable global reset.

### 5.2 Wiring, energy, and thermal infeasibility

**Failure.** Long-range or continuously active links erase functional gains once physical cost is included.

**Stress test.** Compare against distance-, capacity-, and performance-matched sparse baselines. Include link length, bandwidth, firing or event rate, coding overhead, idle energy, cooling, and peak power.

**Reject condition.** HC-1R is Pareto-dominated after real cost accounting or violates a hard power, material, or thermal envelope.

### 5.3 Hub overload and targeted fragility

**Failure.** A small connector set carries most traffic or control energy and fails under saturation, damage, or drift.

**Stress test.** Random, degree-targeted, betweenness-targeted, connector-targeted, control-targeted, and load-induced lesions; compare real and simulated lesions.

**Reject condition.** Small targeted lesions produce a discontinuous drop in task performance, observability, or controllability; distributed rerouting cannot restore service within the allowed time and energy.

### 5.4 Correlated cross-layer and common-cause failure

**Failure.** Multiplex layers appear redundant but share the same physical support, so one fault disables several at once. General interdependent-network models show that tight dependency can amplify cascades ([Buldyrev et al., 2010](https://www.nature.com/articles/nature08932)), although direct transfer to brains is an extrapolation.

**Stress test.** Label physical failure domains and inject simultaneous faults by domain, not just independent node deletion. Include shared power, clock, bus, cooling, vascular-like supply, routing policy, training update, and sensor artifacts.

**Reject condition.** Common-cause loss is close to full correlated loss, the architecture has no islanded safe mode, or adding a layer increases worst-case collapse probability.

### 5.5 Delay-driven and non-normal instability

**Failure.** Long delays, phase offsets, and recurrent gain create oscillatory instability or large transient amplification even when eigenvalues suggest asymptotic stability.

**Stress test.** Sweep delays and jitter, examine pseudospectra and transient gain, and perturb around multiple trajectories rather than one equilibrium.

**Reject condition.** Plausible delay variation yields unbounded or unsafe transients, loss of phase-selective routing, or a control-energy explosion.

### 5.6 Hyperedge hallucination

**Failure.** Measurement mixing, hidden common causes, nonlinear pairwise interactions, or estimator bias are mislabeled as physical higher-order coupling.

**Stress test.** Compare preregistered pairwise linear, pairwise nonlinear, latent-state, hypergraph, and mechanistic models on held-out observations and interventions. Vary sampling, parcellation, and estimator.

**Reject condition.** Hyperedge support is unstable, non-replicating, or disappears under common-cause control; predictive gains do not survive complexity penalties.

### 5.7 Controllability and observability illusion

**Failure.** Rank conditions or graph metrics imply control while actual transitions require unrealistic energy or hidden states cannot be observed.

**Stress test.** Prospective perturbation, actuator saturation, sensor dropout, model mismatch, nonlinear dynamics, and target uncertainty.

**Reject condition.** Empirical transition error or energy exceeds the bound, or nominally distinct states are observationally indistinguishable.

### 5.8 Noise masquerading as repertoire or metastability

**Failure.** A large count of transient states reflects estimator noise, random switching, or measurement artifact rather than reusable computation.

**Stress test.** Test-retest replication, cross-session decoding, recurrence under matched context, perturbational return, and surrogate time-series tests.

**Reject condition.** State identities do not reproduce, do not condition behavior, or are matched by stationary and phase-randomized surrogates.

### 5.9 Plasticity-driven drift and topology collapse

**Failure.** Adaptive weights or gates undermine stability, concentrate load, erase old capabilities, or invalidate the control model.

**Stress test.** Long-horizon learning with adversarial sequences, delayed feedback, distribution shift, resource scarcity, and rollback to earlier states.

**Reject condition.** The system leaves the feasible set, loses previously retained capabilities beyond the declared interference budget, or changes faster than assurance models can be revalidated.

## 6. Falsifiable comparative research program

**[HC-1R PROPOSAL]**

### 6.1 Required baselines

HC-1R should be tested against, at minimum:

1. **B0: static sparse modular pairwise network** with matched nodes and material budget;
2. **B1: density-matched random and small-world networks** with matched weight and distance distributions;
3. **B2: temporal pairwise multiplex network** without hyperedges;
4. **B3: static hypergraph** without time-varying routing;
5. **B4: centralized connector-hub architecture** with matched capacity;
6. **B5: same HC-1R model with phase gating disabled** while mean activity and energy are matched;
7. **B6: stationary and phase-randomized surrogates** for dynamic-state claims.

Comparisons must hold physical budgets constant. It is invalid to give HC-1R more power, wire, sensors, or model parameters and attribute the result to topology.

### 6.2 Minimum decisive experiments

#### Experiment A: route-repertoire advantage

Use workloads requiring rapid context switches, concurrent specialized processing, and delayed integration. Measure utility, latency, active routes, energy, and interference.

**Supports HC-1R if:** temporal multiplexity improves held-out utility or robustness per cost over B0 and B1.  
**Falsifies the routing claim if:** the static aggregate matches or exceeds it.

#### Experiment B: causal oscillatory gate

Apply phase-specific perturbations while matching amplitude, average activity, and arousal-like global state.

**Supports HC-1R if:** perturbation selectively changes directed transfer and task behavior along the predicted route.  
**Falsifies the mechanism if:** transfer is phase-insensitive or a simpler gain model explains the result.

#### Experiment C: hyperedge necessity

Fit pairwise linear, pairwise nonlinear, latent-common-cause, and directed-hypergraph models using identical training data and complexity control. Then perturb combinations of source nodes.

**Supports HC-1R if:** the hypergraph uniquely predicts joint interventions and provides held-out utility at acceptable cost.  
**Falsifies the higher-order claim if:** simpler models match it.

#### Experiment D: bounded metastable repertoire

Identify states without using task labels, then test recurrence, transition structure, task relevance, and response to perturbation on held-out sessions.

**Supports HC-1R if:** differentiated states recur, transitions are non-random, and an intermediate dynamical corridor outperforms frozen and globally synchronized regimes.  
**Falsifies the claim if:** state structure is surrogate-like, non-reproducible, or utility is monotonic toward one extreme.

#### Experiment E: distributed control and resilience

Prospectively predict stimulation-induced transitions, then perform targeted, random, and common-cause lesions.

**Supports HC-1R if:** empirical transition energy is bounded, predictions beat degree and spatial nulls, and capability degrades gracefully.  
**Falsifies the claim if:** metrics fail prospective perturbation or a small targeted/common-cause fault collapses function.

#### Experiment F: perturbational differentiation

Apply equal-energy local probes across operating states and baselines.

**Supports HC-1R if:** responses are both distributed and differentiated, predict independent task capabilities, and return safely.  
**Falsifies the claim if:** responses are local, homogeneous, unstable, or behaviorally irrelevant.

#### Experiment G: optional causal-emergence test

Predeclare microstates, candidate macro partitions, intervention distributions, and lags. Compare EI and predictive validity across real interventions.

**Supports the limited claim if:** positive CE generalizes across held-out interventions and reasonable estimator choices.  
**Falsifies causal emergence as an HC-1R feature if:** it is partition-fragile or observational only. Failure does not falsify the rest of HC-1R.

### 6.3 System-level acceptance rule

The architecture remains **EXTRAPOLATED** until one physical system satisfies the qualification rules in Section 1.2 under the same experimental campaign. Component demonstrations cannot be added together as if they were a system demonstration.

An acceptance claim should report:

- the physical node, channel, layer, delay, capacity, cost, and failure-domain map;
- the identified dynamical model and uncertainty;
- all baseline definitions;
- preregistered observables and thresholds;
- held-out and perturbational results;
- energy, wiring, latency, and thermal accounting;
- random, targeted, and common-cause lesion curves;
- negative results and mechanisms removed after falsification.

## 7. Rejected shortcuts

- **Raw connection count as intelligence:** rejected; it confounds opportunity with selective, causal use.
- **Functional correlation as physical wiring:** rejected; it changes the type of claim.
- **Coherence as proof of communication:** rejected without directionality and intervention.
- **Every clique as a hyperedge:** rejected; clique topology may be entirely pairwise.
- **Graph controllability rank as practical control:** rejected without finite energy and prospective validation.
- **Maximum Kuramoto variance as optimal metastability:** rejected; it is one proxy and can reflect noise.
- **Power laws as proof of criticality:** rejected; non-critical mechanisms can produce them.
- **Positive causal-emergence score as consciousness:** rejected; the score is scale- and intervention-dependent and does not verify experience.
- **PCI-like complexity as synthetic-consciousness certification:** rejected; use it only as a perturbational systems observable.
- **More multiplex layers as more robustness:** rejected unless their physical failure domains are genuinely diverse.

## 8. Bottom-line architecture

The strongest scientifically defensible HC-1R is a **sparse-but-route-rich**, modular, delayed, temporal multiplex with:

- explicit physical channel maps and budgets;
- signed excitation, inhibition, and slower homeostatic control;
- sparse context-sensitive gates, potentially including oscillatory and cross-frequency gates;
- only empirically necessary directed hyperedges;
- distributed control, sensing, and rotating connector roles;
- a bounded metastable corridor rather than permanent integration or exact criticality;
- perturbation-based identification and validation;
- and adversarial lesion, common-cause, delay, and resource tests.

Its distinctive prediction is not “more connections yield more mind.” It is:

> Under equal physical budgets, a selectively gated temporal and higher-order architecture can realize more reproducible, controllable, and robust causal routes than a static pairwise network, without collapsing differentiation or concentrating failure.

That prediction is measurable and falsifiable. Until demonstrated in one integrated physical system, HC-1R remains **EXTRAPOLATED**.

## 9. Annotated primary and review sources

**[CURRENT SOURCE]** These entries preserve the evidentiary role and boundary of the literature used above. Publication does not imply demonstration of the integrated HC-1R system.

### Definitions, network organization, and cost

- Sporns, Tononi & Kötter, [The Human Connectome: A Structural Description of the Human Brain](https://doi.org/10.1371/journal.pcbi.0010042) (2005). Defines the structural connectome; does not identify functional or effective coupling.
- Bullmore & Sporns, [Complex brain networks](https://www.nature.com/articles/nrn2575) (2009). Authoritative graph-theoretic review and structural/functional/effective distinction.
- Bullmore & Sporns, [The economy of brain network organization](https://www.nature.com/articles/nrn3214) (2012). Establishes cost-efficiency trade-offs and hub/rich-club costs; contradicts raw maximization.
- Attwell & Laughlin, [An energy budget for signaling in the grey matter of the brain](https://doi.org/10.1097/00004647-200110000-00001) (2001). Quantifies large signaling and postsynaptic energy costs.
- Ercsey-Ravasz et al., [A predictive network model of cerebral cortical connectivity based on a distance rule](https://pubmed.ncbi.nlm.nih.gov/24094111/) (2013). Macaque tracer evidence for strong spatial wiring constraints.

### Temporal, multiplex, and dynamic organization

- Holme & Saramäki, [Temporal Networks](https://doi.org/10.1016/j.physrep.2012.03.001) (2012). Authoritative temporal-network formalism.
- Mucha et al., [Community structure in time-dependent, multiscale, and multiplex networks](https://doi.org/10.1126/science.1184819) (2010). Multislice community framework.
- De Domenico et al., [Mathematical formulation of multilayer networks](https://doi.org/10.1103/PhysRevX.3.041022) (2013). Tensorial multilayer formalism.
- Bassett et al., [Dynamic reconfiguration of human brain networks during learning](https://doi.org/10.1073/pnas.1018985108) (2011). Empirical multilayer reconfiguration during learning.
- Hutchison et al., [Dynamic functional connectivity: promise, issues, and interpretations](https://doi.org/10.1016/j.neuroimage.2013.05.079) (2013). Review of evidence and methodological limitations.
- Laumann et al., [On the stability of BOLD fMRI correlations](https://pubmed.ncbi.nlm.nih.gov/27591147/) (2017). Shows how sampling, motion, and sleep complicate dynamic-FC claims.

### Integration, segregation, metastability, and oscillatory routing

- Tognoli & Kelso, [The metastable brain](https://doi.org/10.1016/j.neuron.2013.12.022) (2014). Foundational synthesis of metastable integration and segregation.
- Deco et al., [Rethinking segregation and integration](https://www.nature.com/articles/nrn3963) (2015). Whole-brain modeling review.
- Shine et al., [The Dynamics of Functional Brain Networks](https://doi.org/10.1016/j.neuron.2016.09.018) (2016). Links integrated states with working-memory performance.
- O'Byrne & Jerbi, [Metastability demystified](https://www.nature.com/articles/s41583-024-00883-1) (2024). Critical review of definitions and measurement.
- Fries, [Rhythms for Cognition: Communication through Coherence](https://doi.org/10.1016/j.neuron.2015.09.034) (2015). Canonical oscillatory-routing synthesis.
- Palmigiano et al., [Flexible information routing by transient synchrony](https://www.nature.com/articles/nn.4569) (2017). Model demonstration of transient gamma routing.
- Vidaurre et al., [Spontaneous cortical activity transiently organises into frequency specific phase-coupling networks](https://www.nature.com/articles/s41467-018-05316-z) (2018). Large-scale MEG evidence.
- Hahn et al., [Portraits of communication in neuronal networks](https://www.nature.com/articles/s41583-018-0094-0) (2019). Reviews multiple communication mechanisms and their boundaries.

### Higher-order interaction and causal emergence

- Battiston et al., [Networks beyond pairwise interactions: structure and dynamics](https://doi.org/10.1016/j.physrep.2020.05.004) (2020). Authoritative higher-order network review.
- Luppi et al., [A synergistic core for human brain evolution and cognition](https://www.nature.com/articles/s41593-022-01070-0) (2022). Human imaging evidence for synergy-redundancy gradients.
- Varley et al., [Multivariate information theory uncovers synergistic subsystems of the human cerebral cortex](https://www.nature.com/articles/s42003-023-04843-w) (2023). O-information analysis and estimator caveats.
- Santoro et al., [Higher-order connectomics of human brain function](https://www.nature.com/articles/s41467-024-54472-y) (2024). Predictive gains from higher-order fMRI features; not causal proof.
- Hoel, Albantakis & Tononi, [Quantifying causal emergence shows that macro can beat micro](https://doi.org/10.1073/pnas.1314922110) (2013). Formal effective-information result in simple systems.
- Mediano et al., [Greater than the parts](https://doi.org/10.1098/rsta.2021.0246) (2022). Review of information-decomposition approaches to causal emergence.
- Dewhurst, [Causal emergence from effective information: neither causal nor emergent?](https://doi.org/10.1002/tht3.489) (2021). Direct conceptual counterargument.

### Control and perturbation

- Gu et al., [Controllability of structural brain networks](https://www.nature.com/articles/ncomms9414) (2015). Influential linear structural-control model.
- Tu et al., [Warnings and caveats in brain controllability](https://doi.org/10.1016/j.neuroimage.2018.04.010) (2018). Null-model and weighted-degree challenge.
- Tang & Bassett, [Control of dynamics in brain networks](https://doi.org/10.1103/RevModPhys.90.031003) (2018). Authoritative review stressing nonlinear and practical gaps.
- Stiso et al., [White Matter Network Architecture Guides Direct Electrical Stimulation through Optimal State Transitions](https://doi.org/10.1016/j.celrep.2019.08.008) (2019). Intracranial stimulation evidence with simplified-model limits.
- Massimini et al., [Breakdown of cortical effective connectivity during sleep](https://doi.org/10.1126/science.1117256) (2005). Direct TMS-EEG perturbation evidence.
- Casali et al., [A theoretically based index of consciousness independent of sensory processing and behavior](https://doi.org/10.1126/scitranslmed.3006294) (2013). PCI demonstration and its human-neurophysiology scope.

### Vulnerability, pathological dynamics, and criticality

- Uhlhaas & Singer, [Neural synchrony in brain disorders](https://doi.org/10.1016/j.neuron.2006.09.020) (2006). Review of disorder-specific abnormal synchrony.
- Crossley et al., [The hubs of the human connectome are generally implicated in the anatomy of brain disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107735/) (2014). Large cross-disorder hub-vulnerability analysis.
- Fornito, Zalesky & Breakspear, [The connectomics of brain disorders](https://www.nature.com/articles/nrn3901) (2015). Review of topology-dependent vulnerability, degeneracy, and compensation.
- Aerts et al., [Brain networks under attack](https://doi.org/10.1093/brain/aww194) (2016). Computational and empirical lesion review.
- Buldyrev et al., [Catastrophic cascade of failures in interdependent networks](https://www.nature.com/articles/nature08932) (2010). General coupled-network failure theory; application to HC-1R is extrapolated.
- Haimovici et al., [Brain organization into resting state networks emerges at criticality on a model of the human connectome](https://doi.org/10.1103/PhysRevLett.110.178101) (2013). Model support for criticality.
- Wilting & Priesemann, [25 years of criticality in neuroscience](https://doi.org/10.1016/j.conb.2019.08.002) (2019). Review of contradictory evidence and alternative regimes.
- Destexhe & Touboul, [Is there sufficient evidence for criticality in cortical systems?](https://doi.org/10.1523/ENEURO.0551-20.2021) (2021). Demonstrates false-positive criticality signatures in non-critical systems.

## 10. Classification summary

| Candidate | Classification for HC-1R | Reason |
|---|---|---|
| Temporal multiplex routing | **EXTRAPOLATED** | Strong mathematics and descriptive brain evidence; causal physical role not jointly demonstrated |
| Dynamic integration/segregation and metastability | **EXTRAPOLATED** | Biological phenomenon is supported; definition, optimum, and HC mechanism remain open |
| Oscillatory and cross-frequency routing | **EXTRAPOLATED** | Circuit-specific evidence; coherence is not a universal causal route |
| Irreducible higher-order interactions | **EXTRAPOLATED** | Predictive higher-order signals exist; physical hyperedges require stronger controls |
| Distributed practical controllability/observability | **EXTRAPOLATED** | Some perturbation-linked support; common metrics and models remain disputed |
| Perturbational differentiation | **EXTRAPOLATED** | Human assay is demonstrated; transfer to HC-1R is unvalidated |
| Macro causal emergence | **SPECULATIVE** | Formal possibility, preliminary neural application, strong scale/intervention dependence |
| Distributed redundancy and rotating connectors | **EXTRAPOLATED** | Topology-dependent resilience is supported; cost-effective HC realization is untested |
| Homeostatic stability control | **EXTRAPOLATED** | Regulation is biologically necessary; HC control law is unspecified and untested |
| Exact criticality as a requirement | **REJECTED** | Evidence is contested and it conflicts with robust-control assumptions |
| Maximum density or permanent global integration | **REJECTED** | Violates economy, selectivity, differentiation, and resilience constraints |
| Single permanent superhub/global clock | **REJECTED** | Creates bottleneck and common-cause failure without necessary functional gain |

