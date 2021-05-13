# shaker-action

This action uses [shaker](shaker) in your GitHub workflow to detect flakiness. If the job ends in failure, flakes were detected and errors will be reported.

We have support to projects that use `maven` or `pytest`.

## Default Usage (copy and past it in your workflow)

```yaml
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v2.3.4
  - name: Shaker
    uses: STAR-RG/shaker-action@main
    with:
      testing_tool: maven  # or pytest
```
### If you don't have any workflow

Just criate a `.yml` file under the folder `.github/workflows` and create a event triger to run shaker:

```yaml
# main.yml - This is a basic workflow to help you get started with Actions 

name: CI

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
        uses: STAR-RG/shaker-action@main
        with:
          testing_tool: maven  # or pytest
```


## All parameters

```yaml
# Checks-out your repository under $GITHUB_WORKSPACE so Shaker can access it
- uses: actions/checkout@v2.3.4
- name: Shaker
  uses: STAR-RG/shaker-action@main
  with:
    # Testing tool
    # Currently supported tools: pytest, maven
    # Required
    # Example: testing_tool: maven
    testing_tool: ""

    # Extra arguments
    # Optional
    # Example: extra_arguments: -q
    extra_arguments: ""

    # Number of no-stress runs
    # Optional, default: 1
    # Example: no_stress_runs: "1"
    no_stress_runs: ""

    # Number of stress runs
    # Optional, default: 3
    # Example: stress_runs: "3"
    stress_runs: ""
```



### TODO
- [ ] Add support to Android (Doing).
- [ ] Add support to Java with gradle.
