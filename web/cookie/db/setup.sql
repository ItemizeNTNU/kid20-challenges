CREATE TABLE Users(
  username VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(100),
  name VARCHAR(100),
  favmuppet VARCHAR(100),
  favsound VARCHAR(100)
);
INSERT INTO Users VALUES('admin', 'Man_Skulle_Tro_Jeg_Var_Mer_Kreativ :(', 'Cookie Monster','Cookie Monster', 'OMM-nom-nom-nom...'); 