***Python Premier***

* A python identifier(variable) cannot begin with a numeral. python has 33 reserved words that can't be used as identifiers 
* Instantiation is the process of creating a new instance of a class
* Many python's built in classes support internal form e.g. ``` temp = 98.6 ``` create an instance of the float class
* In methods, we have accessors - they return information about the state of an object while mutators cahnge the state of an object 
* Python's built in class could be mutable or immutable 
* python supports integral values using binary, octal or hexademicl. This is done by using a prefix of the number `0` then a characcter to describe the base.  e.g. `0b1001`, `0o52` & `0x7f`
* Sequence types: `list`, `tuple` and `str` classes
* The `list` constructor produces an empty list by default. However, the construtor `list()` will accept any parameter that is of an iterable type
`list('hello')` = `['h', 'e', 'l', 'l' 'o']`
`mylist` = `[]`
`myTuple` = `()`
`oneList` = `[32]`
`oneTuple` = `(32,)` **notice the trailing comma**
* A set is a collection of element without duplicates and without
* Set is highly optimised checking whether a specific element is contained in the set. it is based on the datastructure called hash table 
* Only instance of immutble types can be added to a set. mutable types such as list, dictionaries, sets can't be added to a set hence you can't have `a set of sets `
* `frozenSet` is an immutable type of set. so you can have a `set of frozen sets`
* A set is delimited with `{}` but `{}` does not delimit an empty set but an empty dictionary. instead the constructor `set()` gives an empty set
*   `pairs = [('ga', 'irish'), ('de', 'German')]`  
    `dict(pairs) will give {'ga':'irish', 'de': 'German'}`