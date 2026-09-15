-- =============================================
-- Initial Seed - Pokémon TCG Database
-- =============================================


-- ---------------------------------------------
-- Collections
-- ---------------------------------------------

INSERT INTO tbl_collections (
    collectionSetName,
    releaseDate,
    totalCardsInCollection
)
VALUES
    ('Base Set', '1999-01-09', 102),
    ('Jungle', '1999-06-16', 64);


-- ---------------------------------------------
-- Types
-- ---------------------------------------------

INSERT INTO tbl_types (typeName)
VALUES
    ('Fire'),
    ('Water'),
    ('Grass'),
    ('Lightning'),
    ('Psychic'),
    ('Fighting'),
    ('Colorless');


-- ---------------------------------------------
-- Stages
-- ---------------------------------------------

INSERT INTO tbl_stages (stageName)
VALUES
    ('Basic'),
    ('Stage 1'),
    ('Stage 2');


-- ---------------------------------------------
-- Cards
-- ---------------------------------------------

INSERT INTO tbl_cards (
    hp,
    name,
    type_id,
    stage_id,
    info,
    attack,
    damage,
    weak,
    ressis,
    retreat,
    cardNumberInCollection,
    collection_id
)
VALUES
    (
        120,
        'Charizard',
        1,
        3,
        'Spits fire that is hot enough to melt boulders.',
        'Fire Spin',
        '100',
        'Water',
        'Fighting',
        '3',
        4,
        1
    ),
    (
        100,
        'Blastoise',
        2,
        3,
        'A brutal Pokémon with pressurized water jets.',
        'Hydro Pump',
        '40+',
        'Lightning',
        NULL,
        '3',
        2,
        1
    ),
    (
        40,
        'Pikachu',
        4,
        1,
        'When several of these Pokémon gather, their electricity can cause lightning storms.',
        'Thunder Jolt',
        '30',
        'Fighting',
        NULL,
        '1',
        58,
        1
    ),
    (
        40,
        'Bulbasaur',
        3,
        1,
        'A strange seed was planted on its back at birth.',
        'Leech Seed',
        '20',
        'Fire',
        NULL,
        '1',
        44,
        1
    );