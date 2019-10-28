#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 03:59:26 2019

@author: yashpatil
"""

from gurobipy import Model,GRB

class optimization_model:
    def __init__(self):
        self.model = Model('network_optimization')
        
    
    def create_start_time_variables(self):
        self.S = self.model.addVars(50, 
                               vtype = GRB.INTEGER, 
                               lb = 0, 
                               ub = 100, 
                               name = 'S')
        
    def create_end_time_variables(self):
        self.C = self.model.addVars(50, 
                               vtype = GRB.INTEGER, 
                               lb = 0, 
                               ub = 100, 
                               name = 'C')
        
    def create_work_time_variables(self):
        self.X = self.model.addVars(50,2,100, 
                               vtype = GRB.BINARY, 
                               name = 'X')
        

        
    
        
    
    


