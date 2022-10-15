
# made by Andrea Leone

# this product is free to use

class objectList:
    
  Uobjects = []
  
  # init objectList function to the preimposted configuration  
  def __init__(self, Uinstance = [None]):
    
    for i in range(len(Uinstance)):
      
      if (str(type(Uinstance[i])) != "<type 'instance'>" or Uinstance[i] is None):
        
        raise Exception("Warning: invalid arguments")
        
      else:
        
        pass       
    
    self.Uobjects.extend(filter(None, Uinstance)) 
    
    # list of name objects in Uobjects list
    self.strUobjects = []
   
    # list of indexes in Uobjects list
    self.indexes = []              
    
    # find and pick all objects name in strUobjects list
    for i in range (len(self.Uobjects)):
       
     self.strUobjects.append(self.Uobjects[i].__class__.__name__) 
    
    # find and pick all objects index in Uobjects list 
    for i in range (len(self.Uobjects)):
       
     self.indexes.append(i)
     
 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
 
  def objectList(self, index = None, name = None, pickIndex = false):
   
   # check if index is not empty, is int and the name is empty
   if (index is not None and isinstance(index, int) and name is None and pickIndex is false):
   
   # check if index is between the positive and negative range of Uobjects list
     if (index >= len(self.Uobjects) or index < (len(self.Uobjects)*-1)):
     
       raise Exception("Warning: index out of range")
     
     else:
       
       return strUobjects[index]
       
   # check if index is empty and the name is empty
   elif (index is None and name is None and pickIndex is false):
         
     return self.strUobjects
   
   # check if index is empty and name is a string 
   elif (index is None and isinstance(name, str) == true and pickIndex is false):

     if (name in strUobjects):
     
       return name
      
     else:
     
       raise Exception("Warning: no object named in list")
       
   # check if index is empty and the name is empty and pickIndex is true
   elif (index is None and name is None and pickIndex is true):
     
     return self.indexes
   
   # check if index is empty and name is a string 
   elif (index is None and isinstance(name, str) == true and pickIndex is true):

     if (name in strUobjects):
       
       return strUobjects.index(name)
      
     else:
     
       raise Exception("Warning: no object named in list")
       
   # check if index is not empty and name is not empty
   elif (index is not None and name is not None):
   
     raise Exception("Warning: only one of the two arguments can be used (not both of them)")
   
   else:
     
     raise Exception("Warning: invalid argument in 'instanceList'.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  
  # function to add objects in the Uobjects list 
  def add(self, object = None):
    
    # check if the object type is in fact an object
    if (str(type(object)) == "<type 'instance'>"):
      
      self.Uobjects.append(object)
      self.Uobjects = list(filter(None, self.Uobjects))
      self.strUobjects.append(object.__class__.__name__)
      self.indexes.append(len(self.indexes))
      
    elif (object is None):
    
      raise Exception("Warning: invalid value 'None', must pass an object type value.")
      
    else:
    
      raise Exception("Warning: cannot pass a non class instance to 'objectList'.")


  def call(self, index = None):
    
    if (index is None):
    
      for i in range (len(self.Uobjects)):
      
        self.Uobjects[i].__run__()
        
      
    elif (isinstance(index, int) == true):
    
      if (index >= len(self.Uobjects) or index < (len(self.Uobjects)*-1)):
        
        raise Exception("Warning: index out of range")
       
      else:
    
        self.Uobjects[index].__run__()
      
    else:
    
      raise Exception("Warning: invalid index")

  
  def delete(self, index = None, name = None):
  
    if (isinstance(index, int) == true and name is None):
    
      self.Uobjects.pop(index)
      self.strUobjects.pop(index)
      self.indexes.pop()
      
    elif (index is None and isinstance(name, str) == true):
    
      if (name in self.strUobjects):
        
        self.Uobjects.pop(self.strUobjects.index(name))
        self.strUobjects.remove(name)
        self.indexes.pop()
#------------------------------------------------------