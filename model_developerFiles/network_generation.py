#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 03:30:01 2019

@author: yashpatil
"""

import random
import math

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
        for task in self.task_list[:-1]:
            successor_options = [activity.task_index for activity in self.task_list[task.task_index+1:]]
            successors_to_be_picked = random.randint(1,len(successor_options))
            task.successor_list = random.sample(successor_options, k = successors_to_be_picked)

        for task in self.task_list:
            for successor_index in task.successor_list:
                if task.task_index not in self.get_task_by_index(successor_index).predecessor_list:
                    self.get_task_by_index(successor_index).predecessor_list.append(task.task_index)
                    
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
                
   










        
