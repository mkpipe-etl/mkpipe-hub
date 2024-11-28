# PostgreSQL Extractor

This plugin allows you to extract data from PostgreSQL databases into `mkpipe`.

---

## Installation
Install the plugin via pip:
```bash
pip install mkpipe-extractor-postgres
```

---

## Usage
Configure the PostgreSQL extractor in your `elt.yaml` file:
```yaml
extractor:
  name: postgres
  config:
    host: "localhost"
    port: 5432
    user: "username"
    password: "password"
    database: "my_database"
    table: "my_table"
```

Then run:
```bash
mkpipe run elt.yaml
```

---

## Repository
[PostgreSQL Extractor Repository](https://github.com/m-karakus/mkpipe-extractor-postgres)
