LINK:- **bit.ly/2V819eq**   

Indexing during Iteration - use enumerate(). It will return the result in a form of tuple. If you don't specify an index then default it starts from zero.

- Patterns captures experience in software development that have been proven to work again and again, and thus provide a solution to specific problems.Patterns are not invented, they are discovered.

Categories of Patterns depending on their Abstraction Level:-

There are 3 abstraction levels:-

1. Idioms -> These are the lowest-level patterns.They are language specific and they solve very particular problems in a particular language.These idioms typically don't necessarily migrate correctly into other languages.
They are very programming languages specific.
2. Architectural Patterns -> This is the highest-level that we have regarding patterns.Architectural Patterns have to do with things like MVC, Microservices, pipes and filters(UNIX and LINUX) that really allow us to in
general provide the structure for a complete working system.They are very high-level and sit on the top of Design Patterns.
3. Design Patterns -> Design Patterns fit exactly in the middle b/w Idioms and Architectural Patterns.Design Patterns have to do with specific issues on the design of a part of a system not a full system but just maybe a
part and once again these are solutions of recurring problems and they have a particular feature that they are usually language independent but they are typically oriented to a specific programming paradigm.



Relevance of Design Patterns:-

1. Tried and tested solutions  --> Design patterns are focused on uncommon problems that occur very frequently 
2. Common Language 



Design Patterns are Reusable units.


**Limitations of Design Patterns**:

1. Unjustified use
2. Design Patterns tend to be Kludges for weak programming languages
3. Ineffecient Solutions

Python has a support for Iterators which is a classical design pattern but you don't consider it as the design pattern as it is very well supported in the language itself.

The 23 Design Patterns are actually classified based on their use:-

* Creational Patterns --> They to do with how we instantiate objects, how we create them in a way that is flexible and allows us to make our code not so hard-code.
* Structural Patterns --> These have to do with the general structure, the general structure has to do with the way that we put together classes and objects and how they communicate between them and how we provide a much
more sophisticated complex operation between them.
* Behavioral Patterns --> They have to do with the communication of assignment of responsibilities that have or that occur between different components here.


**Design Principles**:-

1. We have to separate out the things that change from those that stay the same.
2. Program to an interface, not an implementation  --> what we have to understand here is that when we are designing an object,the object has 2 things i.e. it has an Interface and it has an Implementation.

The interface has to do with how rest of the world interacts with that object. In Programming Languages, we can think of an Interface as what methods are supported for this particular object. If it has relations with the
other objects then all those things are part of the interface. If it has to do with how publicly the clients use it the contagion has to do with how do I get, how does the object internally work and usually the Implementation is something that we want to keep hidden.


In many programming languages we can think of an interface as a different programming construct. In Python there is nothing like that, there is a concept of **Abstract Base Classes(ABC)** that works as interfaces in other
languages.

In General, Interface has to do with the contract on how a particular object works and we should just work with what is publicly known as and published according to its interface and its implementation details are ignored
because they are not or they should be really not necessary for us to understand in order to use them successfully on our objects.

3. Prefer Composition over Inheritance  --> Composition and Inheritance are 2 ways in which we can reuse code in Object Oriented Programming. 

Composition basically means that instead of extending the class we can instantiate a class contain it inside some objects and then make use of Delegation to actually make use of these compose classes.

4. Delegation

The points 3 and 4 works together and allow us to have a much simpler elegant design but maybe not necessarily as much simple but probably more SOLID with less issues because in Inheritance there is a very strong coupling between the Original Base class and other Derived classes and the issue is that if you happen to modify the base class you might end up impacting the Derived Classes.


**Anatomy of a Design Pattern**:-

1. Intent -> It has to do with what's the general definition or general use of the design pattern.
2. Motivation -> Why do we need it, why is it useful in under which circumstances you typically might end up using it and for practical purposes.
3. Structure - UML diagram of the pattern so that we can see all the patterns involved.
4. Implementation

Singleton Pattern:- The singleton pattern is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

`is` allows us to check if two objects are same. Same means they are physically in the memory they represent the same object. In other words they have the same memory address.
~

