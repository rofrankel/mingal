mingal - a MINimalistic Genetic Algorithm Library
=================================================

Usage
-----

In a nutshell, you use mingal by sublcassing `mingal.Candidate` and passing your
sublclass to `mingal.sim`. You'll almost certainly want to override at least the
`compute_fitness` method. Each method's docstring should be sufficient for you
to override it when applicable.

In many cases, it will be easiest for you to maintain the bit string gene
representation and override only the `compute_fitness` method; this lets you use
the `mutate` and `mate` methods provided. Of course, if encoding and decoding
such a representation is sufficiently difficult and/or you want more structured
mutation and mating (which might be the case if the space of *feasible*
candidates in your problem is sparse) then you can override `mate` and `mutate`
as well.

Running `python mingal.py` will run a sample simulation.  See the bottom of
mingal.py for the code which runs this sample.

If you use or modify this, I'd appreciate the opportunity to see what you did.
