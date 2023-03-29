### copiar a parte do código que executa o jest
fazer igual a biblioteca que passa isso.

substituir o runner padrao pelo meu runner adptado que troca a ordem
alterar so a configuração.

### save run contents

- Expected json: 

```json
// "test_session": 
{
    "project_infos": {
        "name": "name",
        "commit": 12312312
    },
    "tests_run_configurations": [
        {
            "type": "plain, stress",
            "id": "",
            "running_times": 1
        }
    ],
    "modulos": [
        {
            "nome_modulo": "nome",
            "test_cases": [
                {
                    "test_name": "test_name",
                    "test_result": "result",
                    "test_run_configuration_id": 12
                }
            ]
        }
    ]
}
```

stream version:

```json
{
    "project_name": "name",
    "project_commit": "commit",
    "tests_run_configurations_type": "plain",
    "tests_run_configurations_times": 12,
    "run_timer": 12,
    "nome_modulo": "name",
    "test_case_name": "name",
    "test_case_result": "result",
}
```

# 2- add karma tool
# 1- add jest tool