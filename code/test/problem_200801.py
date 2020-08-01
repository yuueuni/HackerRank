# Toss

"""
SELECT distinct user.id, concat(IFNULL(character.title, ""),character.job,' ',user.name)
FROM `user`, `character`
WHERE user.id = character.user_id
ORDER BY user.id DESC
"""

import json

def get_summary(data, target_value):
   answer = []
   for d in data:
      if d.get('value') == target_value:
         child_pk = d.get('pk') -1
         if not d.get('is_active'):
            return 'INACTIVE'
         break
   
   count = 0
   while count < 3:
      if data[child_pk].get('is_active'):
         answer.append(data[child_pk].get('value'))
         if child_pk == 0:
            break
         child_pk = data[child_pk].get('parent') -1
      else:
         return 'INACTIVE'
      count += 1
   
   if not answer:
      return 'INACTIVE'
   answer.reverse()
   answer = '>'.join(answer)
   return answer


input_value, target = input().split('/')
json_data = json.loads(input_value)
result = get_summary(json_data, target)
print(result)