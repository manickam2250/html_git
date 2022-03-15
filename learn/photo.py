import requests
res=requests.get("https://thumbs.dreamstime.com/b/innovative-architecture-civil-engineering-plan-building-construction-project-creative-graphic-design-showing-concept-186913485.jpg")
with open("/home/manikam//Music/html/tamil_developer/college_task/college/departments/CIVIL/images/CIVIL.jpg","wb")as file1:
    file1.write(res.content)