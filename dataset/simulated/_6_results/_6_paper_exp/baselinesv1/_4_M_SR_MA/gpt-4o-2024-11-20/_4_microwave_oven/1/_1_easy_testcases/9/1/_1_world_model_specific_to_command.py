# The given features and variables correctly model the relevant appliance commands required for the user task.
# The following sequence of features from the current code is needed to achieve this command:
#   1. weight_defrost: Modelled in feature_list["weight_defrost"]
#       - Adjust weight to 20 oz using weight defrost mode.
#       - User Manual Text: "Press 'WEIGHT DEFROST', screen will display 'dEF1'. Press numerical buttons to input weight to be defrosted. Input the weight ranged between 4~100 Oz. Press 'START/+30SEC.' to start defrosting and the cooking time remained will be displayed."
#   2. child_lock_control: Modelled in feature_list["child_lock_control"]
#       - Activate child lock.
#       - User Manual Text: "Lock: In waiting state, press 'STOP/CANCEL' for 3 seconds, there will be a long 'beep' denoting the entering into the children-lock state; meanwhile, screen will display '[ - - - ] '"

# Goal Variable Values:
# 1. Set `variable_weight_defrost` to "20" (defrost 20 oz of chicken).
# 2. Set `variable_start_running` to "on" (start the appliance).
# 3. Set `variable_child_lock` to "locked" (activate child lock).
class ExtendedSimulator(Simulator): 
    pass