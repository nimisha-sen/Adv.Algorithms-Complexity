import csv
from csv_opener import open_csv_file
from job_sequencing import job_sequencing
from job_sequencing import get_length_of_first_column
'''
We have a csv with Reports Deadline and payment as columns

We use a quick sort algo to sort csv rows the basis of its length

Then we use greedy job sequencing algo to to process the most imp. legal doc first

We use a ?? algo for word processing
'''

'''CSV Tasks'''

# Function to get the length of the first column value
def get_length_of_first_column(row):
    return len(row[0])


# open main file (Before merge)
res = open_csv_file('notsorted_excel_legal.csv')
fields = res[0]
rows = res[1]


# Apply merge sort on rows based on length of first column ie Report length
sorted_rows = sorted(rows, key=get_length_of_first_column)

# Writing the sorted rows to new CSV file
# == Utilizes Sorting Algorithm and writes to a file ==
with open("LegalDocs_sorted_by_len.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(sorted_rows)

# Open the new file
res = open_csv_file('LegalDocs_sorted_by_len.csv')
fields = res[0]
rows = res[1]



# Perform Job Sequencing
'''
Utilize Job Sequencing Greedy algorithm such that it tells me which row to 
process first given the length of 1st column and maximizes the amount and minimizes deadline.
''' 
max_deadline_chosen = 3
selected_jobs, rejected_jobs = job_sequencing(rows,max_deadline_chosen)

#Display selected jobs
print("Selected Jobs which have deadline of " + str(max_deadline_chosen) + " days :")
for job in selected_jobs:
    print(job)

print("Rejected Jobs which have deadline of " + str(max_deadline_chosen) + " days :")
for job in rejected_jobs:
    print(job)


# Now I will classify from array how many times each word has appeared
to_find_word_arr = ['biotech','real-estate', 'house']

for job in selected_jobs:
    first_column_words = job[0].split() # We Assume words are separated by space
    word_count = {word: 0 for word in to_find_word_arr} # lambda func
    
    # lower() is used to convert to lower cases to avoid any mis matches
    for word in first_column_words:
        if word.lower() in to_find_word_arr:
            word_count[word.lower()] += 1 # we increment if found to be matching
    
    # Display first 128 chars in print
    print("\nWord count for job:", job[0:128])
    for word, count in word_count.items():
        print(f"{word}: {count} instances")


