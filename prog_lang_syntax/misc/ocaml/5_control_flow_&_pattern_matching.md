# Control flow
## 1. If then else
1. Note
    1. In OCaml, `if ... then ... else ...` is an expression but not a statement, so it will always evaluate to a value

    1. Both `then` and `else` branches must return the same type, or the program will not compile.

    1. The `else` branch is required, except when the return type is explicitly unit.
        ```
        # let x = 10 in if x > 5 then print_endline "greater";;
        greater
        - : unit = ()
        ```

1. Use eg

    1. simple, work as expression: then just single line 

    1. Complex, work as "branching"
        ```
        if times < 1 then begin
            thing_to_do (); 
            repeat (times- 1) thing_to_do 
        end
        else begin 
            thing_to_do (); 
            repeat (times- 1) thing_to_do 
        end ;; 
        ```
        
## 2. Loop
1. while loop
    ```
    # let i = ref 0 in 
      while !i < 5 do 
        print_int !i; 
        i := !i + 1 
      done;; 
      01234- : unit = ()
    ```

1. for loop 
    ```
    # for i = 0 to 4 do 
        print_int i 
      done;; 
    01234- : unit = () 
    
    # for i = 4 downto 0 do 
      print_int i 
    done;; 
    43210- : unit = ()
    ```


# Pattern matching
1. Intro: Pattern-matching allows you to destructure and analyze data structures in a structured and readable way. It is often used for handling complex data types like tuples, lists, and custom types.

1. Basic syntax
    1. syntax:
        ```
        match expression with 
        | pattern1-> result1 
        | pattern2-> result2 
        | ...;;
        ```
    1. note
        1. Indent: 
            For `match` and `|` no indent. If `|` line too long, need to indent
        1. semicolon: only a double semicolon at the end of whole match expression.
        1. The `_` pattern matches any value not explicitly handled by previous patterns.
        1. If multiple pattern matches, will result in first pattern.
    1. eg:
        1. basic match
            ```
            # let x = 3 in 
              match x with 
              | 1-> "one" 
              | 2-> "two" 
              | 3-> "three" 
              | _-> "other";;
            - : string = "three"
            ```

        1. match list (access list's i^th element)
            `x::u` will be matched to: `x` is the first element, `u` will be the rest of the list.
            ```
            # match [1; 2; 3] with
            | x :: u-> x 
            | []-> raise Exit;;
            - : int = 1 
            
            # match [1; 2; 3] with 
            | x :: y :: u-> y 
            | x :: u-> x 
            | []-> raise Exit;;
            - : int = 2
            ```
        
        1. match tuple 
            eg 1
            ```
            # let pair = (1, 2) in
            match pair with 
            | (0, 0)-> "both zero" 
            | (1, _)-> "first is 1" 
            | (_, 2)-> "second is 2" 
            | _-> "other";;
            - : string = "first is 1"
            ```

            eg2 (access tupple's i^th element):  
            explain: extract the 3rd element of the product of 4 types.
            'a is the type of the first element. Others are similar.
            ```
            # let f x = match x with (h, i, j, k)-> j;; 
            val f : 'a * 'b * 'c * 'd-> 'c = <fun>
            ```

1. Anonymous function for pattern matching
    1. Syntax: use `function` keyword. Equivalent to `match ... with ...`
        ```
        function 
        | pattern1-> expression1 
        | pattern2-> expression2 
        | ...
        ```
    
    1. eg
        ```
        # (function 
        | 0-> "zero" 
        | 1-> "one" 
        | _-> "other") 1 ;;
        - : string = "one"

        # (function 
        | []-> "empty" 
        | h :: _-> "non-empty") [1; 2; 3] ;;
        - : string = "non-empty"
        ```
    
    1. note: this is actually just a kind of way to write funciton:
        ```
        function | x -> x * x
        ```
        is same with
        ```
        fun x -> x * x
        ```