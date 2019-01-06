
# implicit boolean tests: 'empty' instances yield False

#%%

print('-- None --')
if None:
  print('None')
if not None:
  print('not None')
  
print('-- numbers --')
if 0:
  print('3')
if -1:
  print('-1')
if 3:
  print('3')
if 0.0:
  print('0.0')
if -1.3:
  print('-1.3')

print('-- strings --')
if '':
  print('')
if 'a':
  print('a')

print('-- lists, tuples , dicts --')
if []:
  print('[]')
if [2]:
  print('[2]')
if ():
  print('()')
if (5):
  print('(5)')
if {}:
  print('{}')
if {'a': 3}:
  print({'a': 3})
  