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

    def list_all_values(self):
        # return all list
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
        self.current_value = str(value)
        if str(value) in self.value_range:
            self.current_value = str(value)
            self.value_index = self.value_range.index(value)
        else:
            # throw exception and error message 
            error_msg = f"Value {value} is not in the value range {self.value_range}. Please only assign valid variable values."
            warnings.warn(error_msg, category=UserWarning)
            #raise ValueError(error_msg)
        
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
            return 1
            #raise ValueError("Can only compare with another DiscreteVariable instance")
        
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

    def list_all_values(self):
        return self.value_range
    
    def __lt__(self, other):
        return self.value_index < other.value_index
    
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
                current_value = round(current_value, 2)
                if step_value == 0:
                    break
            if valid_flag:
                break
        if not valid_flag: 
            error_msg = f"Value {target_value} is not in any of the value ranges {self.value_ranges_steps}. Please check what the variable is representing and re-assign the value of this variable."
            warnings.warn(error_msg, category=UserWarning)
            print(error_msg)
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
            return 1
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
    
    def list_all_values(self):
        value_ranges_steps = copy.deepcopy(self.value_ranges_steps)
        value_range_string = "The value ranges are as follows: "
        for i, (range_start, range_end, step_value) in enumerate(value_ranges_steps):
            value_range_string += f"from {range_start} to {range_end}, with step value of {step_value}"
            if i < len(value_ranges_steps) - 1:
                value_range_string += "; "
            else:
                value_range_string += "."
            value_ranges_steps[i] = [range_start, range_end, step_value]
    def __lt__(self, other):
        return self.current_value < other.current_value

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
        
            # the current value must be inside the value range 

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
                return 
        raise AssertionError(f"Value {target_value} is not in any of the value ranges {self.value_ranges_steps}. Please modify the current value or value range.")

        

    def prev(self):
        current_seconds = self.convert_to_seconds(self.current_value)

        if current_seconds - self.step_value < self.value_range[0]:
            for i, (range_start, range_end, step_value) in enumerate(self.value_ranges_steps):
                range_start_seconds = self.convert_to_seconds(range_start)
                range_end_seconds = self.convert_to_seconds(range_end)
                if current_seconds >= range_start_seconds and current_seconds - self.step_value < range_start_seconds:
                    if i > 0:
                        prev_range_end_seconds = self.convert_to_seconds(self.value_ranges_steps[i-1][1])
                        prev_range_step_value = self.value_ranges_steps[i-1][2]
                        if current_seconds == prev_range_end_seconds:
                            self.current_value = self.convert_to_time_format(prev_range_end_seconds - prev_range_step_value)
                        else:
                            self.current_value = self.value_ranges_steps[i-1][1]
                        self.set_value_range_and_step(self.current_value)
                        return
                    else:
                        if self.round_over:
                            self.current_value = self.value_ranges_steps[-1][1]
                            self.set_value_range_and_step(self.current_value)
                            return
                        else:
                            pass
        else:
            new_seconds = current_seconds - self.step_value
            self.current_value = self.convert_to_time_format(new_seconds)

    def next(self):
        current_seconds = self.convert_to_seconds(self.current_value)
        if current_seconds + self.step_value > self.value_range[1]:
           

            for i, (range_start, range_end, step_value) in enumerate(self.value_ranges_steps):

                range_start_seconds = self.convert_to_seconds(range_start)
                range_end_seconds = self.convert_to_seconds(range_end)
                if current_seconds <= range_end_seconds and current_seconds + self.step_value > range_end_seconds:
                    if i < len(self.value_ranges_steps) - 1:
                        next_range_start_seconds = self.convert_to_seconds(self.value_ranges_steps[i+1][0])
                        next_range_step_value = self.value_ranges_steps[i+1][2]
                        if current_seconds == next_range_start_seconds:
                            self.current_value = self.convert_to_time_format(next_range_start_seconds + next_range_step_value)
                        else:
                            self.current_value = self.value_ranges_steps[i+1][0] 
                        self.set_value_range_and_step(self.current_value)
                        return 
                    else:
                        if self.round_over:
                            self.current_value = self.value_ranges_steps[0][0]
                            self.set_value_range_and_step(self.current_value)
                            return
                        else:
                            pass
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
            return 1
            #raise ValueError("Can only compare with another TimeVariable instance")
        
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
    
    def list_all_values(self):
        value_ranges_steps = copy.deepcopy(self.value_ranges_steps)
        value_range_string = "In the format of 'HH:MM:SS', the value ranges are "
        for i, (range_start, range_end, step_value) in enumerate(value_ranges_steps):
            value_range_string += f"from {range_start} to {range_end}, with step value of {step_value} seconds"
            if i < len(value_ranges_steps) - 1:
                value_range_string += ", "
            else:
                value_range_string += "."
            value_ranges_steps[i] = [range_start, range_end, step_value]

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
    
            