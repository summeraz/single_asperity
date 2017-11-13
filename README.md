## Investigating Alkylsilane Monolayer Tribology at a Single-Asperity Contact with Molecular Dynamics Simulation
This repository contains initialization and run scripts associated with
systems from the above manuscript. The BibTeX citation for this manuscript is
provided below.
```
@article{doi:10.1021/acs.langmuir.7b02479,
author = {Summers, Andrew Z. and Iacovella, Christopher R. and Cummings, Peter T. and McCabe, Clare}, 
title = {Investigating Alkylsilane Monolayer Tribology at a Single-Asperity Contact with Molecular Dynamics Simulation},
journal = {Langmuir},
volume = {33},
number = {42},
pages = {11270-11280},
year = {2017},
doi = {10.1021/acs.langmuir.7b02479},
    note ={PMID: 28915731},
URL = {http://dx.doi.org/10.1021/acs.langmuir.7b02479},
eprint = {http://dx.doi.org/10.1021/acs.langmuir.7b02479}
}
```

## Details
Initialization scripts rely on the mBuild and Foyer packages, part of the MoSDeF
framework, which can be installed via Anaconda (or from source via Github).
Simulations were performed using the LAMMPS molecular dynamics simulation engine,
version 14 May 2016.

## Instructions
Instructions for creating an Anaconda environment for running these scripts are as
follows:
- Download and install Anaconda (https://www.continuum.io/downloads)
- Update conda
  * `>> conda update conda`
  * `>> conda clean -i`
- Create a new conda environment (Python 3.5 is recommended)
  * `>> conda config --add channels omnia`
  * `>> conda config --add channels mosdef`
  * `>> conda create -y --name foo python=3.5 mdtraj mbuild foyer jupyter pytest`
- Activate the new environment
  * `>> source activate hack35`
- Clone the git repository
  * `>> git clone https://github.com/summeraz/single_asperity.git`
- Install the `single_asperity` Python package
  * `>> cd single_asperity`
  * `>> pip install .`
