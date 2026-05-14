import time


def solve_problem_746() -> int:
    MOD: int = 1000000007
    N_LIMIT: int = 2021
    MAX_VAL: int = 4 * N_LIMIT + 1

    # Precompute factorials and inverse factorials
    fact: list[int] = [1] * MAX_VAL
    inv_fact: list[int] = [1] * MAX_VAL
    for i in range(1, MAX_VAL):
        fact[i] = (fact[i - 1] * i) % MOD
    inv_fact[MAX_VAL - 1] = pow(fact[MAX_VAL - 1], MOD - 2, MOD)
    for i in range(MAX_VAL - 2, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    # Added type hints to n and r, and the return type -> int
    def nCr_mod(n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    # Precompute inverses for the block placement formula
    inv: list[int] = [0] * MAX_VAL
    for i in range(1, MAX_VAL):
        inv[i] = pow(i, MOD - 2, MOD)

    # Precompute powers of 4
    pow4: list[int] = [1] * (N_LIMIT + 1)
    for i in range(1, N_LIMIT + 1):
        pow4[i] = (pow4[i - 1] * 4) % MOD

    total_s: int = 0
    for n in range(2, N_LIMIT + 1):
        m_n_val: int = 0
        for k in range(n + 1):
            nk: int = 0
            if k == 0:
                nk = (fact[2 * n] * fact[2 * n]) % MOD
            else:
                # N(k) calculation
                # Number of ways to place k non-overlapping blocks of 4 in 4n seats
                ways_blocks: int = (4 * n * nCr_mod(4 * n - 3 * k, k)) % MOD
                ways_blocks = (ways_blocks * inv[4 * n - 3 * k]) % MOD

                nk = (ways_blocks * fact[k]) % MOD
                nk = (nk * pow4[k]) % MOD
                nk = (nk * fact[2 * n - 2 * k]) % MOD
                nk = (nk * fact[2 * n - 2 * k]) % MOD

            term: int = (nCr_mod(n, k) * nk) % MOD
            if k % 2 == 1:
                m_n_val = (m_n_val - term) % MOD
            else:
                m_n_val = (m_n_val + term) % MOD

        # M(n) = 2 * (Inclusion-Exclusion Sum)
        total_s = (total_s + 2 * m_n_val) % MOD

    return total_s % MOD


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_746()
    end = time.perf_counter()

    print(f"Result of problem 746 is {result}.")
    print(f"Finished in {end - begin} seconds.")

    assert result == 867150922, "The result is wrong"
