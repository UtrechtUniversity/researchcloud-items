# Design principles for developers and contributors

In this document several ideas and design principles are explained that anyone working on this repository should keep in mind.
These are more guidelines than strict rules, although they should only be deviated from for good reason.
Any deviations should be considered to be added inside this document.
As a living document, it should get more complete over time.

## Build small
There are many arguments in favor of building small: it allows for quick iteration, prevents complexity and allows others to quickly understand it.
It also inherently tends to help with the `Build reusable` and `Build sustainably` section of this document.
Building small specifically refers to the amount of logical steps and actions your roles/playbooks make.

## Build little
In addition to building small, building little refers to the act of trying to solve the problem with as little steps as possible, and also as close to recommended as posible.
The reason is two-fold: when little happens it will be easier to understand in the future by yourself or others.
Additionally, if anything changes in the recommended way in official documentation, it should be easier to replace your existing code with this new way.

## Build reusable
Reusable parts have their reason in their name: parts that can be reused need not be created.
Also reusability comes in different levels: because this software is (primarily) used in SURF Research Cloud, it should be taken into mind that different users have different needs, which can be served with different existing items.

## Build modular
This point can be seen as a continuation of the `Build resusable` section.
When a role or playbook has variables, it helps in preventing continuously updating the code, for example with new software versions.
An update of the variable should be sufficient. 
And as described in the `Build reusable` section, different needs can be served through the same piece of code with changed variables.

## Build sustainably
While no project advertises the building of unsustainable code, it is worth to keep thinking to yourself: "Is this code sustainable"?
Not only do new versions of technologies get released constantly, end-users change their requirements and new users can have very similar but slightly different demands.
It pays off in the long run to think about these scenario's and try to incorporate anything in your code that makes it more sustainable, which is likely to fit into any of the other sections in this document.

## Build intentionally
Not all software is meant to be used by every user, not should every file be available to anyone.
When writing your code, keep this in mind and make things available on a limited basis.
Grant permissions only on those specific files needed, instead of entire directories.
Install software only for all users to be shared if it makes sense, else consider personal installations.
