from cx_Freeze import  setup,Executable
#import cx Freeze
setup( name= "ventana",
           version= "0,1",
           description = "ventana",
       executables =[Executable("primos.py")],)
