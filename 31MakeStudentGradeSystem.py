# Problem-31---> Make a student grade system --> 
# Key Point --> name , number , grade(A,B,C) show 

class StudentGrade :
    def __init__(self,name='',score=0):
        self.name =name
        self.score =score
    def result(self):
        result ={"name":self.name,"score":self.score}
        
        if 360<=self.score<=400 :
            result['grade']='A'
        elif 320<=self.score<360 :
            result['grade']='B'
        elif 260<=self.score<320 :
            result['grade']='C'
        elif 200<=self.score<260 :
            result['grade']='D'
        elif 0<=self.score<200 :
            result['grade']='F'
        else :
            result='Something went is worng'
        return result

student1= StudentGrade('Tarek Hasan',50)
print(student1.result()) # {'name': 'Tarek Hasan', 'score': 50, 'grade': 'F'}

student2= StudentGrade('Barek Kasan',770)
print(student2.result()) # Something went is worng

student3= StudentGrade('Zarek Tia',370)
print(student3.result()) # {'name': 'Zarek Tia', 'score': 370, 'grade': 'A'}
