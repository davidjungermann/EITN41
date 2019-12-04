Commitment scheme x = h(v,k), where v is a 1-bit commitment, k is a K-bit random string. In this task, K = 16 bits.
h is a hash function with output truncated to X bits. 

Choose appropriate X. 

Write code to simulate: 

The probablility of breaking the binding property of the scheme. Non-idiot attacker, which means that the attacker picks a value for k that they know can break the binding property before comitting to v. Closely related to well-known property for hash functions. 

The probablility of breaking the concealing property of the scheme. The attack is carried out by the receiver of the commitment, which means it's not possible choose optimal values before the commitment. Closely related to well-known property for hash functions. 

Probability of breaking the concealing property = ratio between number of x values for which the committed bit can be uniquely determined and the total number of possible x values.

A hint is that the birthday paradox is closely related to one of the two cases.

To get on the right track, it can be useful to consider two column vectors, representing all possible
values for x:
v = 0          v = 1
----------------------
h(0, 0)        h(1, 0)
h(0, 1)        h(1, 1)
h(0, 2)        h(1, 2)
          .
          .
          .
          .
          .
          .
h(0, 2^16 − 1) h(1, 2^16 − 1)

Now, what is required for breaking the binding property? What is required for breaking the concealing(hiding?)
property?


https://cs.nyu.edu/courses/fall08/G22.3210-001/lect/lecture14.pdf 

In simple protocols, the commit phase consists of a single message from the sender to the receiver. This message is called the commitment. It is essential that the specific value chosen cannot be known by the receiver at that time (this is called the hiding property). A simple reveal phase would consist of a single message, the opening, from the sender to the receiver, followed by a check performed by the receiver. The value chosen during the commit phase must be the only one that the sender can compute and that validates during the reveal phase (this is called the binding property).


Pre-image resistance:
Given a hash value h it should be difficult to find any message m such that h = hash(m). This concept is related to that of a one-way function. Functions that lack this property are vulnerable to preimage attacks.

Second pre-image resistance:
Given an input m1, it should be difficult to find a different input m2 such that hash(m1) = hash(m2). This property is sometimes referred to as weak collision resistance. Functions that lack this property are vulnerable to second-preimage attacks.

Collision resistance: 
It should be difficult to find two different messages m1 and m2 such that hash(m1) = hash(m2). Such a pair is called a cryptographic hash collision. This property is sometimes referred to as strong collision resistance. It requires a hash value at least twice as long as that required for pre-image resistance; otherwise collisions may be found by a birthday attack.[4]


1.


