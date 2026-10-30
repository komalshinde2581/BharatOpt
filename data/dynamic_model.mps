NAME          LOCAL_MODEL
ROWS
 N  OBJ
 L  Labor_Capacity
 L  Chip_Stock
 L  Cleanroom
 G  Min_Tablets
COLUMNS
    Laptops    OBJ        1200.0
    Laptops    Labor_Capacity 8.0
    Laptops    Chip_Stock 2.0
    Laptops    Cleanroom  1.8
    Servers    OBJ        4200.0
    Servers    Labor_Capacity 18.0
    Servers    Chip_Stock 8.0
    Servers    Cleanroom  6.5
    Smartphones OBJ        410.0
    Smartphones Labor_Capacity 2.5
    Smartphones Chip_Stock 1.0
    Smartphones Cleanroom  0.5
    Tablets    OBJ        620.0
    Tablets    Labor_Capacity 4.0
    Tablets    Chip_Stock 1.0
    Tablets    Cleanroom  0.9
    Tablets    Min_Tablets 1.0
RHS
    RHS1      Labor_Capacity 1800.0
    RHS1      Chip_Stock 2200.0
    RHS1      Cleanroom  950.0
    RHS1      Min_Tablets 60.0
BOUNDS
 LO BND       Laptops    0.0
 LO BND       Servers    0.0
 LO BND       Smartphones 0.0
 LO BND       Tablets    0.0
ENDATA