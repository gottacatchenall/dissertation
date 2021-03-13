# Dissertation Outline

## Chapter Structure

1. Introduction and Review: Simulation models in ecology; scaling up from metacommunities to ranges
2. EcologicalDynamics.jl
3. Forecasting Horizon
4. Corridor Optimization


## Chapter One  

Summary of the motivation for what I do here.

### Why is understanding metacommunities important to ecology and evolution?
- the scale at which (many) evolutionary and ecological processes intersect
- landscapes scales up to ranges [@Leibold2003MetCom]
- applied angle. landscape and climate change is causing rapid changes to the structure of Earth's landscapes and biodiversity
- Can we understand? -> Can we predict? -> Can we forecast/manage?

### Why simulate? Models and mechanisms
- Ecology is as much a study of emergent properties across scales as it is anything to do with biology.
- The data we collect from these systems is inherently noisy.
- Data we collect is information produced by a combination of "true" mechanisms + noise.
- What is an ecological mechanism? A mapping between low dimensional latent/parameter space and information space.
- If a simulation makes data the looks like real data, does it represent the "true" world?
- Does it matter? Newtonian Gravity was "right", until GR was more right.
- Mechanisms that are incorrect that produce information that shates statistical properties with
empirical data is still useful.
- Feynman on Models



## Chapter Two --- EcologicalDynamics.jl

### Intro

- Why do we need software to simulate metacommunity dynamics?
- Why are dynamics fundamental to ecology? The encode mechanism
- Here we provide examples in how this software can be used to
understand species interaction across space and time


### Software Description
- Written in Julia, interfaces with data structures in EcoJulia

### What can you do with this?
- Generate distribution of metacommunity measurements based on
mechanistic hypotheses about species interaction

### Case Studies
- Plant pollinator nestedness
- Food web SAR
- Host parasite evolution

## 3. Chapter Three --- Forecasting Horizon

How far into the future can we foresast the behavior of ecological
communities, given a certain accuracy of both the true dynamics and
data.

## 4. Chapter Four --- Corridor Optimization

Given a constraint, what corridor in a landscape enables ecosystem functioning?
What is defined by a target state, and how do you define an optimization algorithm
to decide what decision under the
