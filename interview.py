# Write a Python script that reads a YAML pipeline definition file, validates that all 
# required keys are present (trigger, stages, pool), checks that no stage 
# is missing a jobs section, 
# 
# 
# and outputs a structured validation report.

# pipeline.yml


import yaml

#type string
file = open("./pipeline.yml")

#


yamlObject = yaml(file)


for key in ["trigger", "stages", "pool"]:
    if key not in yamlObject: 
        Throw('tesdt') 'missing required key'



stages = yamlObject["stages"]


for stage in stages:
    if "jobs" not in stage:
        throw new Exception('missing required key')



print("Number of stages analyzed: " + stages.length())
print("")









