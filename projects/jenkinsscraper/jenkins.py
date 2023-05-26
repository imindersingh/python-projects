import requests
import matplotlib.pyplot as plt
import numpy as np

# Get the build data from Jenkins

job_urls = [
    {
        "url": "/jenkins/job/CIR/job/job-name/job/job-name/api/json?pretty=true&tree=builds[number,status,timestamp,id,result,duration,fullDisplayName,description,url]&start=-20",
        "name": "1",
    },
    {
        "url": "/jenkins/job/CIR/job/job-name/job/job-name/api/json?pretty=true&tree=builds[number,status,timestamp,id,result,duration,fullDisplayName,description,url]&start=-20",
        "name": "2",
    },
    {
        "url": "/jenkins/job/CIR/job/job-name/job/job-name/api/json?pretty=true&tree=builds[number,status,timestamp,id,result,duration,fullDisplayName,description,url]&start=-20",
        "name": "3",
    },
    {
        "url": "/jenkins/job/CIR/job/job-name/job/job-name/api/json?pretty=true&tree=builds[number,status,timestamp,id,result,duration,fullDisplayName,description,url]&start=-20",
        "name": "4",
    },
    {
        "url": "/jenkins/job/CIR/job/job-name/job/job-name/api/json?pretty=true&tree=builds[number,status,timestamp,id,result,duration,fullDisplayName,description,url]&start=-20",
        "name": "5",
    },
]

result_counts = {"pass": [], "fail": [], "aborted": []}

# Iterate through job URLs
for job in job_urls:
    response = requests.get(job["url"])
    if response.status_code == 200:
        data = response.json()
        builds = data["builds"][:20]

        # Initialize counters for the current job
        job_counts = {"pass": 0, "fail": 0, "aborted": 0}

        # Iterate through builds
        for build in builds:
            build_details_url = build["url"] + "api/json"
            build_response = requests.get(build_details_url)

            if build_response.status_code == 200:
                build_data = build_response.json()
                description = build_data["description"]
                result = build_data["result"]

                # Filter builds with specific description
                if description is not None:
                    if "Tier: dvqa, Test Suite: regression" in description:
                        if result == "SUCCESS":
                            job_counts["pass"] += 1
                        elif result == "FAILURE":
                            job_counts["fail"] += 1
                        elif result == "ABORTED":
                            job_counts["aborted"] += 1

        # Append the counts for the current job
        result_counts["pass"].append(job_counts["pass"])
        result_counts["fail"].append(job_counts["fail"])
        result_counts["aborted"].append(job_counts["aborted"])

# Plotting the results
results = list(result_counts.keys())
counts = list(result_counts.values())

# Generate a list of job names
job_names = [job["name"] for job in job_urls]

# Set the positions for the bars
bar_positions = np.arange(len(job_urls))

# Set the width of the bars
bar_width = 0.2

# Set the colors for each count
pass_color = "green"
fail_color = "red"
aborted_color = "grey"

# Plotting the clustered bar chart
plt.bar(bar_positions, counts[0], width=bar_width, label="Pass", color=pass_color)
plt.bar(
    bar_positions + bar_width,
    counts[1],
    width=bar_width,
    label="Fail",
    color=fail_color,
)
plt.bar(
    bar_positions + 2 * bar_width,
    counts[2],
    width=bar_width,
    label="Aborted",
    color=aborted_color,
)

# Add job names as x-axis labels
plt.xticks(bar_positions + bar_width, job_names)

# Labeling the chart
plt.xlabel("Job")
plt.ylabel("Count")
plt.title("Build Results by Job")
plt.legend()

# Display the chart
plt.show()
