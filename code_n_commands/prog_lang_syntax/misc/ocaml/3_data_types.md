# Different types
1. int
    By default a num without decimal point is an int
    ```
    # 1;;
    - : int = 1
    ```

1. float
    ```
    1.5;;
    - : float = 1.5

     8.;;
    - : float = 8.
    ```

1. string: string is also a value with type string
    ```
    # "hello";;
    - : string = "hello"
    ```

1. boolean
    ```
    # 1 > 2;;
    - : bool = false
    ```

1. unit: the type of functions like `print_endline` is unit (and the value is `()`)
    ```
    # let x = 10 in if x > 5 then print_endline "greater";; 
    greater
    - : unit = ()
    ```
1. special "compund type": like for function, for list
    ```
    (*list of integers*)
    # let a = [1;2;3];;
    val a : int list = [1; 2; 3]   

    (*a typle of int and float*)
    # let x = (1, 2.0);;
    val x : int * float = (1, 2.)

    (*function*)
    (**a func that inputs an int and outputs an int **)
    # let fn x = x * x;;
    val fn : int -> int = <fun> 

    (**
    Complicated: is right assoc:
    "int -> float -> int" is "int -> (float -> int)", means takes an int and returns a function of "float -> int"
    or can be simply interpreted as only the last is the return type, all previous are the input type by order
    **)
    # let f (a:int) (b:float) = 3;;
    val f : int -> float -> int = <fun>
    ```

# Type convert
```
(*convert int to float*)
# float_of_int 8;;
- : float = 8.
```

# Type specific operation
1. float
    1. float module: Tut3 P12

1. String concatenate
    With `^`:
    ```
    # let say_hi name = print_string ("Hello, " ^ name ^ "!\n") ;;
    val say_hi : string -> unit = <fun>
    ```
