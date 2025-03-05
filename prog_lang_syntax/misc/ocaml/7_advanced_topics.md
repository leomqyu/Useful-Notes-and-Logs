# 1. High order functions
1. Intro
    Means that a functions takes function as argument

1. Eg. a fn that repeats fn for some times
    1. Define
        ```
        # let rec repeat times thing_to_do = 
            if times < 1 then () 
            else begin 
              thing_to_do (); 
              repeat (times- 1) thing_to_do 
            end ;; 
        val repeat : int-> 'a-> unit = <fun>
        ```
    1. Use
        Note: the argument passed must be wrapped in another function so that the functions execution will be delayed.
        ```
        # (*repeat say hi*)
        # let say_hi name = print_string ("Hello, " ^ name ^ "!\n") ;; 
        val say_hi : string-> unit = <fun>
        # repeat 3 (fun ()-> say_hi "Camel");;

        # (*print big spaces*)
        # let print_big_space () = repeat 10 print_newline;; val print_big_space : unit-> unit = <fun>
        ```

1. Wrong eg
    If func is called like this (roughly, no '()' after 'thing_to_do' in func definition), only one time of 'Hello, Camel!' because:    
    in OCaml, the arguments are evaluated before the function itself, so in this case, we ended up saying ”hi” before we even got to the repeat function.
    ```
    # repeat 3 (say_hi "Camel");; 
    Hello, Camel!
    -: unit = ()
    ```

# 2. Currying and Uncurrying

1. Background
    in OCaml all functions really just take one parameter, when call add x y, actually calling two functions: ((add x) y): take in `int`, output `int -> int`
    ```
    # let add x y = x + y;;
    val add : int -> int -> int = <fun>
    ```
    But if pass the param as a tuple, then is really taking a single input: input is of type `int * int`, output is of type `int`
    ```
    # let add (x, y) = x + y;;
    val add : int * int -> int = <fun>
    ```
    Sometimes it helps to apply parts of a function in different orders, and sometimes it helps to make a function really take all its parameters at once.
    Term `curry`: separate the function input params into parts; `uncarry`: combine the argument into a single argument.

1. Operation
    1. curry
        Take in 3 arguments `f`, `x`, `y`, output is the value of expression `f (x, y)`, which is the result of the function that takes a tuple as input
        ```
        # let curry f x y = f (x, y);;
         val curry : ('a * 'b-> 'c)-> 'a-> 'b-> 'c = <fun>
        ```

    1. uncurry
        take in 2 arguments `f` and `(x, y)` return is `f x y`.
        ```
        # let uncurry f (x, y) = f x y;;
         val uncurry : ('a-> 'b-> 'c)-> 'a * 'b-> 'c = <fun>
        ```

1. Example use
    1. Specializing function
        ```
        (*Take in a tuple, cal the product*)
        # let calculate_total (price, quantity) =
          price *. float_of_int quantity;;
        val calculate_total : float * int-> float = <fun>

        (*
        `curried_total` is still a function: 
        is the function of curry after already given the first input.
        So if give it another 2 separate inputs of `x` and `y`
        It will calculate and output the value of calculate_total (x, y)
        *)
        # let curried_total = curry calculate_total;;
        val curried_total : float-> int-> float = <fun>

        (*
        `buy_one` is another function based on the function of `curried_total`
        So can calculate with price = 9.99 fixed
        *)
        # let buy_one = curried_total 9.99;;
        val buy_one : int-> float = <fun>
        ```

# 3. Variants
Note in type alias also use keyword `type`
1. Intro
    To represent data that may take on multiple different forms, where each form is marked by an explicit tag.

2. Syntax
    1. Use `type` as keyword
    1. a `tag` or `constructor` is used to denote a certain "form". Tag's name must be capitalized.
    1. Each form is marked with `|`
    1. Each form can optoinally be specified with a value using keyword `of`. Can be a single type or a tuple
    ```
    (*create a variant*)
    type <variant> =
      | <Tag> [ of <type> [* <type>]... ]
      | <Tag> [ of <type> [* <type>]... ]
      | ...

    (*declare an instance*)
    let x = <Tag> value
    ```

4. Example uses
    1. Enumeration
        ```
        # type character_class = 
        | Weekday 
        | Weekend;; 
        type character_class = Weekday | Weekend

        (*types have ordering*)
        # Weekday < Weekend;;
        - : bool = true

        (*Pattern matching can be performed*)
        # let schedule = function 
        | Weekday-> "work" 
        | Weekend-> "Rest";; 
        val schedule : character_class-> string = <fun>
        ```

    1. Calculation area for different shapes
        ```
        # type shape = 
            | Circle of float
            | Rectangle of float * float
            | Square of float;;

        # let area = function 
            | Circle radius-> 3.14 *. radius *. radius 
            | Rectangle (width, height)-> width *. height 
            | Square side-> side *. side;;

        # let c = Circle 5.0;;
        # area c;;
        - : float = 78.5
        ```

    1. recursive variant: tree
        ```
        # type binary_tree = 
            | Leaf 
            | Node of int * binary_tree * binary_tree;;

        (*define a tree but defining its root node*)
        # let tree = Node (10, Node (5, Leaf, Leaf), Node (15, Leaf, Leaf));;

        # let rec sum tree = 
            match tree with 
            | Leaf-> 0 
            | Node (value, left, right)-> value + sum left + sum right;; 
            
        # sum tree;;
        - : int = 30
        ```

# 4. Type aliase
Note in variant also use keyword `type`
```
(*give name to float * float*)
# type latitude_longitude = float * float;;
type latitude_longitude = float * float

(*give name to function parameters*)
# let add ((x, y) as arg) = (fst arg) + (snd arg);;
val add : int * int -> int = <fun>
# add (1,2);;
- : int = 3
```

# 5. Exception
1. Syntax
    1. declaring
        `exception <Name> of <type>`
        1. defines a kind of exception like a global variable
        1. `<name>` must be capital
        1. `<type> is the type of variable of the exception information`
        ```
        exception Foo of string;;
        ```

    1. raising
        ```
        raise Foo "Oh no!"
        ```

    1. handle
        1. Syntax `try <action> with <exception_type> -> <expression for handling>`
        ```
        try i_will_fail () with Foo _ -> ();;
        - : unit = ()
        ```

1. built-in errors
    Tut3 P11