"""
Run calculations non-adaptively, running bound vanish windows for 8 ns
and all others for 6 ns.
"""


def main() -> None:
    import a3fe as a3

    calc = a3.Calculation()
    calc.setup()
    # Run the bound vanish leg for longer
    for leg in calc.legs:
        for stage in leg.stages:
            if (
                leg.leg_type == a3.LegType.BOUND
                and stage.stage_type == a3.StageType.VANISH
            ):
                stage.run(adaptive=False, runtime=8)
            else:
                stage.run(adaptive=False, runtime=6)
    calc.wait()

    # Set the equilibration time to 1 ns unless bound vanish, in which case 3 ns
    for leg in calc.legs:
        for stage in leg.stages:
            if (
                leg.leg_type == a3.LegType.BOUND
                and stage.stage_type == a3.StageType.VANISH
            ):
                for lam in stage.lam_windows:
                    lam._equilibrated = True
                    lam._equil_time = 3
            else:
                for lam in stage.lam_windows:
                    lam._equilibrated = True
                    lam._equil_time = 1

    calc.analyse()
    calc.analyse_convergence()
    results_df = calc.get_results_df()
    calc._dump()
    print(results_df)


if __name__ == "__main__":
    main()
