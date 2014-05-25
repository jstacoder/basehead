basehead
========

python wrapper for basecamp-next api

+++++++++++++++++++++++++++

to use:
  open basehead/core.py abd input your basecamp accout number, 
  to find it look in your url on basecamp
  
  also the code expects a file in the directory that the core.py 
  file is, called auth.txt
  
  this file should contain 
  
  BASECAMP_USERNAME
  BASECAMP_PASSWORD
  
  
  on two seperate lines just like that
  
  then open up ipython
  
  and:
  
  >>> from people import get_me
  >>> me = get_me() # me is all the data from the above users account
  
  
  or if you like objects
  
  >>> from basehead.basecamp import BaseCamper
  >>> bc = BaseCamper()
  
  now bc has all your account data
  
  more to come
