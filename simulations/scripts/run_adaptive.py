"""
Run calculations adaptively, with a runtime constant of 
0.0005 kcal^2 mol^-2 ns^-1 and with lambda windows spaced
with a thermodynamic speed of 2 kcal mol^-1.
"""


def main() -> None:
    import a3fe as a3

    # Set up
    calc = a3.Calculation()
    calc.setup()
    calc.recursively_set_attr("runtime_constant", 0.0005)

    # Get optimal lambda values
    # NOTE: Change reference_sim_cost to the cost of the bound leg of the MIF complex
    # on your GPUs.
    calc.get_optimal_lam_vals(
        delta_er=2, set_relative_sim_cost=True, reference_sim_cost=0.21
    )
    calc.wait()

    # Run
    calc.run(adaptive=True)
    calc.wait()
    calc.analyse()
    calc.analyse_convergence()
    results_df = calc.get_results_df()
    calc._dump()
    print(results_df)


if __name__ == "__main__":
    main()
