CREATE TABLE military_stats (
    Date DATE NOT NULL,
    tanks INT NOT NULL,
    apv INT NOT NULL,
    artillery INT NOT NULL,
    mlrs INT NOT NULL,
    aaws INT NOT NULL,
    aircraft INT NOT NULL,
    helicopters INT NOT NULL,
    uav INT NOT NULL,
    vehicles INT NOT NULL,
    boats INT NOT NULL,
    submarines INT NOT NULL,
    se INT NOT NULL,
    missiles INT NOT NULL,
    personnel INT NOT NULL
);

select * from military_stats;
drop * from military_stats;
