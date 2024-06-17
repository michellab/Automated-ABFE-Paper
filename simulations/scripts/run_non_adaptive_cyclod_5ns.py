"""
Run calculations using the protocol for the Cyclophilin D non-adaptive runs.
This involves 5 ns of simulation time per window, with 1 ns discarded to equilibration,
and a linear lambda schedule.
"""


def main() -> None:
    import a3fe as a3

    calc = a3.Calculation()

    # Set lambda values other than the defaults
    cfg = a3.SystemPreparationConfig()
    leg_lam_vals = {
        a3.StageType.RESTRAIN: [
            0.0,
            0.01,
            0.025,
            0.05,
            0.075,
            0.1,
            0.15,
            0.2,
            0.35,
            0.5,
            0.75,
            1.0,
        ],
        a3.StageType.DISCHARGE: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        a3.StageType.VANISH: [
            0.0,
            0.05,
            0.1,
            0.15,
            0.2,
            0.25,
            0.3,
            0.35,
            0.4,
            0.45,
            0.5,
            0.55,
            0.6,
            0.65,
            0.7,
            0.75,
            0.8,
            0.85,
            0.9,
            0.95,
            1.0,
        ],
    }
    cfg.lambda_values = {a3.LegType.BOUND: leg_lam_vals, a3.LegType.FREE: leg_lam_vals}
    calc.setup(bound_leg_sysprep_cfg=cfg, free_leg_sysprep_cfg=cfg)

    # Run
    calc.run(adaptive=False, runtime=5)
    calc.wait()

    # Analyse
    calc.recursively_set_attr("_equilibrated", True)
    calc.recursively_set_attr("_equil_time", 1)
    calc.analyse()
    calc.analyse_convergence()
    results_df = calc.get_results_df()
    calc._dump()
    print(results_df)


if __name__ == "__main__":
    main()
