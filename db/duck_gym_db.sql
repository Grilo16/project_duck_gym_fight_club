DROP TABLE IF EXISTS ducks_in_classes;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS ducks;

CREATE TABLE ducks (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    attack INT,
    defense INT,
    health INT
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    duration INT

);

CREATE TABLE ducks_in_classes (
    id SERIAL PRIMARY KEY,
    duck_id INT REFERENCES ducks(id) ON DELETE CASCADE NOT NULL,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE NOT NULL,
    UNIQUE (duck_id, gym_class_id)
    
);