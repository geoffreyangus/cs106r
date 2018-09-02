''' Student Data 
Breaks up student data into classes and presents in plots. 
'''
from csv import DictReader, DictWriter  
import numpy as np

class Student:
    ''' Class for one student in the course.  
    '''
    def __init__(self, row):
        self.email = row['email']
        self.class_name = row['class']
        self.name = row['name']

        self.exercises = {}
        self.projects = {}
        self.challenges = {}

        for key, value in row.iteritems():
            if 'Exercise' in key and not 'DRAFT' in key: 
                self.exercises[key] = (value == 'complete') 
            if 'Project' in key and not 'DRAFT' in key: 
                self.projects[key] = (value == 'complete') 
            if 'Challenge' in key and not 'DRAFT' in key: 
                self.challenges[key] = (value == 'complete') 
        
        self.exercise_completion = np.mean(self.exercises.values())
        self.project_completion = np.mean(self.projects.values())
        self.challenge_completion = np.mean(self.challenges.values())
    
    def to_dict(self):
        student_dict = {'email': self.email,
                        'class_name': self.class_name,
                        'name': self.name}
        student_dict.update(self.exercises)
        student_dict.update(self.projects)
        student_dict.update(self.challenges)
        return student_dict

class ClassData:  

    def __init__(self, completion_filename, contact_filename):
        with open(contact_filename, 'r') as contact_file:
            data = DictReader(contact_file)
            data = [row for row in data]
            bj_contact_data = {row['School Email (Bom Jesus)'].strip('"'): row for row in data}
            personal_contact_data = {row['Personal Email (The one that you will check)'].strip('"'): row for row in data}
            username_contact_data = {row['Username'].strip('"'): row for row in data}
        
        self.classes = {}
        self.students = {} 

        with open(completion_filename, 'r') as completion_file:
            raw_data = DictReader(completion_file)
            misses = 0
            for row in raw_data:
                email = row['email']
                if email in bj_contact_data:
                    row['class'] = bj_contact_data[email]['Class']
                elif email in personal_contact_data:
                    row['class'] = personal_contact_data[email]['Class']
                elif email in username_contact_data:
                    row['class'] = username_contact_data[email]['Class']
                else: 
                    misses += 1 
                    row['class'] = 'none'
                
                student = Student(row)
                self.classes.setdefault(student.class_name, {}).setdefault('students', []).append(student)
                self.students[student.email] = student
            print '------------------------------------------'
            print 'Found ', len(self.classes), ' classes.'
            print 'Found ', len(self.students), ' students.'
            print 'Found classes for ', int(100 - 100.0*misses / len(self.students)), '% of students'
                

    def output_student_data(self, filename):
        with open(filename, 'w') as output_file:
            fieldnames = self.students.values()[0].to_dict().keys()
            fieldnames.sort(reverse = True)
            writer = DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students.values():
                writer.writerow(student.to_dict()) 

    def output_class_data(self, filename):
        with open(filename, 'w') as output_file:
            fieldnames = ['name', 'num_students', 'exercises', 'projects', 'challenges']
            writer = DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            class_names = self.classes.keys()
            class_names.sort()
            for class_name in class_names:
                students = self.classes[class_name]['students']
                row = {'name': class_name, 
                       'num_students': len(students),
                       'exercises': round(np.mean([student.exercise_completion for student in students]), 3),
                       'projects': round(np.mean([student.project_completion for student in students]), 3),
                       'challenges': round(np.mean([student.challenge_completion for student in students]), 3)} 
                writer.writerow(row)


def main():
    completion_filename = './student_data/week6.csv'
    contact_filename = './student_data/contact.csv'
    data = ClassData(completion_filename, contact_filename)
    data.output_student_data('./student_data/week6_students.csv')
    data.output_class_data('./student_data/week6_classes.csv')

if __name__ == "__main__":
    main()