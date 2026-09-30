# claude-deneme

## nozzle.py

İdeal gaz için choked (tıkanmış) lüle akışında kütle debisini hesaplar.
`choked_mass_flow(P0, T0, gamma, R, A_throat)` fonksiyonu SI birimlerinde
(Pa, K, -, J/(kg·K), m²) girdi alır ve kg/s cinsinden debi döndürür.
Dosyanın sonunda hava için örnek bir hesap vardır: `python nozzle.py`
