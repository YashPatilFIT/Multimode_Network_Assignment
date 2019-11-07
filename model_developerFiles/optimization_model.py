#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 03:59:26 2019

@author: yashpatil
"""

from gurobipy import Model,GRB
#from network_generation import Scenario

class optimization_model:
    def __init__(self, scenario):
        self.scenario = scenario
        self.model = Model('network_optimization')

    def create_start_time_variables(self):
        self.S = self.model.addVars(self.scenario.settings.number_of_tasks, 
                               vtype = GRB.INTEGER, 
                               lb = 0, 
                               ub = self.scenario.settings.number_of_time_periods, 
                               name = 'S')
        
    def create_end_time_variables(self):
        self.C = self.model.addVars(self.scenario.settings.number_of_tasks, 
                               vtype = GRB.INTEGER, 
                               lb = 0, 
                               ub = self.scenario.settings.number_of_time_periods, 
                               name = 'C')
        
    def create_work_time_variables(self):
        self.X = self.model.addVars(self.scenario.settings.number_of_tasks,self.scenario.settings.number_of_modes,self.scenario.settings.number_of_time_periods, 
                               vtype = GRB.BINARY, 
                               name = 'X')
        
    def create_tech_assignment_variables(self):
        self.V = self.model.addVars(self.scenario.settings.number_of_techs,self.scenario.settings.number_of_tasks,self.scenario.settings.number_of_time_periods, 
                               vtype = GRB.BINARY, 
                               name = 'V')
        
    def create_model_variables(self):
        self.create_start_time_variables()
        self.create_end_time_variables()
        self.create_work_time_variables()
        self.create_tech_assignment_variables()
        
        

        
    
        
    
    


