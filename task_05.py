#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" check your blood pressure!"""

QUESTION_BP = raw_input('what is your blood pressure')
QUESTION_BP =   int(QUESTION_BP)

USER_BP = None

if USER_BP <= 89:
    BP_STATUS = 'LOW'

elif 90 <= QUESTION_BP <= 119:
    BP_STATUS = 'IDEAL'

elif 120 <= QUESTION_BP <= 139:
    BP_STATUS = 'WARNING'

elif 140 <= QUESTION_BP <= 159:
    BP_STATUS = 'HIGH'

else:
    BP_STATUS = 'EMERGENCY'

FINAL_STATUS = 'your status is currently: {}'.format(BP_STATUS)
print FINAL_STATUS



    


