# Introduction to Algorithm
Design

Language: Python

An algorithm is a procedure to accomplish a specific
task. An algorithm is the idea behind any reasonable computer program

An algorithm is a procedure that takes any of the possible input instances
and transforms it to the desired output. There are many different algorithms
that can solve the problem of sorting. For example, insertion sort is a method
that starts with a single element (thus trivially forming a sorted list) and then
incrementally inserts the remaining elements so that the list remains sorted

There are three desirable properties for a good algorithm. We seek algorithms that are correct and efficient, while being easy to implement. These
goals may not be simultaneously achievable. In industrial settings, any program that seems to give good enough answers without slowing the application
down is often acceptable, regardless of whether a better algorithm exists. The
issue of finding the best possible answer or achieving maximum efficiency usually
arises in industry only after serious performance or legal troubles

Take-Home Lesson: There is a fundamental difference between algorithms,
procedures that always produce a correct result, and heuristics, which may
usually do a good job but provide no guarantee of correctness

Take-Home Lesson: Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated

We need tools to distinguish correct algorithms from
incorrect ones, the primary one of which is called a proof.
A proper mathematical proof consists of several parts. First, there is a
clear, precise statement of what you are trying to prove. Second, there is a set
of assumptions of things that are taken to be true, and hence can be used as
part of the proof. Third, there is a chain of reasoning that takes you from these
assumptions to the statement you are trying to prove. Finally, there is a little
square ( ) or QED at the bottom to denote that you have finished, representing
the Latin phrase for “thus it is demonstrated.”

Take-Home Lesson: An important and honorable technique in algorithm design is to narrow the set of allowable instances until there is a correct and
efficient algorithm. For example, we can restrict a graph problem from general
graphs down to trees, or a geometric problem from two dimensions down to
one.

Reasoning about an algorithm is impossible without a careful description of the
sequence of steps that are to be performed. The three most common forms of
algorithmic notation are (1) English, (2) pseudocode, or (3) a real programming
language. Pseudocode is perhaps the most mysterious of the bunch, but it is
best defined as a programming language that never complains about syntax
errors.
All three methods are useful because there is a natural tradeoff between
greater ease of expression and precision. English is the most natural but least
precise programming language, while Java and C/C++ are precise but difficult
to write and understand. Pseudocode is generally useful because it represents
a happy medium.
The choice of which notation is best depends upon which method you are
most comfortable with. I usually prefer to describe the ideas of an algorithm in
English (with pictures!), moving to a more formal, programming-language-like
pseudocode or even real code to clarify sufficiently tricky details.
A common mistake my students make is to use pseudocode to dress up an
ill-defined idea so that it looks more formal. Clarity should be the goal.

Take-Home Lesson: The heart of any algorithm is an idea. If your idea is
not clearly revealed when you express an algorithm, then you are using too
low-level a notation to describe it.

Take-Home Lesson: Searching for counterexamples is the best way to disprove
the correctness of a heuristic

Failure to find a counterexample to a given algorithm does not mean “it is
obvious” that the algorithm is correct. A proof or demonstration of correctness
is needed. Often mathematical induction is the method of choice.

Take-Home Lesson: Mathematical induction is usually the right way to verify
the correctness of a recursive or incremental insertion algorithm

- Permutations are arrangements, or orderings, of items. For example,
{1, 4, 3, 2} and {4, 3, 2, 1} are two distinct permutations of the same set
of four integers. We have already seen permutations in the robot optimization problem, and in sorting. Permutations are likely the object in
question whenever your problem seeks an “arrangement,” “tour,” “ordering,” or “sequence.”

• Subsets represent selections from a set of items. For example, {1, 3, 4}
and {2} are two distinct subsets of the first four integers. Order does
not matter in subsets the way it does with permutations, so the subsets
{1, 3, 4} and {4, 3, 1} would be considered identical. Subsets arose as candidate solutions in the movie scheduling problem. They are likely the
object in question whenever your problem seeks a “cluster,” “collection,”
“committee,” “group,” “packaging,” or “selection.”

• Trees represent hierarchical relationships between items. Figure 1.9(a)
shows part of the family tree of the Skiena clan. Trees are likely the
object in question whenever your problem seeks a “hierarchy,” “dominance
relationship,” “ancestor/descendant relationship,” or “taxonomy.”

• Graphs represent relationships between arbitrary pairs of objects. Figure
1.9(b) models a network of roads as a graph, where the vertices are cities
and the edges are roads connecting pairs of cities. Graphs are likely the
object in question whenever you seek a “network,” “circuit,” “web,” or
“relationship.”

• Points define locations in some geometric space. For example, the locations of McDonald’s restaurants can be described by points on a map/plane.
Points are likely the object in question whenever your problems work on
“sites,” “positions,” “data records,” or “locations.”

• Polygons define regions in some geometric spaces. For example, the borders of a country can be described by a polygon on a map/plane. Polygons
and polyhedra are likely the object in question whenever you are working
on “shapes,” “regions,” “configurations,” or “boundaries.”

• Strings represent sequences of characters, or patterns. For example, the
names of students in a class can be represented by strings. Strings are
likely the object in question whenever you are dealing with “text,” “characters,” “patterns,” or “label”

- The elements of a permutation of {1,...,n} get renumbered
after element deletion in order to remain a permutation of {1,...,n − 1}.
renumbering gives {1, 4, 2, 3}, a permutation of {1, 2, 3, 4}. Permutations
are recursive objects.

• Subsets – Every subset of {1,...,n} contains a subset of {1,...,n − 1}
obtained by deleting element n, if it is present. Subsets are recursive
objects.
• Trees – Delete the root of a tree and what do you get? A collection of
smaller trees. Delete any leaf of a tree and what do you get? A slightly
smaller tree. Trees are recursive objects.
• Graphs – Delete any vertex from a graph, and you get a smaller graph.
Now divide the vertices of a graph into two groups, left and right. Cut
through all edges that span from left to right, and what do you get? Two
smaller graphs, and a bunch of broken edges. Graphs are recursive objects.
• Points – Take a cloud of points, and separate them into two groups by
drawing a line. Now you have two smaller clouds of points. Point sets are
recursive objects.
• Polygons – Inserting any internal chord between two non-adjacent vertices of a simple polygon cuts it into two smaller polygons. Polygons are
recursive objects.
• Strings – Delete the first character from a string and what do you get?
A shorter string. Strings are recursive objects.