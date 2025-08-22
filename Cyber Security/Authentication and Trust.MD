# Authentication and Trust

Created: 12 May 2025 18:11 Is Completed: Yes

Authentication is essential for verifying tokens. We need to confirm that
presented tokens are genuine (or at least genuine enough) and that they
sufficiently prove the presenter's legitimacy. For tokens the system hasn't
encountered before, we need a way to evaluate their credibility before
acceptance.

A common approach we use daily is the "challenge-response" model, where one
token verifies another. The username and password system exemplifies this. When
logging into a computer or online service, we first present a username—a token
claiming our identity. (This is similar to presenting a bank card at an ATM,
which serves as an identity claim).

Usernames are relatively weak tokens since they're often easy to guess,
particularly when derived from real names or structured formats like email
addresses.

Because usernames are weak identity proof, we require a second, stronger
token—the password. Passwords were historically considered more reliable because
they're meant to be secret, known only to the legitimate identity holder.
However, we now know that people frequently reuse passwords and choose ones that
are easily remembered and guessed. Despite these limitations, the password
system's convenience means it will likely persist for years to come.

A password functions as a shared secret—both the claimant and system must know
it (or its representation) for verification. This requires a system for
generating passwords, linking them to usernames, and sharing this information
with the appropriate parties. However, we face a circular problem: how do we
ensure we're sharing these credentials with the right entities when we haven't
yet established their identity?

i.e. - we lack **trust.**

Establishing trust deserves its own detailed study as it extends beyond token
issuance. For now, we'll focus on trust within Identification and
Authentication.

## Simple trust concepts

As children, we begin with implicit trust in everything around us. We soon learn
this isn't always wise and start seeking external validation of what's "safe."
This typically comes from parents or guardians who've proven their
trustworthiness. At school, these authority figures (our "principals") assure us
that teachers are trustworthy. Teachers then become delegated authorities whose
trust judgments we accept.

This demonstrates a "chain of trust." Each trusted entity connects to a
previously trusted one, forming a chain that leads back to the **root
authority**.

A system based on an external root authority works well when such an authority
exists. This model underlies passports, driving licenses, ID cards, banknotes,
and more. These tokens gain trustworthiness through issuance by agencies
connected to a central authority—typically governmental or organizational
management. (While individual views on these authorities' trustworthiness may
vary, we're discussing the fundamental concept).

Sometimes that root authority isn't external, and we have to establish our own
rules for evaluating trust before issuing tokens to an entity.

DAC

### Reminder: Discretionary Access Control (DAC)

We previously examined DAC and its implementation. But is DAC sufficient, and
why have alternative approaches been developed?

### Problems with DAC

### **Trojan Horses**

Named after the ancient wooden horse of Troy, a computer Trojan Horse is
software that appears harmless and performs useful functions while secretly
causing damage in the background. For example, a text editor might allow users
to create documents while secretly copying the text to a hidden file. Or a
modified Unix "ls" command might list directory contents while simultaneously
altering DAC permissions, spreading malicious code, or copying sensitive data to
unauthorized recipients.

A closer examination reveals that DAC fails to prevent certain types of harmful
activities. When a Trojan Horse enters the system, DAC allows it to operate with
all the privileges of its host process, making it likely to achieve its
malicious goals. DAC simply assumes that all system components are legitimate
and doesn't verify a subject's intentions before granting access.

### **Protection against Trojans**

Several approaches exist to protect against Trojans:

- We could review the source code thoroughly, compile it with a trusted
  compiler, and run it on a system with verified libraries—though this becomes
  impractical with commercial software and frequent updates.

Or

- We can accept the risks of Trojans and focus on minimizing potential damage.

OR

- We can combine these approaches by limiting how untrusted software
  (potentially all programs) can access certain operations.

To implement this protection, we establish a **Trusted Computer Base (TCB)**
comprising:

- A **Reference Monitor** that enforces access control policies
- Access routines for sensitive operations (such as disk writing and network
  communication)
- A verified Trojan-free environment (meaning we've validated the TCB's
  trustworthiness)

Under this system, untrusted software must access restricted operations and
controlled objects through the TCB. The reference monitor evaluates each access
request and enforces MAC policies to protect both objects and the system
(including the TCB). This approach reduces the risk of asset compromise or
damage.

When an untrusted process needs to access a protected object, it must make a
request through the TCB. Inside the TCB, the reference monitor's Access
Enforcement Facility (AEF) consults with the internal Access Control Decision
Facility (ADF) to verify if the process can use the requested restricted
operation.

The reference monitor may block access at this first checkpoint. If the process
is permitted to proceed, a second verification occurs—the AEF and ADF check
whether the process can perform its intended action on the protected object. The
ADF may instruct the AEF to block the operation if the process lacks proper
authorization. Otherwise, the operation proceeds if the process is acting within
its defined access rights.

This creates a hybrid system that uses DAC as the primary access control policy
while incorporating MAC elements to handle untrusted software. Now let's examine
MAC more closely.

### Mandatory Access Control

Unlike DAC, MAC offers stronger protection against Trojans. Since subjects and
objects are grouped into security classes (groups of entities with identical
security attributes), it enables more precise control over process actions.
Furthermore, MAC prevents rogue processes from altering permissions because
subjects cannot modify permissions directly. Instead, changes must go through a
formal, tightly controlled approval process.

MAC systems typically implement multiple security levels, and they commonly
appear in both military and commercial contexts.

### Military and Commercial MAC

These two MAC implementations share basic security level concepts but serve
different purposes:

- The Military version focuses on secrecy—preventing information disclosure to
  unauthorized individuals.
- The Commercial version prioritizes integrity—protecting business-critical data
  from damage.

To properly manage security, we need a way to track who can do what with
different resources in our system. We can do this using Access Control Lists
(ACLs). This system has three main parts:

(S, O, A)

These parts are:

- S - all the users and programs that can access things (called "subjects")
- O - all the files, folders, and resources that can be accessed (called
  "objects")
- A - a table that shows what each subject is allowed to do with each object

The system also includes 'P', which is simply a list of all possible actions
that subjects can perform on objects (like read, write, or delete).

### Consider the following ACLs:File-1: ((Cathy,r), (Eve, orw))File-2: ((Alice, r), (Bob, orw), (Cathy,r), (Dan, r))File-3: ((Alice, orw), (Bob, r), (Cathy, r))File-4: ((Alice, r), (Cathy, r), (Dan, orw))File-5: ((Bob, r), (Cathy, orw), (Dan, r))If you have any questions about this activity, please post them in the [Week 2 Activity Forum Q&A](https://onlinestudy.york.ac.uk/courses/1532/modules/12488)

- File-1: ((Cathy,r), (Eve, orw))
- File-2: ((Alice, r), (Bob, orw), (Cathy,r), (Dan, r))
- File-3: ((Alice, orw), (Bob, r), (Cathy, r))
- File-4: ((Alice, r), (Cathy, r), (Dan, orw))
- File-5: ((Bob, r), (Cathy, orw), (Dan, r))

| File 1 | File 2 | File 3 | File 4 | File 5 |
| ------ | ------ | ------ | ------ | ------ |
| Alice  |        | R      | Orw    | R      |
| Bob    |        | Orw    | R      |        |
| Cathy  | R      | R      | R      | R      |
| Dan    |        | r      |        | orw    |
| Eve    | orw    |        |        |        |
