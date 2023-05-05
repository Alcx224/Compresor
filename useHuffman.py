from logicahuffman import HuffmanCoding
import tkinter as tk
from tkinter import filedialog
import shutil
import os

root = tk.Tk()
root.withdraw()

path = filedialog.askopenfilename()
src_path = path
dir_path = os.path.dirname(os.path.realpath(__file__))
shutil.copy(src_path, dir_path)
h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)