#Introduction

This is the introduction for the working of the example mimicing the logic of the interested project, "Development of an interactive flow visualization tool for visual / blockly programming, for educational use".

The expected result from this programme is to obtain a JSON structure for the targeted file (here, 'main.py') which will be dumped in the empty JSON file "data.json".
***
##Flow of the code
The lines of the targeted file is read by ```.readLines()```(an in-built function of Python). Intializing an empty dictionary, (here, "dict_to_export") a ```for loop``` is executed to read the lines of the targeted input file/code one-by-one.

The nested ```if-else``` conditions look for the assignment operator (i.e. '='). 
#### If true :
> A nested ```if-else``` is executed, looking for logical operators('+','/','-','*') and insert the corresponding variables and sub-variables from the made-list ```.split(+)``` in the empty dictionary.

For example :
```c = a+b```

Here ```c``` is the variable in which added values of ```a``` and ```b``` are getting assigned, making ```a``` and ```b``` sub-variables.


#### If false :
>A linear dictionary is appended in  the initial empty dictionary with key-pair values of variables and their assigned values.




The last ```if-else``` condition looks for the keyword ```"print"``` , inserting a key-pair value in the ```dict_to_export``` dictionary; the key being the variable whose value is to be printed and the value of the key is the expression assigned to the variable.

After the execution of the ```for loop``` is terminated, with the help of the in-built library ```json``` of Python, the now acquired dictionary, ```dict_to_export``` is coverted to json string/s and dumped in the empty JSON file, "data.json", 
***
###### Overall goals of the project
Here is an overall view of the project, according to my understanding.


*First Step

[<img src="https://github.com/deathzombie/Example/blob/main/initial%20.png" width = 30% height = 60%>]

*Second Step

[<img src="https://github.com/deathzombie/Example/blob/main/final.png" width = 30% height = 60%>]



