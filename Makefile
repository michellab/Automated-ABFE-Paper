PACKAGE_NAME  := a3fe_reproduce
CONDA_ENV_RUN := conda run --no-capture-output --name $(PACKAGE_NAME)

ANALYSIS_NBS := $(wildcard analysis/*.ipynb)

.PHONY: env test-analysis

env:
	mamba create     --name $(PACKAGE_NAME)
	mamba env update --name $(PACKAGE_NAME) --file devtools/envs/base.yaml
	$(CONDA_ENV_RUN) pip install --no-build-isolation --no-deps git+https://github.com/michellab/a3fe.git

test-analysis:
	$(CONDA_ENV_RUN) jupyter nbconvert --to notebook --execute $(ANALYSIS_NBS)
