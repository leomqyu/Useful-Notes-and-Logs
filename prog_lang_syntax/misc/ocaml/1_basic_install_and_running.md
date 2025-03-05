# Install

1. Install and init
```
# install
sudo apt-get install opam
# init
opam init -y
```

2. each time start
```
eval $(opam env)
eval $(opam env --switch=default)       # go to default switch
```
alternatively, can write to ~/.profile to init every time

# Switch
0. Intro: to create isolated environment (including Ocaml compiler, libraries, binaries)

1. basic op
```
# 1. list switches
opam switch list

# 2. create, activate, confirm a new switch
opam switch create my_switch <compiler-version>
opam switch my_switch
opam switch
```

# Compile and Run
1. by byte file  
compiles OCaml source files to bytecode object files and links these object files to produce bytecode executable files
```
# compile: 
ocamlc -o hello.byte hello.ml

# run
./hello.byte    # run the file directly
ocamlrun hello.byte
```

2. by native code object file  
ocamlopt compiles OCaml source files to native code object files and links these object files to produce executables.
```
ocamlopt-o hello.native hello.ml
./hello.native
```

3. differences: see tut


# Utop
0. intro  
is a improved toplevel (顶层窗口) (i.e. read-eval-print loop) for OCamle

1. install
```
opam install utop
```

2. use
like command line python 
```
utop
```

3. exit
ctrl+D or type `quit`

# Debug
Tut3 P14-15