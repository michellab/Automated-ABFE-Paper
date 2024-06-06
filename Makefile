PACKAGE_NAME  := a3fe_reproduce
CONDA_ENV_RUN := conda run --no-capture-output --name $(PACKAGE_NAME)

ANALYSIS_DIRS := $(wildcard analysis/*)
ANALYSIS_NBS := $(wildcard $(ANALYSIS_DIRS)/*analysis.ipynb)
ANALYSIS_OUTPUT_DIRS := $(ANALYSIS_DIRS:%=%/final_analysis)

.PHONY: env test-analysis clean

env:
	mamba create     --name $(PACKAGE_NAME)
	mamba env update --name $(PACKAGE_NAME) --file devtools/envs/base.yaml
	$(CONDA_ENV_RUN) pip install --no-build-isolation --no-deps git+https://github.com/michellab/a3fe.git

test-analysis:
	$(CONDA_ENV_RUN) jupyter nbconvert --to notebook --execute $(ANALYSIS_NBS)

clean:
	# Remove all pngs in the analysis output directories
	find $(ANALYSIS_OUTPUT_DIRS) -name '*.png' -type f -delete
	# Remove all .tex files in the analysis output directories
	find $(ANALYSIS_OUTPUT_DIRS) -name '*.tex' -type f -delete
	# Clean all the notebooks
	nb-clean clean $(ANALYSIS_NBS)
	# Remove any .nbconvert.ipynb notebooks
	find $(ANALYSIS_DIRS) -name '*.nbconvert.ipynb' -type f -delete
