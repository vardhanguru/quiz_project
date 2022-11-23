from question import Question
from data import question_data
from brain import Brain
import brain
ques_list=[]
count=0
for i in question_data:
    ques_list.append(Question(i["text"],i["answer"]))


m=Brain(ques_list)
while m.Questions_pending():
    if m.next_question():
        count+=1
print("your score is {}".format(count))
