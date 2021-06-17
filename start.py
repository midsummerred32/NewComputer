import os
import trevor_directory

#Asks if you want to install programs.
def start():
  doYouWantPrograms = input("Would you like to install programs? (y/n) ")
  if doYouWantPrograms == "n" or "N":
    startDirectory()
  
  elif doYouWantPrograms == "y" or "Y":
    installing_programs()
    
  else:
    print("Invalid Response")


# Uses Winget to install programs.
def installing_programs():
  print("Installing Programs!")
  os.system("winget import -i ./programs.json")
  print("Done!")
  making_directory()

# Asks if you want Trevor Folder.
def startDirectory():
  doYouWantTrevorFolder = input("Would you like to make the Trevor Folder? (y/n) ")
  
  if doYouWantTrevorFolder == "y" or "Y":
    making_directory()
  
  elif doYouWantTrevorFolder == "n" or "N":
    exit(code="Python Script is Done!")
    
  else:
    print("Invalid Response")

# Creates my directory structrue.
def making_directory():
  print("Making Directory Structure!")
  print(trevor_directory.directory)
  os.chdir(trevor_directory.directory)
  os.system("mkdir Trevor")
  os.chdir(".\Trevor")
  os.system("mkdir 3D_Printer, Audiobooks, Coding, Documents, Downloads, Images, Installers, MB_Workbooks, Music, Other, ROMS, Unzipped_ZIPS, Videos, VMs")
  print("Done making directories.")
  exit(code="Python Script is Done!")



start()