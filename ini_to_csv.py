import os
import csv





def extract_smelly_class_mapping(dir, ini_file):
   smell = ini_file.split('.')[0]
   lines = [line.strip() for line in open(os.path.join(os.path.dirname(__file__), dir, ini_file), 'r')]

   count = 1
   class_list = []

   while True:
      samples = [l for l in lines if l.startswith(str(count) + '.')]
      if len(samples) < 2:
         break

      class_list.append(samples[1].split('=')[1].strip())
      count = count + 1


   return {smell: class_list}

def parse_ini_in_dir(dir):
   smell_files = {}
   directory = os.path.join(os.path.dirname(__file__), dir)
   for root,dirs,files in os.walk(directory):
      for file in files:
         if file.endswith(".ini"):
            smell_files.update(extract_smelly_class_mapping(dir, file))

   return smell_files



def write_class_smells_to_csv(tag, smells_dict):
   smells_list = smells_dict.keys()
   class_wise_smell_list = []

   all_class_list = sum(smells_dict.values(), [])  #flatten list of lists

   for class_id in all_class_list:

      class_wise_smell_list.append(
         {"class": class_id } | dict((smell, 1 if class_id in classes else 0) for smell, classes in smells_dict.items())
      )



   keys = class_wise_smell_list[0].keys()

   dir = os.path.join(os.path.dirname(__file__),  "output", tag.split('#')[0])
   if not os.path.exists(dir):
      os.makedirs(dir)
   with open(os.path.join(dir, tag.split('#')[1].replace(".", "_") + '.csv'), 'w', newline='')  as output_file:
       dict_writer = csv.DictWriter(output_file, keys)
       dict_writer.writeheader()
       dict_writer.writerows(class_wise_smell_list)




for dirpath, dirnames, filenames in os.walk("raw"):
   for project in dirnames:
      for dirpath2, dirnames2, filenames2 in os.walk(os.path.join(os.path.dirname(__file__), dirpath, project)):
         for release in dirnames2:
            # print(project + '#' + release)
            # print(os.path.join(os.path.dirname(__file__), dirpath2, release))
            write_class_smells_to_csv(project + '#' + release, parse_ini_in_dir(os.path.join(os.path.dirname(__file__), dirpath2, release)))