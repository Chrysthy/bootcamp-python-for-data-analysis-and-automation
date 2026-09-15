# Pokémon TCG Database 🃏

A PostgreSQL database project created to practice relational database concepts using Pokémon TCG cards and collections as the main theme.
The project stores information about Pokémon cards, their collections, types, and evolution stages while using relationships between tables through foreign keys.

---

## 📌 About the Project

This project simulates a relational database for managing Pokémon TCG cards.

Instead of storing all information in a single table, the data is separated into different tables for:

- Cards
- Collections
- Pokémon types
- Pokémon stages

The tables are connected using **Primary Keys** and **Foreign Keys**, creating a structured relational database.

---

## 🎯 Objective

The main goal of this project is to practice PostgreSQL and relational database concepts, including:

- Creating databases and tables
- Defining data types
- Primary Keys
- Foreign Keys
- Table relationships
- `CREATE TABLE`
- `INSERT INTO`
- `SELECT`
- `COUNT`
- Seed data
- Database organization
- Basic database normalization

---

## 🗃️ Database Structure

The database contains four main tables.

### `tbl_collections`

Stores information about Pokémon TCG collections.

---

### `tbl_types`

Stores the Pokémon card types.


Examples:

- Fire
- Water
- Grass
- Lightning
- Psychic
- Fighting
- Colorless

---

### `tbl_stages`

Stores the Pokémon evolution stages.

Examples:

- Basic
- Stage 1
- Stage 2

---

### `tbl_cards`

Stores the Pokémon TCG cards and connects them to collections, types, and stages.


---

## 🔗 Relationships

The `tbl_cards` table contains three Foreign Keys:

```sql
FOREIGN KEY (collection_id)
REFERENCES tbl_collections(id);

FOREIGN KEY (type_id)
REFERENCES tbl_types(id);

FOREIGN KEY (stage_id)
REFERENCES tbl_stages(id);


## 🛠️ Technologies 

- PostgreSQL 
- SQL 
- Git 
- GitHub