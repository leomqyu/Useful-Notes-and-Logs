# list
1. Intro
    1. list can contain any type of data, mixed type also OK.

1. declaration
    ```
    # # empty list. type is `a'`
    # let a = [];; 
    val a : 'a list = [] 

    # # use type annotations to explicitly specify
    # let b = ([] : int list);; 
    val b : int list = [] 

    # let c = [1; 2; 3];; 
    val c : int list = [1; 2; 3] 

    # # list of list
    # let d = [[1; 2]; [3]];; 
    val d : int list list = [[1; 2]; [3]]
    ```

1. Common built-in operation
    1. Access
        ```
        List.nth <list> <index>
        ```
    2. append
        Idea: concatenates 2 lists  
        Syntax: use `@` or `List.append`
        ```
        # let c = [1; 2; 3];;
        # c @ [1];;
        - : int list = [1; 2; 3; 1] 
        
        # List.append c [1];;
        - : int list = [1; 2; 3; 1]
        ```

    3. list constructor (add value at the head)
        Syntax: `some_value :: list`
        (Note to add is a value but not a list, unlike concatenate)
        ```
        # 1 :: c;;
        - : int list = [1; 1; 2; 3] 
        ```
    4. map
        1. List.map
            1. syntax: 
                `List.map <function> <list>`
            2. example:
            ```
            # List.map (fun x -> x * 2) [1;2;3];;
            - : int list = [2; 4; 6]
            ```
        2. List.map2
            1. syntax
                `List.map <function> <list1> <list2>`
                Note: if diff len, error

            2. example
            ```
            List.map2 (+) [1;2;3] [4;5;6];;
            ```
            

    1. assoc
        1. List.assoc
            returns the value associated with key a in the list of pairs l
            ```
            # List.assoc 2 [(1, "one"); (2, "two"); (3, "three")];;
            - : string = "two"
            ```
        1. List.mem_assoc
            return true if a binding exists, and false if no bindings exist for the given key
            ```
            # List.mem_assoc 2 [(1, "one"); (2, "two"); (3, "three")];;
            - : bool = true
            ```

    1. Sort
    Usnig `List.sort`. Pass a comparison function and a list.  
    ```
    # let list = [4;9;1;10];; 

    (*ascend*)
    # List.sort (fun a b-> a- b) [4;9;1;10];;
    # List.sort compare [4;9;1;10];;

    (*descend*)
    # let desc = List.sort (fun a b-> b- a) list ;;
    # List.sort (Fun.flip compare) [4;9;1;10];;

    (*others*)
    (*can also sort string*)
    # List.sort compare ["Bob"; "Amy"; "Charlie"];;
    - : string list = ["Amy"; "Bob"; "Charlie"]

    (*can sort tuple, by first element*)
    # List.sort compare [(1, 3), (2, 2), (3, 1)];;
    - : ((int * int) * (int * int) * (int * int)) list = [((1, 3), (2, 2), (3, 1))]
    ```

    1. Fold (accumulation)
        tut3 P7-8

1. Other self-written operation
    1. Access: see section 4 pattern matching

    1. Iterate over lists
        eg1: print all elements
        ```
        let rec print_nums nums = 
          match nums with 
          (* if empty do nothing else print*) 
          | []-> () 
          | n :: rest-> 
            Printf.printf "%d\n" n;  
            print_nums rest
        ```

        eg2: apply a function to all elements and ...
        1. Print out
            ```
            let rec print_all fn nums = 
                match nums with 
                | []-> () 
                | n :: rest-> 
                    fn n; 
                    print_all fn rest;;
            ```
        1. Store in a list (also can use built-in list module `map`)
            ```
            let rec map fn l = 
              match l with
              | [] -> []
              | h :: t -> fn h :: map fn t;;
            ```
        
    
    1. Find sum of list
        ```
        let rec total l = 
          match l with
          | [] -> 0
          | h::t -> h + total t;;
        ```

    1. Find len of list
        ```
        let rec length l = 
          match l with
          | [] -> 0
          | _::t -> 1 + length t;;
        ```


# Tuple
1. Intro
    Can have any num of value. Can have mixed data type.
    A tuple of 2 values aka pair

2. Declare
    ```
    # (3, 'K');;
    - : int * char = (3, 'K')
    ```
    Note: type is int `*` char. The `*` symbol stands for product type.

3. Access
    1. For 2 value tuple
    ```
    # fst (3, 'g');;
    - : int = 3 
    
    # snd (3, 'g');;
    - : char = 'g'
    ```

    1. Generally: see section 4 pattern matching

# Record
1. Intro
    Like a struct where in a record, each element has a name and a value. The name-value pair is called a `field`.

1. Declare
    Note: 
    1. also use the `type` keyword, but diff with variants is that it use `{}` but not `|`.
    1. In OCaml, records are data structures used to group named fields, and they are distinct from OCaml’s classes.
    ```
    # type character = { 
        name : string; 
        health : int; 
        level : int; 
      };;
    ```

1. access
    Use `.`
    ```
    # let aatrox = { 
        name = "Aatrox"; 
        health = 500; 
        level = 1; 
      };;
    val aatrox : character = {name = "Aatrox"; health = 500; level = 1}

    # aatrox.name;;
    - : string = "Aatrox" 
    # aatrox.level;;
    - : int = 1
    ```

1. copy with partial chage
    ```
    # let varus = { aatrox with name = "Varus"};;
    val varus : character = {name = "Varus"; health = 500; level = 1}
    ```

1. pattern matching
    Note that records behave like single constructor variants. That allows pattern matching on them.
    ```
    # match aatrox with { level; _ }-> level;;
    - : int = 1
    ```