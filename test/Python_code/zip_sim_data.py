# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:53:03 2023

@author: Campbell
"""

import shutil

top_data_folder = '../sim_data'
output_file_name = '../sim_data/zipped_archive.zip'

shutil.make_archive(output_file_name, 'zip', top_data_folder)