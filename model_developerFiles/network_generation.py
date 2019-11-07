#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 03:30:01 2019

@author: yashpatil
"""

import random
import math
import numpy as np

class Settings:
    def __init__(self, number_of_tasks, number_of_techs, 
                 number_of_modes, number_of_time_periods):
        self.number_of_tasks = number_of_tasks
        self.number_of_techs = number_of_techs
        self.number_of_modes = number_of_modes
        self.number_of_time_periods = number_of_time_periods

class Task:
    def __init__(self, task_name, index, number_of_modes):
        self.task_name = task_name
        self.task_index = index
        self.number_of_modes = number_of_modes
        self.task_duration = [1 for _ in range(self.number_of_modes)]
        self.techs_requirement = [1 for _ in range(self.number_of_modes)]
        self.successor_list = []
        self.predecessor_list = []
        self.mode_indicator = [1 for _ in range(self.number_of_modes)]
        
    def populate_task(self):
        for i in range(self.number_of_modes):
            self.task_duration[i] = random.randint(1,6)
            self.techs_requirement[i] = random.randint(1,3)
            
        
        
        
class Tech:
    def __init__(self, tech_name, tech_index, tech_shift):
        self.tech_name = tech_name
        self.tech_index = tech_index
        self.tech_shift = tech_shift
        self.tech_regular_availability = []            
        self.tech_overtime_availability = []
        
    def populate_availability(self,number_of_time_periods):
        if self.tech_shift == 'Day':
            for t in range(number_of_time_periods):
                if math.ceil((t+1)/7)%2 == 1:
                    self.tech_regular_availability.append(t)
        elif self.tech_shift == 'Night':
            for t in range(number_of_time_periods):
                if math.ceil((t+1)/7)%2 == 0:
                    self.tech_regular_availability.append(t)
            
        
class Scenario:
    def __init__(self, settings):
        self.settings = settings
        self.task_list = []
        self.tech_list = []
        
    def populate_tasks(self):
        for i in range(self.settings.number_of_tasks):
            task = Task('Test', i, self.settings.number_of_modes)
            task.populate_task()
            self.task_list.append(task)
            
    def populate_techs(self):
        for k in range(self.settings.number_of_techs):
            tech = Tech('TestTech', k, 'Day')
            tech.populate_availability(self.settings.number_of_time_periods)
            self.tech_list.append(tech)
            
    def get_task_by_index(self,task_index):
        for task in self.task_list:
            if task.task_index == task_index:
                return task
            
    def create_network(self):
        A = np.zeros((self.settings.number_of_tasks-2,self.settings.number_of_tasks-2))
        
        for i in range(self.settings.number_of_tasks-3):
            for j in range(i+1,self.settings.number_of_tasks-2):
                A[i,j] = random.randint(0,1)
        
        for i in range(self.settings.number_of_tasks-3):
            dsum = sum(A[i,:])
            if dsum == 0:
                dsum = 1
            for j in range(i+1,self.settings.number_of_tasks-2):
                A[i,j] = A[i,j]/dsum
        Adj = A        
        S = A
        for rep in range(self.settings.number_of_tasks):
            S = S.dot(A)
            for i in range(self.settings.number_of_tasks-3):
                for j in range(i+1,self.settings.number_of_tasks-2):
                    if(A[i,j]>0 and S[i,j]>0):
                        Adj[i,j] = 0
                        
        final_adjacency = np.zeros((self.settings.number_of_tasks,self.settings.number_of_tasks))
        final_adjacency[1:self.settings.number_of_tasks-1,1:self.settings.number_of_tasks-1] = Adj
        for i in range(self.settings.number_of_tasks-2):
            if sum(Adj[i,:]) == 0:
                final_adjacency[i+1,self.settings.number_of_tasks-1] = 1
            if sum(Adj[:,i]) == 0:
                final_adjacency[0,i+1] = 1
                
        for i in range(self.settings.number_of_tasks):
            for j in range(self.settings.number_of_tasks):
                if final_adjacency[i,j] > 0:
                    final_adjacency[i,j] = 1
                
        for i in range(self.settings.number_of_tasks-1):
            for j in range(i+1,self.settings.number_of_tasks):
                if (final_adjacency[i,j] == 1):
                    self.get_task_by_index(i).successor_list.append(j)
                    self.get_task_by_index(j).predecessor_list.append(i)
        
                    
    def set_milestones(self):
        task = self.task_list[0]
        task.task_name = 'milestone_start'
        task.number_of_modes = 1
        task.task_duration = [1]
        task.techs_requirement = [0]
        task.mode_indicator = [1]
        
        task = self.task_list[-1]
        task.task_name = 'milestone_end'
        task.number_of_modes = 1
        task.task_duration = [1]
        task.techs_requirement = [0]
        task.mode_indicator = [1]
        
    def populate_scenario(self):
        self.populate_tasks()
        self.populate_techs()
        self.create_network()
        self.set_milestones()
                
   
settings = Settings(50,8,2,100)

scenario = Scenario(settings)
scenario.populate_scenario()









        
