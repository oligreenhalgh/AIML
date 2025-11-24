import numpy as np
"""
The goal of this take-home assignment is to implement, in Python, a
small library that samples and evaluates assignments in 
discrete probabilistic graphical models (PGMs). 
"""
def distr_values(cpt, parents, values, spaces):
    # Reduces a full CPT to a specific 1D distribution for a child node,
    # given the current state of its parents.
    if len(parents) == 0:
        return cpt
    else:
        selection = []
        for parents_idx in parents:
            parent_value = values[parents_idx]
            parent_space = spaces[parents_idx]
            idx = parent_space.index(parent_value)
            selection.append(idx)
        selection.append(slice(None))
        tupslice = tuple(selection)
        distr = cpt[tupslice]
        return distr

def distr_sample(space, distr):
    # Randomly selects value from a domain based on probability distribution
    sample = np.random.choice(space, p=distr)
    prob = float(distr[space.index(sample)])
    return sample, prob

def pgm_evalsample(spaces, graph, cpts, assign):
    # Iterates through graph to fill in missing values and calculate join probability
    samples = list(assign)
    probability = []
    joint_probability = 1
    for space_ix, cpt in enumerate(cpts):
        parents = graph[space_ix]
        space = spaces[space_ix]
        distribution = distr_values(cpt,parents,samples , spaces)
        probability.append(distribution)
        val = samples[space_ix]
        if val is None:
            sample_val, calc_probability = distr_sample(space, distribution)
            samples[space_ix] = sample_val
        else:
            fixed_value_index = space.index(val)
            calc_probability = distribution[fixed_value_index]
        joint_probability = joint_probability*calc_probability
    return samples, probability, joint_probability


