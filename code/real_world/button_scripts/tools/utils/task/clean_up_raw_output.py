import os

def batch_filter_raw_output(method_dir):
    for machine_type in os.listdir(method_dir):
        machine_dir = os.path.join(method_dir, machine_type)
        if not os.path.isdir(machine_dir):
            continue
        for question_id in os.listdir(machine_dir):
            question_dir = os.path.join(machine_dir, question_id, "_1_var_testcases")
            if not os.path.isdir(question_dir):
                continue
            for var_id in os.listdir(question_dir):
                filter_raw_output(machine_dir, machine_type, question_id, var_id)


def filter_raw_output(base_dir, filename_prefix, question_id, var_id):
    """
    Modifies the `_4_raw_output.txt` file by keeping only the content after the matching `processing:` line.
    
    Args:
        base_dir (str): Path to the base folder (e.g. path to `_6_washing_machine`).
        filename_prefix (str): The name prefix (e.g. "_6_washing_machine").
        question_id (int): The question ID (e.g. 2).
        var_id (int): The variable ID (e.g. 2).
    """
    target_line = f"processing:  {filename_prefix} {question_id} var {var_id}"
    target_path = os.path.join(
        base_dir,
        str(question_id),
        "_1_var_testcases",
        str(var_id),
        "1",
        "_4_raw_output.txt"
    )

    if not os.path.exists(target_path):
        print(f"File not found: {target_path}")
        return

    with open(target_path, "r") as f:
        lines = f.readlines()

    # Find the index where the target line appears
    for i, line in enumerate(lines):
        if target_line in line:
            # Keep everything *after* this line
            new_lines = lines[i+1:]
            break
    else:
        print(f"Target line not found in: {target_path}")
        return

    with open(target_path, "w") as f:
        f.writelines(new_lines)

    print(f"Trimmed file saved: {target_path}")

if __name__ == "__main__":
    # Example usage
    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    method_dir = os.path.expanduser("~/TextToActions/datasetv2/simulated/_6_results/_6_paper_exp/baselinesv1/_4_M_SR_MA/gpt-4o-2024-11-20")#"/path/to/your/method_dir"  # Replace with your actual path
    batch_filter_raw_output(method_dir)