"""İdeal gaz için choked (tıkanmış) lüle akışı hesabı."""

import math


def choked_mass_flow(P0, T0, gamma, R, A_throat):
    """Choked flow kütle debisini döndürür [kg/s].

    mdot = A * P0 * sqrt(gamma / (R * T0)) * (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))

    Parametreler:
        P0: Durgunluk (toplam) basıncı [Pa]
        T0: Durgunluk (toplam) sıcaklığı [K]
        gamma: Özgül ısı oranı cp/cv [-]
        R: Özgül gaz sabiti [J/(kg*K)]
        A_throat: Boğaz alanı [m^2]
    """
    if P0 <= 0 or T0 <= 0 or R <= 0 or A_throat <= 0:
        raise ValueError("P0, T0, R ve A_throat pozitif olmalıdır.")
    if gamma <= 1:
        raise ValueError("gamma 1'den büyük olmalıdır.")
    exponent = (gamma + 1) / (2 * (gamma - 1))
    return (
        A_throat
        * P0
        * math.sqrt(gamma / (R * T0))
        * (2 / (gamma + 1)) ** exponent
    )


if __name__ == "__main__":
    # Örnek: hava, P0 = 1 MPa, T0 = 300 K, boğaz çapı 10 mm
    gamma = 1.4
    R = 287.0  # J/(kg*K)
    P0 = 1.0e6  # Pa
    T0 = 300.0  # K
    A = math.pi * (0.010 / 2) ** 2  # m^2

    mdot = choked_mass_flow(P0, T0, gamma, R, A)
    print(f"Choked kütle debisi: {mdot:.4f} kg/s")
