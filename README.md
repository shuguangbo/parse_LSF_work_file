Parse LSF work file
===
  
LSF stores job information in work files:  
lsb.events - restore job information in LSF by replaying this file  
lsb.acct   - database for statistic and analysing on CLI  
  
All work files store job info into fields separated by white space ' ', string type field is enclosed by ", " is escaped by double "" in the field.   
  
This tool can split work file fields correctly, and put fields into a list, then you can follow LSF work file format to handle them.
