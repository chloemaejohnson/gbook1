#!/usr/bin/env python
# coding: utf-8

import pandas as pd
gradebook = pd.DataFrame({"Name":["Chloe", "Kenny", "Libby", "Oliver", "Lit"], 
                   "Grade":[95.5, 90.5, 80.0, 30.0, 75.0]}) 
gradebook

print("The average grade is ", gradebook["Grade"].mean(), ".")
print("The highest score is ", gradebook["Grade"].max(), ".")
print("The lowest score is ", gradebook["Grade"].min(), ".")

