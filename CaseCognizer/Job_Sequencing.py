
def get_length_of_first_column(row):
    return len(row[0])


# Function to perform Job Sequencing Greedy algorithm
def job_sequencing(rows, max_deadline):
    # Sort the rows based on the length of the first column in descending order
    sorted_rows = sorted(rows, key=get_length_of_first_column, reverse=True)

    # Initialize variables for the schedule and set to store selected jobs
    schedule = [-1] * len(sorted_rows)
    job_set = set()
    rejected_jobs = []

    # Fill the schedule
    for row in sorted_rows:
        deadline = int(row[1])  # Assuming the deadline is in the second column
        if deadline <= max_deadline:
            for i in range(min(len(schedule) - 1, deadline - 1), -1, -1):
                if schedule[i] == -1:
                    schedule[i] = tuple(row)  # Convert the list to a tuple
                    job_set.add(tuple(row))   # Convert the list to a tuple
                    break
        else:
            rejected_jobs.append(tuple(row))

    return list(job_set), rejected_jobs