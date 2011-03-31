#!/usr/bin/env python

__author__ = 'Richard Frankel'
__email__ = 'richard@frankel.tv'
__credits__ = ['Richard Frankel']
__copyright__ = "Copyright 2011, Richard Frankel"
__license__ = 'MIT'
__version__ = (0, 1)
__date__ = '31 March 2011'

import copy
from random import random, randrange

class Candidate(object):
    """Candidate base class with sample methods.
    
    Includes basic mating and mutation methods for binary strings. Also includes
    a sample fitness heuristic that attempts to maximize the number of 1's in
    the string.
    """
    length = 32
    p_mut = 0.1
    
    def __init__(self):
        bits = [str(randrange(0, 2)) for i in range(self.length)]
        self.genes = reduce(str.__add__, bits)
        self._fitness = None
    
    @property
    def fitness(self):
        """Return the candidate's fitness.
        
        If the cached fitness is None, then compute the fitness befor returning
        it.  See `compute_fitness`.
        """
        if self._fitness is None:
            self.compute_fitness()
        
        return self._fitness
    
    def compute_fitness(self):
        """Computes and caches the candidate's fitness.
        
        By default, returns the number of '1's in self.genes, which is a bit
        string by default. You'll almost certainly want to override this method
        with something more sophisticated.
        """
        self._fitness = self.genes.count('1')
    
    def mutate(self, clone=False):
        """With probability self.p_mut, randomly flip each bit in self.genes.
        
        Assumes self.genes is a bit string.
        
        Optional: clone. Defaults to False. If truthy, a new object will be
        created containing the mutated genes, and self.genes will not change.
        
        Returns a candidate with the mutated genes (self when clone=False).
        
        If you override this, you'll probably still want to call the equivalent
        of new_cand.compute_fitness() at the end.
        """
        newgenes = ''
        
        for bit in self.genes:
            if random() <= self.p_mut:
                bit = '1' if bit == '0' else '0'
            newgenes += bit
        
        new_cand = self.__class__() if clone else self
        new_cand.genes = newgenes
        new_cand.compute_fitness()
        
        return new_cand
    
    def mate(self, other):
        """Mate self with other, returning the offspring candidate.
        
        Returns a new self.__class__ object, with each bit of the new object's
        genes selected randomly from self or other. Assumes that self.genes is a
        bit string.
        """
        newgenes = ''
        for pair in zip(self.genes, other.genes):
            newgenes += pair[randrange(0, 2)]
        
        new_cand = self.__class__()
        new_cand.genes = newgenes
        return new_cand
    
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __str__(self):
        return str(self.genes)


def resample(pop):
    """Resample a population by fitness.
    
    Takes a list of candidates and returns a new list of candidates, resampled
    proportional to fitness.
    """
    fitnesses = [t.fitness for t in pop]
    
    resampled = list()
    size = len(pop)
    pos = 0
    step = sum(fitnesses) / float(size)
    
    for i in range(size):
        while((i + .5) * step > sum(fitnesses[:pos + 1])):
            pos += 1
        
        resampled.append(pop[pos])

    return resampled

def evolve(pop, crossover=False, survival=False):
    """Generates the next generation of a population.
    
    The input population is expected to be sorted, for performance reasons; the
    returned population is also sorted.
    
    Optional: crossover. Iff true, offspring will be generated sexually rather
    than asexually. Mutation will occur in either case.
    
    Optional: survival. If true, candidates can survive indefinitely; otherwise,
    they live only one generation.
    """
    offspring = []
    size = len(pop)
    resampled = resample(pop)
    
    if crossover:
        # philosophically, double dipping on resampled in this way may
        # unsmoothly penalize bad candidates...a smoother, but slower, approach
        # would be to call resample twice, passing it the same population sorted
        # differently each time.
        for cand in resampled:
            mate = resampled[randrange(size)]
            child = cand.mate(mate)
            offspring.append(child)
    else:
        offspring = resampled
    
    newpop = [cand.mutate(clone=True) for cand in offspring]
    
    # if candidates can live past one generation, add them into the new
    # generation
    if survival:
        newpop += pop
    
    newpop.sort(reverse=True)
    return newpop[:size]

def sim(generations, pop_size, cand_type=Candidate,
        crossover=False, survival=False, verbose=False):
    """Run a simulation.
    
    Requires the number of generations and the size of the population. Unless
    you're running the example, you'll probably want to specify a subclass of
    Candidate as well. Crossover, survival, and verbosity can optionally be set
    to True. See the `evolve` docstring for explanations of crossover and
    survival.
    """
    pop = [cand_type() for i in range(pop_size)]
    pop.sort(reverse=True)
    best = max(pop)
    for i in range(generations):
        if verbose: print 'Generation', i
        pop = evolve(pop, crossover, survival)
        cur_best = max(pop)
        if(cur_best > best): best = copy.deepcopy(cur_best)
        if verbose: print 'best so far:', best, 'with fitness =', best.fitness

    return best


def main():
    best = sim(100, 100, verbose=True, crossover=True, survival=True)
    print '\n', 'best candidate was', best, 'with fitness =', best.fitness

if __name__ == '__main__':
    main()