## This code is to approximate solutions to IVPs for ODEs
To run Euler method, enter the following code on your command line

```
python3 ode.py -time_scheme euler 
```
To run the RK-2 method, use:
```
python3 ode.py -time_scheme rk2 
```

To run the RK-4 method, use:
```
python3 ode.py -time_scheme rk4 
```

You could specify the number of cells(nc), the start time(tmin), end time(tmax) and the initial datum given at tmin as follows:
```  
python3 ode.py -nc 8 -tmin 0.0 -tmax 1.6 -time_scheme rk4 -uinit 2.0 -compute_error yes
```

## To test the order of accuracy, run the script file
```
sh runconvergence "20 40 80 160 320 640"
```

