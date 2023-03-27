[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5347973.svg)](https://doi.org/10.5281/zenodo.5347973)

# shaker

This action uses [shaker](shaker) in your GitHub workflow to detect flakiness. If the job ends in failure, flakes were detected and errors will be reported.

Shaker supports projects using `jest`, `maven` or `pytest`.

## Usage

Add the following code to your GitHub Actions workflow configuration

```yaml
# Checks-out your repository under $GITHUB_WORKSPACE so Shaker can access it
- uses: actions/checkout@v2.3.4
- name: Shaker
  uses: STAR-RG/shaker@main
  with:
    # Tool
    # Currently supported tools: maven, pytest
    # Required
    # Example: testing_tool: maven
    tool: "maven"

    # Pass extra arguments to the tool
    # Optional
    # Example: extra_arguments: -DModule.skip.tests=true
    extra_arguments: ""

    # Number of Shaker runs
    # Optional, default: 3
    # Example: runs: "3"
    runs: "3"
    
    tests_command: "yarn test"
```

## Inputs

| Input | Description |
| --- | --- |
| `tool` | Specifies the tool required to run the tests. Currently supported: `maven` and `pytest`. |
| `extra_arguments` | Optional. Passes extra arguments to the testing tool. For example, you can pass `-DModule.skip.tests=true` to tell Maven to skip a certain module. |
| `runs` | Optional, default: 3. Specifies how many times Shaker will run. |

# Examples


## Jest example 

- ./shaker-js/shaker/shaker.py --stress-runs 1 --no-stress-runs 1 jest "react-styleguidist" --tests-command "yarn test:jest"
- ./shaker-js/shaker/shaker.py --stress-runs 1 --no-stress-runs 1 jest "react-hook-form" --tests-command "yarn test"
- ./shaker-js/shaker/shaker.py --stress-runs 1 --no-stress-runs 1 jest "jests-tests-example" --tests-command "yarn test" --output-folder "jests-tests-example/output"


## Karma example

- ./shaker-js/shaker/shaker.py --stress-runs 1 --no-stress-runs 1 karma "react-helmet" --tests-command "yarn test"

To see examples [visit our website](https://star-rg.github.io/shaker/).


## Github actions example
1 -  Fork the repository (it can be any project of yours).
    - git clone your fork or your own project.
2- Into the project, create a folder called .github/workflows.
    - mkdir -p .github/workflows
3 - Create a file .yml, for example main.yml.
    - touch .github/workflows/main.yml


4 - Write the action that runs Shaker in the .yml file :

```yml
name: CI # This is a basic workflow to help you get started with Actions 

# Controls when the action will run. 
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      - name: Java tests
        uses: STAR-RG/shaker@main
        with:
          tool: maven
          runs: 3
```


and

```shell
git add .github
git commit -m "add shaker action"
git push


git commit --allow-empty -m "empty commit to trigger the action"
git push
```

### TODO:

- Reaproveitar a imagem do ubuntu utilizada
