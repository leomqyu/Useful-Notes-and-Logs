# Definitions
1. Definitions
    1. expression & statement

1. The output of a phrase in toplevel:
    `<"type"> <name> : <"data type"> = <value>`
    eg.
    ```
    # let x = 50 * 50;;
    val x : int = 2500

    # 50 * 50;;
    - : int = 2500
    ```

    1. Before `:` is the ("type" &) name of the "expression" (?)  
        If not anonymous (like 1st eg), shows type (in this case a value: `val`) and the name (in this case `x`).
        If it is anonymous expression (like 2nd eg), `-` will appear.
        
    1. After comma is `<"data type"> = <value>`


# Basics
1. 
    (In toplevel utop,) Each phrase ends with `;;`. This tells the toplevel to evaluate and print the result of the given phrase. So don't care about indent or new line.
    A single `;` is to separate statements within a phrase.

1.
    `()` is to enclose some expression to a single expression. 
    Note: 
    1. empty `()` means empty expression, return is of type `unit`.
        ```
        # ();;
        - : unit = ()
        ```
    1. `(...)` can also be replaced with `begin ... end`

1. `(* comments are enclosed like this and can have multiple lines *)`




# Values
## Intro
1. In OCaml, everything (expressions, functions, ...) has a value and every value has a type.

## Syntax
1. Global Values
    1. Property: can be used in more than 1 line
    1. Note:
        Bindings in OCaml are immutable, meaning that the value assigned to a name never changes. Although variable is often called a variable, it is in fact a constant.
    1. Expression: `let ... = ...`
        ```
        # let x = 50;; 
        val x : int = 50 
        
        # x * x;;
        - : int = 2500
        ```

1. Reference
    1. Idea: is the reference to a value, the value can be updated.
    1. Syntax
        1. Define
            `r` is the reference to a value 0
            ```
            # let r = ref 0;;
            val r : int ref = {contents = 0}
            ```

        1. Dereference
            Use `!`
            ```
            # !r;; (*using ! de-reference operator*)
            - : int = 0
            ```

        1. Update
            Use `:=`
            ```
            # r := 42;;
            - : unit = ()
            ```

1. Local Values
    1. Idea: can only use this variable in the "bounded expressions" of that "phrase".
    1. Syntax
    `let ... = ... in ...`. This is a whole "expression", will finally result in a value.
    ```
    # let d = 6 in d * 7;;
    - : int = 42
    ```

    1. Advanced use
        1. How to read: 
            Then `let` combines with the nearest `in`, and all the things after `in` (considered as a whole expression) is the expression it evaluates. Don't need to care too much, won't cause misunderstanding.
            If indented correctly, then read forwards, each time evaluate the var after `let` to a value, and plug it in the rest.  
        2. How to ident: 
            To keep it simple, just ach time has a `let x = 1 in`, the following expressions should be in new line.  
            Then the place that the variable is valid is inside the indent.  
            ```
            let x = 2 * 3 in
                let y = 2 * x in
                    x + y
            ```

            ~~(Or can follow the other principal that 1. "farthest combine 2. each time has a `let x = 1 in`, the following expressions should be in new line )
            Principal: the expression the `let` evaluates to has the same indent with the `let`.  
            For chained def, 2 `let` no indent.
            For nested, second let has an indent~~
        3. eg:
            1. Multiple local def
                1. chained local def  
                    How to ident: just no indent in the 2 `let`
                    ```
                    # let d = 2 * 3 in 
                      let e = d * 7 in 
                      d * e;;
                    - : int = 252
                    ```
                2. Nested
                    The combination of let in is not combined to the closest, but combined to the farthest.
                    ```
                    # let d = 
                        let e = 2 * 3 in 
                        e * 5 in 
                    d * 7;;
                    - : int = 210
                    ```


# Functions

## Def & intro through eg
```
# let square x = x * x;;
val square : int-> int = <fun> 

# square 50;;
- : int = 2500
```

1. Def of function with `let <name> <params> = <expression>`
1. parameter: `x`; 
    function body: `x * x`: the expression as the "return", the final value this function evaluates to (there's no return in )
1. The output of the def expression shows that:
    1. function is also a value
    1. type of this function: `int-> int`: meaning that take a int as argument (input) and return an int as result (output)
    1. A function value can’t be displayed, which is why `<fun>` is printed instead

## Declaration and call
1. basics
    As in Def & Intro.
1. Notes
    1. Explicitly state parameter type
        use `:`
        ```
        # let f (a:float) (b:int) = a +. float_of_int b;;
        val f : float -> int -> float = <fun>

        # f 1.0 2;;
        - : float = 3.
        (*If input wrong data type, will result in error*)
        ```

    1. Indent
        If short write in a line;
        If long just like python, param at a line, all other lines ident:
        ```
        let square x = 
            x * x;;
        ```



## Anonymous fn
1. Def 
`fun <params> -> <expression>`
```
# fun x y -> x * y;;
- : int -> int -> int = <fun>
```

2. Usage
```
# # direct calculate
# (fun x y -> x * y) 10 20;;
- : int = 200

# # pass as arguments to other functions
# List.map (fun x-> x * x) [1; 2; 3; 4];;- : int list = [1; 4; 9; 16]
```

## Recursive functions
fn that call itself in its own body.  
Declare using `let rec ... = ...`
```
# let rec fibo n = 
    if n <= 1 then n else fibo (n- 1) + fibo (n- 2);; 
val fibo : int-> int = <fun> 

# fibo 5;;
- : int = 5
```