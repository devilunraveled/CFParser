##CFParser


Aim : Making a web scarper script that parses codeforces and performs the following actions:
```   1. Load the test cases in a single file.
   2. Stores the expected output in another file.
   3. Both files should be edited if present, otherwise they should be created.
   4. The testcases all begin with the format -> `testCase_<num>`
   5. Following a newline character, after which the respective testcases are printed to the file.
   6. Creates a corresponding file with the name `codeforces_<problemNumber>`.
   7. The file has a default code template and is appended with the description at the top.
   8. The problem statement is also presented as comments after the description.
   9. The I/O is also given after the problems.
```
Interface : 
```   
    1. Commmand input format 1: 
    -> python ~/cpinit <`c`(for contest)> <contestNum> <`-all`(for all)/`a/b/..` : `problemCode`>  
    2. Commmand input format 2: 
    -> python ~/cpinit <`p`(for problem)> <problemCode -> Alphanumeric>  
```
