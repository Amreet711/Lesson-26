student_data={"lucy":78,"aaral":84,"airlie":87,"kailah":92,"amreet":98}
total=0
for value in student_data.values():
    total = total + value
average=total/len(student_data)
print(f"Class Average: {average}")
check=input("Please enter the name of the student who's grade you wish to see: ")
print(student_data.get(check,"This student does not exist. Please try another name."))
student_data2 = {val: key for key, val in student_data.items()}
highest_score=max(student_data.values())
lowest_score=min(student_data.values())
print("The Highest Score: ", highest_score)
print("The Highest Scorer: ", student_data2.get(highest_score))
print("The Lowest Score: ", lowest_score)
print("The Lowest Scorer: ", student_data2.get(lowest_score))