basehead
========

python wrapper for basecamp-next api
-------------------------------------


to use:
  open basehead/core.py abd input your basecamp accout number, 
  to find it look in your url on basecamp
  
  also the code expects a file in the directory that the core.py 
  file is, called auth.txt
  
  this file should contain 
  
  BASECAMP_USERNAME<br />
  BASECAMP_PASSWORD
  
  
  on two seperate lines just like that
  
  then open up ipython
  
  and:
  <pre>
  [in]: from people import get_me
  [out]: me = get_me() # me is all the data from the above users account
  </pre>
  
  or if you like objects
  <pre>
  [in]: from basehead.basecamp import BaseCamper
  [out]: bc = BaseCamper()
  </pre>
  now bc has all your account data
  
  more to come
