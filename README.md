## This code is to approximate solutions to IVPs for ODEs
To run the Euler method, enter the following code on your command line

```
python ode.py -time_scheme euler 
```
To run the RK-2 method, use:
```
python ode.py -time_scheme rk2 
```

To run the RK-4 method, use:
```
python ode.py -time_scheme rk4 
```

When you run any of the above commands, the solution gets saved in a file called sol.txt. 

You could specify the number of cells(nc), the start time(tmin), end time(tmax) and the initial datum(yinit) at t=tmin as follows:
```  
python ode.py -nc 8 -tmin 0.0 -tmax 1.6 -time_scheme rk4 -yinit 2.0 -compute_error yes
```
To compare the solutions generated by Euler, RK-2, RK-4 methods, you can copy these after running each method into files of the form: euler.txt, rk2.txt, rk4.txt etc. For example:

```  
python ode.py -nc 8 -tmin 0.0 -tmax 1.6 -time_scheme rk2 -yinit 2.0 -compute_error yes
```
and then subsequently:
```
cp sol.txt rk2.txt
```
Once you have saved the solution files corresponding to all the methods you want to compare, run the plot.py file:
```  
python plot.py
```

To test the order of accuracy, run the script file, which will generate an error.txt file.
```
sh runconvergence "20 40 80 160 320 640"
```

  