import csv
import re

class JCoupFileMaker:
    """A class that's pruporse is to create tbl J coupling files from assigned
       J coupling signal. The assigment is saved into a csv file with a format shown
       below:
           Hydrogen,Jcouplingconstant
           NH1,4.23
           NH2,6.27
           NH3,2.52
       To use the class you've to create its object instance with 
       two arguments `jcoup_fname` and `jcoupwrite_fname` as in 
       the example below:
       
       ```python
       from JCouplingparser import JCoupFileMaker

       jcoup = JCoupFileMaker(jcoupcsv_fname='jcoup.csv',
                              jcoupwrite_fname='jcoup.tbl')
       jcoup.read_jcoupcsv()
       jcoup.save_jcoup_file()
    ```
    Arguments:
        jcoup_fname: It is a filename for the csv file with assigned
                     J couplings.
        jcoupwrite_fname: It is a filename for J-coup tbl file written by the class.

    """

    def __init__(self, jcoupcsv_fname=None, jcoupwrite_fname=None):
        self.basestring = 'assign (resid   {0} and name hn )   (resid  {0} and name n ) '+\
                          '(resid   {1} and name ca)   (resid  {1} and name ha )  {2} 0.5'
        self.csv_regexp = '([A-Z]+)([0-9]+)\ *'
        self.regexp_comp = re.compile(self.csv_regexp)
        self.read_file_lines = []
        self.jcoupcsv_fname = jcoupcsv_fname
        self.jcoupwrite_fname = jcoupwrite_fname

    def read_jcoupcsv(self):
        """
        A method that, allows for reading specified CSV file with 
        J coupling constants. The structure of the file is specified
        in the class's docstring.
        """
        with open(self.jcoupcsv_fname, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                keys = list(row.keys())
                strength = row[keys[1]]
                matched = self.regexp_comp.match(row[keys[0]])
                # group(1) is aminoacid atom name, group(2) is resiude number
                # strength is j-coupling constant
                self.read_file_lines.append((matched.group(1), int(matched.group(2)), float(strength)))


    def save_jcoup_file(self):
        """
        A method that saves tbl file with given J coupling constants
        """
        with open(self.jcoupwrite_fname, 'w') as f:
            read_file_lines_len = len(self.read_file_lines)
            for i, line in enumerate(self.read_file_lines):
                atom, resid, strength = line
                if resid == 1:
                    continue
                to_write = self.basestring.format(resid-1, resid, strength)
                if i < read_file_lines_len:
                    to_write += '\n'
                f.write(to_write)

if __name__ == '__main__':
    jcoupmaker = JCoupFileMaker(jcoupcsv_fname='jcoup.csv', jcoupwrite_fname='jcoup.tbl')
    jcoupmaker.read_jcoupcsv()
    jcoupmaker.save_jcoup_file()
