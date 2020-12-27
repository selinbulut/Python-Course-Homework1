

list_ad= ['Mehmet', 'Ahmet', 'Ayşe' ]

list_soyad= ['Yılmaz', 'Çelik','Bulut']


check= False


for i in range(3): 
 for x in list_ad:
    kullanici_adi= input("Lütfen adınızı giriniz: ")

    soyadı= input("Lütfen soyadınızı giriniz: ")

    if kullanici_adi == x :
     for y in list_soyad:
      if soyadı == y :
        print("Welcome")
        check= True
        break
    else: 
      print('yeniden deneyiniz..')
    
 if not check :
    print("Lütfen daha sonra tekrar deneyiniz..")
  
    
course_list = []

lesson= input('lütfen seçtiğiniz dersleri giriniz..')
course_list.append(lesson)



if len(course_list) < 3 :
    print('En az 3 ders giriniz..')
    
elif len(course_list) > 5:
    print('En fazla 5 ders girebilirsiniz...')
        
else: 
    print('Dersleriniz kaydedildi...')
        
        
midterm_grade = int(input('Please enter midterm grade...'))
final_grade = int(input('please enter final grade...'))
project_grade = int(input('please enter project grade...'))

grades= {'Midterm Exam': midterm_grade, 'Final': final_grade, 'Project' : project_grade }

print(grades)

total_grades = (midterm_grade*0.3) + (final_grade*0.5) + (project_grade*0.2)

if total_grades >= 90:
    print('AA')
elif 70 <= total_grades < 90:
    print('BB')
elif 50 <= total_grades < 70:
    print('CC')
elif 30 <= total_grades < 50:
    print('DD')
elif total_grades <= 30:
    print('FF')