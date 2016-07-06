# python-exit-point
Python exit handler (ctrl-c) that allows you to set specific "exit points," removing uncertainty when exiting loops.

Also provides options for custom cleanup functions, exit messages, and debug information.

An "exit point" is a location in your code (typically in a loop) where you feel comfortable terminating your program. Previously, if you pressed "ctrl-c" while a program was executing a loop, there was no way to know where in the loop the program would terminate. Using "exit points," you can set specific points in the loop where a program will terminate.

This is useful in control scenarios where you have loops controlling physical processes that *must* fully execute before termination. 

## Importing exitPoint

```python
from exitPoint import exitPoint
```

## Using exitPoint

The "exitPoint" function doesn't *require* any arguments and can be used by simply placing the following:

```python
exitPoint()
```

wherever you would like an "exit point" to exist.

For example:

```python
while(True) :
	exitPoint()
	print("Check out this infinite loop!")
```


The "exitPoint" function has three *optional* arguments:
- **Debug** (if set to True, the name of the program that is exiting is printed before exiting)
- **FunctionToExecute** (defines function to execute before exiting)
- **Message** (defines message to print before exiting)

Example (Debug on, testFunction will execute before exiting, "Goodbye message!" will print before exiting):

```python
exitPoint(True, testFunction, "Goodbye message!")
```
