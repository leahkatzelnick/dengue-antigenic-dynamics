import os
import numpy as np
import random
from itertools import product
import sys

clade_resolution = sys.argv[1]
antigenic_resolution = sys.argv[2]

frequency_path = './source/southeast_asia_%s_frequencies.csv'%(clade_resolution)
titer_path = './source/%s_Dij.csv'%antigenic_resolution
out_path = './southeast_asia/%s/%s/'%(clade_resolution, antigenic_resolution)

beta_vals = np.linspace(0,3,8)
gamma_vals = np.linspace(0,2,8)
sigma_vals = np.linspace(0,3,8)

for (b,g,s) in product(beta_vals, gamma_vals, sigma_vals):
	name = ''.join(random.choice('0123456789abcdef') for n in xrange(30))
	cmd = 'python ./antigenic_fitness.py --frequency_path %s --titer_path %s --out_path %s --name %s --years_back 2 --years_forward 5 --beta %f --gamma %f --sigma %f --DENV4_f0 0'%(frequency_path, titer_path, out_path, name, b,g,s)

	os.system('sbatch -t 20:00:00 --wrap="%s"'%cmd)
	os.system('sleep 0.05')
