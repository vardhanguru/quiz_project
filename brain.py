class Brain:
    def __init__(self,lists):
        self.question_number=0
        self.question_list=lists
    def Questions_pending(self):
        return self.question_number<len(self.question_list)
    def next_question(self):
        curr_question=self.question_list[self.question_number]
        self.question_number+=1
        input_from_user=input("Q.{} is {} True/False?".format(self.question_number,curr_question.text))
        # print(self.question_list[self.question_number].)
        return curr_question.answer==input_from_user