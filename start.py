import os

# Uses Winget to install programs.
def installing_programs():
  print("Installing Programs!")
  os.system("winget import -i ./programs.json")
  print("Done!")
  gathering_directory_info()

# Creates my directory structrue.
def gathering_directory_info():
  print("Making Directory Structure!")
  trevor_directory = input("Where would you like the Trevor directory? ")
  print(trevor_directory)

  def making_directory():
    os.system(f"cd {trevor_directory}")
    os.system("mkdir Trevor")
    os.system("cd Trevor")
    os.system("mkdir 3D Printer, Audiobooks, Coding, Documents, Downloads, Images Installer, MB Workbooks, Music, Other, ROMS, Unzipped ZIPS, Videos,VMs")
    print("Done making directories.")

  areYouSure = input("Are you sure this directory is correct? (y/n)")
  if areYouSure == "n" or "N":
    print("Run the script again with the correct path.")
    exit()
  
  if areYouSure != "y" or "Y" or "n" or "N":
    print("Invalid Response")

  else:
    making_directory()

installing_programs()