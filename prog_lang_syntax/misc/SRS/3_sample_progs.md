# 1. data reading 

1. Basic reading in in-file data and mock running
    ```
    * LIBNAME ABC 'D:\';
    DATA fitness;       /* to declare that now working on which dataset; or `WORK.FITNESS` */
        LENGTH name $ 14;
        INPUT name $ weight waist pulse jumps;
        CARDS;
        Hodges    191  36  50   60
        Kerr      189  37  52   60
    RUN;

    PROC PRINT data=fitness;
        title 'Fitness data';
    RUN;
    ```

1. Input source eg
    1. In-stream: refer to 1.1
    1. External file
        ```
        DATA toads;
        INFILE "&filepath/ToadJump.dat";
        INPUT ToadName $ Weight Jump1 Jump2 Jump3;
        RUN;
        ```

2. Input format eg
    1. list input
        ```
        LIBNAME STUDENT "C:\";
        DATA STUDENT.SCORES;
        LENGTH NAME $ 14;
        INPUT NAME $ & AGE SEX $ GRADE @@;
        CARDS;
        CHAN CHI SHING  15 M 70.5 CHEUNG TIN  16 M 67.2
        LEUNG MAN SHAN  18 F 72.0 MA YUEN LAN  . F 80.1 
        WU KEUNG  17 M 75.3
        RUN;
        ```
    2. column input
        ```
        LIBNAME STUDENT "&filepath";
        DATA STUDENT.SCORES;
        INPUT NAME $ 1-15 AGE 17-18 SEX $ 20 GRADE 22-25;
        CARDS;
        CHAN CHI SHING  15 M 70.5
        CHEUNG TIN      16 M 67.2
        RUN;
        ```

    3. informat input
        ```
        DATA SCORES;
        INPUT @17 AGE 2. @1 NAME $15. @19 SEX $1. +1 GRADE 4.1;
        CARDS;
        CHAN CHI SHING  15M 70.5
        CHEUNG TIN     *16M 67.2
        LEUNG MAN SHAN  18F 72.0
        MA YUEN LAN      .F 80.1
        RUN;
        ```