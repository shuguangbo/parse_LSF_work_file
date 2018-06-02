#!/usr/bin/env python
#  -*- coding: utf-8 -*-

JOB='"JOB_FINISH" "10.1" 1527327585 7610 1000 33554438 1 1527326745 0 0 1527326746 "lsfadmin" "normal" "" "" "" "lsf-master.localdomain.com" "" "" "" "" "10/1527326745.7610" 1 "pac" 1 "lsf-pac.localdomain.com" 32 60.0 "" "sleep 1000" -1.000000 -1.000000 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 "" "default" 65280 1 "" "" 0 2048 0 "" "" "" "" 0 "" 0 "" -1 "/lsfadmin" "" "" "" -1 "" "" 5136 "" 1527326746 "" "" 2 1032 "0" 1033 "0" 0 0 0 2048 "select[type == any] order[r15s:pg] " "" -1 "" -1 0 "" 0 0 "" 839 "" 0 "" 0.000000 0.00 0.00 0.00 0.00 1 "lsf-pac.localdomain.com" -1 0 0 0'

def parse_lsf(JOB) :
    fields=[]
    s_start=0;
    n_start=-1;
    pre_char=''
    for i in range(len(JOB)) :
      if pre_char == ' ' :
        if s_start == -1 and n_start == -1 :
          if JOB[i] == '"' :
            s_start = i
          else :
            n_start = i 
    
      if JOB[i] == ' ' :
         if s_start != -1 and JOB[i-1] == '"' and (JOB[i-2] != '"' or ( JOB[i-3] == ' ')) :
           fields.append('' if JOB[s_start:i] == '""' else JOB[s_start+1:i-1])
           s_start = -1
         if n_start != -1 :
           fields.append(JOB[n_start:i])
           n_start = -1

      if i == len(JOB) - 1 :
        if s_start != -1 :
          fields.append('' if JOB[s_start:] == '""' else JOB[s_start+1:i])
        else:
          fields.append(JOB[n_start:])
    
      pre_char = JOB[i]

    return fields

f = parse_lsf(JOB)
print f
