The following repository contains initialization and run scripts associated with
systems included in the paper "Invesigating Alkylsilane Monolayer Tribology at a
Single-Asperity Contact with Molecular Dynamics Simulation".

Initialization scripts rely on the mBuild and Foyer packages, part of the MoSDeF
framework, which can be installed via Anaconda (or from source via Github).

Instructions for creating an Anaconda environment for running these scripts are as
follows:
- Download and install Anaconda (https://www.continuum.io/downloads)
- Update conda
  `>> conda update conda`
  `>> conda clean -i`
- Create a new conda environment (Python 3.5 is recommended)
  `>> conda config --add channels omnia`
  `>> conda config --add channels mosdef`
  `>> conda create -y --name foo python=3.5 mdtraj mbuild foyer jupyter pytest`
- Activate the new environment
  `>> source activate hack35`
- Clone the git repository
  `>> git clone https://github.com/summeraz/single_asperity.git`
- Install the `single_asperity` Python package
  `>> cd single_asperity`
  `>> pip install .`

Simulations were performed using the LAMMPS molecular dynamics simulation engine,
version 14 May 2016.
