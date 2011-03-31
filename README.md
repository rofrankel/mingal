mingal - a MINimalistic Genetic Algorithm Library
=================================================

Usage
-----

In a nutshell, you use mingal by sublcassing `mingal.Candidate` and passing
your sublclass to `mingal.sim`. You'll almost certainly want to override at
least the `compute_fitness` method. Each method's docstring should be
sufficient for you to override it when applicable.

In many cases, it will be easiest for you to maintain the bit string gene
representation and override only the `compute_fitness` method; this lets you
use the `mutate` and `mate` methods provided. Of course, if encoding and
decoding such a representation is sufficiently difficult and/or you want more
structured mutation and mating (which might be the case if the space of
*feasible* candidates in your problem is sparse) then you can override `mate`
and `mutate` as well.

Sample
------

By default, Candidate maximizes the number of '1's in a bit string.

Running `python mingal.py` will run a sample simulation. See the bottom of
mingal.py for the code which runs this sample.

License
-------

mingal is released under the MIT license, the text of which follows. That
basically means you can do whatever you want with it. However, if you use or
modify mingal, I'd appreciate it if you'd take the time to [send me an
email](mailto:richard@frankel.tv?subject=mingal) and show me what you did.

Copyright (C) 2011 by Richard Frankel (richard@frankel.tv)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.