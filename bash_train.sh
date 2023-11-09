#!/bin/bash
#SBATCH -J dm_train
#SBATCH --partition=gpu
#SBATCH --gres=gpu:a100-40g:1
#SBATCH -t 100:00:00

source activate dm_grid27

mkdir /gpfs/space/home/jesusjav/05_deepmind_setup/grid-cells/results/
python -B train.py --task_root='/gpfs/space/home/jesusjav/05_deepmind_setup/grid-cells/' --saver_results_directory='/gpfs/space/home/jesusjav/05_deepmind_setup/grid-cells/results/'