class homework (object):
    def __init__(self,subject, teacher):
        self.sub=subject
        self.teach=teacher
    def __str___(self):
        return f"{self.sub=}"
    def how_many_tasks(self, for_page, pages):
        amount=for_page*pages
        return amount
    def marks(self,mark):
        if mark==5 or mark==4:
            return "great work"
        else:
            return "try better"
        
class task(homework):
    def hardness(self):
        if self.sub=="maths":
            self.percent=100
        else:
            self.percent=50
        return self.percent

hw1=homework("maths","Ivan")
print(hw1.teach,"gave us ",hw1.how_many_tasks(5,3),hw1.sub,"tasks to do") #Ivan gave us  15 maths tasks to do
print(hw1.teach,"said ",":,,",hw1.marks(5),"!''","after checking ",hw1.sub) #Ivan said  :,, great work !'' after checking  maths


hw2=task("maths","Elen")

print("hometask is" , hw2.hardness(), "% hard") #hometask is 100 % hard
print(hw2.teach,"gave us ",hw2.how_many_tasks(4,8),hw2.sub,"tasks to do") #Elen gave us  32 maths tasks to do
print(hw2.teach,"said ",":,,",hw1.marks(5),"!''","after checking ",hw2.sub) #Elen said  :,, try better !'' after checking  maths

