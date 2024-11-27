from src.file_converter import convert_txt_to_csv
from config.constants import Contants

# :: Specify the path to the file
txt_file_path = "datasets/raw/qs.census2007.txt"

# :: Specify the path where you want to save the .csv file
output_dir = Contants.OUTPUT_DIR

# :: Convert the .txt file to a .csv file
convert_txt_to_csv(txt_file_path, output_dir)
