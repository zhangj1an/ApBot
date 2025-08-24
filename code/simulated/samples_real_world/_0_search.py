import heapq
import sys 
import numbers
# also need  to write hard-coded policies for input strings.
# if the input string is non zero, then parse the string to map to corresponding buttons 
import copy 

class AStarSearch:
    def __init__(self, start_state, goal_state, actions, important_variable_name_list, feature_name, verbose=False):
        # only care about whether the target variable matches with the goal state
        self.start_state = start_state
        self.goal_state = goal_state
        self.actions = actions
        self.weight_of_heuristic = 1
        self.important_variable_name_list = important_variable_name_list
        self.verbose = verbose
        self.feature_name = feature_name
        self.start_state.feature.current_value = (feature_name, 1)
        

    
    def is_goal(self, state):
        goal_copy = self.goal_state.copy()
        state_copy = state.copy()
        goal_copy.feature.current_value = None 
        state_copy.feature.current_value = None


        #print(f"important variable name list: {self.important_variable_name_list}")

        for variable_name in self.important_variable_name_list:
            state_variable = state_copy.get_variable_by_name(variable_name)
            goal_variable = goal_copy.get_variable_by_name(variable_name)
            if state_variable is None or goal_variable is None:
                print(f"cannot get variable by name: {variable_name}")
                return False
            value_match = str(state_variable.get_current_value()) == str(goal_variable.get_current_value())
            if isinstance(state_variable.get_current_value(), numbers.Number):
                value_match = state_variable.get_current_value() == goal_variable.get_current_value()
            if not value_match:
                #print(f"Variable name: {variable_name} State variable: {state_variable.get_current_value()} Goal variable: {goal_variable.get_current_value()}")
                return False
        #print(f"goal reached check... list of important variables: {self.important_variable_name_list} ")
        return True
        
    
    def apply_action(self, state, action):
        new_state = copy.deepcopy(state)
        # if actions is number actions, then add a digit to it
        print(f"applying action: {action}, {self.feature_name}")
        new_state.run_action(action, feature_name =self.feature_name)
        return new_state
    
    def search(self):
        open_list = []
        closed_list = set()
        
        heuristics = self.weight_of_heuristic * self.start_state.heuristics(self.goal_state)
        start_node = (heuristics, 0, self.start_state, [])
        heapq.heappush(open_list, start_node)
        
        if self.verbose:
            print(f"Goal state: \n{self.goal_state}\n\n")
            print(f"Starting A* search from \n{self.start_state}\n with heuristic {heuristics}\n\n")
        
        max_iteration = 1000
        current_iteration = 0 
        while open_list and current_iteration < max_iteration:
            
            _, cost, current_state, path = heapq.heappop(open_list)
            

            if self.verbose:
                print(f"Expanding state \n{current_state}\n {current_state.get_current_value()}\n with cost {cost} and heuristic {self.weight_of_heuristic * current_state.heuristics(self.goal_state)}\n\n")
            
            if self.is_goal(current_state):
                if self.verbose:
                    print(f"Goal reached! State: \n{current_state}\n with path: \n{path}")
                return path
            
            closed_list.add(current_state)
            if (hasattr(self.goal_state, "meta_actions_dict")) and all(item in self.goal_state.meta_actions_dict.values() for item in self.actions): 
                # need to refer to the goal variable 
                # and access the dict to get the sequence of actions
                #action_list = getattr(self.goal_state, self.actions[0])
                variable_name = self.important_variable_name_list[0]
                goal_variable_value = getattr(self.goal_state, variable_name).get_current_value()
                goal_string = self.start_state.get_original_input(goal_variable_value, self.feature_name, variable_name)
                output_actions_list = []

                print(f"goal string: {goal_string}, goal variable value: {goal_variable_value}, variable_name: {variable_name}, feature name: {self.feature_name}")
                meta_actions_dict = getattr(self.goal_state, "meta_actions_dict")
                for alphabet in goal_string: 
                    corresponding_action = meta_actions_dict[alphabet]
                    output_actions_list.append(corresponding_action)
                print(f"output actions list: {output_actions_list}")
                return output_actions_list

                # the variable should have type inputstring? not really. just look for a variable that has
                pass
            else:
                for action in self.actions:
                    # if actions is in the meta_actions. 
                    # if feature list shows an action containing the word: meta action
                    # look for that variable and get all the actions in the list. 
                    # need to look for the variable of interest (should be of type input string) as shown in the feature list.
                    # then use the dict to parse the string into a list of actions can. 
                    
                    

                    new_state = self.apply_action(current_state, action)
                    new_state_feature = new_state.get_current_value()
                    new_cost = 1
                    
                    if new_state in closed_list:
                        if self.verbose:
                            print(f"After applying action {action}, the new state \n{new_state}\n {new_state_feature}\n is already in closed list. \n\n")
                        continue
                    
                    if str(new_state) in [str(state) for _, _, state, _ in open_list]:
                        if self.verbose:
                            print(f"After applying action {action}, the new state \n{new_state}\n {new_state_feature}\n is already in open list. \n\n")
                            #items = "\n\n".join([str(f) for _, _, f, _ in open_list])
                            #print(f"open list: {items}")
                        continue
                    
                    estimated_cost = new_cost + self.weight_of_heuristic * new_state.heuristics(self.goal_state)
                    heapq.heappush(open_list, (estimated_cost, new_cost, new_state, path + [action]))
                    if self.verbose:
                        print(f"After applying action {action}, adding new state \n{new_state}\n with estimated cost {estimated_cost} to open list. \n\n")
                current_iteration += 1
        #if self.verbose:
        print(f"No solution found. Goal:\n {self.goal_state}\n. Current: {self.start_state}")
        #exit()
        return None  # no solution found

class VariableSearch:
    def __init__(self, start_variable, goal_variable, action_effects, verbose=False):
        self.start_variable = start_variable
        self.goal_variable = goal_variable
        self.action_effects = action_effects
        self.verbose = verbose
        self.input_string = ""
        self.weight_of_heuristic = 1

        # types of effects: next, prev according to step value, or add a digit (in this particular input string for this variable only) so during search, bring a input string along with it 

    def is_goal(self, variable):
        value_match = str(variable.get_current_value()) == str(self.goal_variable.get_current_value())
        if isinstance(variable.get_current_value(), numbers.Number):
            value_match = variable.get_current_value() == self.goal_variable.get_current_value()
        return value_match
    
    def apply_action(self, variable_original, action_tuple):
        variable = copy.deepcopy(variable_original)
        action_name = action_tuple[0]
        action_effect = action_tuple[1]
        # types of action effect: next, prev, add a digit. add digit should not be used for planning. 
        if action_effect == "next":
            variable.next()
        elif action_effect == "prev":
            variable.prev()
        return variable 
    
    # decide whether to use search: if the proposed action tuples does not contain adding digits, then use search.
    def search(self):
        open_list = []
        closed_list = set()
        heuristics = self.weight_of_heuristic * self.start_variable.compare(self.goal_variable)
        start_node = (heuristics, 0, self.start_variable, [])
        heapq.heappush(open_list, start_node)
        if self.verbose:
            print(f"Goal variable: {self.goal_variable.get_current_value()}\n\n")
            print(f"Starting A* search from {self.start_variable.get_current_value()} with heuristic {heuristics}\n\n")
        max_iteration = 1000
        current_iteration = 0
        while open_list and current_iteration < max_iteration:
            _, cost, current_var, path = heapq.heappop(open_list)

            if self.verbose:
                print(f"Expanding variable {current_var.get_current_value()} with cost {cost} and heuristic {self.weight_of_heuristic * current_var.compare(self.goal_variable)}\n\n")
            if self.is_goal(current_var):
                if self.verbose:
                    print(f"Goal reached! Variable: {current_var.get_current_value()} with path: {path}")
                actions = [action for action, _ in path]
                return actions
            
            closed_list.add(current_var)
            # here ignore actions that require effects of adding digits.
            for action_tuple in self.action_effects:
                new_var = self.apply_action(current_var, action_tuple)
                new_cost = 1
                if new_var in closed_list:
                    if self.verbose:
                        print(f"After applying action {action_tuple}, the new variable {new_var.get_current_value()} is already in closed list.\n\n")
                    continue 

                if str(new_var.get_current_value()) in [str(var.get_current_value()) for _, _, var, _ in open_list]:
                    if self.verbose:
                        print(f"After applying action {action_tuple}, the new variable {new_var.get_current_value()} is already in open list.\n\n")
                    continue

                estimated_cost = new_cost + self.weight_of_heuristic * new_var.compare(self.goal_variable)
                heapq.heappush(open_list, (estimated_cost, new_cost, new_var, path + [action_tuple]))
                if self.verbose:
                    print(f"After applying action {action_tuple}, adding new variable {new_var.get_current_value()} with estimated cost {estimated_cost} to open list.\n\n")
            current_iteration += 1
        print(f"No solution found. Goal: {self.goal_variable.get_current_value()}. Current: {self.start_variable.get_current_value()}")
        return None





        
    