#!/usr/bin/env python3
# lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Always start fresh
Department.drop_table()
Department.create_table()

# Create some rows
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# Update HR
hr.name = "HR"
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

# Delete Payroll
print("Delete Payroll")
payroll.delete()
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor> (still exists in memory!)

# Drop into ipdb REPL for exploration
ipdb.set_trace()
