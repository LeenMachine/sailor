#!/usr/bin/env rnaediting

export PATH=$(dirname "$PWD")/src/py/:$PATH

cwl-runner --jobStore ./tmp ../src/cwl/rnaediting2strands.workflow.cwl workflow_pe.2strands.yml
