def stripRemove(string,word):
    newSte= string.replace(word,"");
    return newSte.strip();
    
  
  

this="    Pakistan long live        "
print(stripRemove(this, "live"));
