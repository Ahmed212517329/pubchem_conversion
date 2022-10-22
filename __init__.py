
def help():
  print("Here are several conversion function to use these function follow these instruction \n ")
  print("You should know what domain  do you have Ex: if you have  cid compound whcih is 964 \n ")
  print("You should know what domain <namespace> do you have Ex: if have cid compound whcih is 964d \n ")
  print("You should know what domain <operation specification> do you have Ex: do you want get name for this compound cid which is 964\n ")
  print("Assume you have cid compound, which is 964, and you want to get molecule name for this cid 964 \n " )
  print("In this case you write in your code \n")
  print("import cu.chem"  "    then type  this code \n")
  print( "cu.chem.ConversionPubchem.compoundcidtoname(964)"" \n ")
help()



"""### **General function which allows fro user to choose their output formal and operation and operation options**"""

#ne or more cid to properties cvs file
def generalpubchemconversion(inputsoecification, inputoperationsoecification,operationsoecification , outputwithoperationoption,*d):
  #input soecification,You have input formula and you want to get other formula ex compound, substance..assay, .....

  #input domain: type of your input identifer Ex cid or aid or sid, fastsmilarity...

  #input soecification: convert to other formula Ex record, description, assaysummary, sids, cids,aids,synonyms....
  #operation:
  #output with operation option Ex: xml, cvs,png,....
  #*input data: Ex list of cid, aid,sid, name,smiles, formula molecule........
  w=str(inputsoecification)
  p=str(inputoperationsoecification)
  h=str(operationsoecification)
  ut=str(outputwithoperationoption)
  #print(type(d))
  strrl=[]# to save list to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
      
  f= ",".join(strrl)
  a   = w +"/"+ p +"/"+ f+"/"+h+'/' + ut
  url     = str("https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + a)
  print(url)
##generalpubchemconversion("compound" ,"cid","sids","xml",["963","1","77"])

"""**compound name conversion**"""

#ne or more cid to properties cvs file
def compoundnametoproperty(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
      
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
compoundnametoproperty()

def compoundnametorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url  = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
      
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/record/xml

def compoundnametosynonyms(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametosynonyms()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/synonyms/xml

def compoundnametoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url) 
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
compoundnametoaid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/aids/xml



def compoundnametoassaysummary(*d):
 #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametoassaysummary()

def compoundnametoclassification(*d):
 #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")


compoundnametoclassification()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/classification/xml



def compoundnametodescription(*d):
 #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametodescription()

def compoundnametosid(*d):
 #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametosid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/sids/xml

def compoundnametocid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametocid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/cids/xml



def compoundnametoconformer(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametoconformer()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/conformers/xml

def compoundnametopng(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to0 make one file
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/name/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "png" 
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/name/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "png" 
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")

compoundnametopng()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/water/png



"""## **compound cid conversion**"""

#ne or more cid to properties cvs file
def compoundcidtoproperty(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str or int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
      
      print(url)
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
          print(url)
    if type(x) is int :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
    if type(x) is float :
      print("Try again, incorrect value enter, you should enter string name or string name list Ex:" "water" "or" "[""water"",""butane""]")
compoundcidtoproperty()





def compoundcidtorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
    print(url)
compoundcidtorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180,964/record/xml



def compoundcidtosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
    print(url)
compoundcidtosynonym(float(18))
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180,964/synonyms/xml

def compoundcidtosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)

compoundcidtosid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180/sids/xml

def compoundcidtoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
    print(url)

compoundcidtoaid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180,964/aids/xml

def compoundcidtoassay(*d):
  ##print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
    print(url)

compoundcidtoassay()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180,964/assaysummary/xml

def compoundcidtoclassification(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
    print(url)

compoundcidtoclassification()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180/classification/xml

def compoundcidtodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
compoundcidtodescription()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/190,180/description/xml

def compoundcidtoconformers(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
    
    f= ",".join(strrl)
    pugin   = "compound/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
    print(url)

compoundcidtoconformers()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/180,190=/conformers/xml

"""### **compound smile**"""

#ne or more cid to properties cvs file
def compoundsmiletoproperty(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + "/property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + "/"+ "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletoproperty()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/CO/property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D/xml



def compoundsmiletorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/cco/record/xml

def compoundsmiletosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletosynonym()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/synonyms/xml

def compoundsmiletosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletosid()

def compoundsmiletocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletocid()

def compoundsmiletoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletoaid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/aids/xml

def compoundsmiletoassaysummary(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletoassaysummary()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/assaysummary/xml



def compoundsmiletoclassification(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletoclassification()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/classification/xml

def compoundsmiletodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletodescription()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/description/xml

def compoundsmiletoconformers(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")
compoundsmiletoconformers()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/description/xml

def compoundsmiletopng(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/smiles/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "png"
      print(url)
    elif type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/smiles/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "png"
          print(url)
    else:
      print(" Incorrect enter value, Try agin with Sting smiles or string smiles list as" "co" "or " "[co"",""cn]")

compoundsmiletopng()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/co/png



"""### ***fastidentity ***"""

def compoundfastidenitycidtocid(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
          print(url)

compoundfastidenitycidtocid()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

#{smiles | smarts | inchi | sdf | cid}

def compoundfastidenitycidtosid(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
          print(url)

compoundfastidenitycidtosid()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

#{smiles | smarts | inchi | sdf | cid}

#@title Default title text
def compoundfastsimilarity_2dcidThreshold95(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastsimilarity_2d/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/cids/txt?Threshold=95'
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastsimilarity_2d/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/cids/txt?Threshold=95'
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          pugin   = "compound/fastsimilarity_2d/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/cids/txt?Threshold=95'
          print(url)

compoundfastsimilarity_2dcidThreshold95()#one cid per requests
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_2d/cid/190/cids/txt?Threshold=95

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_2d/cid/180/cids/txt?Threshold=95

def compoundfastidenitycidtoaid(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
          print(url)

compoundfastidenitycidtoaid()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

#{smiles | smarts | inchi | sdf | cid}

def compoundfastidenitycidtoassaysummary(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
          print(url)

compoundfastidenitycidtoassaysummary()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

#{smiles | smarts | inchi | sdf | cid}

def compoundfastidenitycidtosynonyms(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
          print(url)

compoundfastidenitycidtosynonyms()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

#{smiles | smarts | inchi | sdf | cid}

"""### **fastsimilarity_2d **"""

def compoundfastsimilarity_2dtocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

#compoundfastsimilarity_3dtocid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_2dtosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/sid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

compoundfastsimilarity_2dtosid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_2dtoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
              print(url)

compoundfastsimilarity_2dtoaid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_2dtorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
              print(url)

compoundfastsimilarity_2dtorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_2dtosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
              print(url)

compoundfastsimilarity_2dtosynonym()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_2dtodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
              print(url)

compoundfastsimilarity_2dtodescription()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def tocompoundfastsimilarity_2dtoconformer(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_2d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
              print(url)

tocompoundfastsimilarity_2dtoconformer()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



"""### **fastsimilarity_3d **"""

def compoundfastsimilarity_3dtocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

compoundfastsimilarity_3dtocid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_3dtosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
              print(url)

compoundfastsimilarity_3dtosid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_3dtoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
              print(url)

compoundfastsimilarity_3dtoaid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_3dtorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
              print(url)

compoundfastsimilarity_3dtorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_3dtosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
              print(url)

compoundfastsimilarity_3dtosynonym()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_3dtodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
              print(url)

compoundfastsimilarity_3dtodescription()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsimilarity_3dtoconformer(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsimilarity_3d/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
              print(url)
#compoundfastsimilarity_3dtocompoundfastsimilarity_3dtoconformer()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

"""### **compound identity cid **"""

#ne or more cid to properties cvs file#################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def compoundidentitycidtoproperty(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/identity/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
    print(url)
compoundidentitycidtoproperty()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/BPGDAMSIGCZZLK-UHFFFAOYSA-N/SDF

def compoundidentitycidtodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/identity/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
compoundidentitycidtodescription()

def compoundidentitycidtoconformer(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/identity/cid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
    print(url)
compoundidentitycidtoconformer()

def compoundfastidenitycidtosid(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
          print(url)

compoundfastidenitycidtosid()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

def compoundfastidenitycidtoaid(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
          print(url)

compoundfastidenitycidtoaid()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

def compoundfastidenitycidtosynonyms(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
          print(url)

compoundfastidenitycidtosynonyms()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml

def compoundfastidenitycidtoassaysummary(*d):
  #print(type(d))
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)
    if type(x) is int:
      #print("s")
      x=str(x)
      strrl.append(x)
      pugin   = "compound/fastidentity/cid/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          print(x)
          pugin   = "compound/fastidentity/cid/" + x
          url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
          print(url)

compoundfastidenitycidtoassaysummary()# accept one cid pers request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/180/cids/xml



def compoundsimilaritytocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "compound/similarity/cid/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"  +pugin + '/' + "xml"
    print(url)

compoundsimilaritytocid()##one request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/similarity/cid/2244/XML

def compoundidentitytocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "compound/identity/cid/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"  + '/' +pugin+ '/' + "xml"
    print(url)

compoundidentitytocid()#one request

"""# **compound inchikey**"""

def compoundinchikeytorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/inchikey/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record/xml" 
    print(url)
compoundinchikeytorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/record/xml/xml

def compoundinchikeytosynonym(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/inchikey/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
    print(url)
compoundinchikeytosynonym()#many inchikey per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/synonyms/xml

def compoundinchikeytosid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "compound/inchikey/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)
compoundinchikeytosid()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N,XLYOFNOQVPJJNP-UHFF/sids/xml

def compoundinchikeytoaid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

      f= ",".join(strrl)
      pugin   = "compound/inchikey/" + f
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)
compoundinchikeytoaid()#many inchikey per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N,IJDNQMDRQITEOD-UHFFFAOYSA-N/aids/xml





def compoundinchikeytoassaysummary(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "compound/inchikey/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
    print(url)
compoundinchikeytoassaysummary()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/assaysummary/xml



def compoundinchikeytocid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
      f= ",".join(strrl)
      pugin   = "compound/inchikey/" + f
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
      print(url)
compoundinchikeytocid()#many inchikey per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N,IJDNQMDRQITEOD-UHFFFAOYSA-N/cids/xml

def compoundinchikeytoclassification(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "compound/inchikey/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
    print(url)
compoundinchikeytoclassification()#<Details>Output of classifications is not currently supported for multiple CIDs</Details>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/classification/xml

def compoundinchikeytodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/inchikey/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
compoundinchikeytodescription()# many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N,XLYOFNOQVPJJNP-UHFF/description/xml

def compoundinchikeytoconformers(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    for i in strrl:
      pugin   = "compound/inchikey/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
      print(url)
compoundinchikeytoconformers()# one per reqesut
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/XLYOFNOQVPJJNP-UHFFFAOYSA-N/conformers/xml

def compoundsubstructuretocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

compoundsubstructuretocid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsubstructuretoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
              print(url)

compoundsubstructuretoaid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsubstructuretorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
              print(url)

compoundsubstructuretorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsubstructuretosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
              print(url)

compoundsubstructuretosynonym()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsubstructuretodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "C" + '/' + "xml"
              print(url)

compoundsubstructuretodescription()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsubstructuretoconformer(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
              print(url)

compoundsubstructuretoconformer()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsubstructuretocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/substructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

compoundsubstructuretocid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



"""### **cell**

"""

def cellcellacctoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "cell/cellacc/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'aids/' + "xml"
    print(url)
cellcellacctoaid()#<Message>operation `aids` only supports for one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/cellacc/CVCL_0045/aids/xml

def cellcallacctosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "cell/cellacc/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'summary/' + "xml"
    print(url)
cellcallacctosummary()#many callacc per time
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/cellacc/CVCL_0045,CVCL_0045/summary/xml

def cellsynyomtoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "cell/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'aids/' + "xml"
    print(url)
cellsynyomtoaid() #<Message>operation `aids` only supports for one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/synonym/HeLa/aids/xml

def cellsynyomtoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  
    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "cell/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'summary/' + "xml"
    print(url)
cellsynyomtoaid() #<Message>operation `aids` only supports for one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/synonym/HeLa/aids/xml

def cellsynyomtosummary(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "cell/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'summary/' + "xml"
    print(url)
cellsynyomtosummary() #<`synonym` only supports one entry a time>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/cell/synonym/HeLa/aids/xml

"""### **taxonomy**"""

def taxonomytaxidtosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "taxonomy/taxid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  "summary/xml"
    print(url)
taxonomytaxidtosummary()# support mnny entery
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/taxonomy/taxid/9606,9606/summary/xml

def taxonomytaxidtoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "taxonomy/taxid/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  "aids/xml"
    print(url)
taxonomytaxidtoaid() #operation `aids` only supports for one entry a time
##https://pubchem.ncbi.nlm.nih.gov/rest/pug/taxonomy/taxid/9606/aids/xml

def taxonomysynonymtosummary(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "taxonomy/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'summary/' + "xml"
    print(url)
taxonomysynonymtosummary()#idNamespace `synonym` only supports one entry a time
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/taxonomy/synonym/9606/summary/xml

def taxonomysynonymtoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
  
    pugin   = "taxonomy/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  'aids/' + "xml"
    print(url)
taxonomysynonymtoaid()#<Message>idNamespace `synonym` only supports one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/taxonomy/synonym/9606/aids/xml

"""### *pathway*"""

def pathwaypwacctosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "pathway/pwacc" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/'  + "/summary/JSON"
    print(url)
pathwaypwacctosummary()# support many enter per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/pathway/pwacc/Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983//summary/JSON

def pathwaypwacctoaccessions(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "pathway/pwacc" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/'  + "/accessions/JSON"
    print(url)
pathwaypwacctoaccessions()#many per requests
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/pathway/pwacc/Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983//accessions/JSON

def pathwaypwacctogeneids(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "pathway/pwacc/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/'  + "geneids/JSON"
    print(url)
pathwaypwacctogeneids()#many per requests
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/pathway/pwacc/Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983,Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983//geneids/JSON

def pathwaypwacctocids(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "pathway/pwacc/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/'  + "cids/JSON"
    print(url)
pathwaypwacctocids()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/pathway/pwacc/Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983,Reactome:R-HSA-70171,BioCyc:HUMAN_PWY-4983/cids/JSON

"""### **substance **"""

#ne or more cid to properties cvs file
def substancesidtorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin   + '/reocrdrecord' + "xml"
    print(url)
substancesidtorecord()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123656,123656//xml

def substancessidtosynonym(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
    print(url)
substancessidtosynonym()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123656,123656/synonyms/txt

def substancessidtorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
    print(url)
substancessidtorecord()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123656,123656/record/xml

def substancessidtocid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
    print(url)
substancessidtocid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/53789435/cids/xml

def substancesidtodescription(*d):#<Message>There is no longer a formal description for substances.</Message>

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
substancesidtodescription()
##https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123656,123656/description/xml

def substancesidtoclassification(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "substance/sid/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
    print(url)
substancesidtoclassification()#<Details>Output of classifications is not currently supported for multiple SIDs</Details>

def substancesidtoassaysummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
    print(url)
substancesidtoassaysummary()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123656,123656/assaysummary/xml

def substancesidtosid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)
substancesidtosid()#
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/123656,123656/sids/xml

#ne or more cid to properties cvs file#######################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def substancesourceidtocid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "substance/sourceid/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
      print(url)
substancesourceidtocid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/cids/txt

def substancessourceidtosynonyms(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "substance/sourceid/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
      print(url)
substancessourceidtosynonyms()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/synonyms/txt

def substancessourceidtorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "substance/sourceid/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
      print(url)
substancessourceidtorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/record/xml

"""# *protein** **"""

def proteinaccessiontosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
  
    f= ",".join(strrl)
    pugin   = "protein/accession/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "summary" + '/' + "xml"
    print(url)
proteinaccessiontosummary()#many per request
##https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/accession/P00533,P01422/summary/JSON

def proteinaccessiontoaids(*d):#donedoesnt work
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
  
    pugin   = "protein/accession/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
    print(url)
proteinaccessiontoaids() #operation `aids` only supports for one entry a time
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/accession/P00533,P01422/summary/JSON

def proteinaccessiontoconcise(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
  
    f= ",".join(strrl)
    pugin   = "protein/accession/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "concise" + '/' + "xml"
    print(url)
proteinaccessiontoconcise()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/accession/P01422/concise/xml

def proteingitosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "protein/gi/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "summary" + '/' + "xml"
    print(url)
proteingitosummary()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/gi/116516899,116516899/summary/xml

def proteingitoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)

  for x in strrl:
  

    pugin   = "protein/gi/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
    print(url)
proteingitoaid()#operation `aids` only supports for one entry a time</Message>
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/gi/116516899/aids/xml

def proteingitoconcise(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
  
    pugin   = "protein/gi/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "concise" + '/' + "xml"
    print(url)
proteingitoconcise()#<Message>operation `concise` only supports for one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/gi/116516899,116516899/concise/xml

def proteinsynonymtoaids(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "gene/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
    print(url)
proteinsynonymtoaids()#<Message>idNamespace `synonym` only supports one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/synonym/EGFR/aids/xml

def proteinsynonymtosummary(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
    pugin   = "gene/synonym/" + x
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "summary" + '/' + "xml"
    print(url)
proteinsynonymtosummary()#<Message>idNamespace `synonym` only supports one entry a time</Message>
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/synonym/EGFR/summary/xml

"""### ***gene***"""

def genegenesymboltosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "gene/genesymbol/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "summary" + '/' + "xml"
    print(url)
genegenesymboltosummary()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/gene/genesymbol/EGFR,EGFR/summary/xml

def genegenesymboltoaid(*d):#done
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for x in strrl:
      pugin   = "gene/genesymbol/" + x
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
      print(url)
genegenesymboltoaid()#<Message>operation `aids` only supports for one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/53789435/synonyms/TXT





"""### **assay**"""

def assaytargetgitosid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
  
    f= ",".join(strrl)
    pugin   = "assay/target/gi/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin +  '/' + "sids/xml"
    print(url)
assaytargetgitosid()#Assay record retrieval is limited to 10000 SIDs
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/gi/116516899,116516899/sids/xml

def assaytargetproteinnametorecord(*d):#done$$$$$$$$$$$$$$$$$$$$$$$$###############################
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/target/proteinname" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/'  + "xml"
    print(url)
assaytargetproteinnametorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/proteinname/mevalonatekinase,mevalonatekinase//xml

def assaytargetgeneidtorecord(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/target/geneid" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin  +  '/' + "xml"
    print(url)
assaytargetgeneidtorecord()#many per requests
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/geneid/1956,1956//xml

def assaytargetgenesymbolxml(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/target/genesymbol/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin +  '/' + "xml"
    print(url)
assaytargetgenesymbolxml()#many per requests
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/genesymbol/EGFR,EGFR//xml

def assaytargetaccession(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/target/accession/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  '/' + "xml"
    print(url)
assaytargetaccession()#manyper requests
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/target/accession/1956,13649//xml

def assaytypealltodescription(*d): #done##################@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/all/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypealltodescription()

def assaytypeconfirmatorytodescription(*d):#done##################@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/confirmatory/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypeconfirmatorytodescription()

def assayaidtodoseresponse(*d):#done##################@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "doseresponse" + '/' + "xml"
    print(url)
assayaidtodoseresponse()

def assaytypedoeresponsetodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/doseresponse/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypedoeresponsetodescription()

def assaytypeonholdtodescription(*d):#done##################@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/onhold/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypeonholdtodescription()



def assaytypepaneltodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/panel/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypepaneltodescription()

def assaytypernaitodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/rnai/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypernaitodescription()

def assayscreeningtodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/screening/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assayscreeningtodescription()

def assaytypesummarytodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/summary/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypesummarytodescription()

def assaytypesummarytodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/biochemical/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypesummarytodescription()

def assaytypeinvivotodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/invivo/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypeinvivotodescription()

def assaytypeinvitrotodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/invitro/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypeinvitrotodescription()

def assaytypeactiveconcentrationspecifiedtodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/type/activeconcentrationspecified/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assaytypeactiveconcentrationspecifiedtodescription()

def assayactiveitytodate(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/activity/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "date" + '/' + "xml"
    print(url)
assayactiveitytodate()###No assays found with the given activity name

def assaysourcealltosid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)
assaysourcealltosid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/sourceall/DTP.NCI/sids/xml

def assayaidtocid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
    print(url)
assayaidtocid()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,964/cids/xml

def assayaidtorecord(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
    print(url)
  assayaidtorecord()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,2000/record/xml

def assayaidtotargetproteinGI(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "/targets/ProteinGI,ProteinName,GeneID,GeneSymbol" + '/' + "xml"
    print(url)
assayaidtotargetproteinGI()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,2548//targets/ProteinGI,ProteinName,GeneID,GeneSymbol/xml

def assayaidtorecord(*d):#done#Full-record Retrieval

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/record/'  + "xml"
    print(url)
assayaidtorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/100,200/xml

def assayaidtoconcise(*d):#done#Full-record Retrieval$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + "/concise/xml"
    print(url)
assayaidtoconcise()

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/100,2000/concise/xml

def assayaidtoxml(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)

  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' +  '/' + "xml"
    print(url)
assayaidtoxml()#many 
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,2000//xml

def assayaidtodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
assayaidtodescription()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/100,200/description/xml

def assayaidtodoseresponse(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "assay/aid/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "doseresponse" + '/' + "xml"
      print(url )
assayaidtodoseresponse()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000/doseresponse/xml



def assayaidtodate(*d):#done#####################$$$$$$$$$$$$$$$$$$$$$$$$$$
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "date" + '/' + "xml"
    print(url)
assayaidtodate()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/100,2000/date/xml

def assayaidtosid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)
assayaidtosid(())#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,980/sids/xml

def assayaidtocid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
    print(url)
assayaidtocid()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,986/cids/xml

def assayaidtorecord(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
    print(url)
assayaidtorecord()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/100,982/record/xml

def assayaidtoProteinGIProteinNameGeneIDGeneSymbol(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "/targets/ProteinGI,ProteinName,GeneID,GeneSymbol" + '/' + "xml"
    print(url)#many per request
assayaidtoProteinGIProteinNameGeneIDGeneSymbol()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,986//targets/ProteinGI,ProteinName,GeneID,GeneSymbol/xml

def assayaidtoconcise(*d):#done#Full-record Retrieval
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "assay/aid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + "/concise/xml"
    print(url)
assayaidtoconcise()#many per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1000,980/concise/xml

"""# compound formula 


"""

#ne or more cid to properties cvs file
def compoundformulatoproperty(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
    print(url)
compoundformulatoproperty()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/BPGDAMSIGCZZLK-UHFFFAOYSA-N/SDF

def compoundformulatosynonyms(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
  
    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
    print(url)
compoundformulatosynonyms()

def compoundformulatosids(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
    
    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)
compoundformulatosids()

def compoundformulatoaid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
    print(url)
compoundformulatoaid()

def compoundformulatoassaysummary(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
    print(url)
compoundformulatoassaysummary()

def compoundformulatoclassification(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
    print(url)
compoundformulatoclassification()

def compoundformulatodescription(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
compoundformulatodescription()

def compoundformulatodconformer(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/formula/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
    print(url)
compoundformulatodconformer()

"""## **fast search

### **fastsubstructure
"""

def compoundfastsubstructuretosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

compoundfastsubstructuretosid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsubstructuretoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
              print(url)

compoundfastsubstructuretoaid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsubstructuretorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
              print(url)

compoundfastsubstructuretorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsubstructuretosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
              print(url)

compoundfastsubstructuretosynonym()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsubstructuretodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
              print(url)

compoundfastsubstructuretodescription()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundfastsubstructuretoconformer(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "conformers" + '/' + "xml"
              print(url)

compoundfastsubstructuretoconformer()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml





"""### **fastsuperstructure**"""

def compoundfastsubstructuretocid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsubstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
              print(url)

compoundfastsubstructuretocid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml





def compoundfastsuperstructuretoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
    for i in strrl:
                pugin   = "compound/fastsuperstructure/cid/" + i
                url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
                print(url)

compoundfastsuperstructuretoaid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml





def compoundfastsuperstructuretosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsuperstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
              print(url)

compoundfastsuperstructuretosid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



def compoundfastsuperstructuretosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsuperstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
              print(url)

compoundfastsuperstructuretosynonym( )#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml





def compoundfastsuperstructuretorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsuperstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
              print(url)

compoundfastsuperstructuretorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml





def compoundfastsuperstructuretodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsuperstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
              print(url)

compoundfastsuperstructuretodescription()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



def compoundfastsuperstructuretoassaysummary(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/fastsuperstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
              print(url)

compoundfastsuperstructuretoassaysummary()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

"""### **structure search**"""

def compoundsuperstructuretoaid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/superstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
              print(url)

compoundsuperstructuretoaid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



def compoundsuperstructuretosid(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/superstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
              print(url)

compoundsuperstructuretosid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml





def compoundsuperstructuretosynonym(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/superstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
              print(url)

compoundfastsuperstructuretosynonym()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



def compoundsuperstructuretorecord(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/superstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record" + '/' + "xml"
              print(url)

compoundsuperstructuretorecord()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml



def compoundsuperstructuretodescription(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/superstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
              print(url)

compoundsuperstructuretodescription()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

def compoundsuperstructuretoassaysummary(*d):
  #print(type(d))
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
              pugin   = "compound/superstructure/cid/" + i
              url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
              print(url)

compoundsuperstructuretoassaysummary()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_3d/cid/180/cids/xml

"""inchi # **compound inchi **"""

#ne or more cid to properties cvs file
def compoundinchikeytoproperty(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:
      
    f= ",".join(strrl)
    pugin   = "compound/inchi/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
    print(url)
compoundinchikeytoproperty()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/BPGDAMSIGCZZLK-UHFFFAOYSA-N/SDF

def compoundlistkeytorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/InChI/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "record/xml" + '/' + "xml"
    print(url)
compoundlistkeytorecord()



def compoundlistkeytosynonym(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/InChI/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "synonyms" + '/' + "xml"
    print(url)  
compoundlistkeytosynonym()

def substancesourceidtocids(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "substance/sourceid/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
    print(url)
substancesourceidtocids()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/cids/xml

def substancesourceidtodescritption(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "substance/sourceid/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "description" + '/' + "xml"
    print(url)
substancesourceidtodescritption()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/description/xml

def substancesourceidtoclassification(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceid/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "classification" + '/' + "xml"
    print(url)
substancesourceidtoclassification()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/classification/xml

def substancesourceidtoassaysummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "substance/sourceid/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
    print(url)
substancesourceidtoassaysummary()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/assaysummary/xml

def substancessourceidtosids(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "substance/sourceid/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
      print(url)
substancessourceidtosids()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceid/DTP.NCI/747285/sids/xml

#compound fastsimilarity_2d cid()

#ne or more cid to properties cvs file#############################
def compoundfastsimilarity_2dcidtoproperty(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "compound/fastsimilarity_2d/cid/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids/xml"
      print(url)
compoundfastsimilarity_2dcidtoproperty()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastsimilarity_2d/cid/2244/property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D/xml

"""***substance***"""

#ne or more cid to properties cvs file
def substancesourcealltorecord(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/record' + '/' + "png"
    print(url)
substancesourcealltorecord()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sourceall//record/png

#ne or more cid to properties cvs file
def substancesourcealltosynonym(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/synonyms' + '/' + "png"
    print(url)
substancesourcealltosynonym()

#ne or more cid to properties cvs file
def substancesourcealltocid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/cids' + '/' + "png"
    print(url)
substancesourcealltocid()

#ne or more cid to properties cvs file
def substancesourcealltodescription(*d):

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/description' + '/' + "png"
    print(url)
substancesourcealltodescription()

#ne or more cid to properties cvs file
def substancesourcealltoclassification(*d):

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/classification' + '/' + "png"
    print(url)
substancesourcealltoclassification()

#ne or more cid to properties cvs file
def substancesourcealltoassaysummary(*d):

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/assaysummary' + '/' + "png"
    print(url)
substancesourcealltoassaysummary()

#ne or more cid to properties cvs file
def substancesourcealltosids(*d):

  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)

  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "substance/sourceall/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/sids' + '/' + "png"
    print(url)
substancesourcealltosids()

"""### **Tomrrow **

protein
"""

def proteintsynonymtosummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "protein/synonym/" + i
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "summary" + '/' + "xml"
      print(url)
proteintsynonymtosummary()#<Message>idNamespace `synonym` only supports one entry a time</Message>

#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/synonym/EGFR/summary/xml

def proteinsynonymtoaid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "protein/synonym/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "aids" + '/' + "xml"
    print(url)
proteinsynonymtoaid()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/synonym//aids/xml

def proteinsynonymtoconcise(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "protein/synonym/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "concise" + '/' + "xml"
    print(url)
proteinsynonymtoconcise()#<Message>idNamespace `synonym` only supports one entry a time</Message>

"""substance"""

def substancenametocid(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "substance/name/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "cids" + '/' + "xml"
    print(url)
substancenametocid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/water/cids/xml
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/glucose/cids/xml

def substancenametoassaysummary(*d):#done
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
      pugin   = "substance/name/" + f
      url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "assaysummary" + '/' + "xml"
      print(url)
substancenametoassaysummary()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/glucose/assaysummary/xml

def substancenametosid(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)
  for i in strrl:
    pugin   = "substance/name/" + i
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "sids" + '/' + "xml"
    print(url)
substancenametosid()#one per request
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/water/sids/xml

"""inchi # **compound inchi **"""

#ne or more cid to properties cvs file
def compoundinchikeytoproperty(*d):
  strrl=[]# to save list to make one file
  strr=[]# to save int or stir to make one file
  for x in d:
    if type(x) is str:
      #print("s")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)
  

    if type(x) is int:
      #print("n")
      x=str(x)
      strrl.append(x)
    f= ",".join(strrl)


    if type(x) is list:
      #print("l")
      for m in x:
          x=str(m)
          #print(x)
          strrl.append(x)

  if len(strrl)>0:

    f= ",".join(strrl)
    pugin   = "compound/inchi/" + f
    url     = "https://pubchem.ncbi.nlm.nih.gov/rest/pug" + '/' + pugin + '/' + "property/Title,MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChI,InChIKey,IUPACName,XLogP,ExactMass,MonoisotopicMass,TPSA,Complexity,Charge,HBondDonorCount,HBondAcceptorCount,RotatableBondCount,HeavyAtomCount,IsotopeAtomCount,AtomStereoCount,DefinedAtomStereoCount,UndefinedAtomStereoCount,BondStereoCount,DefinedBondStereoCount,UndefinedBondStereoCount,CovalentUnitCount,Volume3D,XStericQuadrupole3D,YStericQuadrupole3D,ZStericQuadrupole3D,FeatureCount3D,FeatureAcceptorCount3D,FeatureDonorCount3D,FeatureAnionCount3D,FeatureCationCount3D,FeatureRingCount3D,FeatureHydrophobeCount3D,ConformerModelRMSD3D,EffectiveRotorCount3D,ConformerCount3D,Fingerprint2D" + '/' + "xml"
    print(url)
compoundinchikeytoproperty()
#https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/BPGDAMSIGCZZLK-UHFFFAOYSA-N/SDF