# JCouplingparser


### Introduction

A class that's pruporse is to create tbl J coupling files from a csv with assigned
J coupling signals. The assigment is read from a csv file with a format shown
as below:
    Hydrogen,Jcouplingconstant
    NH1,4.23
    NH2,6.27
    NH3,2.52
To use the class you have to create its object instance with
two arguments `jcoup_fname` and `jcoupwrite_fname` as in
the example below.

### Example

```
from JCouplingparser import JCoupFileMaker

jcoup = JCoupFileMaker(jcoupcsv_fname='jcoup.csv',
                       jcoupwrite_fname='jcoup.tbl')
jcoup.read_jcoupcsv()
jcoup.save_jcoup_file()
```

### Usage
The script is used as it is, imported directly from the directory, where the repository was cloned into.
