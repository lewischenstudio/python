score = int(input("Enter your student's score: "))

if score >= 90:
    print("Your student's grade is A and score is " + str(score) + ".")
else: # consider a score < 90
    if score >= 80:
        print("Your student's grade is B and score is " + str(score) + ".")
    else: # consider a score < 80
        if score >= 70:
            print("Your student's grade is C and score is " + str(score) + ".")
        else: # consider a score < 70
            if score >= 60:
                print("Your student's grade is D and score is " + str(score) + ".")
            else: # consider a score < 60, which is the same as saying if score < 60:
                print("Your student's grade is F and score is " + str(score) + ".")