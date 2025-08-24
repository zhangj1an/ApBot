# 🤖 ApBot: Robot Operation of Home Appliances by Reading User Manuals

This repository accompanies the paper **"ApBot: Robot Operation of Home Appliances by Reading User Manuals"**, and contains **open-sourced code, datasets, simulation tools, and baseline experiments** to support research on robotic operation of household appliances.

ApBot enables robots to operate **previously unseen appliances** by “reading” their user manuals, grounding symbolic actions to **real-world control elements**, and executing policies **robustly and interactively** with textual or visual feedback.

---

## 📦 What's in this Repository?

The repository is organized into three main parts:

* **`code/`** – Core implementation for foundation models, symbolic reasoning, visual grounding, simulation, and real-world execution. It consists of:

  * `foundation_models/` – GPT, OWL, and SAM2 integration
  * `simulated/` – Scripts for parsing user manuals, grounding, generating test cases, and running experiments. Includes:

    * `paper_exp/` – Scripts and outputs for reproducing experiments and baselines reported in the paper
  * `real_world/` – Scripts for running real-world experiments

* **`dataset/`** – Structured datasets for training and evaluation. It consists of:

  * `simulated/` – Includes six simulated appliances (e.g., microwave, washer), each with user manuals, control panel images, and symbolic simulators
  * `real_world/` – Includes real-world recordings of five appliances, structured in the same format as the simulated data

* **`README`** – Documentation and usage guide

---

## 🧠 Key Features

* **Structured Appliance Modeling**: Automatically extract and build symbolic models (variables, features, actions) from unstructured manuals.
* **Vision-Language Grounding**: Ground control instructions to appliance control panels using large VLMs (e.g., OWL-V2).
* **Closed-loop Execution**: Monitor execution visually and update world models based on feedback.
* **Simulated + Real-world Evaluation**: Test and benchmark baseline methods in both controlled and real scenarios.

-----

## 💻 Code

This repository contains structured code, foundational models, and scripts for appliance control research. It is organized into **foundational models**, **real-world**, and **simulated** directories.

<details>
<summary>📁 <code>code/</code></summary>
The heart of the project, containing the logic for visual grounding, reasoning, and simulation.

<ul>
<details>
<summary>📁 <code>foundation_models/</code></summary>
Contains foundational models such as GPT, OWL, and SAM2.
<ul>
<li>📄 <code>gpt_4o_model.py</code> – Used to call GPT</li>
<li>📄 <code>owlv2_crane5_api.py</code> – Starts a microservice to recognize appliance panel buttons and dials</li>
<li>📄 <code>owlv2_crane5_query.py</code> – Once the API is running, functions in this script can be used to call OWLv2</li>
</ul>
</details>



<details>
<summary>📁 <code>simulated/</code></summary>
Simulation-related scripts for processing user manuals, grounding control panel elements, and generating test cases.
<ul>
<li>📄 <code>init.py</code></li>
<li>📄 <code>_0_t2a_config.py</code> – Specifies the root code path</li>
<li>📄 <code>_1_pdf_to_text.py</code> – Converts PDF user manuals to text</li>
<li>📄 <code>_2_extract_control_panel_element_names_from_user_manual.py</code> – Extracts button/dial name lists from manuals</li>
<li>📄 <code>_3_detect_bbox_from_photos.py</code> – Detects bounding boxes from appliance panel images</li>
<li>📄 <code>_4_map_control_panel_element_names_to_bbox_indexes.py</code> – Maps button/dial names to possible bounding box indices</li>
<li>📄 <code>_5_json_map_control_panel_element_names_to_bbox_indexes.py</code> – Formats the previous mapping results into JSON</li>
<li>📄 <code>_6_remove_duplicate_bboxes.py</code> – Ensures one-to-one mapping between buttons/dials and bounding box indices</li>
<li>📄 <code>_7_json_map_control_panel_element_names_to_bbox_indexes.py</code> – (Appears redundant; formats mapping results into JSON again)</li>
<li>📄 <code>_8_visualise_grounding_control_element_name_result.py</code> – Generates visualization images showing all buttons/dials as labeled bounding boxes</li>
<li>📄 <code>_10_propose_action_names.py</code> – Proposes actions based on user manuals</li>
<li>📄 <code>_11_generated_grounded_action_json.py</code> – Maps proposed actions to bounding box coordinates</li>
<li>📄 <code>_12_match_proposed_action_to_oracle_action.py</code> – Checks if proposed actions match oracle execution regions using bounding box coordinates</li>
<li>📄 <code>_13_visualisation_grounding_action_result.py</code> – Generates visualization images displaying grounded actions as labeled bounding boxes</li>
<li>📄 <code>_18_generate_testcases.py</code> – (Deprecated) Generates ambiguous instructions that can be satisfied by one or multiple policies</li>
<li>📄 <code>_18_generate_testcases_v2.py</code> – Generates instructions requiring different step sizes to achieve goals</li>
<li>📄 <code>_19_generate_target_state.py</code> – For each test instruction, generates the target state in the appliance simulator</li>

<details>
<summary>📁 <code>samples/</code></summary>
Used as example appliance models.
<ul>
<li>📄 <code>_0_logic_units.py</code> – Appliance model templates, combines the content of variables, features and actions</li>
<li>📄 <code>_0_sample_machine.py</code> – Example appliance models</li>
<li>📄 <code>_0_search.py</code> – Macro action logics</li>
<li>📄 <code>_1_variables.py</code> – Appliance variable templates</li>
<li>📄 <code>_2_features.py</code> – Appliance feature templates, used to specify the macro actions</li>
<li>📄 <code>_3_actions.py</code> – Appliance dynamics templates, used to specify action effects</li>
</ul>
</details>

<details>
<summary>📁 <code>prompts/</code></summary>
Stores all the prompts used.
<ul>
<li>📄 <code>various prompt text file:</code> – Is used for the python files in the simulated/ folder</li>
<li>📄 <code>paper_exp/baselines_v1/:</code> – Is used for various baselines in the paper. _4_HV_M_SR_MA_agnostic refers to the ApBot algorithm.</li>
<li>📄 <code>_17_testcase/:</code> – The prompt used to generate instructions that are ambiguous or specific</li>
<li>📄 <code>_17_testcase_v2/:</code> – The prompt used to generate instructions that require different numbers of steps to finish</li>
</ul>
</details>

<details>
<summary>📁 <code>paper_exp/</code></summary>
<ul>
<li>
<details>
<summary>📁 </code>baselines_v1/</code></summary>
<ul>
<li>📄 code for running paper baselines. ApBot has the file name _4_M_SR_MA_agnostic. </li>
</ul>
</details>
</li>
<li>
<details>
<summary>📁 </code>real_world/</code></summary>
<ul>
<li>📄 code for running real world experiments</li>
</ul>
</details>
</li>
</ul>
</details>

<details>
<summary>📁 <code>utils/</code></summary>
<ul>
<li> Some helper functions to load files.
<li> <details>
<summary>📁 <code>task/</code></summary>
<ul>
<li>📄 <code>calibrate_current_value.py</code> – During close loop execution, if the display is an unexpected value, calibrates the appliance model according to predefined routines and templates</li>
<li>📄 <code>check_reasoning_file_existance.py</code> – Checks file existence</li>
<li>📄 <code>check_state_reached.py</code> – Checks if the appliance state has reached those required by an instruction</li>
<li>📄 <code>compare_visual_grounding.py</code> – Compares the results between ApBot and Molmo visual grounding performance</li>
<li>📄 <code>derive_variable_definition.py</code> – Helper function to help update the variable in the appliance model when there is a feedback mismatch</li>
<li>📄 <code>generate_report.py</code> – After baseline results are out, use it to generate instruction execution results</li>
<li>📄 <code>generate_updated_goal.py</code> – Used to update the ApBot appliance model target state</li>
<li>📄 <code>interact_with_simulator.py</code> – Used for ApBot to interact with appliance simulators</li>
<li>📄 <code>mathces_run_action_format.py</code> – Used to check command formats used by ApBot to interact with appliance simulators.</li>
<li>📄 <code>prepare_simulator.py</code> – Used to load appliance simulators</li>
<li>📄 <code>propose_actions.py</code> – During close-loop execution, ApBot proposes a suitable action given the current appliance state</li>
<li>📄 <code>propose_feature_list.py</code> – Proposes macro actions of appliance models</li>
<li>📄 <code>propose_goal_state.py</code> – Proposes the appliance model's target state</li>
<li>📄 <code>propose_variables.py</code> – Proposes appliance model variables</li>
<li>📄 <code>propose_world_model_agnostic_to_command.py</code> – Proposes the appliance model's action dynamics</li>
</ul>
</details>
</ul>
</details>

</ul>
</details>

<details>
<summary>📁 <code>real_world/</code></summary>
Scripts for real-world execution. Code structure is the combined content of the dataset folder and the simulated code folder.
</details>

</details>
</ul>

-----

## 💾 Appliance Simulation Dataset

This repository contains structured datasets, simulators, and baseline experiment results for appliance control research. It is organized into **simulated** and **real-world** datasets.

### 1\. Simulated

The simulated dataset includes data for the following appliances, with **5 instances** each:

  * Dehumidifier
  * Bottle Washer
  * Rice Cooker
  * Microwave Oven
  * Bread Maker
  * Washing Machine

<details>
<summary>📁 <code>simulated/</code></summary>
The root directory for all simulated appliance data.

<ul>
<details>
<summary>📁 <code>0_websites/</code></summary>
Appliance panel images and user manuals (source websites).
</details>

<details>
<summary>📁 <code>1_user_manual/</code></summary>
Contains different forms of user manuals (PDF, image, text, and parsed elements).
<ul>
<li>📁 <strong>0_pdf/</strong> – Raw PDF manuals, manually added</li>
<li>📁 <strong>1_image/</strong> – Image versions of manuals, generated via code</li>
<li>📁 <strong>2_text/</strong> – Extracted text from PDFs, generated via code</li>
<li>📁 <strong>3_extracted_control_panel_element_names/</strong> – Control panel element names extracted from manuals, generated via code</li>
</ul>
</details>

<details>
<summary>📁 <code>2_control_panel_images/</code></summary>
Control panel images and grounded elements.
<ul>
<li>📁 <strong>0_raw/</strong> – Images copied from websites, manually added</li>
<li>📁 <strong>1_selected/</strong> – Final selected single image, manually added</li>
<li>
<details>
<summary>📁 2_ground_control_panel_elements/</summary>
<ul>
<li>📁 <strong>1_validity_control_panel/</strong> – One bounding box per image circling a button or dial</li>
<li>📁 <strong>2_bboxes_on_control_panel/</strong> – JSON files of button/dial bounding boxes</li>
<li>📁 <strong>3_bboxes_on_control_panel_visualisation/</strong> – Visual summary of all bounding boxes</li>
<li>📁 <strong>4_query_images_bbox_to_name/</strong> – Red box for query, green boxes as references</li>
<li>📁 <strong>5_query_images_unique_bbox_id/</strong> – Indexed candidate boxes per button/dial</li>
</ul>
</details>
</li>
</ul>
</details>

<details>
<summary>📁 <code>3_simulators/</code></summary>
Contains simulators and their associated assets.
<ul>
<li>📁 <strong>0_control_panel_images_groundtruth_annotation/</strong> – COCO annotations (manual)</li>
<li>📁 <strong>1_oracle_available_actions/</strong> – Oracle action lists (manual)</li>
<li>📁 <strong>2_map_oracle_action_to_annotation_label/</strong> – Dict: action names → labels + types (manual)</li>
<li>📁 <strong>3_oracle_simulator_action_to_bbox_mapping/</strong> – Auto: action names → bbox coords</li>
<li>📁 <strong>4_simulators_with_states_and_display/</strong> – Sim: action → text display (manual)</li>
<li>
<details>
<summary>📁 5_testcases/</summary>
<ul>
<li>📁 <strong>1_testcases_var_raw/</strong> – Generated task instructions</li>
<li>📁 <strong>2_testcases_var/</strong> – Selected instructions (manual)</li>
<li>📁 <strong>3_testcases_var_with_target_states/</strong> – Target states (generated)</li>
<li>📁 <strong>4_testcases_var_formatted/</strong> – Generated + manually corrected</li>
</ul>
</details>
</li>
</ul>
</details>

<details>
<summary>📁 <code>4_visual_grounding/</code></summary>
Visual grounding data for control panel elements and action names.
<ul>
<li>
<details>
<summary>📁 0_control_panel_element_bbox/</summary>
<ul>
<li>📁 <strong>0_control_panel_element_index/</strong> – Bbox index → element names</li>
<li>📁 <strong>1_control_panel_element_index_json/</strong> – Element names → bbox indices</li>
<li>📁 <strong>2_control_panel_element_index_json_unique/</strong> – Unique name → bbox index</li>
<li>📁 <strong>3_proposed_control_panel_element_bbox/</strong> – Element name → coordinates</li>
<li>📁 <strong>4_visualised_proposed_control_panel_element_bbox/</strong> – Indexed bbox visualization</li>
<li>📁 <strong>5_visualised_localised_buttons_no_label/</strong> – Center-indexed bbox visualizations</li>
<li>📁 <strong>6_visualised_localised_buttons_legends/</strong> – Bbox index → coordinates</li>
<li>📁 <strong>7_proposed_buttons_to_oracle_action_mapping/</strong> – Proposed bbox → oracle actions</li>
<li>📁 <strong>9_extracted_control_panel_labels/</strong> – Element names from manual</li>
</ul>
</details>
</li>
<li>
<details>
<summary>📁 1_action_names/</summary>
<ul>
<li>📁 <strong>1_proposed_action_names/</strong> – Proposed actions</li>
<li>📁 <strong>2_proposed_world_model_action_bbox/</strong> – Action name → bbox</li>
<li>📁 <strong>3_proposed_to_oracle_action_mapping/</strong> – Action name → oracle mapping (ApBot)</li>
<li>📁 <strong>4_molmo_proposed_action_coords/</strong> – Action name → image coords</li>
<li>📁 <strong>5_molmo_proposed_actions_visualisation/</strong> – Visualized action positions</li>
<li>📁 <strong>6_molmo_proposed_to_oracle_action_mapping/</strong> – Action name → oracle mapping (Molmo)</li>
</ul>
</details>
</li>
</ul>
</details>

<details>
<summary>📁 <code>6_results/</code></summary>
<ul>
<li>📁 <strong>1_visual_grounding_action_results/</strong> – Metrics for action visual grounding</li>
<li>📁 <strong>3_visualize_proposed_actions/</strong> – Visual results of grounded actions</li>
<li>
<details>
<summary>📁 6_paper_exp/</summary>
<ul>
<li><strong>Baseline experiment results</strong></li>
<li>📁 <strong>11_visualisation/</strong> – Baseline output visualizations</li>
</ul>
</details>
</li>
</ul>
</details>
</details>
</ul>

-----

### 2\. Real World

The real-world dataset includes data for the following appliances, with **1 instance** each:

  * Washing Machine
  * Rice Cooker
  * Blender
  * Water Dispenser
  * Induction Cooker

The internal folder structure is identical to the simulated dataset.

-----

## 🧪 Baseline Experiments

The baseline experiments evaluate different combinations of **perception**, **appliance model**, **reasoning**, and **policy**.

| ID | Name | Visual Grounding (Perception) | Have Access To User Manual | Reasoning | Action Policy | Name in Paper |
| :-- | :---------------------- | :---------------------------- | :--------------- | :------------ | :----------------- | :------------------------------------------------ |
| 1 | NV_M_UR_LP | Oracle | Yes | Unstructured | LLM | LLM as policy w/ grounded actions |
| 2 | HV_M_UR_LP | Proposed | Yes | Unstructured | LLM | LLM as policy w/ image |
| 4 | M_SR_MA | Proposed | Yes | Structured | Macro-actions | **ApBot** |
| 5 | HV_M_SR_LP | Proposed | Yes | Structured | LLM | ApBot w/o button policy |
| 7 | HV_M_UR_MA | Proposed | Yes | Unstructured | Macro-actions | ApBot w/o model |
| 8 | HV_M_SR_MA_OL | Proposed | Yes | Structured | Macro-actions | ApBot w/o close-loop update |
| 9 | oracle_V_oracle_M | Oracle | Yes | Structured & Oracle | Macro-actions | N.A |
| 10 | oracle_V_proposed_M | Oracle | Yes | Structured | Macro-actions | N.A |

-----

## 📊 Results

  * **Visual Grounding Metrics**: Stored in `dataset/simulated/6_results/1_visual_grounding_action_results/`
  * **Action Visualizations**: Stored in `dataset/simulated/6_results/3_visualize_proposed_actions/`
  * **Baseline Experiment Outputs**: Stored in `dataset/simulated/6_results/6_paper_exp/`
  * **Comparative Visualisations**: Stored in `dataset/simulated/6_results/6_paper_exp/11_visualisation/`

-----

## 🚀 Usage

To understand and run the full ApBot pipeline, start from the **`code/simulated/`** directory. The pipeline includes **reading PDFs**, **visual grounding**, **building symbolic models**, and **testing the model**. Below is the step-by-step process:

---

### 1. 📘 Read and Parse User Manuals

Convert appliance manuals from PDF to structured elements.

| Step | Description                                   | Script                                                       |
| ---- | --------------------------------------------- | ------------------------------------------------------------ |
| 1.1  | Convert PDF manuals into raw text             | `_1_pdf_to_text.py`                                          |
| 1.2  | Extract control panel element names from text | `_2_extract_control_panel_element_names_from_user_manual.py` |

---

### 2. 🖼️ Perform Visual Grounding

Use control panel images and align them with textual instructions.

| Step | Description                                 | Script                                                                                                                     |
| ---- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 2.1  | Detect bounding boxes from panel images     | `_3_detect_bbox_from_photos.py`                                                                                            |
| 2.2  | Map detected boxes to control element names | `_4_map_control_panel_element_names_to_bbox_indexes.py`                                                                    |
| 2.3  | Format mappings into structured JSON        | `_5_json_map_control_panel_element_names_to_bbox_indexes.py`, `_7_json_map_control_panel_element_names_to_bbox_indexes.py` |
| 2.4  | Remove duplicate or conflicting mappings    | `_6_remove_duplicate_bboxes.py`                                                                                            |
| 2.5  | Visualize grounding results                 | `_8_visualise_grounding_control_element_name_result.py`                                                                    |

---

### 3. 🧠 Build the Appliance World Model

Generate appliance variables, features, and macro-actions.

| Step | Description                                   | Script                                          |
| ---- | --------------------------------------------- | ----------------------------------------------- |
| 3.1  | Propose actions from manuals                  | `_10_propose_action_names.py`                   |
| 3.2  | Map actions to bounding boxes                 | `_11_generated_grounded_action_json.py`         |
| 3.3  | Match proposed actions to oracle ground-truth | `_12_match_proposed_action_to_oracle_action.py` |
| 3.4  | Visualize grounded actions                    | `_13_visualisation_grounding_action_result.py`  |

---

### 4. 🧪 Test Using Simulated Instructions

Generate test instructions and target appliance states.

| Step | Description                                  | Script                         |
| ---- | -------------------------------------------- | ------------------------------ |
| 4.1  | Generate ambiguous or multistep instructions | `_18_generate_testcases_v2.py` |
| 4.2  | Generate target states for each test         | `_19_generate_target_state.py` |

---

### 5. 🧹 Run ApBot (Symbolic Reasoning + Policy Execution)

Run the main ApBot experiment using the generated appliance model and test instructions.

| Step | Description                                                                  | Script                                          |
| ---- | ---------------------------------------------------------------------------- | ----------------------------------------------- |
| 5.1  | Main file for symbolic reasoning and macro-action execution (ApBot pipeline) | `paper_exp/baselines_v1/_4_M_SR_MA_agnostic.py` |

---

### 🛠️ Optional: World Model Construction and Reasoning Helpers

Located in `code/utils/task/`, these helper scripts support reasoning, calibration, and simulator interaction during closed-loop execution. For example:

* `interact_with_simulator.py` – ApBot interacting with simulator
* `generate_updated_goal.py` – Update goals dynamically based on feedback
* `propose_goal_state.py` – Generate target states
* `check_state_reached.py` – Check if state matches the goal
* `calibrate_current_value.py` – Adjust model if observed feedback is off