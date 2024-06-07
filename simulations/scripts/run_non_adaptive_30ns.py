"""Run calculations non-adaptively, running each window for 0.2 ns"""


def main() -> None:
    import a3fe as a3

    calc = a3.Calculation()
    calc.setup()
    calc.run(adaptive=False, runtime=0.2)
    calc.wait()
    calc.set_attr_values("_equilibrated", True)
    calc.set_attr_values("_equil_time", 0)
    calc.analyse()
    calc.analyse_convergence()
    results_df = calc.get_results_df()
    calc._dump()
    print(results_df)


if __name__ == "__main__":
    main()