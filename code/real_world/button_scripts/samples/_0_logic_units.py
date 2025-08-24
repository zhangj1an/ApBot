import copy
import inspect
import warnings
class Variable():
    def __init__(self, value_range=None, current_value=None, round_over = True, ):
        self.value_range = value_range
        self.current_value = current_value
        self.round_over = round_over
        
    
    def prev(self):
        pass
    
    def next(self):
        pass
    
    def set_current_value(self, value):
        pass
    
    def set_value_range(self, value_range):
        pass
    
    def get_current_value(self):
        pass

    def get_state(self):
        pass

    def compare(self, other):
        pass


class DiscreteVariable(Variable):
    def __init__(self, value_range=None, current_value=None, round_over = True, ):
        super().__init__(value_range=value_range, current_value=current_value, round_over = round_over)
        if self.value_range is not None:
            assert all(isinstance(item, str) for item in self.value_range), \
                f"Value range items for DiscreteVariable must be strings. Current value: {self.value_range}"
        if self.value_range is not None and self.current_value is not None:
            assert self.current_value in self.value_range, f"Current value {self.current_value} is not in the value range {self.value_range}"
        
            self.value_index = self.value_range.index(self.current_value)
        else:
            self.value_index = 0
     
    def prev(self):
        if self.value_index == 0:
            if self.round_over:
                self.value_index = len(self.value_range) - 1
            else:
                self.value_index = 0
        else:
            self.value_index -= 1
        self.current_value = self.value_range[self.value_index] 
    
    def next(self):
        if self.value_index == len(self.value_range) - 1:
            if self.round_over:
                self.value_index = 0
            else:
                self.value_index = len(self.value_range) - 1
        else:
            self.value_index += 1
        self.current_value = self.value_range[self.value_index]
    
    def set_current_value(self, value):
        # the value must insde the value range
        #assert value in self.value_range, f"Value {value} is not in the value range {self.value_range}"
        self.current_value = value 
        if self.current_value in self.value_range:
            self.value_index = self.value_range.index(value)
    
    def set_value_range(self, value_range):
        if self.value_range == value_range:
            return 
        self.value_range = value_range
        self.value_index = 0
        self.current_value = self.value_range[self.value_index]
        
    def get_current_value(self):
        return self.current_value

    def compare(self, other):
        if not isinstance(other, DiscreteVariable):
            raise ValueError("Can only compare with another DiscreteVariable instance")
        
        self_range_span = len(self.value_range) - 1
        other_range_span = len(other.value_range) - 1

        # Adjust the penalty for range difference
        if self_range_span != other_range_span:
            #print("difference in discrete value range, stopping")
            #exit()
            range_diff_penalty = abs(self_range_span - other_range_span) * 10  # Lower the weight for range differences
        else:
            range_diff_penalty = 0
        
        if self_range_span == 0:
            self_range_span = 1
        if other_range_span == 0:
            other_range_span = 1

        # Normalize values
        self_normalized_value = self.value_index / self_range_span
        other_normalized_value = other.value_index / other_range_span

        # Difference between normalized values
        diff = abs(self_normalized_value - other_normalized_value)

        # Apply a minimum difference threshold to ensure small differences aren't ignored
        if range_diff_penalty > 0:
            minimum_diff = 0.1  # You can adjust this value
            diff = max(diff, minimum_diff)

        # Add the range difference penalty to the total difference
        total_diff = diff + range_diff_penalty
        #print(f"total_diff: {total_diff}, diff: {diff}, range_diff_penalty: {range_diff_penalty}")
        return total_diff

class ContinuousVariable(Variable):
    def __init__(self, value_ranges_steps=None, current_value=None, round_over=True):
        # value_ranges_steps is a list of tuples [(range_start, range_end, step_value), ...]
        super().__init__(value_range=None, current_value=current_value, round_over=round_over)
        if value_ranges_steps:
            assert all(isinstance(step, (tuple, list)) and len(step) == 3 and
                       all(isinstance(v, (int, float)) for v in step)
                       for step in value_ranges_steps), \
                "Value ranges and steps for ContinuousVariable must be numbers (can be decimals)."
            # Ensure ranges do not overlap
            sorted_ranges = sorted(value_ranges_steps, key=lambda x: x[0])  # Sort by range_start
            for i in range(len(sorted_ranges) - 1):
                assert sorted_ranges[i][1] <= sorted_ranges[i + 1][0], \
                    f"Value ranges {sorted_ranges[i]} and {sorted_ranges[i + 1]} overlap; ContinuousVariables should have nonoverlapping value ranges."
            # current value must be int or float
            current_value_type = type(current_value)
            assert isinstance(current_value, (int, float)), f"Continuous Variable current value must be a number (with type int or float). Current value type: {current_value_type}. Current value: {current_value}"
        self.value_ranges_steps = value_ranges_steps or [(0, 1, 1)]  # Default range if none provided
        if current_value is not None:
            self.set_current_value(current_value)
            assert self.current_value >= self.value_range[0] and self.current_value <= self.value_range[1], f"Current value {self.current_value} is not in the value range {self.value_range}"
        else:
            self.set_current_value(self.value_ranges_steps[0][0])

    def set_value_range_and_step(self, target_value):
        # Sets the appropriate value range and step based on the current value
        valid_flag = False
        for (range_start, range_end, step_value) in self.value_ranges_steps:
            
            current_value = range_start
            while current_value <= range_end:
                if target_value == current_value:
                    self.value_range = (range_start, range_end)
                    self.step_value = step_value
                    self.current_value = target_value
                    valid_flag = True
                    break
                current_value += step_value
        if not valid_flag: 
            warnings.warn(f"Value {target_value} is not in any of the value ranges {self.value_ranges_steps}. Please check what the variable is representing and re-assign the value of this variable.", category=UserWarning)
        # if the assigned value is not in valid value range, leave it as it is, as the value might be input by input string and the process is not done yet.
        #assert valid_flag, f"Value {self.current_value} is not in any of the value ranges {self.value_ranges_steps}"

    def prev(self):
        # Decrease current_value by step_value, considering multiple ranges
        if self.current_value - self.step_value < self.value_range[0]:
            # Handle underflow: switch to the previous range if applicable
            for (i, value_range_steps) in enumerate(self.value_ranges_steps):
                range_start, range_end, step_value = value_range_steps
                if self.current_value >= range_start and self.current_value - self.step_value < range_start:
                    if i > 0:
                        if self.current_value == self.value_ranges_steps[i-1][1]:
                            self.current_value = self.value_ranges_steps[i-1][1] - self.value_ranges_steps[i-1][2]
                        else:
                            self.current_value = self.value_ranges_steps[i-1][1]
                        self.set_value_range_and_step(self.current_value)
                        return
                    else:
                        # If round_over is True, wrap around to the last range's upper bound
                        if self.round_over:
                            self.current_value = self.value_ranges_steps[-1][1]
                            self.set_value_range_and_step(self.current_value)
                            return
                        else:
                            pass
        else:
            self.current_value -= self.step_value

    def next(self):
        # Increase current_value by step_value, considering multiple ranges
        if self.current_value + self.step_value > self.value_range[1]:
            # Handle overflow: switch to the next range if applicable
            for (i, value_range_steps) in enumerate(self.value_ranges_steps):
                range_start, range_end, step_value = value_range_steps


                if self.current_value <= range_end and self.current_value + self.step_value > range_end:
                    if i < len(self.value_ranges_steps) - 1:
                        #print("here, signal 2")
                        if self.current_value == self.value_ranges_steps[i+1][0]:
                            self.current_value = self.value_ranges_steps[i+1][0] + self.value_ranges_steps[i+1][2]
                        else:
                            self.current_value = self.value_ranges_steps[i+1][0]
                        self.set_value_range_and_step(self.current_value)
                        return
                    else:
                        # If round_over is True, wrap around to the last range's upper bound
                        if self.round_over:
                            #print("here, signal 1")
                            self.current_value = self.value_ranges_steps[0][0]
                            self.set_value_range_and_step(self.current_value)
                            return
                        else:
                            pass
        else:
            self.current_value += self.step_value

    def set_current_value(self, value):
        # the value must be inside the value range
        if value is None:
            value = self.value_ranges_steps[0][0]
        
       
        # value must be float or int 
        current_value_type = type(value)
        assert isinstance(value, (int, float)), f"Continuous Variable current value must be a number (with type int or float). Current value type: {current_value_type}, Current value: {value}"

        self.set_value_range_and_step(value)

    def set_value_ranges_steps(self, value_ranges_steps, current_value):
        self.value_ranges_steps = value_ranges_steps
        self.set_value_range_and_step(current_value)

    def get_current_value(self):
        return self.current_value

    def compare(self, other):
        if not isinstance(other, ContinuousVariable):
            raise ValueError("Can only compare with another ContinuousVariable instance")
        
        # Get current range span for both variables
        self_range_span = self.value_range[1] - self.value_range[0]
        other_range_span = other.value_range[1] - other.value_range[0]

        # Apply a softer penalty for range differences
        if self_range_span != other_range_span:
            #print("difference in discrete value range, stopping")
            #exit()
            range_diff_penalty = abs(self_range_span - other_range_span) * 10  # Lower the weight for range differences
        else:
            range_diff_penalty = 0
            
        if self_range_span == 0:
            self_range_span = 1
        if other_range_span == 0:
            other_range_span = 1

        # Normalize the current values
        self_normalized_value = (self.current_value - self.value_range[0]) / self_range_span
        other_normalized_value = (other.current_value - other.value_range[0]) / other_range_span

        # Calculate difference between normalized values
        diff = abs(self_normalized_value - other_normalized_value)

        # Apply a minimum difference to avoid small differences being overlooked
        if range_diff_penalty > 0:
            minimum_diff = 0.1  # You can adjust this value
            diff = max(diff, minimum_diff)

        # Add the range difference penalty to the total difference
        total_diff = diff + range_diff_penalty
        #print(f"total_diff: {total_diff}, diff: {diff}, range_diff_penalty: {range_diff_penalty}")
        return total_diff

class TimeVariable(Variable):
    def __init__(self, value_ranges_steps=None, current_value=None, round_over=True):
        # value_ranges_steps is a list of tuples [(range_start, range_end, step_value), ...]
        super().__init__(value_range=None, current_value=current_value, round_over=round_over)
        if value_ranges_steps:
            assert all(isinstance(step, (tuple, list)) and len(step) == 3 and
                       isinstance(step[0], str) and isinstance(step[1], str) and isinstance(step[2], int) and
                       all(self.is_valid_time_format(v) for v in step[:2])
                       for step in value_ranges_steps), \
                f"Value ranges for TimeVariable must be in 'HH:MM:SS' format, and step value must be an integer. Current value: {value_ranges_steps}"
        
        self.value_ranges_steps = value_ranges_steps or [("00:00:00", "00:01:00", 1)]  # Default range if none provided. the value ranges must be in the format of "HH:MM:SS"
        self.current_value = current_value if current_value is not None else self.value_ranges_steps[0][0]
        self.set_value_range_and_step(self.current_value)

    def convert_to_seconds(self, time_str):
        h, m, s = map(int, time_str.split(":"))
        return h * 3600 + m * 60 + s

    def convert_to_time_format(self, total_seconds):
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    def set_value_range_and_step(self, target_value):
        current_seconds = self.convert_to_seconds(target_value)
        for (range_start, range_end, step_value) in self.value_ranges_steps:
            range_start_seconds = self.convert_to_seconds(range_start)
            range_end_seconds = self.convert_to_seconds(range_end)
            if range_start_seconds <= current_seconds <= range_end_seconds:
                self.value_range = (range_start_seconds, range_end_seconds)
                self.step_value = step_value
                self.current_value = target_value
                break

    def prev(self):
        current_seconds = self.convert_to_seconds(self.current_value)
        if current_seconds - self.step_value < self.value_range[0]:
            for i, (range_start, range_end, step_value) in enumerate(self.value_ranges_steps):
                range_start_seconds = self.convert_to_seconds(range_start)
                range_end_seconds = self.convert_to_seconds(range_end)
                if range_start_seconds <= current_seconds - self.step_value <= range_end_seconds:
                    self.current_value = self.convert_to_time_format(range_end_seconds)
                    self.set_value_range_and_step(self.current_value)
                    return
            if self.round_over:
                self.current_value = self.convert_to_time_format(self.convert_to_seconds(self.value_ranges_steps[-1][1]))
            else:
                self.current_value = self.convert_to_time_format(self.convert_to_seconds(self.value_ranges_steps[0][0]))
            self.set_value_range_and_step(self.current_value)
        else:
            new_seconds = current_seconds - self.step_value
            self.current_value = self.convert_to_time_format(new_seconds)

    def next(self):
        current_seconds = self.convert_to_seconds(self.current_value)
        if current_seconds + self.step_value > self.value_range[1]:
            for i, (range_start, range_end, step_value) in enumerate(self.value_ranges_steps):

                range_start_seconds = self.convert_to_seconds(range_start)
                range_end_seconds = self.convert_to_seconds(range_end)
                if range_start_seconds <= current_seconds + self.step_value <= range_end_seconds:
                    self.current_value = self.convert_to_time_format(range_start_seconds)
                    self.set_value_range_and_step(self.current_value)
                    return
            if self.round_over:
                self.current_value = self.convert_to_time_format(self.convert_to_seconds(self.value_ranges_steps[0][0]))
            else:
                self.current_value = self.convert_to_time_format(self.convert_to_seconds(self.value_ranges_steps[-1][1]))
            self.set_value_range_and_step(self.current_value)
        else:
            new_seconds = current_seconds + self.step_value
            self.current_value = self.convert_to_time_format(new_seconds)

    def set_current_value(self, value):
        self.set_value_range_and_step(value)

    def set_value_ranges_steps(self, value_ranges_steps, current_value):
        self.value_ranges_steps = value_ranges_steps
        self.set_value_range_and_step(current_value)

    def get_current_value(self):
        return self.current_value

    def is_valid_time_format(self, time_str):
        try:
            h, m, s = map(int, time_str.split(":"))
            return h >= 0  and 0 <= m < 100 and 0 <= s < 100
        except ValueError:
            print(f"h: {h}, m: {m}, s: {s} ")
            return False
    def compare(self, other):
        if not isinstance(other, TimeVariable):
            raise ValueError("Can only compare with another TimeVariable instance")
        
        self_range_span = self.value_range[1] - self.value_range[0]
        other_range_span = other.value_range[1] - other.value_range[0]

        if self_range_span == 0:
            self_range_span = 1
        if other_range_span == 0:
            other_range_span = 1
        
        self_normalized_value = (self.convert_to_seconds(self.current_value) - self.value_range[0]) / self_range_span
        other_normalized_value = (self.convert_to_seconds(other.current_value) - other.value_range[0]) / other_range_span
        
        diff = abs(self_normalized_value - other_normalized_value)
        
        return diff

class InputString():
    def __init__(self):
        self.input_string = "" 

    def add_digit(self, digit, length_limit = 6):
        self.input_string += str(digit)
        if len(self.input_string)>length_limit:
            self.input_string = self.input_string[-length_limit:]
    
    def add_alphabet(self, alphabet, length_limit = 10):
        self.input_string += alphabet
        if len(self.input_string)>length_limit:
            self.input_string = self.input_string[-length_limit:]
            
    def get_time(self):
        value = min(max(int(self.input_string), 0), 999999)
        time_string = str(value).zfill(6)
        return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
    
    def get_value(self):
        pass
    
meta_actions_dict = {
        "0": "press_number_0_button",
        "1": "press_number_1_button",
        "2": "press_number_2_button",
        "3": "press_number_3_button",
        "4": "press_number_4_button",
        "5": "press_number_5_button",
        "6": "press_number_6_button",
        "7": "press_number_7_button",
        "8": "press_number_8_button",
        "9": "press_number_9_button",
}

meta_actions_on_number = ["press_number_1_button", "press_number_2_button", "press_number_3_button", "press_number_4_button", "press_number_5_button", "press_number_6_button", "press_number_7_button", "press_number_8_button", "press_number_9_button", "press_number_0_button"]

class Feature():
    def __init__(self, feature_list=None, current_value=("empty", 1)):
        self.feature_list = feature_list
        self.feature_list["empty"] = [{"step": 1, "actions": ["empty"]}]
        self.current_value = current_value # (feature, step)
        self.build_index_map()
    
    def get_current_value(self):
        return self.current_value
    
    def reach_end(self):
        feature_length = len(self.feature_list[self.current_value[0]])
        if self.current_value[1] == feature_length:
            return True
        return False
    
    def build_index_map(self):
        index_map = {}
        for feature, steps in self.feature_list.items():
            for index, step in enumerate(steps):
                step_key = f"{feature}_step_{step['step']}"
                index_map[step_key] = index
        self.feature_index_map = index_map

    def get_feature_step_detail(self, feature, step):
        step_key = f"{feature}_step_{step}"
        if step_key in self.feature_index_map:
            step_index = self.feature_index_map[step_key]
            return self.feature_list[feature][step_index]
        else:
            return None
        
    def get_actions(self, feature, step):
        detail = self.get_feature_step_detail(feature, step)
        if detail is not None:
            return detail["actions"]
        return None

    def update_progress(self, button_name):
        # return feature the machine will be at if the button execute successfully. 
        feature = self.current_value[0]
        step = self.current_value[1] 
        # still adjusting the same variable, then no change in progress 
        details = self.get_feature_step_detail(feature, step)
        if details is not None:
            controls = details["actions"] 
            if "variable" in details and button_name in controls:
                return
        
        next_step_details = self.get_feature_step_detail(feature, step + 1)
        # if taking action on the next step, then progress to next step
        if next_step_details is not None: 
            next_step_controls = next_step_details["actions"]
            if button_name in next_step_controls:
                self.current_value = (feature, step + 1) 
                return
            else:
                next_next_step_details = self.get_feature_step_detail(feature, step + 2)
                if next_next_step_details is not None:
                    next_next_step_controls = next_next_step_details["actions"]
                    if button_name in next_next_step_controls:
                        self.current_value = (feature, step+2)
                        return 
        
        # checking if skipping steps to future steps in the same feature. but this part can be deleted
        while True:
            next_step_details = self.get_feature_step_detail(feature, step + 1)
            if next_step_details is None:
                break
            
            # this part can be deleted
            if "skippable" not in next_step_details.keys() or next_step_details["skippable"] == False:
                break 

            # this part can be deleted
            if next_step_details["needs_check"] == True and button_name in next_step_details["actions"]:
                self.current_value = (feature, step + 1)
                return
            
            step += 1

        # the action is not valid in this feature and is meant to transit to another feature
        
        for feature in self.feature_list.keys():
            
            a = self.get_actions(feature, 1)
            
            if button_name in self.get_actions(feature, 1):
                
                self.current_value = (feature, 1)
       
        
    
    def get_current_variable(self, action):
        detail = self.get_feature_step_detail(self.current_value[0], self.current_value[1])
        if detail is not None:
            valid_actions = detail["actions"]
            if action in valid_actions and "variable" in detail:
                return detail["variable"]
        return None
    
    def compare(self, other):
        if self.current_value != other.current_value:
            return 1
        return 0

import copy
import inspect

class Appliance():

    def __init__(self):
        self.reset()
    
    def update_display(self, variable):
        if variable is not None:
            variable_name = self.find_attribute_name(variable).replace("variable_", "")
            self.display = f"{variable_name}: {variable.get_current_value()}"
        else:
            detail = self.feature.get_feature_step_detail(self.feature.current_value[0], self.feature.current_value[1])
            next_step_detail = self.feature.get_feature_step_detail(self.feature.current_value[0], self.feature.current_value[1] + 1)
            if detail is not None and "variable" not in detail and next_step_detail is not None and "variable" in next_step_detail:
                variable = getattr(self, next_step_detail["variable"])
                variable_name = self.find_attribute_name(variable).replace("variable_", "")
                self.display = f"{variable_name}: {variable.get_current_value()}"
                    
            # if current step has no variable, but next step has variable, display next step variable 
            else:
                self.display = "Display is not showing anything"
        # otherwise do not modify display
        
    
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
        #print("self_vars", self_vars)
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
        self.feature.update_progress(action_name)
        current_variable = self.get_current_variable(action_name)
        self.assign_variable_to_next(current_variable, **kwargs)

    def execute_action_and_set_prev(self, action_name = "", **kwargs):
        self.feature.update_progress(action_name)
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
        action = getattr(self, action_name, None)

        if callable(action):
            # Get the parameter names of the action method
            sig = inspect.signature(action)
            
            valid_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
            
            
            for _ in range(execution_times):
                action(**valid_kwargs)
        appliance_state_with_feature = self.get_state()
        feedback = {}
        feedback["feature"] = self.feature.current_value
        # get current value being adjusted. if previous has a value, display that; if next has a value, display that. 
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
        return feedback
    
    
    def set_feasible(self):
        self.feasible.set_current_value(1)
    def set_infeasible(self):
        self.feasible.set_current_value(0)
    def __lt__(self, other):
        return str(self) < str(other)
