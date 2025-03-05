# Built-in math operation
1. Basically just like other lang: `+ - * /`

1. For float, add a `.` after symbols
    ```
    8.0 *. 8.0;;
    3.0 /. 2.0;;
    ```

# Built-in print function
1. print with endline
    ```
    print_endline "Hello, OCaml!";;
    ```
1. print format
    ```
    let n = 10;;
    Printf.printf "%d\n" n;;
    ```

1. print a special type
    ```
    (*print int*)
    let n = 10;;
    print_int i;;

    (*print string*)
    let str = "Hello, OCaml!";;
    print_string str;;
    ```
