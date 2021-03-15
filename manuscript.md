# Chapter One: Simulation models for determining ecological mechanisms

## Why is understanding metacommunities important to ecology and evolution?
- the scale at which (many) evolutionary and ecological processes intersect
- landscapes scales up to ranges [@Leibold2003MetCom]
- applied angle. landscape and climate change is causing rapid changes to the structure of Earth's landscapes and biodiversity
- Can we understand? -> Can we predict? -> Can we forecast/manage?
- Ecology is as much a study of emergent properties across scales as it is anything to do with biology.
- The data we collect from these systems is inherently noisy.
- Data we collect is information produced by a combination of "true" mechanisms (interacting in unknown ways) + noise.

Why are dynamics fundamental to ecology? They encode mechanism

## What methods have been used to understand metacommunities?

## How can mechanistic models supplement this?

## Why should we use mechanistic models in ecology?

What is an ecological mechanism? A mapping between low dimensional latent/parameter space and information space.

Science is fundamentally a theory of epistemology: a methodology and set of
principles to make justified claims about the world. Descriptive claims about
the world (the Earth goes around the sun,  more species are found near the
equator than far from it) are considered justified if they make predictions that
agree with observed reality.
In order to determine if a descriptive claim agrees
with reality, it must be translated into a quantitative model that makes
predictions about things that can be measured. These quantitative models take
many forms. A subclass of these models, mechanistic models, represent latent
processes that can not be observed or measured, either inherently or due to
technological limitations.

If one abandons the notion that a model represents some "truth" about the the
world, vs. for predictive accuracy. The problem is you cannot tell the
difference --- the induction problem.

Yet there are limits to the scope of simulation models. How do we know when they
are appropriate, versus a ML/non-mechanistic model?

- If a simulation makes data the looks like real data, does it represent the "true" world?
- Does it matter? Newtonian Gravity was "right", until GR was more right.
- Mechanisms that are incorrect that produce information that shates statistical properties with
empirical data is still useful.
- Feynman on Models


# Chapter Two: MetacommunityDynamics.jl

## Introduction

### Why do we need software to simulate metacommunity dynamics?

Here we provide examples in how this software can be used to
understand species interaction across space and time based around four mechanisms in @Vellend2010ConSyn.

### What can you do with this?
- Generate sample of metacommunity trajectories based on
mechanistic hypotheses.

## Software and Model Description
Written in Julia, interfaces with data structures in EcoJulia.
Virtual laboratory [@Grimm2005IndBas].

- `Landscape`: a set of locations in space with corresponding environment data.
- `Metaweb`: a set of species which form a species pool, plus an interaction network.
- An `AbstractDynamics` model is composed of `AbstractDispersalModel` + `AbstractSelectionModel` + `AbstractDriftModel`.
- Running `simulate(dynamicsmodel)` where `dynamicsmodel` is of the type `AbstractDynamics` simulates a `MetacommunityTrajectory{MT}` (where `MT` is a `MeasurementType`; at the moment: `Occupancy`, `Abundance`, or `Trait`)
- Simulates `Observer`s with given `ObserverError`.


## Case Studies


### Food web SAR and rank abundance

This case study simulates a food web according to the following dynamics
models: Lotka-Voltera, MacArthur Consumer-Resource, Allometric MacArthur CR. The trajectories are sampled to generated expected 1) species area relationship and 2) rank-abundance curves for each model. 

### Plant-pollinator nestedness

This case study simulates a metaweb of plants and pollinators across space.
We simulate an expected amount of nestedness in the interaction network using
various models of the dynamics of trait evolution


# Chapter Three: The forecasting horizon of ecological systems

How far into the future can we foresast the behavior of ecological
communities, given a certain accuracy of both the true dynamics and
data.


Expected accuracy as a function of 1) data amount and 2) measurement error.


# Chapter Four: Optimizing corridor placement in an uncertain world

Given a constraint, what corridor in a landscape enables ecosystem functioning?
What is defined by a target state, and how do you define an optimization algorithm
to decide what the best decision under the constraint is.


