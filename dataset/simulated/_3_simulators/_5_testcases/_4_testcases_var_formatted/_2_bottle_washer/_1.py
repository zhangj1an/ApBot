[
    {
        "command": "Turn on the machine and set it to automatic sterilize and dry for 30 minutes.",
        "id": 1,
        "important_target_states": {
            "variable_drying_time": 30,
            "variable_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 30,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    },
    {
        "command": "Power on the device and initiate a 45-minute automatic sterilize and dry cycle.",
        "id": 2,
        "important_target_states": {
            "variable_drying_time": 45,
            "variable_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 45,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    },
    {
        "command": "Switch on the appliance and run a 60-minute automatic sterilize and dry program.",
        "id": 3,
        "important_target_states": {
            "variable_drying_time": 60,
            "variable_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 60,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    },
    {
        "command": "Turn on the machine and start the sterilize-only function.",
        "id": 4,
        "important_target_states": {
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 0,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    },
    {
        "command": "Activate the device and initiate the dry-only function for 30 minutes.",
        "id": 5,
        "important_target_states": {
            "variable_drying_cycle": 30,
            "variable_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_drying_cycle": 30,
            "variable_drying_time": 0,
            "variable_on_off": "on",
            "variable_sterilization_cycle": 0
        }
    },
    {
        "command": "Power on the appliance and set it to dry-only mode for 45 minutes.",
        "id": 6,
        "important_target_states": {
            "variable_drying_cycle": 45,
            "variable_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_drying_cycle": 45,
            "variable_drying_time": 0,
            "variable_on_off": "on",
            "variable_sterilization_cycle": 0
        }
    },
    {
        "command": "Turn on the unit and operate the dry-only feature for 60 minutes.",
        "id": 7,
        "important_target_states": {
            "variable_drying_cycle": 60,
            "variable_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_drying_cycle": 60,
            "variable_drying_time": 0,
            "variable_on_off": "on",
            "variable_sterilization_cycle": 0
        }
    },
    {
        "command": "Power up the machine and perform automatic sterilize and dry for 30 minutes, assuming the bottles are for an infant.",
        "id": 8,
        "important_target_states": {
            "variable_drying_time": 30,
            "variable_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 30,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    },
    {
        "command": "Switch on the device and commence a 45-minute automatic sterilize and dry cycle, ensuring pet-safe use.",
        "id": 9,
        "important_target_states": {
            "variable_drying_time": 45,
            "variable_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 45,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    },
    {
        "command": "Activate the appliance and opt for a 60-minute automatic sterilize and dry run, considering cold weather conditions.",
        "id": 10,
        "important_target_states": {
            "variable_drying_time": 60,
            "variable_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_drying_cycle": 0,
            "variable_drying_time": 60,
            "variable_on_off": "on",
            "variable_sterilization_cycle": "running"
        }
    }
]
