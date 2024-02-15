'''
IBEHS 1P10 Mini Milestone 7 Main File

Team Number: 47

Student 1 Details (Maaz Ghazi, 400456045):
Student 2 Details (Aditya Diwan, 400454725):
Student 2 Details (Imran Chowdhary, 400470828):

Date: November 15, 2022
'''

""" GIVEN Functions """
## This function calculates the gear ratio of your gearing mechanism
## This is a repeat of Mini-Milestone 6 (CP3), Objective #1
def calc_GR(gear_list1, gear_list2):
    ratio1 = gear_list1[-1] / gear_list1[0]
    ratio2 = gear_list2[-1] / gear_list2[0]
    gear_ratio = ratio1 * ratio2
    return gear_ratio

## This function calculates the pitch diameter (in mm) for a set of gears
## This is a repeat of Mini-Milestone 6 (CP3), Objective #2
def calc_PD(gear_list, module):
    pitch_diameter_list = []
    for gear in gear_list:
        pitch_diameter_list.append(gear * module)
    return pitch_diameter_list

## This function calculates the center distance (in mm) between input and output for a set of gears
## This is a repeat of Mini-Milestone 6 (CP3), Objective #3
def calc_CD(pitch_diameter_list):
    center_distance = 0
    for gear in pitch_diameter_list:
        center_distance += gear
    center_distance -= (pitch_diameter_list[0])/2
    center_distance -= (pitch_diameter_list[len(pitch_diameter_list)-1])/2
    return center_distance




##Student ID: (400454725)
'''
COPY ALL FUNCTIONS REQUIRED FOR OBJECTIVE 1 IN THE SPACE BELOW
'''
## CODE GOES HERE

def verify_gear_ratio(GR, gear_listFL, gear_listSL1, gear_list_SL2):

   Gr_FF= calc_GR(gear_listFL, gear_listSL1)
   GR_TH= calc_GR(gear_listFL, gear_list_SL2)

   if Gr_FF == GR:
        FF_Boolean= True
   else:
        FF_Boolean= False

   if GR_TH == GR:
        Thumb_Boolean= True
   else:
        Thumb_Boolean= False

   return ([FF_Boolean,Thumb_Boolean])

##Student ID: (400456045 and 400470828)
'''
COPY ALL FUNCTIONS REQUIRED FOR OBJECTIVE 2 IN THE SPACE BELOW
'''
## CODE GOES HERE

def verify_center_distance(module, first_lvl, forefinger, thumb):
    x = []
    first_lvl_CD = 42
    forefinger_CD = 42
    thumb_CD = 36
    

    calc_first_lvl = calc_CD(first_lvl)
    calc_forefinger = calc_CD(forefinger)
    calc_thumb = calc_CD(thumb)

    if calc_first_lvl == first_lvl_CD:
        x.append(True)
    else:
        x.append(False)

    if calc_forefinger == forefinger_CD:
        x.append(True)
    else:
        x.append(False)

    if calc_thumb == thumb_CD:
        x.append(True)
    else:
        x.append(False)

    return x

##Main Function

'''
ADD MAIN FUNCTION IN THE SPACE BELOW TO COMPLETE PROGRAM
'''
## CODE GOES HERE

def main():
    gear_ratio= (56/9)
    gear_listFL=[12, 20, 32]
    gear_listSL1=[12, 11, 11, 28]
    gear_listSL2=[12, 16, 28]
    module = 1


    objective_1 = verify_gear_ratio(gear_ratio, gear_listFL, gear_listSL1, gear_listSL2)
    print("Aditya Diwan","\n") 
    print("The calculated Forefinger Gear Ratio is:","\t", objective_1[0])
    print("The calculated Thumb Gear ratio is:","\t", (objective_1[1]),"\n")
    
    objective_2 = verify_center_distance(module, gear_listFL, gear_listSL1, gear_listSL2)
    print ("Maaz Ghazi & Imran Chowdhury", "\n")
    print("Calculated the first level center distance:","\t", (objective_2[0]))
    print ("Calculated the forefinger center distance:","\t", (objective_2[1]))
    print ("Calculated the thumb center distance:","\t", (objective_2[2]))
    return()



#Add function call here (main)
main()
