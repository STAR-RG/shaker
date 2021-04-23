from colorama import Fore, Style, init


def print_failures(failures, no_stress_runs, stress_runs, config_size):
    print("")

    total_runs = no_stress_runs + (stress_runs * config_size)

    for module in failures:
        print(
            f"==== Failure in module {Fore.RED}{Style.BRIGHT}{module}{Fore.RESET}{Style.RESET_ALL} ===="
        )

        for test_case in failures[module]:
            print(f"{'':<5}> at {Fore.GREEN}{Style.BRIGHT}{test_case}{Style.RESET_ALL}")

            function_failures = failures[module][test_case]

            no_stress_failures = 0
            stress_failures = 0
            descriptions = set()

            for failure in function_failures:
                if failure["config"] == "no-stress":
                    no_stress_failures += 1
                else:
                    stress_failures += 1

                descriptions.add(failure["description"])

            if no_stress_runs > 0:
                perc_of_no_stress_runs = (no_stress_failures / total_runs) * 100
                print(
                    f"{'':<7}No stress failures: {no_stress_failures} ({perc_of_no_stress_runs:.2f}%)"
                )

            if stress_runs > 0:
                perc_of_stress_runs = (stress_failures / total_runs) * 100
                print(
                    f"{'':<7}Stress failures: {stress_failures} ({perc_of_stress_runs:.2f}%)"
                )

            total_failures = no_stress_failures + stress_failures
            perc_of_total_failures = (total_failures / total_runs) * 100
            print(
                f"{'':<7}Total failures: {total_failures} ({perc_of_total_failures:.2f}%)"
            )

            print(f"\n{'':<7}> Descriptions: {Fore.RED}{Style.BRIGHT}")
            for description in descriptions:
                for line in description.split("\n"):
                    print(f"{'':<9}{line}")
                print(Style.RESET_ALL)

    """import json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(failures, f, ensure_ascii=False, indent=4)"""
