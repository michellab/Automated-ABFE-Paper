"""Run calculations non-adaptively, running each window for 200 ps."""


def main() -> None:
    import a3fe as a3

    calc = a3.Calculation()
    calc.setup()
    calc.run(adaptive=False, runtime=0.2)
    calc.wait()
    calc.recursively_set_attr("_equilibrated", True)
    calc.recursively_set_attr("_equil_time", 0)
    calc.analyse()
    calc.analyse_convergence()
    results_df = calc.get_results_df()
    calc._dump()
    print(results_df)


if __name__ == "__main__":
    main()
