# data

1. Other input syntax
    ```
    * 1;
    INPUT #2 AGE SEX $ GRADE #1 NAME $ &;
    /* #n ask SAS o go to n-th data line of the CURRENT record*/
    ```

2. Output in DATA
    ```
    * put: output to log;
    DATA;
        X=TODAY(); Y=YEAR(X); M=MONTH(X); D=DAY(X);
        PUT Y= M= D=;
    RUN;
    /*PUT _ALL_: all var, including _N_ and _ERROR_*/
    ```


# proc
1. print
    ```
    PROC PRINT data=fitness;
	    title 'Fitness data';
    RUN;

    PROC PRINT DATA=AA(OBS=10 WHERE=(REGION=1));
    RUN;
    ```

1. sort
    ```
    PROC SORT;
        BY name;
    RUN;
    ```

1. stats calculation
   1. mean
    ```
    PROC MEANS maxdec=1 data=fitness;
    RUN;
    ```
    `maxdec=1`: in output, only up to 1 decimal place

1. plot
    ```
    SYMBOL1 COLOR=RED VALUE=NONE INTERPOL=JOIN;
    * Defines the characteristics of symbols that display the data plotted;
    * INTERPOL=JOIN connects data points with straight lines;
    * VALUE=NONE suppresses the ploting symbol;
    PROC GPLOT DATA=EXPONENTIAL; 
            PLOT Y*X; 
    RUN;
    ```
