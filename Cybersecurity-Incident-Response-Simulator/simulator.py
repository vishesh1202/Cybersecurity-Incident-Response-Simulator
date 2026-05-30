from detection_engine import detect
from response_engine import respond

with open("logs/generated_logs.txt") as file:

    for line in file:

        incident = detect(line)

        if incident:
            respond(incident)