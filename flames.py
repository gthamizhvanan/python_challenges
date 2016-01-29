"""FLAMES - Find Your Relationship - Its just a funny app"""
# Python 3
# FLAMES #
fn = input('Enter First Name  :')
ln = input('Enter Second Name :')

if fn.isalpha() and ln.isalpha():
  fn = fn.upper().replace(' ','')
  ln = ln.upper().replace(' ','')
  #print (fn)
  def findDiff(fn,ln):
   for i,j in enumerate(ln):
    for p,q in enumerate(fn):
     if j==q:
      fn = fn.replace(j,'',1)
      ln = ln.replace(j,'',1)
      break
   diffVal = len(fn)+len(ln)
   return diffVal

  intDiffLen = findDiff(fn,ln)
  ch         = intDiffLen - 1

  def findRelationShip(ch):
   l = ['F','L','A','M','E','S']
   for i,j in enumerate(l):
    if(len(l) == 1):
     return l
    else:
     t = ch % len(l)
     del l[t]
     if(len(l) > 1):
      alv = -(len(l)-t)
      if len(l[alv:]) >= 1:
       lv = l[alv:]
       fv = l[:alv]
       l = lv+fv
     else:
       return l

  lstFlames = {'F':'Friend','L':'Love','A':'Affection','M':'Marriage','E':'Enemy','S':'Sister'}
  lstRelFind = findRelationShip(ch)
  strRelFind = ''.join(lstRelFind)
  print (lstFlames[strRelFind])
else:
  print ("Invalid Name Entered, Just Try One More Time !!!")


