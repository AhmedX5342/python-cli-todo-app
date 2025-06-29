import json
import math
from datetime import datetime


with open('tasks.json','r') as file:
  data = json.load(file)

# -------------------------------------------------
def viewTasks():
  print('')
  print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
  print('-------------------------------------------------------------------------------------')
  for task in data['tasks']:
    if task['priority']=="HIGH":
      print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
    else:
      print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')

def is_valid_date(date_str):
  try:
    datetime.strptime(date_str, "%d/%m/%Y")
    return True
  except ValueError:
    return False

def addTask():
  print('-------------------------------------------------------------------------------------')
  title = input('enter task title: ').strip()
  dueDate = input('enter task due date (dd/mm/yyyy): ')
  if (is_valid_date(dueDate)==False):
    print('please enter a valid due date (dd/mm/yyyy)')
    return
  
  priority = input('enter task priority (LOW,MEDIUM,HIGH): ').upper()
  if (priority== "LOW" or priority== "MEDIUM" or priority== "HIGH"):
    pass
  else:
    print('please enter a valid priority (LOW,MEDIUM,HIGH)')
    return
  
  category = input('enter task category (work,personal,study): ').lower()
  if (category== "work" or category== "personal" or category== "study"):
    pass
  else:
    print('please enter a valid category (work,personal,study)')
    return

  # adding task to JSON file
  newTask =  {"id":len(data['tasks'])+1,"title":title,"dueDate":dueDate,"priority":priority,"category":category,"done":"False", "created":datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
  
  data['tasks'].append(newTask)
  
  with open('tasks.json', 'w') as file:
    json.dump(data, file, indent=2)
    
  print('task added successfully')

def modifyTask():
  print('')
  print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
  print('-------------------------------------------------------------------------------------')
  for task in data['tasks']:
    print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
  print('')
  
  # ----- selecting row
  secondInput = math.floor(int(input(f'enter the ID of the task you wish to modify (1-{len(data['tasks'])}): ')))
  
  if(secondInput>=0 and secondInput<=len(data['tasks'])):
    print('-------------------------------------------------------------')
  else:
    print(f'please enter a valid id (1-{len(data['tasks'])})')
  
  # ----- selecting column
  print(f'editing task "{data['tasks'][secondInput-1]['title']}"')
  print('1: Title\n2: Due Date\n3: Priority\n4: Category\n5: Completed')
  thirdInput = math.floor(int(input(f'enter the column you wish to modify (1-5): ')))
  if(thirdInput>0 and thirdInput<=5):
    pass
  else:
    print('please enter a valid number (1-5)')
    return
  
  # ----- editing column
  match thirdInput:
    case 1: # title
      fourthInput = input('please enter the new title: ')
      data['tasks'][secondInput-1]['title']=fourthInput
    case 2: # due date
      fourthInput = input('please enter the new due date (dd/mm/yyyy): ')
      if (is_valid_date(fourthInput)==False):
        print('please enter a valid due date (dd/mm/yyyy)')
        return
      data['tasks'][secondInput-1]['dueDate']=fourthInput
    case 3: # priority
      fourthInput = input('please enter the new priority (LOW,MEDIUM,HIGH): ')
      if (fourthInput== "LOW" or fourthInput== "MEDIUM" or fourthInput== "HIGH"):
        pass
      else:
        print('please enter a valid priority (LOW,MEDIUM,HIGH)')
        return
      data['tasks'][secondInput-1]['priority']=fourthInput
    case 4: # category
      fourthInput = input('please enter the new category (work,study,personal): ')
      if (fourthInput== "work" or fourthInput== "personal" or fourthInput== "study"):
        pass
      else:
        print('please enter a valid category (work,personal,study)')
        return
      data['tasks'][secondInput-1]['category']=fourthInput
    case 5: # done
      if(data['tasks'][secondInput-1]['done']=="True"):
        data['tasks'][secondInput-1]['done']="False"
      else:
        data['tasks'][secondInput-1]['done']="True"

  with open('tasks.json', 'w') as file:
    json.dump(data, file, indent=2)
    
  print('task modified successfully')

def deleteTask():
  print('')
  print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
  print('-------------------------------------------------------------------------------------')
  for task in data['tasks']:
    print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
  print('')
  
  # ----- selecting row
  secondInput = math.floor(int(input(f'enter the ID of the task you wish to delete (1-{len(data['tasks'])}): ')))
  
  if(secondInput>=0 and secondInput<=len(data['tasks'])):
    deleted_task = data['tasks'].pop(secondInput-1)
    with open('tasks.json', 'w') as file:
      json.dump(data, file, indent=4)
      
    print(f'successfully deleted "{deleted_task['title']}"')
  else:
    print(f'please enter a valid id (1-{len(data['tasks'])})')

def completeTask():
  print('')
  print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
  print('-------------------------------------------------------------------------------------')
  for task in data['tasks']:
    print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
  print('')
  
  # ----- selecting row
  secondInput = math.floor(int(input(f'enter the ID of the task you wish to complete/uncomplete (1-{len(data['tasks'])}): ')))
  
  if(secondInput>=0 and secondInput<=len(data['tasks'])):
    if(data['tasks'][secondInput-1]['done']=="True"):
      data['tasks'][secondInput-1]['done']="False"
      print(f'successfully uncompleted "{data['tasks'][secondInput-1]['title']}"')
    else:
      data['tasks'][secondInput-1]['done']="True"
      print(f'successfully completed "{data['tasks'][secondInput-1]['title']}"')

    with open('tasks.json', 'w') as file:
      json.dump(data, file, indent=4) 
  else:
    print(f'please enter a valid id (1-{len(data['tasks'])})')

def filterTasks():
  secondInput = math.floor(int(input('1: filter by status\n2: filter by priority\n3: filter by category\nenter 1-3: ')))
  if(secondInput>0 and secondInput<=3):
    match secondInput:
      case 1: # filter by status
        print('')
        print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
        print('-------------------------------------------------------------------------------------')
        for task in data['tasks']:
          if (task['done']=="False"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
        for task in data['tasks']:
          if (task['done']=="True"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
      case 2: # filter by priority
        print('')
        print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
        print('-------------------------------------------------------------------------------------')
        for task in data['tasks']:
          if (task['priority']=="HIGH"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
        for task in data['tasks']:
          if (task['priority']=="MEDIUM"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
        for task in data['tasks']:
          if (task['priority']=="LOW"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
      case 3: # filter by category
        print('')
        print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
        print('-------------------------------------------------------------------------------------')
        for task in data['tasks']:
          if (task['category']=="study"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
        for task in data['tasks']:
          if (task['category']=="work"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
        for task in data['tasks']:
          if (task['category']=="personal"):
            if task['priority']=="HIGH":
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
            else:
              print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')

def searchTasks():
  secondInput = input('search title: ').strip()
  print('')
  print('|  ID  |  Title  |  Due Date  |  Priority  |  Category  |  Completed  | Created at  |')
  for task in data['tasks']:
    if secondInput in task['title']:
      print('-------------------------------------------------------------------------------------')
      if task['priority']=="HIGH":
        print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  \033[91m{task['priority']}\033[0m  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
      else:
        print(f'|  {task['id']}  |  {task['title']}  |  {task['dueDate']}  |  {task['priority']}  |  {task['category']}  |  {task['done']}  |  {task['created']} ')
# -------------------------------------------------
# try:
while True:
  print('-------------------------------------------------------------------------------------')
  firstInput = input("1: view tasks \n2: add task\n3: modify tasks\n4: delete tasks\n5: complete task\n6: filter\n7: search\n\nEnter choice 1-7, 'q' to quit ")

  if firstInput.strip()=='1':
    viewTasks()
  if firstInput.strip()=='2':
    addTask()
  if firstInput.strip()=='3':
    modifyTask()
  if firstInput.strip()=='4':
    deleteTask()
  if firstInput.strip()=='5':
    completeTask()
  if firstInput.strip()=='6':
    filterTasks()
  if firstInput.strip()=='7':
    searchTasks()
  if firstInput.strip()=='q':
    print('exited')
    break

# except:
#   print('\nexited')