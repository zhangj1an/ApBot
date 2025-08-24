import copy
import inspect

class Appliance():

    def __init__(self):
        self.reset()
    
    def update_display(self, variable=None):
        feedback = {"feature": self.feature.current_value}
        
        
        if variable is not None:
            variable_name = self.find_attribute_name(variable).replace("variable_", "")
            feedback[variable_name] = variable.get_current_value()
        else:
            appliance_state_with_feature = self.get_state()

            current_feature_name, current_feature_step = self.feature.current_value
            current_feature_detail = self.feature.get_feature_step_detail(current_feature_name, current_feature_step)
            if "variable" in current_feature_detail:
                variable_name = current_feature_detail["variable"]
                feedback[variable_name] = appliance_state_with_feature[variable_name]
            if self.feature.get_feature_step_detail(current_feature_name, current_feature_step - 1) is not None and "variable" in self.feature.get_feature_step_detail(current_feature_name, current_feature_step - 1): 
                variable_name = self.feature.get_feature_step_detail(current_feature_name, current_feature_step - 1)["variable"]
                feedback[variable_name] = appliance_state_with_feature[variable_name]
            if self.feature.get_feature_step_detail(current_feature_name, current_feature_step + 1) is not None and "variable" in self.feature.get_feature_step_detail(current_feature_name, current_feature_step + 1):
                variable_name = self.feature.get_feature_step_detail(current_feature_name, current_feature_step + 1)["variable"]
                feedback[variable_name] = appliance_state_with_feature[variable_name]
        if len(feedback) == 1:
            for special_var in ["variable_power", "variable_on_off"]:
                special_variable = self.get_variable_by_name(special_var)
                if special_variable is not None:
                    feedback[special_var] = special_variable.get_current_value()   
        self.display = feedback
        
    
    def get_variable_value(self, variable_name):
        # check this variable name exists
        variable = getattr(self, variable_name, None)
        if variable is not None:
            return variable.get_current_value()
        return None
    
    def get_current_variable(self, action):
        variable_name = self.feature.get_current_variable(action)
        if variable_name:
            variable = getattr(self, variable_name)
            return variable
        else:
            return None
    
    def reset(self):
        return 
    
    def assign_variable_to_next(self, variable, **kwargs):
        if variable is not None:
            variable.next(**kwargs)

    def assign_variable_to_prev(self, variable, **kwargs):
        if variable is not None:
            variable.prev(**kwargs)
    
    def get_current_value(self):
        return self.feature.get_current_value()


    def get_variables(self):
        return sorted(
            [(key, value) 
            for key, value in self.__dict__.items() 
            if isinstance(value, (Variable))], # InputString, Feature
            key=lambda x: x[0]  # Sort by the variable name (key)
        )
    
    def get_variable_by_name(self, variable_name):
        return getattr(self, variable_name, None)
    
    def __str__(self):
        variable_strs = [
            f"{key}: {value.get_current_value()}"
            for key, value in self.get_variables()
        ]
        result = "\n".join(variable_strs)
        return result

    def get_state(self):
        result_dict = {
            key: value.get_current_value()
            for key, value in self.get_variables()
        }
        return result_dict
    
    def heuristics(self, other):

        self_copy = self.copy()
        other_copy = other.copy()
        differences = self_copy.compare_states(other_copy)
        
    
        #feature_same = (self.feature.current_value[0] == other.feature.current_value[0]) 
        
        #differences = self.compare_states(other)
        total_difference = sum(differences) / len(differences)

        #if not feature_same:

        #    total_difference *= 100
        
        return total_difference
    
    def find_attribute_name(self, obj):
        for name, value in inspect.getmembers(self):
            if value is obj:
                return name
        return None

    def compare_states(self, other):
        self_vars = self.get_variables()
        other_vars = other.get_variables()
        
        #print("other_vars", other_vars)
        differences = []
        
        # Iterate over the variables, comparing both key names and values
        for (key1, var1), (key2, var2) in zip(self_vars, other_vars):

            if key1 != key2:  # If key names differ, append 'inf'
                differences.append(float('inf'))
            else:
                comparison = var1.compare(var2)
                differences.append(comparison)
        #print("differences", differences)
        
        return differences

    def __eq__(self, other):
        differences = self.compare_states(other)
        return all(diff == 0 for diff in differences)

    def __hash__(self):
        return hash(tuple((var[0], var[1].current_value) for var in self.get_variables()))
    
    def copy(self):
        return copy.deepcopy(self)
    
    def execute_action_and_set_next(self, action_name="", **kwargs):
        #self.feature.update_progress(action_name)
        current_variable = self.get_current_variable(action_name)
        self.assign_variable_to_next(current_variable, **kwargs)

    def execute_action_and_set_prev(self, action_name = "", **kwargs):
        #self.feature.update_progress(action_name)
        current_variable = self.get_current_variable(action_name)
        self.assign_variable_to_prev(current_variable, **kwargs)

    def press_number_button(self, action_name, digit):
        # Update feature and set variable based on input string
        self.feature.update_progress(action_name)
        variable = self.get_current_variable(action_name)
        variable_name = self.feature.get_current_variable(action_name)
        current_feature = self.feature.current_value[0]
        self.variable_input_string.add_digit(digit)
        value = self.process_input_string(current_feature, variable_name)
        variable.set_current_value(value)
    
    def press_number_0_button(self): 
        self.press_number_button("press_number_0_button", "0")
    
    def press_number_1_button(self):
        self.press_number_button("press_number_1_button", "1")
    
    def press_number_2_button(self):
        self.press_number_button("press_number_2_button", "2")
    
    def press_number_3_button(self):
        self.press_number_button("press_number_3_button", "3")
    
    def press_number_4_button(self):
        self.press_number_button("press_number_4_button", "4")
    
    def press_number_5_button(self):
        self.press_number_button("press_number_5_button", "5")
    
    def press_number_6_button(self):
        self.press_number_button("press_number_6_button", "6")
    
    def press_number_7_button(self):
        self.press_number_button("press_number_7_button", "7")
    
    def press_number_8_button(self):
        self.press_number_button("press_number_8_button", "8")
    
    def press_number_9_button(self):
        self.press_number_button("press_number_9_button", "9")

    def run_action(self, action_name, execution_times=1, **kwargs):
        #print("received action", action_name)
        #print("execution_times", execution_times)
        action = getattr(self, action_name, None)
        
        if callable(action):
            sig = inspect.signature(action)
            valid_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
            
            for _ in range(execution_times):
                action(**valid_kwargs)

        self.update_display()
        return self.display
    
    
    def set_feasible(self):
        self.feasible.set_current_value(1)
    def set_infeasible(self):
        self.feasible.set_current_value(0)
    def __lt__(self, other):
        return str(self) < str(other)
